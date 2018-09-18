#!/bin/env python3

from bs4 import BeautifulSoup
from selenium import webdriver
import time

def scrapefunction(userin, passin):
    browser = webdriver.Chrome(executable_path='/home/skvutte/Downloads/chromedriver/chromedriver')
    browser.set_window_size(1366,768)
    browser.set_window_position(0,0)
    url = "https://sso-cas.rmit.edu.au/rmitcas/login?service=https://mytimetable.rmit.edu.au/even/student"
    browser.get(url)

    username = browser.find_element_by_id("username")
    password = browser.find_element_by_id("password")

    username.send_keys(userin)
    password.send_keys(passin)

    time.sleep(15)

    select = browser.find_element_by_name("submit")
    if select:
        select.click()

    time.sleep(15)
    html = browser.page_source
    soup = BeautifulSoup(html, "lxml")
    return soup.find_all('a')

