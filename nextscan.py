#!/usr/bin/env python3

import re
import requests
from bs4 import BeautifulSoup

class Url_handler(object):

    first_get_link_lists = []

    def __init__(self,url):
        self.url = url

    def link(self):
        self.rep = requests.get(self.url)
        self.soup = BeautifulSoup(self.rep.text,"html5lib")
        self.link = self.soup.select('a[href]')


        def link_handler2(http_link):
            rep = requests.get(http_link)
            soup = BeautifulSoup(rep.text,"html5lib")
            link = soup.select('a[href]')
            for each in link:
                searchObj = re.search('http.*">',str(each))
                if searchObj:
                    if self.url in searchObj.group() and searchObj.group()[:11] in self.url:
                        #print(searchObj.group().split('"')[0])
                        get_type_link = searchObj.group().split('"')[0]
                        if get_type_link not in self.first_get_link_lists:
                            self.first_get_link_lists.append(get_type_link)
                            #print(get_type_link)
                            link_handler1(get_type_link)



        def link_handler1(http_link):
            rep = requests.get(http_link)
            soup = BeautifulSoup(rep.text,"html5lib")
            link = soup.select('a[href]')
            for each in link:
                searchObj = re.search('http.*">',str(each))
                if searchObj:
                    if self.url in searchObj.group() and searchObj.group()[:11] in self.url:
                        #print(searchObj.group().split('"')[0])
                        get_type_link = searchObj.group().split('"')[0]
                        if get_type_link not in self.first_get_link_lists:
                            self.first_get_link_lists.append(get_type_link)
                            #print(get_type_link)
                            #get_method_link_handler1(get_type_link)
                            link_handler2(get_type_link)


        for each in self.link:
            searchObj = re.search('http.*">',str(each))
            if searchObj:
                if self.url in searchObj.group() and searchObj.group()[:11] in self.url:
                    #print(searchObj.group().split('"')[0])
                    link_handler1(searchObj.group().split('"')[0])

        self.get_link_handler()

    def get_link_handler(self):
        for each in self.first_get_link_lists:
            if "&" in each or "=" in each or "?" in each:
                print(each)
       


url_handler = Url_handler("https://anrakutei.jp")
url_handler.link()

    
"""
first_get_link_lists = []

# get_method_link_handler1 和 2 相互调用，递归获取网站链接
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
                    #print(get_type_link)
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
                    #print(get_type_link)
                    get_method_link_handler2(get_type_link)


    #print(link)


url = "https://anrakutei.jp"

rep = requests.get(url)


def url_handler1(page):
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

url_handler1(rep.text)

#print(first_get_link_lists)
for each in first_get_link_lists:
    if "&" in each or "?" in each or "=" in each:
        print(each)
    else:
        pass
"""
