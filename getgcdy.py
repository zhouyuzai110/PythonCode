from bs4 import BeautifulSoup
import requests
import re


headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}

BASEURL = 'https://www.12371.cn/zxfb/'

pattern = re.compile("(item=\[\{.*)")

r = requests.get(BASEURL, headers=headers)
soup = BeautifulSoup(r.content, "html.parser")
lll = pattern.findall(str(soup))



print(lll[0].replace('item=',''))
