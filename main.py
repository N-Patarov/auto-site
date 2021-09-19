from os import getloadavg
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
import time
import urllib.request
from bs4 import BeautifulSoup
import re


browser = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
count = 0
tags = {
'novini' : '//input[@phx-value-tag-id="1"]',
'politika' : '//input[@phx-value-tag-id="2"]',
'sport' : '//input[@phx-value-tag-id="3"]',
'razvlekatelni' : '//input[@phx-value-tag-id="20"]',
'hranitelni_magazini' : '//input[@phx-value-tag-id="19"]',
'online_magazini' : '//input[@phx-value-tag-id="6"]',
'biznes_i_finansi' : '//input[@phx-value-tag-id="18"]',
'avto_i_mps' : '//input[@phx-value-tag-id="9"]',
'obrazovanie' : '//input[@phx-value-tag-id="12"]',
'software_i_hardware' : '//input[@phx-value-tag-id="14"]',
'stroitelstvo' : '//input[@phx-value-tag-id="22"]',
'moda_i_kozmetika' : '//input[@phx-value-tag-id="16"]',
'multimediq_i_tv' : '//input[@phx-value-tag-id="15"]',
'durjavni_institucii' : '//input[@phx-value-tag-id="13"]',
'gotvarstvo_i_kulinariq' : '//input[@phx-value-tag-id="10"]',
'medicina' : '//input[@phx-value-tag-id="11"]',
'el_uslugi' : '//input[@phx-value-tag-id="8"]',
'hazart' : '//input[@phx-value-tag-id="7"]',
'socialni_mreji' : '//input[@phx-value-tag-id="5"]',
'restoranti' : '//input[@phx-value-tag-id="4"]',
'tenis_na_masa' : '//input[@phx-value-tag-id="23"]',
}




def main ():
    global count
    setup()
    search()
    print(tags)
    while count<=len(description):
        check()
        if is_there == False:
            add()
            count+=1
        else:
            print("website is already added")
            count+=1
    print("Done")

def setup():
    admin_email="email"
    admin_password="password"

    browser.get('https://google.com')
    browser.find_element_by_id("L2AGLb").click()
    browser.maximize_window()
    browser.switch_to.window(browser.window_handles[0])
    browser.get("https://izberi.site/websites/new")
    browser.execute_script("window.open('https://google.com')")
    browser.find_element_by_name("admin[email]").send_keys(admin_email)
    browser.find_element_by_name("admin[password]").send_keys(admin_password + Keys.ENTER)
    browser.execute_script("window.open('https://google.com')")
    browser.switch_to.window(browser.window_handles[1])
    browser.get("https://izberi.site/websites/")





def search():
    global tag
    query = input("what do you want to search: ")
    url = 'https://google.com/search?q='+query+'&near=sofia&num=30'
    tag = input("what tag do you want to check: ")
    request = urllib.request.Request(url)

    # Set a normal User Agent header, otherwise Google will block the request.
    request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
    raw_response = urllib.request.urlopen(request).read()

    # Read the repsonse as a utf-8 string
    html = raw_response.decode("utf-8")


    soup = BeautifulSoup(html, 'html.parser')
    global links
    global description
    links = []
    description = []
    # Find all the search result divs
    divs = soup.select("#search div.g")
    for div in divs:
        # Search for a h3 tag
        h3 = div.select("h3")
        url = div.select("cite")

        # Check if we have found a result
        if (len(h3) >= 1):

            # Print the title
            url=url[0].get_text()
            print(url)
            try:
                pattern = re.compile(r'https?://www\.(.+?\.(?:net|org|com|gov|site|bg|ro|me|eu|no|co|uk|it|in|gr|edu|fi|online|tv|biz|buzz|auction|pro|es|ru)).*')
                real_link = pattern.match(url).group(1)
                links.append(real_link)
            except AttributeError:
                pattern = re.compile(r'https?://(.+?\.(?:net|org|com|gov|site|bg|ro|me|eu|no|co|uk|it|in|gr|edu|fi|online|tv|biz|buzz|auction|pro|es|ru)).*')
                real_link = pattern.match(url).group(1)
                links.append(real_link)
            description.append(h3[0].get_text())
    print(links)
    print(description)


def check():
    global count
    browser.switch_to.window(browser.window_handles[1])
    browser.find_element_by_id("query").send_keys(links[count]+Keys.ENTER)
    global is_there
    is_there = False
    try:
        site_name_normal = WebDriverWait(browser, 4).until(
        EC.presence_of_element_located((By.TAG_NAME, "h5"))
        ).text
        site_name=site_name_normal.lower()
        if site_name == links[count].lower():
            is_there = True
        else:
            is_there = False

    except TimeoutException:
        is_there = False
    browser.get("https://izberi.site/websites/")


def add():
    try:
        print("adding website...")
        time.sleep(1)
        browser.switch_to.window(browser.window_handles[0])
        browser.find_element_by_id("websites_title").send_keys(links[count])
        browser.find_element_by_id("websites_description").send_keys(description[count])
        browser.find_element_by_id("websites_likes").send_keys("0")
        browser.find_element_by_id("websites_urls").send_keys(links[count])
        browser.find_element_by_id("websites_priority").send_keys("1")
        browser.find_element_by_xpath("//button[@type='submit']").click()
        print("added")
        browser.execute_script("window.scrollTo(10,document.body.scrollHeight)")
        time.sleep(2)
        website_to_click = WebDriverWait(browser, 4).until(
        EC.presence_of_element_located((By.LINK_TEXT, links[count]))
        )
        website_to_click.click()
        browser.find_element_by_xpath(tags[tag]).click()
        browser.back()
        browser.back()
        browser.find_element_by_id("websites_title").clear()
        browser.find_element_by_id("websites_description").clear()
        browser.find_element_by_id("websites_likes").clear()
        browser.find_element_by_id("websites_urls").clear()
        browser.find_element_by_id("websites_priority").clear()
    except IndexError:
        print("Done")
if __name__ == '__main__':
    main()
