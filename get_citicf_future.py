from turtle import title
from bs4 import BeautifulSoup
import requests
import os
import sys
import time
import json

cookie = 'CITICSFID=4e380633-9498-43f7-a22e-0da4a3f14e47; __jsluid_s=3aca0e0c59ef31d6187d6a5233eb8e67; __jsluid_h=4392e93b61b0ee095e66c3b12db33ac0; Hm_lvt_eb9b2943105704fc985fd700527c1a9e=1667274225,1669780424; Hm_lpvt_eb9b2943105704fc985fd700527c1a9e=1669780998'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'cookie': cookie
}
item_code = '0001070205'
down_load_path = "C:/Users/saber/Desktop/pythonscript/futures/"
page_baseurl = 'https://www.citicf.com/e-futures/research/getArticles?code=%s&page=' % item_code
link_baseurl = 'https://www.citicf.com/e-futures/content/%s/' % item_code
download_baseurl = 'https://www.citicf.com'


def write_into_file(path, target_content):
    with open(path, 'wb') as write_file:
        write_file.write(target_content)


def get_link_list(url):
    r = requests.get(url, headers=headers, verify=False)
    soup_json = json.loads(str(BeautifulSoup(r.content, "html.parser")))
    content = soup_json.get("data").get("result").get("content")
    id_title_map = list(map(proc_dict, content))
    return id_title_map


def proc_dict(dict):
    item = []
    id = dict.get('id')
    title = proc_title(dict.get('title'))
    item.append(id)
    item.append(title)
    return item


def proc_title(title):
    if '——' in title:
        title_split = title.split('——')
        re_title = title_split[0].replace('】', '——' + title_split[-1] + '】')
        return re_title
    else:
        return title


def get_pdf(url, title):

    r = requests.get(url, headers=headers, verify=False)
    soup = BeautifulSoup(r.content, "html.parser")
    href = soup.find('div', {'class': 'detailed-download'}).find('a').get('href')
    down_link = download_baseurl + href
    PDF = requests.get(url=down_link, headers=headers, verify=False).content
    write_into_file(down_load_path + title, PDF)


def check_uniq(name, name_list):
    if name not in name_list:
        return True


def main():
    name_list = os.listdir(down_load_path)
    for i in range(1, 3):
        page_link = page_baseurl + str(i)
        link_list = get_link_list(page_link)
        for link in link_list:
            url = link_baseurl + str(link[0])
            title = link[1] + '.pdf'
            if check_uniq(title, name_list):
                print(url)
                get_pdf(url, title)


if __name__ == '__main__':
    main()
