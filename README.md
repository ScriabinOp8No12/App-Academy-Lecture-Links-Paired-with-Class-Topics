# What this project does

This Python project automatically grabs all the App Academy Lecture Zoom links and pairs them with the associated App Academy 
Open Topics for that day. The data is then conveniently stored into Google sheets so that students can access everything 
in one place when they need to review the class material.  

The Zoom links, passcodes, and dates are extracted from Gmail using the Gmail API and then stored in Google Sheets by
using a Google Sheets service account.  The Google Sheets API was not used. The App Academy Open topics are scraped 
using Selenium webdriver, using fairly complex logic to log in, click on specific elements, scrape neighbor elements, 
and finally store the topics into dictionaries.  

# Motivation and greatest challenges

I wanted to hone my Python skills with this project, and create something that would benefit me and my classmates! 
The hardest problems / bugs to solve were: 

1. Selenium webdriver opens App Academy Open in the default light theme on Chrome. However, I was using the dark theme 
on App Academy Open, and unfortunately, some of the class names were different between the light and dark theme!
2. App Academy Open caches the last page you clicked on for that specific week. This was causing issues with the scraping
because my code had Selenium try to click certain buttons, but they weren't always visible. This bug was hard to fix because 
it wasn't consistent. The solution was to always click on the first day of the week that showed up in App Academy
Open (like Monday) to avoid the cache issue.
3. I was not properly using environment variables. I learned that the specific run configuration needs to have the path 
to that exact python module, and that I need to run that run configuration and NOT the python module itself.
4. The Gmail API quickstart guide and tutorials from Youtube and ChatGPT were missing a key component, which stopped me 
from getting my authentication tokens. The solution was adding my Gmail account under the "test users" field. 

# Setup
Estimated setup time: 30 minutes - 1 hour 

# Requirements: 
1. Python 3.11
2. Gmail API 
3. Gsheets Service Account 
4. Email from Gmail with the App Academy Lecture for that day
5. App Academy Open Account and Google Chrome browser (both optional) 
6. Libraries for each Python module

# Gmail API setup:

This guide does a good job, but it misses one step:<br>https://ei.docs.wso2.com/en/latest/micro-integrator/references/connectors/gmail-connector/configuring-gmail-api/

Here are the steps to follow (as seen above, but with one extra step)

1. Sign in with your Gmail account at this link:<br>https://console.cloud.google.com/projectselector2/apis/credentials
2. Click on 'Select a Project' and click 'New Project' in the top right
3. Enter 'GmailConnector' or another name for your project and click 'Create'
4. Click 'Configure Consent Screen' near the top right or 'Oauth Consent Screen' from the left menu, click 'External' and click 'Create'
5. In the "App name" field, input your project name, either "GmailConnector" or whatever you named your project in step 3
6. Enter your Gmail account in the "User support email" field and in the "Developer contact information" at the bottom of the page
7. Click "Save and Continue"
8. # Key step the guide misses - Within the "OAuth consent screen", click "Add Users" under the "Test users" field and input the same Gmail account you logged in with in step 1
9. Click "Credentials" from the left menu, and then click "Create Credentials" then select "OAuth client ID"
10. Select "Web application" from the drop-down menu
11. In the "Authorized redirect URIs" section, put https://developers.google.com/oauthplayground as the URI 
12. You now have your Client ID and Client Secret. Save them in a secure place, we will be using these later!
13. Click "Library" from the left side menu, and use the search bar and type in "Gmail API". Click on it and then click "Enable"

# Gmail API Access and Refresh Tokens

1. 