import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint
from datetime import datetime


def getSoup(link):
    req = requests.get(link)
    html = req.content
    soup = BeautifulSoup(html, "html.parser")
    return soup


def get_category(categories, link):
    soup = getSoup(link)
    soup = soup.find("ul", {"id": "shelfList"})
    if soup == None:
        print(link)
        categories.append(link)
        return categories
    items = soup.findAll("div", {"class": "product-list-item-content-wrapper"})
    # categories.extend(items)
    for item in items:
        item = item.find("a")['href']
        get_category(categories, item)


def get_product_links(link):
    result = {}
    product_links = []
    categories = []
    soup = getSoup(link)
    last_page = soup.find("a", {"class": "link last-page"})['href'].split("=")[-1]
    headers = soup.find("ul", {"class": "thread breadcrumbs"}).findAll("li")
    for header in headers:
        header = header.text.strip()
        categories.append(header)
    key = ":".join(categories)
    print(key)
    for i in range(1, int(last_page)+1):
        page_link = "https://eshop.ntn-snr.com/en/Single-row-deep-groove-ball-bearings-2246325.html?catalogParam%5Bpage%5D={}".format(i)
        page_soup = getSoup(page_link)
        page_product_links = page_soup.findAll("a", {"class": "is-product-short-label"})
        for page_product_link in page_product_links:
            page_product_link = page_product_link['href']
            print(page_product_link)
            product_links.extend(page_product_links)
    result[key] = page_product_links
    return result

def get_category_driver():
    link = "https://eshop.ntn-snr.com/en/Industry-Solutions-12078.html"
    categories = []
    categories_json = {}
    get_category(categories, link)
    categories_json["cat"] = categories
    with open("categories.json", "w") as f:
        json.dump(categories_json, f)

def get_links_driver():
    with open("categories.json", "r") as f:
        cats = json.load(f)["cat"]
    with open("product_links.json", "r") as f:
        product_links = json.load(f)
    for cat in cats:
        result = get_product_links(cat)
        product_links[list(result.keys())[0]] = list(result.values())[0]
        with open("product_links.json", "w") as f:
            json.dump(product_links, f)

def driver():
    # get_category_driver()
    # get_product_links("https://eshop.ntn-snr.com/en/Single-row-deep-groove-ball-bearings-2246325.html")
    get_links_driver()
