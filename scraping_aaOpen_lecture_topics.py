from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import os
import time
import json

startTime = time.time()

# ** Make sure to run "aa_open" run configuration NOT THE ACTUAL PYTHON FILE

main_page_url = r'https://open.appacademy.io/learn/js-py---pt-jan-2023-online/'
login_page_url = r'https://open.appacademy.io/login'

browser = webdriver.Chrome()
# Go to the login page using selenium on Chrome
browser.get(login_page_url)
# Grab the password from the environment variable
# Suggestion: Prompt from console instead of storing it in the environment variable -> more secure!
password_value = os.environ['APP_ACADEMY_PASSWORD']
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

# print(week_names)

topics = []
final_list_of_dictionaries = []

for week_name in week_names:
    # Find the ELEMENTS (not element without the s) containing the week name
    weeks = browser.find_elements(by=By.XPATH, value=f"//li[contains(text(), '{week_name}')]")
    for week in weeks:
        # Click on the week using JS
        browser.execute_script("arguments[0].click();", week)
        #print(f"Clicked on {week_name}")

        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        day_elements = browser.find_elements(by=By.CSS_SELECTOR,
                                             value='h3.sc-dnqmqq kcAQXs, h3.sc-dnqmqq jLQnpZ')
        for day_element in day_elements:
            day_text = day_element.text
            if day_text in days:
                # just click on the first day we see that's valid, that will allow the entire html to load
                browser.execute_script("arguments[0].click();", day_element)
                # print(f"Clicked on {day_text}")
                # IMPORTANT: Need to wait at least 2 seconds otherwise THE URL WON'T CHANGE (it'll grab wrong data)
                time.sleep(2)
                # once we click on a valid day, all the html for the week will be properly loaded, so we break the loop
                break
        # with the time.sleep(2), we now see the url getting updated!
        current_url = browser.current_url
        # print('Current url', current_url)

        new_result = browser.page_source
        # Update the doc object, otherwise if we use the original doc object, our data will be blank
        each_day_doc = BeautifulSoup(new_result, "html.parser")

        # **** Light theme and Dark theme have different CLASSES!!!! Selenium opens the browser in light theme, not the dark theme I use normally
        # if using both in the search: h3_elements = each_day_doc.find_all('h3', class_=['sc-dnqmqq ftHzVO', 'sc-dnqmqq kcAQXs'])

        # some days have a different class for some reason, even though they are both light themed
        h3_elements = each_day_doc.find_all('h3', class_=['sc-dnqmqq kcAQXs', 'sc-dnqmqq jLQnpZ'])

        individual_dictionaries = {}
        valid_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Saturday']
        not_valid_topics = ['Learning Boost', 'End of Day', 'Formative Quiz', 'Practice Problems']
        for h3_element in h3_elements:
            if h3_element.text in valid_days:
                # Set the variable name then the key of the dictionary to be the valid day of the week
                current_day = h3_element.text
                individual_dictionaries[current_day] = []
                # Use the ul tag to find the topics names within the current valid day, search for the next ul element
                next_ul = h3_element.find_next('ul')
                # If there is another ul element, then find all the li elements within the ul element
                if next_ul:
                    topic_lis = next_ul.find_all('li')
                    # Loop through these ul elements, rename them, and find the specific text containing the topics
                    for topic_li in topic_lis:
                        topic_header = topic_li.find('header', class_='sc-gqjmRU kvshPl')
                        # If the text isn't within the invalid topics list, then add the topic text value as a value
                        # of the current day we are on (start at Monday)
                        if topic_header and topic_header.text not in not_valid_topics:
                            individual_dictionaries[current_day].append(topic_header.text)
        final_list_of_dictionaries.append(individual_dictionaries)

        #print(individual_dictionaries)

    browser.get(main_page_url)
    # Have to find the menu_element here again (won't work if we use just the line below that)
    menu_element = browser.find_element(by=By.CSS_SELECTOR, value='a.sc-hwwEjo.ieBOLv')
    browser.execute_script('arguments[0].click();', menu_element)

# print(final_list_of_dictionaries)

with open('scraped_output.txt', 'w') as f:
    json.dump(final_list_of_dictionaries, f)

with open('scraped_output.txt', 'r') as f:
    data = json.load(f)

print(data)

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))

# Took 307 seconds to scrape all topics from week 1 through week 24