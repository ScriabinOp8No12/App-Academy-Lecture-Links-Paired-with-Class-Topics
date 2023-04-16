from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import os
import time
import requests
import pandas as pd

main_page_url = r'https://open.appacademy.io/learn/js-py---pt-jan-2023-online/'
login_page_url = r'https://open.appacademy.io/login'
browser = webdriver.Chrome()
# Go to the login page using selenium on Chrome
browser.get(login_page_url)
# Grab the password from the **environment variable**
# Igor suggestion: Prompt from console instead of storing it in the environment variable -> more secure!
password_value = os.environ['APP_ACADEMY_PASSWORD']
# Use the following 2 lines to make sure the password is correct
# password_value = os.environ.get('APP_ACADEMY_PASSWORD')
# print(password_value)

# Enter my email and password (selenium version 2022+ needed to use the By and value combo to 'find element by name'
# https://stackoverflow.com/questions/35632810/python-selenium-find-element-by-name
email = browser.find_element(by=By.NAME, value='user[email]')
password = browser.find_element(by=By.NAME, value='user[password]')
# Email and password (2 lines below) are typed into aa open
email.send_keys('nharwit@gmail.com')
password.send_keys(password_value)
# Click the submit button to log in
# Need to use xpath to locate it because it doesn't have a name attribute like the username and password fields above
submit_button = browser.find_element(by=By.XPATH, value='//button[@type="submit"]')
submit_button.click()
# Wait 10 seconds to let the page load
browser.implicitly_wait(10)
# Locate the hamburger menu in the top left, the element is an "a tag" with a class name specified below
menu_element = browser.find_element(by=By.CSS_SELECTOR, value='a.sc-hwwEjo.ieBOLv')
# Click on the hamburger menu
browser.execute_script('arguments[0].click();', menu_element)
# Instead of using time.sleep(10) and always waiting the specified number of seconds,
# We can use the following 2 lines of code logic to wait for the li elements with class name to show up (the weeks)
wait = WebDriverWait(browser, 10)
week_elements = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'li.sc-kpOJdX.juxBLx')))
# Stores the HTML source code of the current page loaded in the browser object into the variable result.
# This is done so that the HTML source code can be parsed and analyzed using BeautifulSoup in the next line of code.
result = browser.page_source
doc = BeautifulSoup(result, "html.parser")
# Scrapes all 'weeks' of the li tag with class specified below
week_links = doc.find_all('li', {'class': 'sc-kpOJdX juxBLx'})
# Looks for the Weeks without the word "Assessment" in them, which weeds out Assessment and Practice Assessment weeks,
# Which contains content that we don't want to scrape.
week_names = []
for week_element in week_links:
    # text property of beautifulsoup Tag class returns all TEXT inside a tag and its children, stripped of any HTML tags
    week_name = week_element.text
    if 'Assessment' not in week_name:
        week_names.append(week_name)

print(week_names)

# ****** NEXT STEPS BELOW ******

# li tag, class of sc-gqjmRU kvshPl, remember to output any text using Beautiful Soup's text property

# Plan:
# Now that we have the week names, we can have Selenium click on them (find element by xpath)
# Find the elements containing the week names

# for week_name in week_names:
#     # Find the ELEMENTS (not element without the s) containing the week name
#     weeks = browser.find_elements(by=By.XPATH, value=f"//li[contains(text(), '{week_name}')]")
#     for week in weeks:
#         # Click on the week
#         week.click()
#         print(f"Clicked on {week_name}")

        # Find the back arrow on APP ACADEMY (NOT browser back arrow) -> h3 tag with class of the following
        # back_arrow_element = browser.find_element(by=By.CSS_SELECTOR, value='h3.sc-cSHVUG VLQzD')
        # Click the back arrow
        # browser.execute_script("arguments[0].click();", back_arrow_element)


    # # Click on the days within the week (Monday, homework for Tuesday, Tuesday, etc.)
    # individual_days_within_week = browser.find_elements(by=By.CSS_SELECTOR, value='.sc-htoDjs.lmwFtC')
    #
    # # Wait for the page to load and stop waiting once we find the topics
    # # ****** THIS LINE BREAKS?!?!?!? ******
    # WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "header.sc-gqjmRU kvshPl")))
    #
    # topic_result = browser.page_source
    # topic_doc = BeautifulSoup(topic_result, "html.parser")
    # # Scrape the information
    # topics = topic_doc.find_all('header', {'class': 'sc-gqjmRU kvshPl'})
    # print(topics)


    # # Find the back arrow on APP ACADEMY (NOT browser back arrow) -> h3 tag with class of the following
    # back_arrow_element = browser.find_element(by=By.CSS_SELECTOR, value='h3.sc-cSHVUG VLQzD')
    # # Click the back arrow
    # browser.execute_script("arguments[0].click();", back_arrow_element)
    #
    # # # Wait for the page to load
    # # WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "li.sc-gqjmRU kvshPl")))
    #
    # # Wait 5 seconds before moving on to the next week
    # time.sleep(5)

# driver.quit()
