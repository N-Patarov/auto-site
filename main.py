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


browser = webdriver.Chrome()
count = 0
description=""





def main ():
    setup()
    search()
    for i in range(3):
        get_info()
        check()
        if is_there == False:
            add()
        else:
            print("website is already added")
            content.clear()

def setup():
    admin_email=""
    admin_password=""

    browser.get('https://google.com')
    browser.find_element_by_id("L2AGLb").click()
    browser.maximize_window()
    browser.switch_to.window(browser.window_handles[0])
    browser.get("https://izberi.site/websites/new")
    try:

        WebDriverWait(browser, 3).until(EC.alert_is_present(),
        'Timed out waiting for PA creation ' +
        'confirmation popup to appear.')
        #if it doe
        alert = browser.switch_to.alert()
        alert.cancel()
        print ("alert accepted")
    except TimeoutException:
            print ("no alert")
            pass
    browser.execute_script("window.open('https://google.com')")
    browser.find_element_by_name("admin[email]").send_keys(admin_email)
    browser.find_element_by_name("admin[password]").send_keys(admin_password + Keys.ENTER)
    browser.execute_script("window.open('https://google.com')")
    browser.switch_to.window(browser.window_handles[1])
    browser.get("https://izberi.site/websites/")
    


def search():
    browser.switch_to.window(browser.window_handles[-1])
    browser.get("https://google.com")
    search=input("type what websites you need to add: ")
    searchbar=browser.find_element_by_name("q")
    searchbar.send_keys(search,Keys.ENTER)

    

def get_info():
    global description
    global site
    browser.switch_to.window(browser.window_handles[2])
    time.sleep(1)
    description = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h3"))
    ).text
    #site = WebDriverWait(browser, 10).until(
     #   EC.presence_of_element_located((By.TAG_NAME, "cite"))
    #)
   
    time.sleep(3)
    global count
    javaScript = f"document.getElementsByTagName('cite')[{count}].click();"
    browser.execute_script(javaScript)
    print(javaScript)
    url=browser.current_url
    #removes the https:// and the / of the url
    #to get just the domain of the website
    try:
        link=url.split("https://")
        link1=link[1].split("/")
        link2=link1[0]
        link3=link2.split("www.")
        real_link=link3[1]

    except IndexError:
        link=url.split("https://")
        link1=link[1].split("/")
        real_link=link1[0]

    time.sleep(3)
    screenshot=browser.save_screenshot("photos/"+"(" + real_link + ")" + ".png")
    global content
    content=[]
    content.append(real_link)
    content.append(description)
    print(content)
    browser.back()
    count+=1
    browser.execute_script("window.scrollBy(0,400)","")
    time.sleep(5)
    del description
    print(count)

def check():
    browser.switch_to.window(browser.window_handles[1])
    browser.find_element_by_id("query").send_keys(content[0]+Keys.ENTER)
    time.sleep(2)
    global is_there
    is_there = False
    try:
        site_name_normal = WebDriverWait(browser, 4).until(
        EC.presence_of_element_located((By.TAG_NAME, "h5"))
        ).text
        site_name=site_name_normal.lower()
        if site_name == content[0]:
            is_there = True
        else:
            is_there = False

    except TimeoutException:
        is_there = False
    browser.get("https://izberi.site/websites/")


def add():
    print("adding website...")
    time.sleep(1)
    browser.switch_to.window(browser.window_handles[0])
    browser.find_element_by_id("websites_title").send_keys(content[0])
    browser.find_element_by_id("websites_description").send_keys(content[1])
    browser.find_element_by_id("websites_likes").send_keys("0")
    browser.find_element_by_id("websites_urls").send_keys(content[0])
    browser.find_element_by_id("websites_priority").send_keys("1")
    browser.find_element_by_xpath("//button[@type='submit']").click()
    content.clear()


if __name__ == '__main__':
    main()
 
