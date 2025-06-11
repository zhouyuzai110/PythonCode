import os
import shutil
from tqdm import tqdm
from collections import defaultdict

# 源目录和目标目录
src_folder = r'\\ttnas\homes\zy0612\douyin_download'
dst_folder = r'\\ttnas\homes\zy0612\Photos_BackUp_Duplicate'

# 确保目标目录存在
if not os.path.exists(dst_folder):
    os.makedirs(dst_folder)

# 用于按 [creation_time]_[description] 分组文件
file_groups = defaultdict(list)

# 获取所有 MP4 文件总数
total_files = sum([len(f) for _, __, f in os.walk(src_folder) if any(ff.endswith('.mp4') for ff in f)])
with tqdm(total=total_files, desc="Processing Files") as pbar:
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            if file.endswith(".mp4"):
                try:
                    # 解析文件名结构
                    parts = file.split("_")
                    if len(parts) < 7:
                        raise ValueError("Invalid filename format")

                    creation_time_part = "_".join(parts[2:6])  # 如 "2025-03-12_23_31_21"
                    description_part = "_".join(parts[6:])  # 如 "梦婷姐三角区好看吗？背影杀耐看型大长腿紧身牛仔裤.mp4"

                    key = f"{creation_time_part}_{description_part}"  # 唯一标识符用于判断重复
                    filepath = os.path.join(root, file)

                    # 添加到分组中
                    file_groups[key].append(filepath)
                except Exception as e:
                    print(f"跳过无效文件 {file}: {e}")
                finally:
                    pbar.update(1)

# 处理每个分组，保留最新创建的文件
for key, files in file_groups.items():
    if len(files) > 1:
        # 按照系统创建时间排序，保留最新的一个
        sorted_files = sorted(
            files,
            key=lambda x: os.path.getctime(x),  # 使用系统创建时间排序
            reverse=True)
        latest_file = sorted_files[0]

        print(f"\n发现重复项（{key}），共 {len(files)} 个文件，保留最新文件：{latest_file}")

        # 移动除最新文件外的所有重复文件
        for old_file in sorted_files[1:]:
            filename = os.path.basename(old_file)
            new_filepath = os.path.join(dst_folder, filename)

            # 如果目标路径已存在相同名称文件，则添加后缀以避免冲突
            counter = 1
            while os.path.exists(new_filepath):
                base, ext = os.path.splitext(filename)
                new_filepath = os.path.join(dst_folder, f"{base}_dup{counter}{ext}")
                counter += 1

            print(f"移动重复文件：{old_file} -> {new_filepath}")
            shutil.move(old_file, new_filepath)
