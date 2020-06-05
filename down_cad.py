from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from creds import username, password
import time
import json
import os, os.path


# def rename():

def login(sel):
    login_link = "https://www.traceparts.com/els/snr/en/sign-in"
    sel.get(login_link)
    sel.find_element_by_xpath("//input[@id='Email']").send_keys(username)
    sel.find_element_by_xpath("//input[@id='Password']").send_keys(password)
    sel.find_element_by_xpath("//button[@id='signin-btn']").click()

def download_file(sel, name, link):
    temp_loc = 'temp/'
    sel.get(link)
    selection = sel.find_element_by_xpath("//select[@id='cad-format-select']")
    for option in selection.find_elements_by_tag_name('option'):
        if option.text == '3D XML':
            option.click()
    time.sleep(2)
    sel.find_element_by_xpath("//button[@id='direct-download']").click()
    while(len(os.listdir(temp_loc)) == 0):
        pass
    while(os.listdir(temp_loc)[0].split('.')[-1] != 'zip'):
        pass
    print(os.listdir(temp_loc)[0])
    time.sleep(1)
    temp_file = "temp/{}".format(os.listdir(temp_loc)[0])
    dest_file = "cads/{}".format(name)
    os.rename(temp_file, dest_file)
    time.sleep(2)

def download_files(sel):
    with open("downs.json") as f:
        details = json.load(f)
    for key, value in details.items():
        try:
            print(".")
            name = "{}.zip".format(key)
            link = value[1]
            download_file(sel, name, link)
        except Exception as e:
            print(e)
            pass

def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    prefs = {"profile.default_content_settings.popups": 0,
                "download.default_directory": r"C:\Users\Pulkit\Desktop\Repos\eshop-ntn\temp\\",
                "directory_upgrade": True}
    options.add_experimental_option("prefs", prefs)
    sel = webdriver.Chrome('./chromedriver', chrome_options=options)
    login(sel)
    download_files(sel)

if __name__ == "__main__":
    driver()