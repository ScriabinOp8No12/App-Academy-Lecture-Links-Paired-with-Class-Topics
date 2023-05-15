# This python file will extract the zoom links from the older recordings (before April 20th)
# They are all within one giant email (from April 20th, 11:40pm MT), so it shouldn't be too hard.
# All the recent / new emails arrive in my inbox once the lecture is recorded

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from bs4 import BeautifulSoup
from datetime import datetime
import re
import base64
import os

emails_data = []
def get_emails_from_sender(access_token, refresh_token, client_id, client_secret, sender):
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
            # Parse email content using BeautifulSoup
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


            # # print(content)
            # print(f'Zoom link: {zoom_link}')
            # print(f'Passcode: {passcode}')

    except HttpError as error:
        print(f'An error occurred: {error}')

    #print(emails_data)
    return emails_data

access_token = os.environ['ACCESS_TOKEN']
refresh_token = os.environ['REFRESH_TOKEN']
client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']
sender = os.environ['INSTRUCTOR_EMAIL']


get_emails_from_sender(access_token, refresh_token, client_id, client_secret, sender)

print(sender)