import os
from docx import Document

# 文章标题
# 文章一级标题
# 文章二级标题
# 文章署名
# 文章副标题
# 黑体小标题

basedir = r'C:\Users\saber\Desktop\pythonscript\xxck'


def file_list(dir):
    return [os.path.join(dir, fn) for fn in os.listdir(dir)]


def add_file_name(filename, target_file):
    with open(target_file, 'a', encoding='utf-8') as file:
        target_line = '# ' + filename + '\n'
        file.write(target_line)


def create_word_paragraph_text_list(file_name: str) -> list:
    # 创建word字符串列表，包含标题内容，每一篇文章用字典保存
    file_paragraph_list: list[dict] = []
    # 打开文档
    document: Document = Document(file_name)
    # 获取文档中的段落
    paragraphs: list[Paragraph] = document.paragraphs
    # 文章可写状态控制
    content_list_writealbe: bool = False
    article_dict_writealbe: bool = False
    article_dict: dict[str, Union[str, list[str]]] = {}
    content_list: list[str] = []
    # 遍历每个段落
    for paragraph in paragraphs:
        # 如果当前段落的样式为文章标题
        if paragraph.style.name == "文章标题":
            # 如果可写状态开关打开
            if article_dict_writealbe:
                # 将文章内容添加到字典中
                article_dict['content'] = [x.replace('\n', '') + '\n\n' + '' for x in content_list if x != '']
                # 将字典添加到列表中
                file_paragraph_list.append(article_dict)
                # 上传上一篇文章并清空字典，加入新的文章标题
                article_dict = {}
                content_list = []
                # 设置新的文章标题
                article_dict['title'] = '## ' + paragraph.text.replace('\n', '') + '\n\n'
                # print(article_dict)
                # article_dict_writealbe = False
            else:
                # 遇到第一个标题时操作，并打开可操作开关
                article_dict['title'] = '## ' + paragraph.text.replace('\n', '') + '\n\n'
                # print(article_dict['title'])
                article_dict_writealbe = True
                content_list_writealbe = True
            continue
        # 如果可写状态开关打开
        if content_list_writealbe:
            # 如果当前段落的样式为黑体小标题
            if paragraph.style.name == "黑体小标题" or paragraph.style.name == "黑体小标题正":
                # 将黑体小标题添加到列表中
                content_list.append('**' + paragraph.text + '**')
            # 如果当前段落的样式为文章一级标题
            elif paragraph.style.name == "文章一级标题":
                # 将一级标题添加到列表中
                content_list.append('### ' + paragraph.text)
            # 如果当前段落的样式为文章二级标题
            elif paragraph.style.name == "文章二级标题":
                # 将二级标题添加到列表中
                content_list.append('#### ' + paragraph.text)
            else:
                # 将普通文本添加到列表中
                content_list.append(paragraph.text)

    # 将文章内容添加到字典中
    article_dict['content'] = [x.replace('\n', '') + '\n\n' + '' for x in content_list if x != '']
    # 将字典添加到列表中
    file_paragraph_list.append(article_dict)
    # print(file_paragraph_list)
    return file_paragraph_list


def write_into_md(filename, content_list):
    with open(filename, 'w', encoding='utf-8') as file:
        for item in content_list:
            # print(item)
            # print(item['title'])
            file.write(item['title'])
            file.writelines(item['content'])


def main():
    for file in file_list(basedir):
        if 'md' not in file:
            filename = file.replace('.docx', '').replace('C:/Users/saber/Desktop/pythonscript/xxck\\', '') + '.md'
            content_list = create_word_paragraph_text_list(file)
            write_into_md(filename, content_list)


if __name__ == '__main__':
    main()
