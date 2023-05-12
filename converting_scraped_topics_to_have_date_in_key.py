# In this scraped output dictionary, I want to convert the Week 14 Thursday key value to April 20, 2023
# and then each day after that to a proper string as well so I can then match my google sheets date with that topic.  Clicked on Week 1 - Intro to JavaScript
#
# Clicked on Week 14 - CSS
# Current url https://open.appacademy.io/learn/js-py---pt-jan-2023-online/week-14---css/learning-boost-instructions
# {'Monday': ['CSS Flexbox Froggy', 'CSS Flexbox', 'CSS Media Queries'], 'Tuesday': ['Flexbox', 'Media Queries'],
# 'Wednesday': ['CSS Grid', 'Frameworks', 'CSS Interactivity', 'Grid'],
# **********************************************************
# 'Thursday': ['Deployment', 'CSS Grid Long Practice'],          THIS ONE HERE!!!!!!!

# WE CAN ADJUST FOR SPRING BREAK LATER with old lecture links

# from scraping_aaOpen_lecture_topics import final_output_dictionary
# from datetime import datetime, timedelta
#
# week14 = {'Monday': ['CSS Flexbox Froggy', 'CSS Flexbox', 'CSS Media Queries'], 'Tuesday': ['Flexbox', 'Media Queries'], 'Wednesday': ['CSS Grid', 'Frameworks', 'CSS Interactivity', 'Grid'], 'Thursday': ['Deployment', 'CSS Grid Long Practice'], 'Saturday': ['Frameworks', 'Review']}
# week15 = {'Monday': [], 'Tuesday': ['Server Basics', 'HTTP Request Components', 'HTTP Response Components', 'RESTful Routes', 'Postman', 'HTTP Basics Long Practice'], 'Wednesday': ['HTTP Basics Long Practice', 'HTTP Server', 'HTTP Response Components', 'HTTP Route Handlers'], 'Thursday': ['Static Assets', 'HTML Form Submission', 'HTML Templating', 'JSON'], 'Saturday': ['Server Request Response Cycle']}
# week16 = {'Monday': ['Promises', 'Promise.all', 'async/await'], 'Tuesday': ['fetch Request', 'fetch Response', 'Promises'], 'Wednesday': ['JSON', 'fetch'], 'Thursday': ['API Documentation', 'Testing API Endpoints', 'Creating API Endpoints', 'Network Protocol'], 'Saturday': ['Web API', 'Review']}
# week17 = {'Monday': [], 'Tuesday': ['Import Scripts into HTML', 'ES6 Modules', 'NodeList vs. HTML Collection', 'Element Selection'], 'Wednesday': ['Add/Remove Attributes', 'Inline-Styling', 'Create/Remove Elements', 'Browser Basics'], 'Thursday': ['Element Selection and Manipulation'], 'Saturday': ['Event Handling', 'Storing Data on Elements', 'Catsagram']}
# week18 = {'Monday': ['WebStorage', 'Cookies'], 'Tuesday': ['Catsagram', 'Battleship'], 'Wednesday': ['Battleship'], 'Thursday': ['Mac Addresses and Ports', 'DNS', 'Network Diagram', 'Networks II', 'Project'], 'Saturday': ['Tic-Tac-Toe', 'Review']}
# week19 = {'Tuesday': ['Server Review', 'Intro to Express', 'Express Route Handlers', 'HTTP Server vs. Express Server', 'Express Request/Response Objects'], 'Wednesday': ['Learning Objectives', 'Express Route Order', 'Express Middleware', 'Error Handling Middleware', 'Express'], 'Thursday': ['Express Routers', 'Serving Static Files in Express', 'Environment Variables', 'Express'], 'Saturday': ['Express']}

from datetime import datetime, timedelta
from scraping_aaOpen_lecture_topics import final_list_of_dictionaries

print(final_list_of_dictionaries)










#
# data = {'Thursday': ['Deployment', 'CSS Grid Long Practice'], 'Saturday': ['Frameworks', 'Review'], 'Monday': [], 'Tuesday': ['Server Basics', 'HTTP Request Components', 'HTTP Response Components', 'RESTful Routes', 'Postman', 'HTTP Basics Long Practice'], 'Wednesday': ['HTTP Basics Long Practice', 'HTTP Server', 'HTTP Response Components', 'HTTP Route Handlers'], 'Thursday': ['Static Assets', 'HTML Form Submission', 'HTML Templating', 'JSON'], 'Saturday': ['Server Request Response Cycle']}
#
# start_date = datetime.strptime('April 20, 2023', '%B %d, %Y')
# days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# new_data = {}
#
# for key in data.keys():
#     date = start_date + timedelta(days=days.index(key))
#     new_data[date.strftime('%B %d, %Y')] = data[key]
#
# print(new_data)
#
#
# # Create a datetime object for the start date (Thursday of Week 14)
# start_date = datetime(2023, 4, 20)
#
# # Create a dictionary to store the topics for each date
# topics_by_date = {}
#
# # Set the current date to the start date
# current_date = start_date
#
# # Loop through each week in your scraped data starting from Week 14
# for week_name, week_data in list(final_output_dictionary.items())[13:]:
#     # Check if this is a new week
#     if 'Monday' in week_data:
#         # Calculate the number of days between the current date and the next Monday
#         days_to_add = (7 - current_date.weekday()) % 7
#         # Create a timedelta object with the number of days to add
#         delta = timedelta(days=days_to_add)
#         # Add the timedelta to the current date to get the date for this Monday
#         current_date += delta
#
#     # Loop through each day in the week
#     for day_name, day_topics in week_data.items():
#         # Add one day to the current date to get the date for this day
#         current_date += timedelta(days=1)
#
#         # Format the current date as a string
#         current_date_str = current_date.strftime('%B %d, %Y')
#         # Add the topics for this day to the dictionary using the current date as the key
#         topics_by_date[current_date_str] = day_topics
#
# # Print out the resulting dictionary
# print(topics_by_date)


