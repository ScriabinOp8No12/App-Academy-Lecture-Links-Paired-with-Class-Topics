from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

# Grab the password from the **environment variable**
password_value = os.environ['APP_ACADEMY_PASSWORD']
# Use the following 2 lines to make sure the password is correct
# password_value = os.environ.get('APP_ACADEMY_PASSWORD')
# print(password_value)

# Enter my email and password (selenium version 2022+ needed to use the By and value combo to 'find element by name'
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

# locate the hamburger menu and click on it, the element is an "a tag" with a class name specified below
menu_element = browser.find_element(by=By.CSS_SELECTOR, value='a.sc-hwwEjo.ieBOLv')
browser.execute_script('arguments[0].click();', menu_element)

# instead of using time.sleep(10) and always waiting the specified number of seconds, INSTEAD
# we can use the following 2 lines of code logic to wait for the li elements with class name to show up (the weeks)
wait = WebDriverWait(browser, 10)
week_elements = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'li.sc-kpOJdX.juxBLx')))

# stores the HTML source code of the current page loaded in the browser object into the variable result.
# This is done so that the HTML source code can be parsed and analyzed using BeautifulSoup in the next line of code.
result = browser.page_source

# needed the result and doc here, after the menu is clicked (not before the menu_element)!
doc = BeautifulSoup(result, "html.parser")

# Scrapes all 'weeks' by finding the li tag and accessing the class specified below
week_links = doc.find_all('li', {'class': 'sc-kpOJdX juxBLx'})

# looks for the Weeks without the word "Assessment" in them, which weeds out Assessment and Practice Assessment weeks,
# which contains content that we don't want to scrape.  We only want the lecture topics to pair with the Zoom links!
week_names = []
for week_element in week_links:
    # text property of beautifulsoup Tag class returns all TEXT inside a tag and its children, stripped of any HTML tags
    week_name = week_element.text
    if 'Assessment' not in week_name:
        week_names.append(week_name)

# The output is beautiful!
print(week_names)




