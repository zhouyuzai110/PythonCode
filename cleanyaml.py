import os
import re

directory = r"C:\Users\saber\Desktop\pythonscript\formatmd\阴阳和谐"


def rename_md_files(directory: str):
    """
    重命名Markdown文件的函数,把文件名中的空格、%删掉  

    参数:
    directory (str): Markdown文件所在的目录路径

    返回:
    无
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                filepath: str = os.path.join(root, file)
                new_name: str = file.replace(' ', '').replace('%', '')
                os.rename(filepath, os.path.join(root, new_name))
                print(filepath)
                print(new_name)


def process_md_files(directory: str):
    """
    处理Markdown文件的函数

    参数:
    directory (str): Markdown文件所在的目录路径

    返回:
    无
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                filepath: str = os.path.join(root, file)

                with open(filepath, 'r+', encoding='utf-8') as f:
                    content: str = f.read()

                    # 匹配并提取title区块的内容
                    match: re.Match = re.search(r'---\n.*?\n---', content, re.DOTALL)
                    if match:
                        title_match: re.Match = re.search(r'title: (.*)', match.group(0))
                        if title_match:
                            new_title_line: str = "# " + title_match.group(1) + "\n"
                            content = content.replace(match.group(0), new_title_line)

                            # 写回处理后的完整内容
                            f.seek(0)
                            f.write(content)
                            f.truncate()

                            print(f"Processed file: {filepath}")


# 调用函数，开始处理指定目录下的Markdown文件
process_md_files(directory)
