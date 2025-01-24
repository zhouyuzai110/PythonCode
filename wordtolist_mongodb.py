from docx import Document
from docx.enum.style import WD_STYLE_TYPE

# 文章标题
# 文章一级标题
# 文章二级标题
# 文章署名
# 文章副标题
# 黑体小标题

article_list = []
file_name = "学习参考第9辑-纪实、周年、综述.docx"
# file_name = "test.docx"
# styles = document.styles
# paragraph_styles = [s for s in styles if s.type == WD_STYLE_TYPE.PARAGRAPH]
# for style in paragraph_styles:
#     print(style.name)
def create_word_paragraph_text(file_name):
    paragraph_list = []
    document = Document(file_name)
    paragraphs = document.paragraphs
    for paragraph in paragraphs:
        if paragraph.style.name == "文章标题":
            paragraph_list.append("split" + paragraph.text)
        else:
            paragraph_list.append(paragraph.text)
    paragraph_text = 'fffff'.join(paragraph_list)
    return paragraph_text


def create_article_dict(content):
    content_list = content.split("fffff")
    content_dict = {
        'title':content_list[0],
        'content':content_list[1:]
    }
    return content_dict


def create_article_list(paragraph_text):
    article_list = []
    articles = paragraph_text.split("split")
    for article in articles:
        # print(article)
        article_dict = create_article_dict(article)
        article_list.append(article_dict)
    return article_list

paragraph_text = create_word_paragraph_text(file_name)
article_list = create_article_list(paragraph_text)
# print(article_list)
for item in article_list:
    print(item['title'])