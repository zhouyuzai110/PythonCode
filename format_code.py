import os
import re
import sys


def format_code(target_file: str, position: int = 40, target_code: str = '#', target_num: int = 2) -> None:
    """
    格式化代码文件中的注释位置。

    该函数打开指定的代码文件，读取每行内容，然后将指定符号（如'#'）的前导空格增加到指定的数量（如40）。
    这样做的目的是为了标准化代码中的注释位置，使其在视觉上更加统一和整洁。

    参数:
    target_file: str - 需要格式化的代码文件的路径。
    position: int - 注释符号应该对齐到的列位置，默认为40。
    target_code: str - 需要格式化的注释符号，默认为'#'。
    target_num: int - 注释符号前应有的空格数量，默认为2。

    返回:
    无返回值，直接将格式化后的代码写回原文件。
    """
    # 以读取模式打开目标文件，并指定编码为utf-8
    with open(target_file, "r", encoding='utf-8') as file:
        # 读取文件所有内容，并按行分割成列表
        lines: list[str] = file.readlines()
        # 初始化一个列表，用于存储格式化后的行
        formatted_lines: list[str] = []
        # 遍历文件的每一行
        for item in lines:
            # 初始化计数器，用于统计注释符号前的空格数量
            start_num = 0
            # 遍历当前行的每一个字符
            for i, char in enumerate(item):
                # 如果当前字符是目标注释符号，则计数器加一
                if char == target_code:
                    start_num += 1
                # 如果空格数量达到目标值，则进行格式化
                elif start_num == target_num:
                    # 构造新行，将注释符号前的空格增加到指定位置
                    new_code = item[:i - 1] + ' ' * (position - i) + item[i - 1:]
                    # 将格式化后的行添加到结果列表
                    formatted_lines.append(new_code)
                    # 终止内层循环，处理下一行
                    break
    # 以写入模式打开目标文件，并指定编码为utf-8
    with open(target_file, "w", encoding='utf-8') as file:
        # 将格式化后的行写回文件
        file.writelines(formatted_lines)


format_code('douyinjson', position=40, target_code='#', target_num=2)
