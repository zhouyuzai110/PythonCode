import json
import os
import re

import requests
from bs4 import BeautifulSoup

re_words = ['.*摄$', '.*摄）$', '.*供图$', '\n', '\u3000', '^△.*', ' ', '.*来源：.*作者：.*', '.*新华社发$', ' ', '新华社.*电.*']

key_words = ['点击观看视频', '共产党员网分享打印', '2020年全国两会', '2020全国两会', '决胜全面建成小康社会', '坚决打赢疫情防控阻击战', '党的二十大报告学习辅导百问']

biaodian = '。；;a\n…”!！—？：）'
origin_list = []
directory_path = 'C:/Users/saber/Desktop/pythonscript/pbc/'


def get_pbc(file):
    try:
        soup = BeautifulSoup(file, "html.parser")
        # print(soup)
        title = soup.find('title').get_text().replace(' ', '').replace('\r\n', '')
        origin_list.append('aaa' + title)
        main_content = soup.find('td', {'class': "content"}).find_all('p')
        # print(main_content)
        for i in main_content:
            # print(i)
            if len(i.get_text()) > 0:
                i_text = i.get_text()
            # else:
            #     i_text = i.find('img').get('alt')
            # if i_text == '　　延伸阅读':
            #     break
            # print(i_text)
            origin_list.append(i_text)

    except Exception as e:
        print(str(e))
        return None


def file_list(directory_path):

    contents = os.listdir(directory_path)
    return [directory_path + x for x in contents]


def replace_str(item):
    for re_word in re_words:
        item = re.sub(re_word, "", item)
        for key_word in key_words:
            if item == key_word:
                item = re.sub(key_word, "", item)
    if 'aaa' in item:
        item = item.replace(item, "\n\n" + item + 'aaa' + '\n')
    if len(item) >= 1 and item[-1] not in biaodian:
        item = item.replace(item, 'bbb' + item + 'bbb')
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


def main(directory_path):
    files = file_list(directory_path)
    print(files)
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            get_pbc(f.read())
    out_list = creat_out_list(origin_list)
    return_out_list = [x for x in out_list if x != '']
    origin_list.clear()
    for text in return_out_list:
        print(text)


if __name__ == '__main__':
    main(directory_path)
