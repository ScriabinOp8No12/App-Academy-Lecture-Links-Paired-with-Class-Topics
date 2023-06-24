from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import re
import base64
import os

# moved emails_data = [] to inside the function, it was here before
# emails_data = []
def get_emails_from_sender(access_token, refresh_token, client_id, client_secret, sender):
    emails_data = []
    new_access_token = None
    try:
        # Create credentials object from access token
        creds = Credentials.from_authorized_user_info(info={
            'access_token': access_token,
            'refresh_token': refresh_token,
            'client_id': client_id,
            'client_secret': client_secret
        })
        # Create Gmail API service
        service = build('gmail', 'v1', credentials=creds)
        # Get the user's email address
        user_id = service.users().getProfile(userId='me').execute()['emailAddress']
        # Create query to search for emails from specific sender
        query = f'from:{sender}'
        # Get list of messages matching the query
        response = service.users().messages().list(userId=user_id, q=query).execute()
        messages = response.get('messages', [])
        # Get the content of each message
        for message in messages:
            msg = service.users().messages().get(userId=user_id, id=message['id']).execute()
            payload = msg['payload']
            if 'parts' in payload:
                parts = payload['parts']
                data = parts[0]['body']['data']
            else:
                data = payload['body']['data']
            # Decode base64 data
            data = data.replace('-', '+').replace('_', '/')
            decoded_data = base64.b64decode(data)
            # Convert decoded data to string
            content = decoded_data.decode('utf-8')
            # ****************** Parse email content using BeautifulSoup ************************
            soup = BeautifulSoup(content, 'html.parser')
            # Find passcode
            passcode = soup.find('span').text.split(': ')[1]

            # Find zoom link -> logic, find the div with the text "you can copy the recording info..."
            # then find it's next sibling, which is always the proper zoom link. Look for an 'a' tag and href attribute
            zoom_link = soup.find('div',
                                  string='You can copy the recording information below and share with others').find_next_sibling(
                'a')['href']
            # Find date information using regex
            # [FOR LATER!] if multiple recordings with same date, only use the one that is the most recent (latest time)
            date = re.search(r'Date: .+', content)
            if date:
                date = date.group()
                # print(f'Date: {date}')
            email_data = {
                'date': date,
                'zoom_link': zoom_link,
                'passcode': passcode
            }
            emails_data.append(email_data)

            ## print(content)
            # print(f'Zoom link: {zoom_link}')
            # print(f'Passcode: {passcode}')

    except HttpError as error:
        print(f'An error occurred: {error}')

        # ADDED block of code below to auto refresh the access token with our now "permanent" refresh token
        if error.resp.status == 401:
            url = 'https://oauth2.googleapis.com/token'
            data = {
                'client_id': client_id,
                'client_secret': client_secret,
                'refresh_token': refresh_token,
                'grant_type': 'refresh_token'
            }
            response = requests.post(url, data=data)
            response_json = response.json()
            new_access_token = response_json['access_token']
            # Block above was added

    # print(emails_data)
    # new_access_token was added
    return emails_data, new_access_token
    # above: return only the last email (use .pop())?

access_token = os.environ['ACCESS_TOKEN']
refresh_token = os.environ['REFRESH_TOKEN']
client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']
sender = os.environ['EMAIL_OF_SENDER']

# added emails_data, access_token =
emails_data, access_token = get_emails_from_sender(access_token, refresh_token, client_id, client_secret, sender)
