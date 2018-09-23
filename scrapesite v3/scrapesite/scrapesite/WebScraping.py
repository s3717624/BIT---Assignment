#!/bin/env python3

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from textwrap import shorten
from django.http import HttpResponse

def scrapefunction(userin, passin):
    browser = webdriver.Chrome(executable_path='C:\\Users\\Will\\AppData\\Local\\Programs\\Python\\Python37-32\\chromedriver\\chromedriver.exe')
    browser.set_window_size(1366,768)
    browser.set_window_position(0,0)
    url = "https://sso-cas.rmit.edu.au/rmitcas/login?service=https://mytimetable.rmit.edu.au/even/student"
    browser.get(url)

    username = browser.find_element_by_id("username")
    password = browser.find_element_by_id("password")

    username.send_keys(userin)
    password.send_keys(passin)

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
    color = []
    currentlink = 0
    i = 0

    while currentlink < len(links):
        browser.get(links[currentlink])
        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'aplus-table')))
        html = browser.page_source
        soup = BeautifulSoup(html, "html.parser")
        course = soup.find('div', attrs={'class': 'desc-text'})
        course.h3.decompose()
        course = course.get_text()
        junk, course, group = course.split('\n\t\t')
        group = shorten(group, width=3, placeholder='')
        for cell in soup.find_all('td'):
            cell = cell.get_text()
            if "\n\n" != cell and "" != cell:
                if i != 0 and i != 3 and i != 4 and i != 7:
                    if i == 1:
                        raw.append(course)
                        raw.append(group)
                        if course not in color:
                            color.append('newcourse')
                            color.append(course)
                        if course + group not in color:
                            color.append(course + group)
                    raw.append(cell)
                    i += 1
                else:
                    i += 1
            if i == 8:
                i = 0
        currentlink += 1

    browser.close()

    w, h = 3, int((len(raw)/3)/2)
    info = [[0 for x in range(w)] for y in range(h)]
    time = []

    i = 0
    j = 0
    k = 0

    while i < len(raw):
        time.append(raw[i+2]+raw[i+3]+raw[i+5])
        info[k][j] = raw[i]
        info[k][j+1] = raw[i+1]
        info[k][j+2] = raw[i+4]
        i += 6
        k += 1

    return time, info, color
