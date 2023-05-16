# This python file extracts the zoom links from the older recordings (before April 20th)
# They were sent to me as 50 attachments within one email (from April 20th, 11:40pm MT)
# All the recent / new emails that came in after April 20th arrive in my inbox once the lecture is recorded
# and are from a different sender (App Academy)
# There's a high chance that you won't need this Python module because all the emails you receive will
# be from App Academy and not be in attachments!

from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from bs4 import BeautifulSoup
import base64
import os


def get_attachments_from_email(access_token, refresh_token, client_id, client_secret, sender, email_subject):
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
    # Create query to search for emails from specific sender with specific subject
    query = f'from:{sender} subject:{email_subject}'
    # Get list of messages matching the query
    response = service.users().messages().list(userId=user_id, q=query).execute()
    messages = response.get('messages', [])
    # Get the first message (assuming there is only one message with the specified sender and subject)
    message = messages[0]
    msg = service.users().messages().get(userId=user_id, id=message['id']).execute()
    payload = msg['payload']
    attachments_data = []
    # Iterate over the parts of the message payload to find attachments
    for part in payload['parts']:
        if part['filename']:
            attachment_id = part['body']['attachmentId']
            attachment = service.users().messages().attachments().get(userId=user_id, messageId=message['id'], id=attachment_id).execute()
            data = attachment['data']
            # Decode base64 data
            data = data.replace('-', '+').replace('_', '/')
            decoded_data = base64.urlsafe_b64decode(data)
            attachments_data.append(decoded_data)

    attachments_html = []
    for data in attachments_data:

        content = data.decode('utf-8')
        soup = BeautifulSoup(content, 'html.parser')
        # Convert the beautifulsoup output to a string!
        body_html = str(soup.body)

        attachments_html.append(body_html)

    return attachments_html


access_token = os.environ['ACCESS_TOKEN']
refresh_token = os.environ['REFRESH_TOKEN']
client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']
sender = os.environ['INSTRUCTOR_EMAIL']
email_subject = 'recordings'

# For above 'sender' and 'email_subject' variable
# Need to specify a specific email with all 50 old lecture recordings since I received multiple
# emails from my instructor, and I don't want to have to filter anything

attachments_html = get_attachments_from_email(access_token, refresh_token, client_id, client_secret, sender, email_subject)

zoom_link_prefix = 'https://us02web.zoom.us/rec/share/'

zoom_links_and_passcodes = []
for html in attachments_html:
    # Remove escape characters, this was the main issue that caused everything else to break!
    html = html.replace('=\r\n', '')
    soup = BeautifulSoup(html, 'html.parser')

    # Find date
    recording_div = soup.find('div', string="Your cloud recording is now available.")
    if recording_div:
        # find next div sibling after we find the div with "Your cloud recording is now available."
        date_div = recording_div.find_next_sibling('div')
        if date_div:
            date = date_div.text.split('\n')[2].strip()
        # some error handling just in case
        else:
            date = None
    else:
        date = None

    # Find passcodes by looking for a span tag with a starting text of "Passcode:"
    passcodes = [span.text.split(': ')[1] for span in
                 soup.find_all('span', string=lambda text: text and text.startswith('Passcode:'))]

    # Find the specific zoom links that have an <a> tag, with text that starts with the zoom_link_prefix value seen about 25 lines higher
    zoom_links = soup.find_all('a', string=lambda text: text and text.startswith(zoom_link_prefix))
    # Zip function creates a tuple, and pairs everything in the lists until one list has more items than the other
    # Iterate over two lists, zoom_links and passcodes, at the same time. For each iteration, we append a dictionary to
    # the zoom_links_and_passcodes list that contains the current date, zoom link, and passcode
    for zoom_link, passcode in zip(zoom_links, passcodes):
        zoom_links_and_passcodes.append({'date': date, 'zoom_link': zoom_link.text, 'passcode': passcode})

print(zoom_links_and_passcodes)
