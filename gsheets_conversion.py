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
# sheet = client.open_by_key(SPREADSHEET_KEY).worksheet('Jan-9th-Cohort-Lectures')
sheet = client.open_by_key(SPREADSHEET_KEY).worksheet('Testing_Sheet')

# Get the email data from the gmail_api email output ('NEW_gmail_zoom_links.py')
dates_zoom_links_and_topics = emails_data

# Look at values in 1st column of Google sheets so that we can check if that date already exists, if it does
# then do NOT update the Google sheet with that data (it'll be a duplicate) AND also add it to a set so we
# avoid lectures that are not valid.
# Gmail api extracts the lectures with the most recent time (or latest time) first, so it's important to NOT run
# this program until after all the Gmail zoom links have arrived in your Gmail inbox.  For example, let's say
# at 5pm MT and 6pm MT, a lecture link is sent to your gmail. In our cohort, these are mistakes, and are 1-2 minute
# long lectures with nothing on them.  At 11:30pm MT, a third and final email comes in with a link, since the
# Pacific Time cohort ends at 11pm MT, we know that this is the correct Zoom info to add to our Google sheets!
# The Gmail API extracts them in the most recent order, so we can simply run this program, extract the correct
# 11:30pm MT lecture, then store it in a set. Now if we try to grab the other ones from the same date, it won't
# add those to the Google Sheets.
dates_in_sheet = set(sheet.col_values(1)[1:])

# Dynamically add the values from the "NEW_gmail_zoom_links.py" file and add them into the Google sheets
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
    # If the Date doesn't show up in the Google sheet date column, and the date isn't a Friday or Sunday
    if formatted_date not in dates_in_sheet and date_obj.weekday() not in [4, 6]:
        # Add that date into the set, so we don't get duplicates
        dates_in_sheet.add(formatted_date)
        # NEXT STEP (add before if statement): Add App Academy Open topics to end of values list
        values = [formatted_date, zoom_link, passcode]
        # Find the last row of the sheet which has data in it (if it's empty, we start on row 1)
        last_row = len(sheet.col_values(1))
        # Insert a new row after the last row of the sheet and input the values there!
        sheet.insert_row(values, last_row + 1)
    # ***** SORT the data in descending order, but don't also sort the 1st row because it has the headers! *****
    # Get all data from the sheet (including the header row)
    data = sheet.get_all_values()
    # Separate the header row from the rest of the data
    header = data[0]
    data = data[1:]

    # Sort the data by the date column in descending order
    date_column_index = 0
    data = sorted(data, key=lambda x: x[date_column_index], reverse=True)

    # Update the sheet with the sorted data (keeping the header row in place)
    sheet.update('A2', data)

# print(dates_in_sheet)


