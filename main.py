import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



browser = webdriver.Firefox()


def main ():
    setup()
    search()
    get_info()
    check()


def setup():
    admin_email=""
    admin_password=""

    browser.get('https://google.com')
    browser.find_element_by_id("L2AGLb").click()
    browser.maximize_window()
    browser.switch_to.window(browser.window_handles[0])
    browser.get("localhost:4000/websites/new")
    browser.execute_script("window.open('https://google.com')")
    browser.find_element_by_name("admin[email]").send_keys(admin_email)
    browser.find_element_by_name("admin[password]").send_keys(admin_password + Keys.ENTER)
    browser.execute_script("window.open('https://google.com')")
    browser.switch_to.window(browser.window_handles[1])
    browser.get("localhost:4000/websites/")
    browser.switch_to.window(browser.window_handles[-1])


def search():
    search=input("type what websites you need to add: ")
    searchbar=browser.find_element_by_name("q")
    searchbar.send_keys(search,Keys.ENTER)

    

def get_info():

    description = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h3"))
    ).text

    site = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "cite"))
    )
    site.click()

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
    
def check():
    browser.switch_to.window(browser.window_handles[1])
    browser.find_element_by_id("query").send_keys(content[0]+Keys.ENTER)
    time.sleep(2)
    site_name = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h5"))
    ).text
    if site_name == content[0]:
        print(site_name)
        print(content[0])
        print("website has been added")
    else:
        print(site_name)
        print(content[0])
        print("website has not been added")


if __name__ == '__main__':
    main()
 