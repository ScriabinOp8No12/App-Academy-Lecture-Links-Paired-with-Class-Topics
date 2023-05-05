# What does this project do?  Why was I motivated to start it?

This Python project automatically grabs all the App Academy Lecture Zoom links and pairs them with the associated App Academy 
Open Topics for that day. The data is then conveniently stored into Google sheets so that students can access everything 
in one place when they need to review the class material.  

The Zoom links, passcode, and date are grabbed from Gmail using the gmail API.  The Google Sheets is autopopulated by
using a Google Sheets service account along with the gspread Python library.  The Google Sheets API was not used.  

The App Academy Open topics are scraped using Selenium webdriver, using fairly complex logic to log in, click on 
specific elements, scrape neighbor elements, and finally store the topics into dictionaries.  

I wanted to hone my Python skills with this project, I had done a scraping project previously, but it was a lot simpler.
What I thought would initially take 10 hours has now taken nearly 50 hours, and it's not completed yet.  The longest bugs
to solve were: 

1. Selenium webdriver opens App Academy Open in the default light theme on Chrome. However, I was using the class names
from App Academy Open in dark theme to scrape the topics. The class names were sometimes different between these two themes! 
2. App Academy Open caches the last page you clicked on for that specific week, this was causing issues with the scraping
because my code had Selenium click certain buttons that weren't always visible. This bug was hard to fix because 
it wasn't consistently showing up. The solution was to always click on the first day of the week that showed up in App Academy
Open (like Monday). 
for that week, which seemed to solve the issue. 
3. I was not properly using environment variables. I learned that the specific run configuration needs to have the path 
to that exact python module, and that I need to run that run configuration and NOT the python module itself.
4. The Gmail API tutorials from Youtube and ChatGPT along with the Gmail API quickstart guide were missing a key component, 
causing me to not be able to get my authentication tokens. The fix was one step: adding my email under the "test user"
