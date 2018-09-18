from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import textwrap

browser = webdriver.Chrome(executable_path='PUT YOUR CHROMEDRIVER PATH HERE')
browser.set_window_size(1366,768)
browser.set_window_position(0,0)
browser.get("https://sso-cas.rmit.edu.au/rmitcas/login?service=https://mytimetable.rmit.edu.au/even/student")

username = browser.find_element_by_id("username")
password = browser.find_element_by_id("password")

inUser = ('PUT YOUR USERNAME HERE')
inPass = ('PUT YOUR PASSWORD HERE')
username.send_keys(inUser)
password.send_keys(inPass)

browser.find_element_by_name("submit").click()

html = browser.page_source
soup = BeautifulSoup(html, "html.parser")

links = []
for a in soup.find_all('a', href=True):
    a = a['href']
    if "#group/" in a:
        a = ("https://sso-cas.rmit.edu.au/rmitcas/login?service=https://mytimetable.rmit.edu.au/even/student" + a)
        links.append(a)

raw = []
currentlink = 0
i = 0

while currentlink < len(links):
    browser.get(links[currentlink])
    wait = WebDriverWait(browser, 10)
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'aplus-table')))
    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")
    course = soup.find('div', attrs={'class': 'desc-text'})
    course.h3.decompose()
    course = course.get_text()
    junk, course, group = course.split('\n\t\t')
    group = textwrap.shorten(group, width=3, placeholder='')
    for cell in soup.find_all('td'):
        cell = cell.get_text()
        if "\n\n" != cell and "" != cell:
            if i != 0 and i != 3 and i != 4 and i != 7:
                if i == 1:
                    raw.append(course)
                    raw.append(group)
                raw.append(cell)
                i += 1
            else:
                i += 1
        if i == 8:
            i = 0
    currentlink += 1


w, h = 6, int(len(raw)/6)
sor = [[0 for x in range(w)] for y in range(h)]

i = 0
j = 0
k = 0

while i < len(raw):
    while j < 6:
        sor[k][j] = raw[i]
        j += 1
        i += 1
    j = 0
    k += 1

print(sor)
