from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os




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
            headers = payload['headers']
            # Get subject and date of email
            subject = [i['value'] for i in headers if i['name']=='Subject'][0]
            date = [i['value'] for i in headers if i['name']=='Date'][0]
            print(f'Subject: {subject}')
            print(f'Date: {date}')
    except HttpError as error:
        print(f'An error occurred: {error}')


access_token = os.environ['ACCESS_TOKEN']
refresh_token = os.environ['REFRESH_TOKEN']
client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']
sender = '2023-01-09-part-time-est@appacademy.io'

get_emails_from_sender(access_token, refresh_token, client_id, client_secret, sender)