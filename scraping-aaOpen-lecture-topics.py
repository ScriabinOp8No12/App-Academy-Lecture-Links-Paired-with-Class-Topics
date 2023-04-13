from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import pandas as pd

# url to main App Academy Open page that has all the weeks on the left side of the screen
main_page_url = r'https://open.appacademy.io/learn/js-py---pt-jan-2023-online/'

login_page_url = r'https://open.appacademy.io/login'

# Use selenium's webdriver to scrape (chrome)
browser = webdriver.Chrome()

# Navigate to the login page
browser.get(login_page_url)

# Enter my email and password
email = browser.find_element(by=By.NAME, value='user[email]')
password = browser.find_element(by=By.NAME, value='user[password]')
email.send_keys('nharwit@gmail.com')
password.send_keys('SET UP ENVIRONMENT VARIABLE SO PEOPLE CAN\'T SEE THIS PASSWORD HERE')

# Click the submit button to log in
submit_button = browser.find_element_by_id('submit')
submit_button.click()
# Wait 10 seconds to let the page load
browser.implicitly_wait(10)
# Get request passing in that main page url above
browser.get(main_page_url)
# Wait 10 seconds to let the page load
browser.implicitly_wait(10)
# stores the HTML source code of the current page loaded in the browser object into the variable result.
# This is done so that the HTML source code can be parsed and analyzed using BeautifulSoup in the next line of code.
result = browser.page_source

doc = BeautifulSoup(result, "html.parser")

link_to_week_1 = doc.find_all('li', {'class': 'sc-kpOJdX ighCXL'})
links_to_weeks = doc.find_all('li', {'class': 'sc-kpOJdX jPCnwj'})

print('week 1 link', link_to_week_1)
print('links from week 2 and on',links_to_weeks)

