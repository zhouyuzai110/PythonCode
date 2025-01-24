import requests
from bs4 import BeautifulSoup


class WebPageScraper:

    def __init__(self, url):
        self.url = url
        self.response = None
        self.soup = None

    def fetch_page(self):
        try:
            # 发送GET请求
            self.response = requests.get(self.url)
            # 检查响应状态码是否为200（表示成功）
            if self.response.status_code == 200:
                self.soup = BeautifulSoup(self.response.text, 'html.parser')
        except requests.exceptions.RequestException as e:
            print(f"Error fetching the page: {e}")

    def extract_data(self):
        if self.soup is not None:
            # 标题通常位于HTML中的<title>标签内
            title = self.soup.find('title').text.strip() if self.soup.title else None

            # 主要内容可能需要根据实际网页结构来定位
            main_content = self._extract_main_content()

            # 副标题可能存在于自定义类名或属性的元素中，这里假设在一个<h2>标签下
            sub_title = self.soup.find('h2').text.strip() if self.soup.h2 else None

            # 作者信息可能在<meta>标签或者文章内的某个特殊标记中，这里假设在一个<span class="author">标签下
            author = self.soup.find('span', class_='author').text.strip() if self.soup.find('span', class_='author') else None

            return {
                'title': title,
                'main_content': main_content,
                'sub_title': sub_title,
                'author': author,
            }
        else:
            return {}

    def _extract_main_content(self):
        # 这里是抽象方法，因为每个网页的内容抽取方式可能不同
        # 您需要根据实际网页DOM结构编写相应的逻辑
        # 示例：如果主要内容在id为'article-body'的<div>标签内
        main_content_element = self.soup.find('div', id='article-body')
        if main_content_element:
            return main_content_element.get_text().strip()
        else:
            return None


# 使用示例
url = "http://example.com/some-webpage"
scraper = WebPageScraper(url)
scraper.fetch_page()
data = scraper.extract_data()
print(data)
