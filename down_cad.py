from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from creds import username, password
import time
import json

def login(sel):
    login_link = "https://www.traceparts.com/els/snr/en/sign-in"
    sel.get(login_link)
    sel.find_element_by_xpath("//input[@id='Email']").send_keys(username)
    sel.find_element_by_xpath("//input[@id='Password']").send_keys(password)
    sel.find_element_by_xpath("//button[@id='signin-btn']").click()

def download_file(sel, name, link):
    sel.get(link)
    selection = sel.find_element_by_xpath("//select[@id='cad-format-select']")
    for option in selection.find_elements_by_tag_name('option'):
        if option.text == '3D XML':
            option.click()
    time.sleep(2)
    sel.find_element_by_xpath("//button[@id='direct-download']").click()
    print("download")
    time.sleep(10)

def download_files(sel):
    with open("downs.json") as f:
        details = json.load(f)
    for key, value in details.items():
        try:
            print(".")
            name = "{}.zip".format(key)
            link = value[1]
            download_file(sel, name, link)
        except:
            pass

def driver():
    sel = webdriver.Chrome('./chromedriver')
    login(sel)
    download_files(sel)

if __name__ == "__main__":
    driver()