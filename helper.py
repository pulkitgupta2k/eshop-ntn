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


def driver():
