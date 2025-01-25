#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import requests
import codecs

import time, os
import json

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'
}
URL = 'http://distrowatch.com/'


#u"获取源码中得超链接"
def get_source(url):

    try:
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content, "html.parser")
        # print(r.content)
        mingci = soup.find_all('th', class_='phr1')
        # for i in mingci:
        # print i.get_text()
        distr = soup.find_all('td', class_='phr2')
        # for j in distr:
        # print j.get_text()
        dianji = soup.find_all('td', class_='phr3')
        # for k in dianji:
        # print k.get_text()

        for item in range(0, len(mingci)):
            print(mingci[item].get_text(), distr[item].get_text(), dianji[item].get_text())

    except (Exception, e):
        print(str(e))
        return None


get_source(URL)
