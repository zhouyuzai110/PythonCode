# -*- coding: UTF-8 -*-
import os
from bs4 import BeautifulSoup

file_path = "C:/Users/saber/Desktop/pythonscript/"


def get_file_name(file_path: str) -> str:
    # 确保 file_path 变量已定义且包含正确的路径
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The path {file_path} does not exist.")

    file_name_list: list[str] = os.listdir(file_path)
    found_file: str = None
    for i in file_name_list:
        # 只检查文件名（排除文件夹），假设你只想要 .txt 文件，可以根据需求更改文件扩展名
        if i.startswith('bookmarks_2022'):
            found_file = i
            break

    return found_file


def parse_bookmarks(input_file_path: str) -> list[str]:
    """
    从给定文件路径中解析HTML内容并返回一个由干净文本链接组成的列表。
    """
    file_name = get_file_name(input_file_path)
    try:
        with open(file_name, 'r', encoding='utf-8') as bookmark_file:
            soup = BeautifulSoup(bookmark_file, "html.parser")
        anchor_tags = soup.find_all('a')
        # print(anchor_tags)
    except Exception as e:
        print(str(e))
        return None

    clean_links: list[str] = []
    for tag in anchor_tags:
        link_url = tag.get('href')
        link_text = tag.get_text()
        clean_links.append("- [" + link_text + "](" + link_url + ")\n")
    return clean_links


def main():
    clean_links = parse_bookmarks(file_path)
    with open('bookmark_cleaned', 'w', encoding='utf-8') as f:
        f.writelines(clean_links)


if __name__ == '__main__':
    main()
