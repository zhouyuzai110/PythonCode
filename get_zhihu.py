from bs4 import BeautifulSoup


def get_zhihu_text():

    with open('zhihu.html', 'r', encoding='utf-8', errors='ignore') as zhihu:
        soup = BeautifulSoup(zhihu.read(), "html.parser")
        text_list = [x.get_text() for x in soup.find_all('p')]
    return text_list


def main():

    for i in get_zhihu_text():
        print(i)


if __name__ == '__main__':
    main()
