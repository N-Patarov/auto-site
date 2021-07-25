import selenium
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os


#content=[description,name]

browser = webdriver.Firefox("/usr/local/bin/")
browser.get('https://google.com')

search=input("type what websites you need to add: ")
searchbar=browser.find_element_by_name("q")
searchbar.send_keys(search)