from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import os
import time
import requests
import pandas as pd

# url to main App Academy Open page that has all the weeks on the left side of the screen
main_page_url = r'https://open.appacademy.io/learn/js-py---pt-jan-2023-online/'

# Need to have selenium webdriver log in as me, because otherwise it won't load the page at all!
login_page_url = r'https://open.appacademy.io/login'

# Use selenium's webdriver to scrape (chrome)
browser = webdriver.Chrome()

# Navigate to the login page
browser.get(login_page_url)

# Grab the password from the environment variable
password_value = os.environ['APP_ACADEMY_PASSWORD']
# Use the following 2 lines to make sure the password is correct
# password_value = os.environ.get('APP_ACADEMY_PASSWORD')
# print(password_value)

# Enter my email and password (selenium version starting in 2022 needed to use the By and value combo to
# 'find element by name'
# https://stackoverflow.com/questions/35632810/python-selenium-find-element-by-name
email = browser.find_element(by=By.NAME, value='user[email]')
password = browser.find_element(by=By.NAME, value='user[password]')
email.send_keys('nharwit@gmail.com')
password.send_keys(password_value)

# Click the submit button to log in
# Need to use xpath to locate it because it doesn't have a name attribute like the username and password fields above!
submit_button = browser.find_element(by=By.XPATH, value='//button[@type="submit"]')
submit_button.click()
# Wait 10 seconds to let the page load
browser.implicitly_wait(10)


# locate the hamburger menu and click on it
# Locate the element using its tag name and class name
menu_element = browser.find_element(by=By.CSS_SELECTOR, value='a.sc-hwwEjo.ieBOLv')
browser.execute_script('arguments[0].click();', menu_element)
# wait 10 seconds to let it click on the menu
time.sleep(10)

# stores the HTML source code of the current page loaded in the browser object into the variable result.
# This is done so that the HTML source code can be parsed and analyzed using BeautifulSoup in the next line of code.
result = browser.page_source

doc = BeautifulSoup(result, "html.parser")


# All weeks except for week 1 (which has a different 2nd part of the class name for some reason...)
week_links = doc.find_all('li', {'class': 'sc-kpOJdX juxBLx'})

week_names = []
for week_element in week_links:
    week_name = week_element.text
    if 'Assessment' not in week_name:
        week_names.append(week_name)


print(week_names)




