import os


def count_files_in_all_subfolders(root_path):
    """
    递归统计指定文件夹及其所有子文件夹中的文件数量
    """
    if not os.path.isdir(root_path):
        return 0

    total = 0
    try:
        for entry in os.listdir(root_path):
            path = os.path.join(root_path, entry)
            if os.path.isfile(path):
                total += 1
            elif os.path.isdir(path):
                total += count_files_in_all_subfolders(path)
    except PermissionError:
        print(f"没有权限访问文件夹: {root_path}")
        return 0

    return total


def count_top_level_folders_and_files(root_path):
    """
    统计root_path目录下各个顶级子文件夹及其所有子文件夹中的文件数量
    """
    if not os.path.isdir(root_path):
        print(f"路径 '{root_path}' 不存在或不是一个文件夹")
        return []

    # 获取root_path下的所有条目
    entries = os.listdir(root_path)

    # 过滤出文件夹并统计文件数量
    results = []
    for entry in entries:
        folder_path = os.path.join(root_path, entry)
        if os.path.isdir(folder_path):
            file_count = count_files_in_all_subfolders(folder_path)
            results.append((entry, file_count))

    return results


if __name__ == '__main__':
    # 替换为你想要统计的文件夹路径
    path_to_check = r'E:\vitepress\docs\.vitepress\dist'
    results = count_top_level_folders_and_files(path_to_check)

    if results:
        print(f"在 '{path_to_check}' 下的顶级文件夹及其文件数量：")
        for folder, count in results:
            print(f"{folder}: {count} 个文件")
