from datetime import datetime, timedelta

# If our topic would fall onto the starting date below, then increase time delta by 7
# Spring break 2023 started on March 27th (Monday), and lasted until the next Monday.
# PUT THE DATE OF THE MONDAY THAT THE WEEKLY BREAK STARTS!
# The 3 weekly breaks are likely: Spring Break, July Break, Winter Break
app_academy_week_long_breaks = ['March 27, 2023', 'July 3, 2023', 'December 25, 2023']

saved_final_list_of_dictionaries = [{'Monday': ['Orientation', 'Skills Survey'], 'Tuesday': ['Tech Setup', 'Tech Setup Check'], 'Wednesday': ['Expressions', 'String Data Type', 'Intro to Functions'], 'Thursday': ['Intro to Functions', 'Control Flow'], 'Saturday': ['Intermediate Functions']}, {'Tuesday': ['Culture Curriculum', 'Intermediate Functions'], 'Wednesday': ['Intermediate Functions'], 'Thursday': ['Intermediate Functions'], 'Saturday': ['Intermediate Functions']}, {'Monday': ['Pair Programming'], 'Tuesday': ['Arrow Functions', 'NodeJS Setup'], 'Wednesday': ['POJO Basics Practice', 'POJO Iteration Practice', 'POJO Long Practice'], 'Thursday': ['References vs Primitives', 'POJO Practice', 'Rest, Spread and Destructuring', 'POJO Long Practice'], 'Saturday': ['Advanced Array Methods', 'Advanced Array Long Practice', 'POJO Practice']}, {'Monday': ['Callbacks'], 'Tuesday': ['Callbacks'], 'Wednesday': ['Scope and Closure', 'Scope and Closure Project'], 'Thursday': ['Scope and Closure Project'], 'Saturday': ['Scope and Closure', 'POJO Practice', 'Review for the Assessment']}, {'Monday': [], 'Tuesday': ['Debugger', 'Recursion'], 'Wednesday': ['Recursion'], 'Thursday': ['Recursion'], 'Saturday': ['Recursion', 'Lecture', 'Data Types', 'Hoisting', 'Variables', 'Scope and Closure']}, {'Monday': ['Runtime Environment', 'Asynchronicity', 'Event Loop'], 'Tuesday': ['Asynchronicity'], 'Wednesday': ['User Input'], 'Thursday': ['User Input'], 'Saturday': ['Browser Basics', 'Recursion Practice', 'Review for the Assessment']}, {'Monday': [], 'Tuesday': ['Basic Coding Principles', 'ES5 Modules', 'Project'], 'Wednesday': ['Object-Oriented Programming', 'Project'], 'Thursday': ['Object-Oriented Programming', 'Project'], 'Saturday': ['Project']}, {'Monday': ['Context in JavaScript', 'Project'], 'Tuesday': ['Context in JavaScript', 'Project'], 'Wednesday': ['Test-driven Development', 'Project'], 'Thursday': ['Test-driven Development', 'Project'], 'Saturday': ['TDD Project', 'Project']}, {'Monday': [], 'Tuesday': ['Guided Practice'], 'Wednesday': ['Big O'], 'Thursday': ['Guided Practice'], 'Saturday': ['Guided Practice', 'Logic, Memory, and Arrays']}, {'Monday': ['Linked Lists and Queues', 'Guided Practice'], 'Tuesday': ['Linked Lists and Queues'], 'Wednesday': ['Guided Practice'], 'Thursday': ['Hash Tables'], 'Saturday': ['Review']}, {'Monday': [], 'Tuesday': ['Binary Search', 'Binary Trees'], 'Wednesday': ['Binary Trees'], 'Thursday': ['Binary Trees'], 'Saturday': ['White-Boarding', 'Sorting']}, {'Monday': ['Sorting'], 'Tuesday': ['Sorting'], 'Wednesday': ['Graphs'], 'Thursday': ['Graphs', 'Solving Problems with Graphs'], 'Saturday': ['Solving Problems with Graphs', 'Review']}, {'Monday': [], 'Tuesday': ['HTML Design Principles', 'Web Accessibility', 'HTML', 'Wireframes'], 'Wednesday': ['Design and HTML'], 'Thursday': ['Linking CSS Stylesheets', 'CSS Selectors', 'Basic CSS Styling', 'CSS Box Model', 'CSS Positioning'], 'Saturday': ['Basic CSS']}, {'Monday': ['CSS Flexbox Froggy', 'CSS Flexbox', 'CSS Media Queries'], 'Tuesday': ['Flexbox', 'Media Queries'], 'Wednesday': ['CSS Grid', 'Frameworks', 'CSS Interactivity', 'Grid'], 'Thursday': ['Deployment', 'CSS Grid Long Practice'], 'Saturday': ['Frameworks', 'Review']}, {'Monday': [], 'Tuesday': ['Server Basics', 'HTTP Request Components', 'HTTP Response Components', 'RESTful Routes', 'Postman', 'HTTP Basics Long Practice'], 'Wednesday': ['HTTP Basics Long Practice', 'HTTP Server', 'HTTP Response Components', 'HTTP Route Handlers'], 'Thursday': ['Static Assets', 'HTML Form Submission', 'HTML Templating', 'JSON'], 'Saturday': ['Server Request Response Cycle']}, {'Monday': ['Promises', 'Promise.all', 'async/await'], 'Tuesday': ['fetch Request', 'fetch Response', 'Promises'], 'Wednesday': ['JSON', 'fetch'], 'Thursday': ['API Documentation', 'Testing API Endpoints', 'Creating API Endpoints', 'Network Protocol'], 'Saturday': ['Web API', 'Review']}, {'Monday': [], 'Tuesday': ['Import Scripts into HTML', 'ES6 Modules', 'NodeList vs. HTML Collection', 'Element Selection'], 'Wednesday': ['Add/Remove Attributes', 'Inline-Styling', 'Create/Remove Elements', 'Browser Basics'], 'Thursday': ['Element Selection and Manipulation'], 'Saturday': ['Event Handling', 'Storing Data on Elements', 'Catsagram']}, {'Monday': ['WebStorage', 'Cookies'], 'Tuesday': ['Catsagram', 'Battleship'], 'Wednesday': ['Battleship'], 'Thursday': ['Mac Addresses and Ports', 'DNS', 'Network Diagram', 'Networks II', 'Project'], 'Saturday': ['Tic-Tac-Toe', 'Review']}, {'Tuesday': ['Server Review', 'Intro to Express', 'Express Route Handlers', 'HTTP Server vs. Express Server', 'Express Request/Response Objects'], 'Wednesday': ['Learning Objectives', 'Express Route Order', 'Express Middleware', 'Error Handling Middleware', 'Express'], 'Thursday': ['Express Routers', 'Serving Static Files in Express', 'Environment Variables', 'Express'], 'Saturday': ['Express']}, {'Monday': ['Morning Boost', 'Intro to Databases', 'Basic SQL'], 'Tuesday': ['Intro to Databases', 'SQL Database Schema', 'CREATE/DROP Tables', 'INSERT Data', 'SELECT Data', 'DELETE Data', 'UPDATE Data', 'Reading .sql Files', 'Intro to SQL and Express'], 'Wednesday': ['Relational Database Schemas', 'Basic SQL'], 'Thursday': ['CREATE Relationships in RDBMS', 'DELETE CASCADE', 'Intermediate Querying', 'Query Using JOIN', '(OPTIONAL) SQL and Express'], 'Saturday': ['SQL Aggregates', 'SQL Subqueries', 'Intermediate SQL', 'Review', '(OPTIONAL) Advanced SQL', '(OPTIONAL) More Advanced SQL']}]

# Creates a datetime object, uses strptime method and formats it in a special way
# %B represents the full month name, %d represents the day of the month as a zero-padded decimal number,
# and %Y represents the year with century as a decimal number

# Alex started teaching us in week 5 (lecture starts Feb. 6th, 2023), that is week 5, so access dictionary index 4
start_date = datetime.strptime('February 6, 2023', '%B %d, %Y') # Monday Week 5, empty, Tuesday Week 5, recursion and iffes

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
        # Create the new key-value pair to the new_week dictionary where the key is a string representing the date
        # of the current day’s activities and the value is the list of activities.
        # The date is formatted as a string using the strftime method of the datetime class.
        new_week[date.strftime('%B %d, %Y')] = topics
    new_list_of_dictionaries.append(new_week)
    # Bump up the time delta by 7 days now to access the new week (new dictionary)
    start_date += timedelta(days=7)

# for week in new_list_of_dictionaries:
#     print(week)



