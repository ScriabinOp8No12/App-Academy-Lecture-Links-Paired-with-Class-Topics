# use a legacy token
# grab zoom links with associate dates
# Check time of posting, and then figure out which date that must go with
# convert that date into the format of week + Monday/Tuesday/Wednesday/Thursday/Saturday to line up with
# AA open topics.  Store these in a dictionary

# Use Google Sheets API to store this output there ->
# *** I'm just going to scrape Slack ***

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import os
import time
import requests
import pandas as pd


from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=C:\\Users\\nharw\\AppData\\Local\\Google\\Chrome\\User Data") # replace with the path to your Chrome profile
browser = webdriver.Chrome(options=options)

slack_channel_link = 'https://app.slack.com/client/T03GU501J/C04EKPNLTQ9/thread/C03GUB0T3-1673626274.605469'
browser.get(slack_channel_link)

#
# options = webdriver.ChromeOptions()
# options.add_argument(r'user-data-dir=C:\Users\nharw\AppData\Local\Google\Chrome\User Data') #Path to my chrome profile
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
# service = Service("C:\\Users\\chromedriver.exe")
# browser = webdriver.Chrome(service=service, options=options)
#
# slack_channel_link = 'https://app.slack.com/client/T03GU501J/C04EKPNLTQ9/thread/C03GUB0T3-1673626274.605469'
# browser.get(slack_channel_link)







