import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
from NEW_gmail_zoom_links import emails_data
from datetime import datetime

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

# Dynamically add these values now -> read these values from the "NEW_gmail_zoom_links.py" file
# and load them into the Google sheets

for email_data in emails_data:
    # Original date string: Date: May 2, 2023 03:58 PM Central Time (US and Canada)
    date_str = email_data['date']
    # Split between the end of "Date:" and before "Central Time"
    # Output is now: May 2, 2023 03:58 PM
    date_str = date_str.split('Date: ')[1].split('Central Time')[0].strip()
    # Parse string into a datetime object, based on the following format
    # %b: month name, %d: zero padded day, %Y: 4 digit year, etc
    date_obj = datetime.strptime(date_str, '%b %d, %Y %I:%M %p')
    # We only want the month, day, and year.  Output is: May 02, 2023
    formatted_date = date_obj.strftime('%B %d, %Y')
    zoom_link = email_data['zoom_link']
    passcode = email_data['passcode']
    # topics_from_aa = email_data['topics']
    # values = [date, zoom_link, passcode, topics_from_aa]
    values = [formatted_date, zoom_link, passcode]

    # Insert a new row at the 2nd column of the sheet and input the values there!
    sheet.insert_row(values, 2)

