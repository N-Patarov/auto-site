import selenium
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os


#content=[description,name]

browser = webdriver.Firefox()


def main ():
    setup()
    search()


def setup():
    admin_email=""
    admin_password=""

    browser.get('https://google.com')
    browser.find_element_by_id("L2AGLb").click()
    browser.maximize_window()
    browser.execute_script("window.open('https://google.com')")
    browser.switch_to.window(browser.window_handles[0])
    browser.get("localhost:4000/websites/new")
    browser.find_element_by_name("admin[email]").send_keys(admin_email)
    browser.find_element_by_name("admin[password]").send_keys(admin_password + Keys.ENTER)
    browser.switch_to.window(browser.window_handles[-1])

def search():
    search=input("type what websites you need to add: ")
    searchbar=browser.find_element_by_name("q")
    searchbar.send_keys(search,Keys.ENTER)


if __name__ == '__main__':
    main()
    