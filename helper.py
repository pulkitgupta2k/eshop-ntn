import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint
from datetime import datetime
import csv

def getSoup(link):
    req = requests.get(link)
    html = req.content
    soup = BeautifulSoup(html, "html.parser")
    return soup

def download_img(visual, name):
    req = requests.get(visual)
    open("images/{}".format(name), "wb").write(req.content)

def download_pdf(pdf_link, name):
    req = requests.get(pdf_link)
    open("pdfs/{}".format(name), "wb").write(req.content)

def tabulate(csvfile, matrix):
    with open(csvfile, "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(matrix)

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
    try:
        last_page = soup.find("a", {"class": "link last-page"})['href'].split("=")[-1]
    except:
        last_page = "1"
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
            product_links.append(page_product_link)
    result[key] = product_links
    return result

def get_product_inf(cat, link):
    result = []
    soup = getSoup(link)
    item_code = soup.find("span", {"itemprop":"name"}).text.strip()
    cats = cat.split(":")
    criteria = []
    value = []
    units = []
    brand = ""
    names = []
    section = []
    for i in range(0, 3):
        try:
            table = soup.findAll("table",{"class":"product-features-table"})[i]
            table_rows = table.findAll("tr")
            for table_row in table_rows:
                table_row = table_row.findAll("td")
                if i==0:
                    section.append("Product Definition")
                if i==1:
                    section.append("Product Performance")
                if i==2:
                    section.append("Product Dimensions")
                if not table_row[0].text == "Brand":
                    criteria.append(table_row[0].text)
                    ans = table_row[1].text.split()
                    value.append(ans[0])
                    try:
                        units.append(ans[1])
                    except:
                        units.append("")
                else:
                    brand = table_row[1].text
        except Exception as e:
            print(e)
            pass



    
    visuals = soup.find("div", {"class": "accordion-content"}).findAll("a")
    for index, visual in enumerate(visuals):
        visual = visual['href']
        name = "{}-{}-{}.jpg".format(item_code.strip(), brand.strip(), index+1)
        name = name.replace("/", "-")
        print(name)
        names.append(name)
        download_img(visual, name)
    try:
        pdf_link = soup.find("a", {"title": "Technical data"})['href']
    except:
        pdf_link = ""
    try:
        pdf_name = "{}-{}-{}.pdf".format(item_code.strip(), brand.strip(), "Datasheet")
        download_pdf(pdf_link, pdf_name)
    except:
        pdf_name = ""
    try:
        cad = soup.find("a", {"title": "View CAD drawing"})['href']
    except:
        cad = ""
    for index, c in enumerate(criteria):
        row = []
        row.append(item_code)
        row.append(c)
        row.append(value[index])
        row.append(units[index])
        row.append(brand)
        row.append(section[index])
        row.extend(names)
        row.append(cad)
        row.append(pdf_link)
        row.append(pdf_name)
        row.append(link)
        row.extend(cats)
        result.append(row)
    return result

def make_sheet():
    with open("product_links.json", "r") as f:
        products = json.load(f)
    heading = [["Item_Code","Criteria",	"Value","Units","Brand","Section","Product Image","Product Diagram","Product Diagram 1","CAD Link","PDF Link","PDF File","Direct Web Link",	"Category 1","Category 2","Category 3","Category 4","Category 5","Category 6"]]
    tabulate("results.csv", heading)
    for cat, links in products.items():
        for link in links:
            try:
                print(link)
                result = get_product_inf(cat, link)
                tabulate("results.csv",result)
            except Exception as e:
                print(e)
                pass

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
    # get_links_driver()
    get_product_inf("Home e-Shop:Industry Solutions:Ball bearings:Radial ball bearings:Single row deep groove ball bearings","https://eshop.ntn-snr.com/en/16003-16C3-689756.html")
    # make_sheet()