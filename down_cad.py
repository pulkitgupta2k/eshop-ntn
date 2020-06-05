from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from creds import username, password

def login(sel):
    login_link = "https://www.traceparts.com/els/snr/en/sign-in"
    sel.get(login_link)
    sel.find_element_by_xpath("//input[@id='Email']").send_keys(username)
    sel.find_element_by_xpath("//input[@id='Password']").send_keys(password)

def driver():
    sel = webdriver.Chrome('./chromedriver')
    login(sel)

if __name__ == "__main__":
    driver()