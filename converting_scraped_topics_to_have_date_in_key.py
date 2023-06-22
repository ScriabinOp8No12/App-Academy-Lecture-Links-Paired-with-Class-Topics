from datetime import datetime, timedelta
import json

# If our topic would fall onto the starting date below, then increase time delta by 7
# Spring break 2023 started on March 27th (Monday), and lasted until the next Monday.
# PUT THE DATE OF THE MONDAY THAT THE WEEKLY BREAK STARTS!
# The 3 weekly breaks are likely: Spring Break, July Break, Winter Break
app_academy_week_long_breaks = ['March 27, 2023', 'July 3, 2023', 'December 25, 2023']

# *********************************
# Read from the scraped_output_weeks1_24.txt
with open('scraped_output_weeks1_24.txt', 'r') as f:
    data = json.load(f)

saved_final_list_of_dictionaries = data
#print(saved_final_list_of_dictionaries)

# Creates a datetime object, uses strptime method and formats it in a special way
# %B represents the full month name, %d represents the day of the month as a zero-padded decimal number,
# and %Y represents the year with century as a decimal number

# Alex started teaching us in week 5 (lecture starts Feb. 6th, 2023), that is week 5, so access dictionary index 4
start_date = datetime.strptime('February 6, 2023', '%B %d, %Y')

days = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
new_list_of_dictionaries = []

# Access dictionary index 4 (5th week -> that's when we started getting lectures from Alex)
for week in saved_final_list_of_dictionaries[4:]:
    new_week = {}
    # iterates over each key value pair within current dictionary
    # days is the key, topics is the value, and week.items() returns a view object that displays a
    # list of the dictionary’s key-value pairs as tuples
    for day, topics in week.items():
        # Now we look at how many days it's been between the values, we use the days dictionary created above
        # to calculate the new date
        date = start_date + timedelta(days=days[day])
        # Check if the date falls into the list of starting dates that is a week off
        if date.strftime('%B %d, %Y') in app_academy_week_long_breaks:
            # Increase the time delta by 7 days
            date += timedelta(days=7)
            # Also increase the start_date variable by 7 days
            start_date += timedelta(days=7)
        # Create the new key-value pair to the new_week dictionary where the key is a string representing the date
        # of the current day’s activities and the value is the list of activities.
        # The date is formatted as a string using the strftime method of the datetime class.
        new_week[date.strftime('%B %d, %Y')] = topics
    new_list_of_dictionaries.append(new_week)
    # Bump up the time delta by 7 days now to access the new week (new dictionary)
    start_date += timedelta(days=7)

for week in new_list_of_dictionaries:
    print(week)
