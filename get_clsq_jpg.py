# -*- coding: UTF-8 -*- 

from bs4 import BeautifulSoup
import requests
import codecs
import time, os

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'}
proxies = {'http': 'socks5://127.0.0.1:1080'}
        

#u"获取源码中得超链接"
def get_hyper_links(url, key_words):

    try:
    	links = []
        r = requests.get(url, headers = headers)
        soup = BeautifulSoup(r.content, "html.parser")
        p = soup.find_all('input')
        for i in p:
            target_link = i.get('src')
            if target_link is not None :
                if target_link.find(key_words[0]) or target_link.find(key_words[1]) > 0:
                    if "imageView" not in target_link and "weixin" not in target_link\
                    and "330x200" not in target_link and "600x120" not in target_link\
                    and "footer" not in target_link:
                    	links.append(target_link) 
        return links
    except Exception,e:
        print str(e)
        return None          


def get_title(url):
    r = requests.get(url, headers = headers)
    soup = BeautifulSoup(r.content,"html.parser")
    title = soup.find('title').get_text()
    return title

def write_into_files(jpgname,url):

    conn = requests.get(url, stream = True, headers = headers) 
    f = open(jpgname,'wb')  
    f.write(conn.raw.read())  

    f.close()  




def main():
    os.chdir("/home/evas/test/cl/")
    while True:
        url = raw_input("the url is : ")
        links = get_hyper_links(url,["jpg","jpeg"])
        title = get_title(url)
        print title
        total_num = len(links)
        num = 1
        if links is not None:
            for link in links:
                try:
                    print link
                    jpgname = title + str(time.time()) + ".jpg"
                    write_into_files(jpgname,link)
                    print('%s of %s Pic Saved!') %(num, total_num)
                    num += 1
                except Exception, e:
                    print str(e)

        
if __name__ == "__main__":

    main()  
	
	