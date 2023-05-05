# What does this project do?  Why was I motivated to start it?

This Python project automatically grabs all the App Academy Lecture Zoom links and pairs them with the associated App Academy 
Open Topics for that day. The data is then conveniently stored into Google sheets so that students can access everything 
in one place when they need to review the class material.  

The Zoom links, passcode, and date are grabbed from Gmail using the gmail API.  The Google Sheets is autopopulated by
using a Google Sheets service account along with the gspread Python library.  The Google Sheets API was not used.  

The App Academy Open topics are scraped using Selenium webdriver, using fairly complex logic to log in, click on 
specific elements, scrape neighbor elements, and finally store the topics into dictionaries.  

I wanted to hone my Python skills with this project, I had done a scraping project previously, but it was a lot simpler.
What I thought would initially take 10 hours has now taken nearly 50 hours, and it's not completed yet. The hardest bugs
to solve were: 

1. Selenium webdriver opens App Academy Open in the default light theme on Chrome. However, I was using the class names
from App Academy Open in dark theme to scrape the topics. The class names were sometimes different between these two themes! 
2. App Academy Open caches the last page you clicked on for that specific week, this was causing issues with the scraping
because my code had Selenium click certain buttons that weren't always visible. This bug was hard to fix because 
it wasn't consistently showing up. The solution was to always click on the first day of the week that showed up in App Academy
Open (like Monday).
3. I was not properly using environment variables. I learned that the specific run configuration needs to have the path 
to that exact python module, and that I need to run that run configuration and NOT the python module itself.
4. The Gmail API quickstart guide and tutorials from Youtube + ChatGPT were missing a key component, which stopped me 
from getting my authentication tokens. The fix was one step: adding my email under the "test user"

# How To Set Everything Up!
This takes 30 minutes to 1 hour to set up (or longer)

# Requirements: 
1. Python 3.11
2. Gmail API - getting your account and tokens setup
3. Gsheets Service Account 
4. Email from Gmail with the App Academy Lecture for that day
5. Libraries for each Python module

# How to get your Gmail API setup (step by step guide):

This guide does a good job, but it misses one crucial step: 
https://ei.docs.wso2.com/en/latest/micro-integrator/references/connectors/gmail-connector/configuring-gmail-api/

Here are the steps to follow (as seen above, but with one extra step)

1. Sign in with your Google account at this link: https://console.cloud.google.com/projectselector2/apis/credentials
2. Click on 'Select a Project' and click 'New Project' in the top right.  
3. Enter GmailConnector or whatever name you want and click 'Create'. You don't need to touch location.  
4. Click 'Configure Consent Screen' near the top right or 'Oauth Consent Screen' from the left menu, click 'External' and click 'Create'.
5. 

