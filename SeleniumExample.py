
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import unittest
import csv

browser = webdriver.Chrome()

browser.get('http://google.com')

element = browser.find_element_by_name('q')

element.send_keys("site:co.il QA Manager")

element.send_keys(Keys.RETURN)



links = []
with open('SitesList.csv') as csv_file:
    file_writer = csv.writer(csv_file)
for row in file_writer:
    links.append(row)

browser.quit()
h


