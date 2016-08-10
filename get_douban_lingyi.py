# -*- coding: UTF-8 -*- 

from bs4 import BeautifulSoup
import socket
import requests
import codecs
import time

DOUBANURL = 'http://www.douban.com/group/tomorrow/discussion?start='

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'}
 

#u"获取网页源码"
def get_page_source(url):
    try:
        r = requests.get(url, timeout = 10, headers = headers)
        return ["200",r.content]
    except Exception,e:
        print str(e)
        return [str(e),None]


#u"获取源码中得帖子名称和点击量"
def get_post_num(url):
    try:
        data = get_page_source(url)
        if data[0] == "200":
            soup = BeautifulSoup(data[1], "html.parser")
            trlist = soup.find_all('tr')
            for item in trlist:
                if len(item.contents) == 9:
                    post_title = item.contents[1].get_text()
                    post_link = item.contents[1].find('a').get('href')
                    post_view = item.contents[5].get_text()
                    douban_post = codecs.open('douban.txt', 'a', 'utf-8')
           
                    complite_word = post_title + '\t' + post_view + '\t' + post_link
                    complite_word = complite_word.replace('\n','')
                    print complite_word
                    douban_post.write(unicode(complite_word))
                    douban_post.write('\n')
                                   
    except Exception,e:
        print str(e)
          

if __name__ == "__main__":

    for page_num in range(1,1459):
        time.sleep(5)
        print '********page %s********' %(page_num)
        douban_link = DOUBANURL + str(25*page_num)
        print douban_link
        get_post_num(douban_link)
