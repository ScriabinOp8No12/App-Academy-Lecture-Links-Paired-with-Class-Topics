import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

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
# email_data = get_emails_from_sender(access_token, refresh_token, client_id, client_secret, sender)

# Write data to Google sheet, specifying the range to put the data into.
cell_list = sheet.range('A1:D5')
values = [
    'Date', 'Zoom Link', 'Passcode', 'Topics from AA',
    'Wheel', '$20.50', '4', '3/1/2022',
    'Door', '$15', '2', '3/15/2022',
    'Engine', '$100', '1', '3/20/2022',
]

# This somehow works, I'm not sure how it iterates using zip (it does it in pairs or something?)
for cell, value in zip(cell_list, values):
    cell.value = value

sheet.update_cells(cell_list)
