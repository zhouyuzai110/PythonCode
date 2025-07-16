import re
import time
from typing import List, Tuple

import requests
from bs4 import BeautifulSoup


def get_chapter_links(base_url: str, proxy: dict, headers: dict) -> List[str]:
    """获取小说所有章节的链接"""
    response = requests.get(base_url, proxies=proxy, headers=headers)
    response.encoding = 'gbk'
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)
    # 查找包含章节链接的列表元素
    chapter_list = soup.find_all('dd', class_='col-md-3')
    if not chapter_list:
        print("未找到章节列表")
        return []

    links = [a.find('a').get('href') for a in chapter_list]
    print(links)
    return links


def get_chapter_content(url: str, proxy: dict, headers: dict) -> Tuple[str, str]:
    """获取单个章节的内容"""
    response = requests.get(url, proxies=proxy, headers=headers)
    response.encoding = 'gbk'
    soup = BeautifulSoup(response.text, 'html.parser')

    # 提取章节标题
    title_tag = soup.find('h1', class_='readTitle')
    chapter_title = title_tag.text.strip() if title_tag else "未知章节名"

    # 提取章节正文内容
    content_div = soup.find('div', id='htmlContent')
    if content_div:
        # 去除可能存在的广告或其他非正文内容
        for ad in content_div.find_all('div', class_='ad'):
            ad.decompose()
        chapter_text = content_div.get_text(strip=False)
    else:
        chapter_text = "无法获取章节内容"

    return chapter_title, chapter_text


def save_to_markdown(filename: str, chapters: List[Tuple[str, str]]) -> None:
    """将章节内容保存为Markdown文件"""
    with open(f'{filename}.md', 'w', encoding='utf-8') as f:
        for title, text in chapters:
            f.write(f'## {title}\n\n')
            # 每段文字之间空一行
            paragraphs = text.split('\n')
            for para in paragraphs:
                if para.strip():  # 跳过空白行
                    f.write(para.strip() + '\n\n')


def main() -> None:
    # 小说主页URL
    base_url = 'https://www.po18ee.com/book/54015/'

    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'
    }

    # SOCKS5代理设置
    proxy = {'http': 'socks5://127.0.0.1:1081', 'https': 'socks5://127.0.0.1:1081'}

    # 获取所有章节链接
    chapter_links: List[str] = get_chapter_links(base_url, proxy, headers)
    if not chapter_links:
        print("没有找到任何章节链接。")
        return

    # 准备存储章节内容
    chapters: List[Tuple[str, str]] = []

    # 遍历每个章节链接，获取内容
    for link in chapter_links:
        # 构建完整的章节URL
        url = link if link.startswith('http') else 'https://www.po18ee.com/' + link.lstrip('/')
        title, text = get_chapter_content(url, proxy, headers)
        print(f'正在抓取章节: {url}---{title}')
        chapters.append((title, text))
        time.sleep(1)

    # 以小说名称作为文件名
    novel_name_match = re.search(r'/book/(\d+)/$', base_url)
    novel_id = novel_name_match.group(1) if novel_name_match else 'novel'
    filename = f'novel_{novel_id}'

    # 保存到Markdown文件
    save_to_markdown(filename, chapters)
    print(f'小说已保存至{filename}.md')


if __name__ == '__main__':
    main()
