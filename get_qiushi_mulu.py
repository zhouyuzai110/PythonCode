import json
import re

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

re_words = ['.*摄$', '.*摄）$', '.*供图$', '\n', '\u3000', '^△.*', ' ', '.*来源：.*作者：.*', '.*新华社发$', '目 录', '目录', ' ', '新华社.*电.*', ' ']

key_words = ['点击观看视频', '共产党员网分享打印', '2020年全国两会', '2020全国两会', '决胜全面建成小康社会', '坚决打赢疫情防控阻击战', '党的二十大报告学习辅导百问']

biaodian = '。；;a\n…”!！—？：）'
origin_list = []

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

# url = 'http://www.pbc.gov.cn'

url = 'http://www.qstheory.cn/dukan/qs/2014/2024-01/01/c_1130048942.htm'


def get_qiushi(url, headers):

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")

    title = get_qiushi_title(url, soup)
    # bar.set_description('{}'.format(title.replace('aaa：', '')))
    origin_list.append(title)
    try:
        main_content = soup.find_all('p')
        for i in main_content:
            if len(i.get_text()) > 0:
                if i.find('a'):
                    target_text = '[' + i.get_text() + '](' + i.find('a').get('href') + ')'
                    origin_list.append(target_text)
                else:
                    i_text = i.get_text()
                    origin_list.append(i_text)

    except Exception as e:
        print(str(e))
        return None


def get_qiushi_title(url, soup):

    if 'dukan' in url or 'wp' in url or 'yaowen' in url or 'laigao' in url:
        title = soup.find('title').get_text().replace(' - 求是网', '').replace(' ', '').replace('\r\n', '')
        h2 = ''
        try:
            h2 = soup.find('h2').get_text().replace('\r\n', '').replace(' ', '')
        except Exception as e:
            pass
        author = soup.find_all('span', {'class': "appellation"})
        target_author = ''
        for item in author:
            if '作者：' in item.get_text():
                target_author = item.get_text().replace(' ', '').replace('作者：', '').replace('\r\n', '')
        title = 'aaa' + target_author + '：' + title + h2

    elif 'llwx' in url or 'zhuanqu' in url or 'zdwz' in url or 'qshyjx' in url:
        title = soup.find('title').get_text().replace(' - 求是网', '').replace(' ', '').replace('\r\n', '')
        div_author = soup.find('div', {'class': "headtitle"}).stripped_strings
        div_author = [text for text in div_author][-1]
        target_author = div_author.replace('来源： ', '').replace('　作者', '').replace('： ', '')
        title = 'aaa' + target_author + '：' + title

    else:
        title = soup.find('title').get_text().replace(' - 求是网', '').replace(' ', '').replace('\r\n', '')
        h2 = ''
        try:
            h2 = soup.find('h2').get_text().replace('\r\n', '').replace(' ', '')
        except Exception as e:
            pass
        author = soup.find_all('span', {'class': "appellation"})
        target_author = ''
        for item in author:
            if '作者：' in item.get_text():
                target_author = item.get_text().replace(' ', '').replace('作者：', '').replace('\r\n', '')
        title = 'aaa' + target_author + '：' + title + h2
    return title


def replace_str(item):
    for re_word in re_words:
        item = re.sub(re_word, "", item)
        for key_word in key_words:
            if item == key_word:
                item = re.sub(key_word, "", item)
    if 'aaa' in item:
        item = item.replace(item, "\n\n" + item + '\n').replace('aaa：', '## ')
    # if len(item) >= 1 and item[-1] not in biaodian:
    #     item = item.replace(item, 'bbb' + item + 'bbb')
    return item


def creat_out_list(origin_list):
    out_list = []
    for i in origin_list:
        return_item = replace_str(i)
        if return_item is not None and return_item != '':
            out_list.append(return_item)
    liebiao_quchong(out_list)
    return out_list


def liebiao_quchong(lists):
    for i in range(len(lists) + 1):
        if i < len(lists) - 1 and lists[i] == lists[i + 1]:
            lists[i] = re.sub('.*', "", lists[i])
            # lists[i + 1] = re.sub('.*', "", lists[i + 1])


def read_link():
    with open('douyinjson', 'r', encoding='UTF-8') as f:
        return f.readlines()


def write_into_file(path, target_content):
    with open(path, 'w', encoding='UTF-8') as write_file:
        write_file.writelines(target_content)


def main():
    target_link = [x.replace('\n', '') for x in read_link()]
    bar = tqdm(target_link, ncols=120)
    for item in bar:
        get_qiushi(item, headers=headers)
    out_list = creat_out_list(origin_list)
    return_out_list = [x + '\n' for x in out_list if x != '']
    write_into_file("mulu2024.md", return_out_list)


if __name__ == '__main__':
    main()
