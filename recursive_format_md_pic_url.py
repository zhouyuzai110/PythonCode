import os
import re
import shutil
import sys
from typing import List

from count_top_level_folder_files import count_res_files
from logger_formatter import LoggerSetup

# filepath = r"E:\PythonCode\formatmd"
# filepath = r"C:\Users\saber\Desktop\pythonscript\formatmd\新建文件夹"
# filepath = r"C:\Users\saber\Downloads\OneNoteMdExporter.v1.4.0\Exports\md\数据科学-20240117 18-04\数据科学"
# filepath = r"F:\vitepress\docs\投资理财"
filepath = r"E:\KnowledgeBase\src\KnowledgeBase"
# filepath = r"E:\KnowledgeBase\src\KnowledgeBase\矩阵幽谧\聚合书签"
logger = LoggerSetup(name=__name__).get_logger()


def clean_lines(lines: list[str]) -> list[str]:
    """
    清理多余的换行符，并保持代码块结构。
    清理换行符，获取代码块的起始位置及需要添加换行的行数
    参数:
        lines (list[str]): 原始文件内容的每一行。

    返回:
        list[str]: 处理后的文件内容。
    """
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
    """
    替换文件中的图片 URL。
    函数用于改变图片url
    参数:
        lines (list[str]): 原始文件内容的每一行。

    返回:
        list[str]: 替换 URL 后的文件内容。
    """
    out_list: list[str] = []  # 初始化结果列表
    for item in lines:  # 遍历输入的字符串列表
        if 'http://ttnas.site:9080' in item:  # 如果字符串中包含指定的url
            item = item.replace('http://ttnas.site:9080', 'https://lskypro.ttnas.site:88')  # 将指定url替换为新的url
            out_list.append(item)  # 将处理后的字符串添加到结果列表中
            # logger.info(item)  # 打印输出处理后的字符串（可注释掉）
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
            logger.info('--------------->', file)


def backup_file(file_path: str) -> None:
    """
    如果存在旧的备份文件，则删除；然后备份原始文件。

    参数:
        file_path (str): 需要备份的文件路径。
    """
    backup_path = file_path + ".bak"

    # 如果已存在同名的 .bak 文件，则删除
    if os.path.exists(backup_path):
        os.remove(backup_path)
        logger.info(f"已删除旧备份文件: {backup_path}")

    shutil.copy2(file_path, backup_path)
    logger.info(f"备份文件至: {backup_path}")


def process_file(file_path: str) -> None:
    """
    处理单个文件，包括备份、读取、清理和写入。

    参数:
        file_path (str): 需要处理的文件路径。
    """
    try:
        # 备份原始文件
        backup_file(file_path)

        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # 替换图片 URL
        changed_lines = change_pic_url(lines)
        # 清理多余换行
        cleaned_lines = clean_lines(changed_lines)

        # 写入处理后的内容
        with open(file_path, 'w', encoding='utf-8') as target_file:
            target_file.writelines(cleaned_lines)

        logger.info(f"成功处理文件: {file_path}")
    except Exception as e:
        logger.warning(f"处理文件 {file_path} 时出错: {e}")


def get_file_recursive(filepath: str) -> None:
    """
    递归遍历指定目录下的所有文件，并处理每个文件。
    递归遍历filepath下所有文件，包括子目录
    参数:
        filepath (str): 起始目录路径。
    """

    files: List[str] = os.listdir(filepath)  # 获取文件夹下的所有文件和子文件夹
    for item in files:  # 遍历每个文件和子文件夹
        target_item: str = os.path.join(filepath, item)  # 构造目标文件夹的路径
        if os.path.isdir(target_item):  # 判断是否是子文件夹
            get_file_recursive(target_item)  # 递归调用get_file_recursive函数
        else:  # 文件夹中是文件
            logger.info(f"正在处理文件: {target_item}")  # 打印文件路径
            # with open(target_item, 'r', encoding='utf-8') as file:  # 以只读方式打开文件
            #     lines: List[str] = file.readlines()  # 读取文件的每一行，并存储到lines列表中
            #     change_url_lines: List[str] = change_pic_url(lines)  # 调用change_pic_url函数，返回处理后的lines列表
            #     cleaned_lines: List[str] = clean_lines(change_url_lines)  # 调用clean_lines函数，返回处理后的change_url_lines列表
            #     # get_pic_file(target_item, change_url_lines)
            #     with open(target_item, "w", encoding='utf-8') as target_file:  # 以写入方式打开文件
            #         target_file.writelines(cleaned_lines)  # 将处理后的lines列表写入文件
            process_file(target_item)


def delete_bak_files(root_dir: str) -> None:
    """
    递归遍历指定目录，删除所有以 .bak 结尾的文件。

    参数:
        root_dir (str): 要遍历的根目录路径。
    """
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".bak"):
                file_path = os.path.join(dirpath, filename)
                try:
                    os.remove(file_path)
                    logger.info(f"已删除备份文件: {file_path}")
                except Exception as e:
                    logger.warning(f"删除文件 {file_path} 时出错: {e}")


def normalize_lines(lines: list[str]) -> list[str]:
    """
    清洗并标准化文本行列表，去除每行两端空白，并过滤空行。
    line.strip() 会移除字符串 line 的首尾空白字符（包括空格、换行 \n、制表符 \t 等）。
    如果 stripped 不是空字符串（即原始行中包含非空白内容），则将其加入结果列表 normalized；
    如果是空字符串（即原行是空行或只包含空白字符），则跳过不添加。

    参数:
        lines (list[str]): 原始文本行列表。

    返回:
        list[str]: 标准化后的文本行列表。
    """
    normalized = []
    for line in lines:
        stripped = line.strip()
        if stripped:
            normalized.append(stripped)
    return normalized


def compare_files_content(file1: str, file2: str) -> bool:
    """
    比较两个文件的文本内容是否一致，忽略空行和行首尾空白。

    参数:
        file1 (str): 第一个文件路径。
        file2 (str): 第二个文件路径。

    返回:
        bool: 内容一致则返回 True，否则返回 False。
    """
    try:
        with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
            lines1 = normalize_lines(f1.readlines())
            lines2 = normalize_lines(f2.readlines())
            return lines1 == lines2
    except Exception as e:
        logger.warning(f"比较文件 {file1} 和 {file2} 时出错: {e}")
        return False


def clean_identical_bak_files(root_dir: str) -> None:
    """
    递归遍历指定目录，删除与原始文件内容相同的 .bak 备份文件（忽略空行和空白）。

    参数:
        root_dir (str): 要遍历的根目录路径。
    """
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".bak"):
                bak_file = os.path.join(dirpath, filename)
                original_file = bak_file[:-4]  # 去掉 .bak 后缀

                if not os.path.exists(original_file):
                    logger.info(f"未找到对应原始文件，跳过: {bak_file}")
                    continue

                if compare_files_content(original_file, bak_file):
                    try:
                        os.remove(bak_file)
                        logger.info(f"已删除内容相同的备份文件: {bak_file}")
                    except Exception as e:
                        logger.info(f"删除文件 {bak_file} 时出错: {e}")
                else:
                    logger.info(f"内容不同，保留备份文件: {bak_file}")


def find_bak_files(root_dir: str) -> None:
    """
    Recursively traverse the specified directory and find all files ending with .bak.
    If any are found, print the file count and their absolute paths.

    Parameters:
        root_dir (str): Root directory to start searching from.
    """
    bak_files = []

    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".bak"):
                bak_path = os.path.join(dirpath, filename)
                bak_files.append(bak_path)

    if bak_files:
        logger.info(f"Found {len(bak_files)} .bak files:")
        for path in bak_files:
            logger.info(path)
    else:
        logger.info("No .bak files found.")


# get_file_recursive(filepath)
def main():

    if len(sys.argv) < 2:
        target_source = filepath
    else:
        target_source = r"{}".format(sys.argv[1])

    # 示例：在程序开始前删除所有 .bak 文件
    delete_bak_files(target_source)

    get_file_recursive(target_source)

    # 递归遍历指定目录，删除与原始文件内容相同的 .bak 备份文件（忽略空行和空白）。
    clean_identical_bak_files(target_source)

    # Recursively traverse the specified directory and find all files ending with .bak.
    find_bak_files(target_source)

    # 统计目录下所有文件数量
    count_res_files(target_source)


if __name__ == '__main__':

    # 启动主流程
    main()
