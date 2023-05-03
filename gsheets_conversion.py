import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
from NEW_gmail_zoom_links import emails_data

# Spreadsheet key is found on the Google sheets url, between the /d/ and /edit
SPREADSHEET_KEY = os.environ['SPREADSHEET_KEY']

# Authenticate using a service account
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
# Replaced first parameter with the json file within this pycharm project
creds = ServiceAccountCredentials.from_json_keyfile_name('gmail-connector-gsheets.json', scope)
client = gspread.authorize(creds)

# Open the Google Sheet (specify the sheet name)
sheet = client.open_by_key(SPREADSHEET_KEY).worksheet('Jan-9th-Cohort-Lectures')

# Get the email data from the first code
dates_zoom_links_and_topics = emails_data
print(dates_zoom_links_and_topics)
# Need to dynamically add these values now, basically read these values from the "NEW_gmail_zoom_links.py" file
# and load them into these variables one after another

date = "5/1/2023"
zoom_link = "zoom.us/test/link"
passcode = "123456"
topics_from_aa = "{Monday: orientation, test, learning}"

values = [
    f'{date}', f'{zoom_link}', f'{passcode}', f'{topics_from_aa}',
]

# Insert a new row at the 2nd column of the sheet and input the values there!
sheet.insert_row(values, 2)

