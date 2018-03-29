# -*- coding: UTF-8 -*- 

from bs4 import BeautifulSoup
import requests
import codecs
import time, os

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'}
proxies = {'http': 'socks5://127.0.0.1:1080'}

origin_url = 'http://92.t9p.today/'        

#u"获取源码中得超链接"
def get_hyper_links(url):

    try:
    	links = []
        r = requests.get(url, headers = headers, proxies = proxies)
        soup = BeautifulSoup(r.content, "html.parser")
        title = soup.find('title').get_text()
        links.append(title)
        p = soup.find_all('img')
        for i in p:
            target_link = i.get('file')
            if target_link is not None :
                target_link = origin_url + target_link
                links.append(target_link) 
                print target_link
        return links
    except Exception,e:
        print str(e)
        return None          



def write_into_files(jpgname,url):

    conn = requests.get(url, stream = True, headers = headers, proxies = proxies) 
    f = open(jpgname,'wb')  
    f.write(conn.raw.read())  
    f.close()  




def main():
    os.chdir("/home/evas/test/cl/")
    while True:
        url = raw_input("the url is : ")
        links = get_hyper_links(url)
        title = links[0]
        print title
        total_num = len(links[1:])
        num = 1
        if links is not None:
            for link in links[1:]:
                try:
                    jpgname = title + str(time.time()) + ".jpg"
                    write_into_files(jpgname,link)
                    print('%s of %s Pic Saved!') %(num, total_num)
                    num += 1
                except Exception, e:
                    print str(e)

        
if __name__ == "__main__":

    main()  
	
	