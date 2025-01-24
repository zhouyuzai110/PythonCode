import os
import hashlib
import shutil
from tqdm import tqdm

# 源文件夹路径
# src_folder = '/path/to/source/folder'
src_folder = r'\\ttnas\homes\zy0612\Photos_BackUp'
# 目标文件夹路径（存放重复文件）
# dst_folder = '/path/to/destination/folder'
dst_folder = r'\\ttnas\homes\zy0612\Photos_BackUp_Duplicate'

# 确保目标文件夹存在
if not os.path.exists(dst_folder):
    os.makedirs(dst_folder)

# 用于存储已经检查过的文件及其哈希值
checked_files = {}

# 遍历源文件夹获取所有文件的总数量
total_files = sum([len(files) for root, dirs, files in os.walk(src_folder)])

with tqdm(total=total_files) as pbar:
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            # 获取完整文件路径
            filepath = os.path.join(root, file)

            # 跳过已存在于目标文件夹的文件和非普通文件（例如目录等）
            if os.path.exists(os.path.join(dst_folder, file)) or not os.path.isfile(filepath):
                continue

            # 计算文件的SHA-1哈希值
            with open(filepath, 'rb') as f:
                sha1_hash = hashlib.sha1(f.read()).hexdigest()

            # 提取哈希值前六位
            hash_prefix = sha1_hash[:6]

            # 如果哈希值已存在于字典中，则表示找到重复文件
            if sha1_hash in checked_files:
                # 创建新的文件名（哈希值前六位 + 短横线 + 原来的文件名）
                new_filename = f"{hash_prefix}-{file}"
                new_filepath = os.path.join(dst_folder, new_filename)

                # 确保新文件名不会与目标文件夹中的现有文件冲突
                while os.path.exists(new_filepath):
                    hash_prefix += "0"  # 若有冲突，增加一个“0”以生成新的文件名
                    new_filename = f"{hash_prefix}-{file}"
                    new_filepath = os.path.join(dst_folder, new_filename)

                # 打印重复文件的信息并等待用户确认
                print(f"发现重复文件：{filepath}，哈希值为：{sha1_hash}，将重命名为：{new_filename}")
                shutil.move(filepath, new_filepath)
                # confirm = input("是否要移动此文件到目标文件夹并重命名？(yes/no) ")
                # if confirm.lower() == "yes":
                #     shutil.move(filepath, new_filepath)
                # else:
                #     print("文件保留原地，继续检查下一个文件...")

                pbar.update(1)  # 更新进度条
            else:
                # 将当前文件及其哈希值存入字典
                checked_files[sha1_hash] = filepath
                pbar.update(1)  # 更新进度条

# 注意：这里仍然保留了用户交互确认部分，请根据实际需求调整。
