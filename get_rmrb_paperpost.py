#!/usr/bin/env python2
# -*- coding: UTF-8 -*- 

from bs4 import BeautifulSoup
import requests
import codecs
import HTMLParser
import time
import sys
import itchat
reload(sys)
sys.setdefaultencoding('utf8')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'}

def create_hyper_links_rmrb():
    
    if len(sys.argv) < 2:
        ymd = time.localtime()
        rmrb_year = str(ymd[0])
        rmrb_month = str(ymd[1])
        rmrb_day = str(ymd[2])
        if len(rmrb_month) < 2:
            rmrb_month = "0" + rmrb_month
        if len(rmrb_day) < 2:
            rmrb_day = "0" + rmrb_day
        rmrb_date = rmrb_year + "-" + rmrb_month + "-" + rmrb_day
        rmrb_link = "http://paperpost.people.com.cn/all-rmrb-" + rmrb_date + ".html"
        return rmrb_link
    else:
        rmrb_link = "http://paperpost.people.com.cn/all-rmrb-" + sys.argv[1] + ".html"
        return rmrb_link
   

#u"获取源码中得超链接"
def get_hyper_links_rmrb():

    url = create_hyper_links_rmrb()
    try:
        r = requests.get(url, headers = headers)
        soup = BeautifulSoup(r.content, "html.parser")
        p = soup.find_all('a')
        links = []
        
        for i in p:
            rmrb_article = i.get_text().replace("\r\n", "")
            rmrb_link = get_short_url(i.get('href'))
            rmrb_article_link = rmrb_article + '\n' + rmrb_link
            links.append(rmrb_article_link)
        return links
    except Exception, e:
            print str(e)


def write_into_files():
    
    try: 
        links = get_hyper_links_rmrb()
        for i in links:
            f = open("rmrb",'a')
            f.write(i)
            f.write("\n") 
            f.close()  

    except Exception,e:
        print str(e)
        return None


def itchat_send():

    sms = get_hyper_links_rmrb()
    sms_text = "\n".join(sms)
    itchat.auto_login()
    name = itchat.search_friends(name = 'Mao')
    Mao = name[0]["UserName"]
    itchat.send_msg(sms_text, toUserName = Mao)


def get_short_url(url):
    """
    获取百度短网址
    @param url: {str} 需要转换的网址
    @return: {str} 成功：转换之后的短网址，失败：原网址
    """
    api = "http://dwz.cn/admin/create"
    data = {
        "url": url
    }
    response = requests.post(api, json=data)
    if response.status_code != 200:
        return url
    result = response.json()
    code = result.get("Code")
    if code == 0:
        return result.get("ShortUrl")
    else:
        return url


def main():

    try:
        write_into_files()
        itchat_send()
    except Exception, e:
        print str(e)

if __name__ == "__main__":
    main()  