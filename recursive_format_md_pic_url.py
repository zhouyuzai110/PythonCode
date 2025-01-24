import os
import re
import sys
from typing import List

filepath = r"C:\Users\saber\Desktop\pythonscript\formatmd"
# filepath = r"C:\Users\saber\Desktop\pythonscript\formatmd\新建文件夹"
# filepath = r"C:\Users\saber\Downloads\OneNoteMdExporter.v1.4.0\Exports\md\数据科学-20240117 18-04\数据科学"
# filepath = r"F:\vitepress\docs\投资理财"


def clean_lines(lines: list[str]) -> list[str]:
    # 清理换行符，获取代码块的起始位置及需要添加换行的行数
    code_start = 0
    add_n: list[str] = []
    clean_more_n: list[str] = [x for x in lines if x != '\n']

    for item in clean_more_n:
        # 如果行中包含三个反引号，则表示代码块的开始或结束
        if "```" in item:
            code_start += 1
        # 如果行中包含大于符号或者以两个竖线包裹的文本，则表示引用块的开始或结束
        if ">" in item or re.match(r'^\|.*\|$', item):
            add_n.append(item)
            continue
        # 如果行以一个或多个空格紧接着换行符，则表示需要忽略该行
        if re.match(r'^\s{1,}\n$', item):
            continue
        # 如果代码块为偶数行，则在行末添加换行符；如果是奇数行，则不添加
        if code_start % 2 == 0:  # "偶数或0"
            add_n.append(item + '\n')
        else:
            add_n.append(item)
    return add_n


def change_pic_url(lines: list[str]) -> list[str]:
    # 函数用于改变图片url
    out_list: list[str] = []  # 初始化结果列表
    for item in lines:  # 遍历输入的字符串列表
        if 'http://ttnas.site:9080' in item:  # 如果字符串中包含指定的url
            item = item.replace('http://ttnas.site:9080', 'https://lskypro.ttnas.site:88')  # 将指定url替换为新的url
            out_list.append(item)  # 将处理后的字符串添加到结果列表中
            # print(item)  # 打印输出处理后的字符串（可注释掉）
        else:
            out_list.append(item)  # 如果字符串不包含指定的url，则直接将字符串添加到结果列表中
    return out_list  # 返回结果列表


def get_pic_flie(file: str, lines: List[str]) -> None:
    """
    根据给定的文件和行列表，获取包含指定文件格式的文件名。

    参数：
    file (str)：要检查的文件名
    lines (List[str])：包含文件名的列表

    返回：
    无

    """
    for item in lines:
        if 'jpg' in item or 'png' in item or 'gif' in item or 'jpeg' in item:
            print('--------------->', file)


def get_file_recursive(filepath: str) -> None:
    # 递归遍历filepath下所有文件，包括子目录

    files: List[str] = os.listdir(filepath)  # 获取文件夹下的所有文件和子文件夹
    for item in files:  # 遍历每个文件和子文件夹
        target_item: str = os.path.join(filepath, item)  # 构造目标文件夹的路径
        if os.path.isdir(target_item):  # 判断是否是子文件夹
            get_file_recursive(target_item)  # 递归调用get_file_recursive函数
        else:  # 文件夹中是文件
            print(target_item)  # 打印文件路径
            with open(target_item, 'r', encoding='utf-8') as file:  # 以只读方式打开文件
                lines: List[str] = file.readlines()  # 读取文件的每一行，并存储到lines列表中
                change_url_lines: List[str] = change_pic_url(lines)  # 调用change_pic_url函数，返回处理后的lines列表
                cleaned_lines: List[str] = clean_lines(change_url_lines)  # 调用clean_lines函数，返回处理后的change_url_lines列表
                # get_pic_file(target_item, change_url_lines)
                with open(target_item, "w", encoding='utf-8') as target_file:  # 以写入方式打开文件
                    target_file.writelines(cleaned_lines)  # 将处理后的lines列表写入文件


# get_file_recursive(filepath)
def main():
    if len(sys.argv) < 2:
        target_source = filepath
    else:
        target_source = r"{}".format(sys.argv[1])
    get_file_recursive(target_source)


if __name__ == '__main__':
    main()
