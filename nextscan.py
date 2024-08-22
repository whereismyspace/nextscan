#!/usr/bin/env python3

import re
import requests
from bs4 import BeautifulSoup

first_get_link_lists = []

def get_method_link_handler2(http_link):
    rep = requests.get(http_link)
    soup = BeautifulSoup(rep.text,"html5lib")
    link = soup.select('a[href]')
    for each in link:
        searchObj = re.search('http.*">',str(each))
        if searchObj:
            if url in searchObj.group() and searchObj.group()[:11] in url:
                #print(searchObj.group().split('"')[0])
                get_type_link = searchObj.group().split('"')[0]
                if get_type_link not in first_get_link_lists:
                    first_get_link_lists.append(get_type_link)
                    print(get_type_link)
                    get_method_link_handler1(get_type_link)

def get_method_link_handler1(http_link):
    rep = requests.get(http_link)
    soup = BeautifulSoup(rep.text,"html5lib")
    link = soup.select('a[href]')
    for each in link:
        searchObj = re.search('http.*">',str(each))
        if searchObj:
            if url in searchObj.group() and searchObj.group()[:11] in url:
                #print(searchObj.group().split('"')[0])
                get_type_link = searchObj.group().split('"')[0]
                if get_type_link not in first_get_link_lists:
                    first_get_link_lists.append(get_type_link)
                    print(get_type_link)
                    get_method_link_handler2(get_type_link)


    #print(link)


url = "https://anrakutei.jp"

rep = requests.get(url)


def url_handler(page):
    soup = BeautifulSoup(page,"html5lib")
    link = soup.select('a[href]')
    #http = link.find_all(href="http")
    #print(link)
    for each in link:
        searchObj = re.search('http.*">',str(each))
        if searchObj:
            if url in searchObj.group() and searchObj.group()[:11] in url:
                print(searchObj.group().split('"')[0])
                get_method_link_handler1(searchObj.group().split('"')[0])
    #print(http)

url_handler(rep.text)

print(first_get_link_lists)
