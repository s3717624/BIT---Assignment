from bs4 import BeautifulSoup
from selenium import webdriver
import time


browser = webdriver.Chrome(executable_path='/home/skvutte/Downloads/chromedriver/chromedriver')
browser.set_window_size(1366,768)
browser.set_window_position(0,0)
url = "https://sso-cas.rmit.edu.au/rmitcas/login?service=https://mytimetable.rmit.edu.au/even/student"
browser.get(url)

username = browser.find_element_by_id("username")
password = browser.find_element_by_id("password")

username.send_keys(inUser)
"""password.send_keys(inPass)"""

time.sleep(60)

browser.find_element_by_name("submit".click())
browser.find_element_by_id("find".click())

time.sleep(15)
html = browser.page_source
soup = BeautifulSoup(html, "lxml")
for link in soup.find_all('a'):
    print(link.get('href'))

