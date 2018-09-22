#!/bin/env python3

from bs4 import BeautifulSoup
from selenium import webdriver
import time

def scrapefunction(userin, passin):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    driver = webdriver.Chrome(executable_path="/home/skvutte/Downloads/chromedriver/chromedriver", chrome_options=chrome_options)
    driver.set_window_size(1366,768)
    driver.set_window_position(0,0)
    url = "https://sso-cas.rmit.edu.au/rmitcas/login?service=https://mytimetable.rmit.edu.au/even/student"
    driver.get(url)

    username = driver.find_element_by_id("username")
    password = driver.find_element_by_id("password")

    username.send_keys(userin)
    password.send_keys(passin)

    select = driver.find_element_by_name("submit")
    if select:
        select.click()

    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")
    scrape = soup.find_all('a')
    return scrape

