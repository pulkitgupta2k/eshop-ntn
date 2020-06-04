from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import json

def get_products(html):
    product_links = {}
    with open('bearing_links.json') as f:
        product_links = json.load(f)
    soup = BeautifulSoup(html, "html.parser")
    page_product_links = soup.findAll("a", {"class": "is-product-short-label"})
    for page_product_link in page_product_links:
        page_product_link = page_product_link['href']
        if page_product_link not in product_links["Home e-Shop:Industry Solutions:Bearing units:Bearing units:NOT_COMPLETE"]:
            product_links["Home e-Shop:Industry Solutions:Bearing units:Bearing units:NOT_COMPLETE"].append(page_product_link)
        # print(page_product_link)
    with open('bearing_links.json', 'w') as f:
        json.dump(product_links, f)

def get_products_groove(html):
    product_links = {}
    with open('groove_links.json') as f:
        product_links = json.load(f)
    soup = BeautifulSoup(html, "html.parser")
    page_product_links = soup.findAll("a", {"class": "is-product-short-label"})
    for page_product_link in page_product_links:
        page_product_link = page_product_link['href']
        if page_product_link not in product_links["Home e-Shop:Industry Solutions:Bearing units:Bearing units"]:
            product_links["Home e-Shop:Industry Solutions:Bearing units:Bearing units"].append(page_product_link)
        print(page_product_link)
    with open('groove_links.json', 'w') as f:
        json.dump(product_links, f)


def bearing(sel):
    link = "https://eshop.ntn-snr.com/en/Bearing-units-2246720.html"
    sel.get(link)
    # for d_1 in range(50,70,10):
    #     d_2 = d_1 + 10
    #     try:
    #         nav = sel.find_element_by_xpath("//button[@class='large button hide-for-xlarge']")
    #         nav.click()
    #         time.sleep(0.5)
    #     except:
    #         pass
    #     shaft_diameter_label = sel.find_elements_by_xpath("//*[@class='accordion-title' and @role='tab']")[4]
    #     shaft_diameter_label.click()
    #     time.sleep(0.5)
    #     begin_diameter = sel.find_elements_by_xpath("//input[@type='text' and @placeholder='mm']")[0]
    #     begin_diameter.clear()
    #     begin_diameter.send_keys(d_1)
    #     end_diameter= sel.find_elements_by_xpath("//input[@type='text' and @placeholder='mm']")[1]
    #     end_diameter.clear()
    #     end_diameter.send_keys(d_2)
    #     # submit = sel.find_element_by_xpath("//input[@class='button rangeSubmit']")
    #     # submit.click()
    #     types = ['Flanged units', 'Pillow block units', 'Take-up cartridge Hanger']
    #     lockings = ['Set screw', 'Excentric locking collar', 'Adapter sleeve']

    #     for t in types:
    #         try:
    #             time.sleep(5)
    #             sel.find_element_by_xpath("//label[@for='{}']".format(t)).click()
    #         except:
    #             sel.find_elements_by_xpath("//*[@class='accordion-title' and @role='tab']")[1].click()
    #             time.sleep(1)
    #             sel.find_element_by_xpath("//label[@for='{}']".format(t)).click()
    #         time.sleep(1)
    #         for l in lockings:
    #             try:
    #                 sel.find_element_by_xpath("//label[@for='{}']".format(l)).click()
    #                 time.sleep(1)
    #             except:
    #                 sel.find_elements_by_xpath("//*[@class='accordion-title' and @role='tab']")[2].click()
    #                 time.sleep(1)
    #                 sel.find_element_by_xpath("//label[@for='{}']".format(l)).click()
    #             time.sleep(1)
    #             while True:
    #                 try:
    #                     html = sel.page_source
    #                     get_products(html)
    #                     sel.find_element_by_xpath("//a[@rel='next']").click()
    #                     time.sleep(0.5)
    #                 except:
    #                     break
    #             try:
    #                 time.sleep(1)
    #                 sel.find_element_by_xpath("//label[@for='{}']".format(l)).click()
    #                 print("closing")
    #             except:
    #                 sel.find_elements_by_xpath("//*[@class='accordion-title' and @role='tab']")[2].click()
    #                 time.sleep(1)
    #                 print("closing_2")
    #                 sel.find_element_by_xpath("//label[@for='{}']".format(l)).click()
    #         try:
    #             time.sleep(5)
    #             print("1ST CLOSEDDDDDDDDDDDDD")
    #             sel.find_element_by_xpath("//label[@for='{}']".format(t)).click()
    #             time.sleep(2)
    #         except:
    #             print("CLOSEDDDDDDDDDDDDDDDDDDDDDddd")
    #             sel.find_elements_by_xpath("//*[@class='accordion-title' and @role='tab']")[1].click()
    #             time.sleep(2)
    #             sel.find_element_by_xpath("//label[@for='{}']".format(t)).click()
    #             time.sleep(1)
    #     time.sleep(5)

    d_1 = 70
    d_2 = 500
    try:
        nav = sel.find_element_by_xpath("//button[@class='large button hide-for-xlarge']")
        nav.click()
        time.sleep(0.5)
    except:
        pass
    shaft_diameter_label = sel.find_elements_by_xpath("//*[@class='accordion-title' and @role='tab']")[4]
    shaft_diameter_label.click()
    time.sleep(0.5)
    begin_diameter = sel.find_elements_by_xpath("//input[@type='text' and @placeholder='mm']")[0]
    begin_diameter.send_keys(d_1)
    end_diameter= sel.find_elements_by_xpath("//input[@type='text' and @placeholder='mm']")[1]
    end_diameter.clear()
    end_diameter.send_keys(d_2)
    submit = sel.find_element_by_xpath("//input[@class='button rangeSubmit']")
    submit.click()
    while True:
        try:
            html = sel.page_source
            get_products(html)
            sel.find_element_by_xpath("//a[@rel='next']").click()
            time.sleep(0.5)
        except:
            break


def groove_ball(sel):
    link = "https://eshop.ntn-snr.com/en/Single-row-deep-groove-ball-bearings-2246325.html"
    sel.get(link)
    for d_1 in range(20,60,20):
        d_2 = d_1 + 20
        try:
            nav = sel.find_element_by_xpath("//button[@class='large button hide-for-xlarge']")
            nav.click()
            time.sleep(0.5)
        except:
            pass
        shaft_diameter_label = sel.find_elements_by_xpath("//*[@class='accordion-title' and @role='tab']")[5]
        shaft_diameter_label.click()
        time.sleep(1)
        try:
            begin_diameter = sel.find_elements_by_xpath("//input[@type='text' and @placeholder='mm']")[0]
            begin_diameter.clear()
            begin_diameter.send_keys(d_1)
            end_diameter= sel.find_elements_by_xpath("//input[@type='text' and @placeholder='mm']")[1]
            end_diameter.clear()
            end_diameter.send_keys(d_2)
        except:
            shaft_diameter_label = sel.find_elements_by_xpath("//*[@class='accordion-title' and @role='tab']")[5]
            shaft_diameter_label.click()
            time.sleep(1)
            begin_diameter = sel.find_elements_by_xpath("//input[@type='text' and @placeholder='mm']")[0]
            begin_diameter.clear()
            begin_diameter.send_keys(d_1)
            end_diameter= sel.find_elements_by_xpath("//input[@type='text' and @placeholder='mm']")[1]
            end_diameter.clear()
            end_diameter.send_keys(d_2)
        submit = sel.find_element_by_xpath("//input[@class='button rangeSubmit']")
        submit.click()
        while True:
            try:
                html = sel.page_source
                get_products_groove(html)
                sel.find_element_by_xpath("//a[@rel='next']").click()
                time.sleep(2)
            except:
                break
    
    d_1 = 60
    d_2 = 900
    try:
        nav = sel.find_element_by_xpath("//button[@class='large button hide-for-xlarge']")
        nav.click()
        time.sleep(0.5)
    except:
        pass
    shaft_diameter_label = sel.find_elements_by_xpath("//*[@class='accordion-title' and @role='tab']")[5]
    shaft_diameter_label.click()
    time.sleep(0.5)
    begin_diameter = sel.find_elements_by_xpath("//input[@type='text' and @placeholder='mm']")[0]
    begin_diameter.send_keys(d_1)
    end_diameter= sel.find_elements_by_xpath("//input[@type='text' and @placeholder='mm']")[1]
    end_diameter.clear()
    end_diameter.send_keys(d_2)
    submit = sel.find_element_by_xpath("//input[@class='button rangeSubmit']")
    submit.click()
    while True:
        try:
            html = sel.page_source
            get_products_groove(html)
            sel.find_element_by_xpath("//a[@rel='next']").click()
            time.sleep(0.5)
        except:
            break




def driver():
    sel = webdriver.Chrome('./chromedriver')
    # bearing(sel)
    groove_ball(sel)
    

if __name__ == "__main__":
    link_1 = "https://eshop.ntn-snr.com/en/Single-row-deep-groove-ball-bearings-2246325.html"
    driver()