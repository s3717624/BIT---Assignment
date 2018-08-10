from bs4 import BeautifulSoup
from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path='E:\Documents\PycharmProjects\chromedriver.exe')
browser.set_window_size(1366,768)
browser.set_window_position(0,0)