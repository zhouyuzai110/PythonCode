import os
import shutil

# 直接在脚本中配置需要备份的文件和目标文件夹
backup_config = {
    "source_files_and_folders": [
        "E:\\PythonCode\\中国指数列表.xlsx", "C:\\Users\\saber\\.ssh", "C:\\Users\\saber\\.gitconfig", 'C:\\Users\\saber\\.condarc',
        'C:\\Users\\saber\\Documents\\Respawn\\Titanfall2\\profile\\savegames'
    ],
    "destination_folder":
    "D:\\OneDrive\\矩阵幽谧\\配置文件"
}


def backup_files_and_folders(backup_list, destination):
    """
    根据提供的列表备份文件和文件夹到指定的目标文件夹。
    如果目标文件夹中有同名文件或文件夹，则覆盖替换。
    
    :param backup_list: 源文件和文件夹路径列表
    :param destination: 目标备份文件夹路径
    """
    for src in backup_list:
        # 忽略不存在的路径
        if not os.path.exists(src):
            print(f"警告：{src} 不存在，跳过。")
            continue

        # 确定目标路径中的相对路径
        basename = os.path.basename(src)
        dest_path = os.path.join(destination, basename)

        try:
            if os.path.isdir(src):
                if os.path.exists(dest_path):
                    shutil.rmtree(dest_path)  # 删除已存在的目录树
                shutil.copytree(src, dest_path)  # 复制整个目录树
            else:
                shutil.copy2(src, dest_path)  # 复制单个文件（会覆盖同名文件）
            print(f"成功备份 {src} 到 {dest_path}")
        except Exception as e:
            print(f"备份 {src} 时出错：{e}")


if __name__ == "__main__":
    source_files_and_folders = backup_config.get('source_files_and_folders', [])
    destination_folder = backup_config.get('destination_folder', '')

    if not destination_folder:
        print("错误：目标备份文件夹未配置。")
    elif not os.path.exists(destination_folder):
        print("错误：目标备份文件夹不存在。")
    elif not source_files_and_folders:
        print("错误：没有配置任何源文件或文件夹进行备份。")
    else:
        backup_files_and_folders(source_files_and_folders, destination_folder)
