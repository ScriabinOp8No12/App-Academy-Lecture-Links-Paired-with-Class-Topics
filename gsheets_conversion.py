import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials
# the import below is taking 14 seconds, it wasn't the new_list_of_dictionaries import ...
from NEW_gmail_zoom_links import emails_data
import json
# Can speed up this import by writing the data to a text file once, then just reading from it?
# from converting_scraped_topics_to_have_date_in_key import new_list_of_dictionaries
from datetime import datetime
import time

startTime = time.time()

# Read from the text file that contains the converted App Academy topics with the Date as the dictionary key
with open('converted_topics_weeks1_24.txt', 'r') as f:
    new_list_of_dictionaries = json.load(f)

# Spreadsheet key is found on the Google sheets url, between the /d/ and /edit
SPREADSHEET_KEY = os.environ['SPREADSHEET_KEY']
# Authenticate using a service account
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
# Replace first parameter with the json file that's in this pycharm project
creds = ServiceAccountCredentials.from_json_keyfile_name('gmail-connector-gsheets.json', scope)
client = gspread.authorize(creds)
# Open the Google Sheet (specify the sheet name you want to populate)
#sheet = client.open_by_key(SPREADSHEET_KEY).worksheet('Jan-9th-Cohort-Lectures')
sheet = client.open_by_key(SPREADSHEET_KEY).worksheet('Testing_Sheet')
#sheet = client.open_by_key(SPREADSHEET_KEY).worksheet('Testing_Time_Complexity_1')

data = sheet.get_all_values()
# Separate the header row from the rest of the data
header = data[0]
data = data[1:]
# Update the sheet with the sorted data (keeping the header row in place)
sheet.update('A2', data)
# Get the email data from the gmail_api email output ('NEW_gmail_zoom_links.py')
dates_zoom_links_and_topics = emails_data
# See 1. for logic on using a set
dates_in_sheet = set(sheet.col_values(2)[1:])
# Count the number of read requests made to Google Sheets, the quota is roughly 60 per minute, which is exceeded
# if we let the 3 for loops iterate all the way through without pausing (500+ iterations for 4 months of lecture data)
counter = 0
# Dynamically add the values from the "NEW_gmail_zoom_links.py" file and add them into the Google sheets
for email_data in emails_data:
    counter += 1
    print(counter)
    # See 2. at end of code to add more than one row at a time

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
    # We have no classes on Friday or Sunday
    if formatted_date not in dates_in_sheet and date_obj.weekday() not in [4, 6]:
        # Add that date into the set, so we don't get duplicates
        dates_in_sheet.add(formatted_date)
        # Get the day of the week as a string
        day_of_week = date_obj.strftime('%A')
        values = [day_of_week, formatted_date, zoom_link, passcode]
        # Find the last row of the sheet which has data in it (if it's empty, we start on row 1)
        last_row = len(sheet.col_values(1))
        # Insert a new row after the last row of the sheet and input the values there!
        sheet.insert_row(values, last_row + 1)
    # Get all data from the sheet (including the header row)
    data = sheet.get_all_values()
    # Separate the header row from the rest of the data
    header = data[0]
    data = data[1:]
    # Sort the data by the date column (column index 1) in descending order
    date_column_index = 1
    data = sorted(data, key=lambda x: datetime.strptime(x[date_column_index], '%B %d, %Y'), reverse=True)
    # Update the sheet with the sorted data (keeping the header row in place)
    sheet.update('A2', data)
    break

# Adding AA Topics to Google Sheets based on date:
found = False
for week in reversed(new_list_of_dictionaries):
    counter += 1
    print(counter)
    for date, topics in reversed(week.items()):
        counter += 1
        print(counter)
        if date in dates_in_sheet:
            # Iterate over the rows of the sheet starting from the first row
            for row_index, row in enumerate(sheet.get_all_values(), start=1):
                counter += 1
                print(counter)
                # Check if the date in the current row matches the date we're looking for
                if row[1] == date:
                    # Update the topics column (column 5) with the topics
                    sheet.update_cell(row_index, 5, ', '.join(topics))
                    # Exit all 3 loops once we've found and updated the single matching row
                    found = True
                    break
            if found:
                break
    if found:
        break

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))

# You might run into a "temporary error" with some html output, if that happens, just run the code again!
# On the first time you run the code, you will want to change everywhere you see the commented out
# time.sleep(1) to time.sleep(3) to not exceed the max quota!  However, on subsequent runs when you are only adding
# 1 row at a time, you can omit the time.sleep()

# Looks like Google sheets does some caching, because it allows me to make 1000
# requests in a few seconds, if I already ran the code and hit the max quota previously

# 1.
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

# 2.
# Need to stop iterations once we find the SINGLE proper email
# if counter == 3:  # change this to be a larger number if we need to add more than just one row of data
#   break
# also need to remove the "break" statement seen in the last line of the loop
#     sheet.update('A2', data)
#     break
