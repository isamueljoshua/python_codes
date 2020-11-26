# coding: utf-8

__author__ = ["Samuel Joshua"]

import time
from selenium import webdriver

# returns a browser object and opens the firefox browser
browser = webdriver.Firefox(executable_path=r'geckodriver.exe')
# browser.get('http://automatetheboringstuff.com/')
# elem = browser.find_element_by_css_selector('body > div.main > div:nth-child(1) > ul:nth-child(20) > li:nth-child(1) > a')
# elem.click()

# # find multiple elements by selector
# elems = browser.find_elements_by_css_selector('p')
# print(len(elems))

# type into a search field and submit the form
# Open site in chrome browser and right click on search field and copy Selector
# here we are searching for the book automate the boring stuff with python
# browser.get('https://www.flipkart.com/')
# searchElem = browser.find_element_by_css_selector('#container > div > div._3ybBIU > div._1tz-RS > div._3pNZKl > div.Y5-ZPI > form > div > div > input')
# searchElem.send_keys('automate the boring stuff with python')
# searchElem.submit()

# time.sleep(8)

# On mozilla browser, copy the CSS Path
browser.get('https://www.amazon.com/')
searchElem = browser.find_element_by_css_selector('#twotabsearchtextbox')
searchElem.send_keys('automate the boring stuff with python')
searchElem.submit()

# since almost all pages look same and page load time was low I had to put sleep to make it wait for each op
time.sleep(8)
browser.back()

time.sleep(6)
browser.forward()

time.sleep(6)
browser.refresh()

time.sleep(6)
browser.quit()

# next step is to read the web pages
browser = webdriver.Firefox(executable_path=r'geckodriver.exe')
browser.get('http://automatetheboringstuff.com/')
elem = browser.find_element_by_css_selector('body > div.main > div:nth-child(1) > blockquote:nth-child(5)')
# get text inside the HTML element
print(elem.text)

# to get the entire web page text via selenium, pass html or body as parameter
elem = browser.find_element_by_css_selector('html')
print()
print(elem.text)