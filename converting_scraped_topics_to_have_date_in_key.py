saved_final_list_of_dictionaries = [{'Monday': ['Orientation', 'Skills Survey'], 'Tuesday': ['Tech Setup', 'Tech Setup Check'], 'Wednesday': ['Expressions', 'String Data Type', 'Intro to Functions'], 'Thursday': ['Intro to Functions', 'Control Flow'], 'Saturday': ['Intermediate Functions']}, {'Tuesday': ['Culture Curriculum', 'Intermediate Functions'], 'Wednesday': ['Intermediate Functions'], 'Thursday': ['Intermediate Functions'], 'Saturday': ['Intermediate Functions']}, {'Monday': ['Pair Programming'], 'Tuesday': ['Arrow Functions', 'NodeJS Setup'], 'Wednesday': ['POJO Basics Practice', 'POJO Iteration Practice', 'POJO Long Practice'], 'Thursday': ['References vs Primitives', 'POJO Practice', 'Rest, Spread and Destructuring', 'POJO Long Practice'], 'Saturday': ['Advanced Array Methods', 'Advanced Array Long Practice', 'POJO Practice']}, {'Monday': ['Callbacks'], 'Tuesday': ['Callbacks'], 'Wednesday': ['Scope and Closure', 'Scope and Closure Project'], 'Thursday': ['Scope and Closure Project'], 'Saturday': ['Scope and Closure', 'POJO Practice', 'Review for the Assessment']}, {'Monday': [], 'Tuesday': ['Debugger', 'Recursion'], 'Wednesday': ['Recursion'], 'Thursday': ['Recursion'], 'Saturday': ['Recursion', 'Lecture', 'Data Types', 'Hoisting', 'Variables', 'Scope and Closure']}, {'Monday': ['Runtime Environment', 'Asynchronicity', 'Event Loop'], 'Tuesday': ['Asynchronicity'], 'Wednesday': ['User Input'], 'Thursday': ['User Input'], 'Saturday': ['Browser Basics', 'Recursion Practice', 'Review for the Assessment']}, {'Monday': [], 'Tuesday': ['Basic Coding Principles', 'ES5 Modules', 'Project'], 'Wednesday': ['Object-Oriented Programming', 'Project'], 'Thursday': ['Object-Oriented Programming', 'Project'], 'Saturday': ['Project']}, {'Monday': ['Context in JavaScript', 'Project'], 'Tuesday': ['Context in JavaScript', 'Project'], 'Wednesday': ['Test-driven Development', 'Project'], 'Thursday': ['Test-driven Development', 'Project'], 'Saturday': ['TDD Project', 'Project']}, {'Monday': [], 'Tuesday': ['Guided Practice'], 'Wednesday': ['Big O'], 'Thursday': ['Guided Practice'], 'Saturday': ['Guided Practice', 'Logic, Memory, and Arrays']}, {'Monday': ['Linked Lists and Queues', 'Guided Practice'], 'Tuesday': ['Linked Lists and Queues'], 'Wednesday': ['Guided Practice'], 'Thursday': ['Hash Tables'], 'Saturday': ['Review']}, {'Monday': [], 'Tuesday': ['Binary Search', 'Binary Trees'], 'Wednesday': ['Binary Trees'], 'Thursday': ['Binary Trees'], 'Saturday': ['White-Boarding', 'Sorting']}, {'Monday': ['Sorting'], 'Tuesday': ['Sorting'], 'Wednesday': ['Graphs'], 'Thursday': ['Graphs', 'Solving Problems with Graphs'], 'Saturday': ['Solving Problems with Graphs', 'Review']}, {'Monday': [], 'Tuesday': ['HTML Design Principles', 'Web Accessibility', 'HTML', 'Wireframes'], 'Wednesday': ['Design and HTML'], 'Thursday': ['Linking CSS Stylesheets', 'CSS Selectors', 'Basic CSS Styling', 'CSS Box Model', 'CSS Positioning'], 'Saturday': ['Basic CSS']}, {'Monday': ['CSS Flexbox Froggy', 'CSS Flexbox', 'CSS Media Queries'], 'Tuesday': ['Flexbox', 'Media Queries'], 'Wednesday': ['CSS Grid', 'Frameworks', 'CSS Interactivity', 'Grid'], 'Thursday': ['Deployment', 'CSS Grid Long Practice'], 'Saturday': ['Frameworks', 'Review']}, {'Monday': [], 'Tuesday': ['Server Basics', 'HTTP Request Components', 'HTTP Response Components', 'RESTful Routes', 'Postman', 'HTTP Basics Long Practice'], 'Wednesday': ['HTTP Basics Long Practice', 'HTTP Server', 'HTTP Response Components', 'HTTP Route Handlers'], 'Thursday': ['Static Assets', 'HTML Form Submission', 'HTML Templating', 'JSON'], 'Saturday': ['Server Request Response Cycle']}, {'Monday': ['Promises', 'Promise.all', 'async/await'], 'Tuesday': ['fetch Request', 'fetch Response', 'Promises'], 'Wednesday': ['JSON', 'fetch'], 'Thursday': ['API Documentation', 'Testing API Endpoints', 'Creating API Endpoints', 'Network Protocol'], 'Saturday': ['Web API', 'Review']}, {'Monday': [], 'Tuesday': ['Import Scripts into HTML', 'ES6 Modules', 'NodeList vs. HTML Collection', 'Element Selection'], 'Wednesday': ['Add/Remove Attributes', 'Inline-Styling', 'Create/Remove Elements', 'Browser Basics'], 'Thursday': ['Element Selection and Manipulation'], 'Saturday': ['Event Handling', 'Storing Data on Elements', 'Catsagram']}, {'Monday': ['WebStorage', 'Cookies'], 'Tuesday': ['Catsagram', 'Battleship'], 'Wednesday': ['Battleship'], 'Thursday': ['Mac Addresses and Ports', 'DNS', 'Network Diagram', 'Networks II', 'Project'], 'Saturday': ['Tic-Tac-Toe', 'Review']}, {'Tuesday': ['Server Review', 'Intro to Express', 'Express Route Handlers', 'HTTP Server vs. Express Server', 'Express Request/Response Objects'], 'Wednesday': ['Learning Objectives', 'Express Route Order', 'Express Middleware', 'Error Handling Middleware', 'Express'], 'Thursday': ['Express Routers', 'Serving Static Files in Express', 'Environment Variables', 'Express'], 'Saturday': ['Express']}, {'Monday': ['Morning Boost', 'Intro to Databases', 'Basic SQL'], 'Tuesday': ['Intro to Databases', 'SQL Database Schema', 'CREATE/DROP Tables', 'INSERT Data', 'SELECT Data', 'DELETE Data', 'UPDATE Data', 'Reading .sql Files', 'Intro to SQL and Express'], 'Wednesday': ['Relational Database Schemas', 'Basic SQL'], 'Thursday': ['CREATE Relationships in RDBMS', 'DELETE CASCADE', 'Intermediate Querying', 'Query Using JOIN', '(OPTIONAL) SQL and Express'], 'Saturday': ['SQL Aggregates', 'SQL Subqueries', 'Intermediate SQL', 'Review', '(OPTIONAL) Advanced SQL', '(OPTIONAL) More Advanced SQL']}]

from datetime import datetime, timedelta

start_date = datetime.strptime('April 17, 2023', '%B %d, %Y')
days = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
new_list_of_dictionaries = []

for week in saved_final_list_of_dictionaries[13:]:
    new_week = {}
    for day, activities in week.items():
        date = start_date + timedelta(days=days[day])
        new_week[date.strftime('%B %d, %Y')] = activities
    new_list_of_dictionaries.append(new_week)
    start_date += timedelta(days=7)

for week in new_list_of_dictionaries:
    print(week)








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


