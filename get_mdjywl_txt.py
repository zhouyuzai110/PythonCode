# -*- coding: UTF-8 -*- 

from bs4 import BeautifulSoup
import requests
import codecs

import time, os

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'}
        

#u"获取源码中得超链接"
def get_hyper_links(url):

    try:
    	links = []
        r = requests.post(url, timeout = 5, headers = headers)
        time.sleep(1)
        soup = BeautifulSoup(r.content,"html.parser")
        p = soup.find_all('a')
        for i in p:
            target_link = i.get('href')
            if target_link is not None :
                print "LINK START --->>> " + target_link
                links.append(target_link)
        return links
    except Exception,e:
        print str(e)
        return None          

def get_zhengwen_text(url):

    try:
        r = requests.get(url, timeout = 5)
        time.sleep(1)
        soup = BeautifulSoup(r.content,"html.parser")
        title = soup.find_all('h1')[-1].get_text()
        # print title
        div_text = soup.find_all('div',{'class':'bookcontent clearfix'})[0]\
                   .get_text().replace(u'　　','\n\n    ')
        # print div_text
        return [title, div_text]
    except Exception, e:
        print str(e)
        return None
    

def write_into_files(url):

    try:
        daixie = get_zhengwen_text(url)
        print "LINK DONE --->>> " + url
        title = daixie[0] + ".txt"
        daitxt = daixie[1].encode("UTF-8")
        with open(title,"w") as f:
            f.write(daitxt)
            print "The File %s Done!" % title

    except Exception, e:
        print str(e)
        return None




def main():

    url = "http://www.wddsnxn.org/mindiaojuyiwenlu/"
    links = get_hyper_links(url)
    if links is not None:
        for link in links:
            write_into_files(link)

        
if __name__ == "__main__":

    main()  
