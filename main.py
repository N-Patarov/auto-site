import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




browser = webdriver.Firefox()


def main ():
    setup()
    search()
    get_info()


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

    link = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "cite"))
    )
    print(link)
    link.click()


def get_info():
    url=browser.current_url
    #removes the https:// and the / of the url
    #to get just the domain of the website
    link=url.split("https://")
    link1=link[1].split("/")
    real_link=link1[0]
    print(real_link)
    screenshot=browser.save_screenshot("(" + real_link + ")" + ".png")

    content=[]
    content.append(real_link)
    

if __name__ == '__main__':
    main()
 