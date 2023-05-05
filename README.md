# What does this project do?

This project automatically grabs all the App Academy Lecture Zoom links and pairs them with the associated App Academy 
Open Topics for that day, and stores them conveniently into Google sheets so that students can access the links and see
which topics that lecture covered!

The Zoom links, passcode, and date are grabbed from Gmail using the gmail API.  The Google Sheets is autopopulated by
using a Google Sheets service account along with the gspread Python library.  

The App Academy Open topics are scraped using Selenium webdriver, using fairly complex logic to log in, scrape specific 
neighbor elements, and storing them all into dictionaries.  
