# ; 在PyTorch中实现图片内容相似性检测，通常会涉及深度学习方法，
# 例如使用预训练的卷积神经网络（CNN）提取图像特征并计算特征向量之间的距离。
# 以下是一个基于ResNet模型的简单示例，用于提取图像特征并计算余弦相似度：

# import torch
# import torchvision.models as models
# from torchvision import transforms
# from PIL import Image
# import os

# # 使用预训练的ResNet模型获取图像特征
# def get_image_features(model, img_path):
#     transform = transforms.Compose([
#         transforms.Resize(256),
#         transforms.CenterCrop(224),
#         transforms.ToTensor(),
#         transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
#     ])

#     img = Image.open(img_path)
#     img_tensor = transform(img).unsqueeze(0)

#     with torch.no_grad():
#         features = model(img_tensor)
#         # 取出最后一层特征向量
#         feature_vector = features.squeeze().numpy()

#     return feature_vector

# # 初始化预训练模型
# model = models.resnet18(pretrained=True)
# model.eval()

# # 原始图片目录
# original_dir = "/path/to/original/directory"
# # 目标文件夹基础路径
# target_base_dir = "/path/to/target/base/directory"

# # 阈值设置
# similarity_threshold = 0.7  # 这里以余弦相似度为例

# def group_and_move_similar_images():
#     processed_images = {}  # 存储已处理图片及其对应的特征向量
#     for root, dirs, files in os.walk(original_dir):
#         for file in files:
#             if file.endswith(('.png', '.jpg', '.jpeg')):
#                 img_path = os.path.join(root, file)

#                 # 计算图片特征
#                 img_features = get_image_features(model, img_path)

#                 # 查找已有相似图片组
#                 similar_group = None
#                 for features, group_files in processed_images.items():
#                     cosine_similarity = np.dot(features, img_features) / (
#                         np.linalg.norm(features) * np.linalg.norm(img_features))
#                     if cosine_similarity > similarity_threshold:
#                         similar_group = group_files
#                         break

#                 # 如果找到了相似图片组，则添加到该组，否则创建新组
#                 if similar_group is not None:
#                     similar_group.append(img_path)
#                     target_group_dir = os.path.join(target_base_dir, str(len(similar_group)))
#                 else:
#                     similar_group = [img_path]
#                     target_group_dir = os.path.join(target_base_dir, str(len(processed_images)))

#                 # 确保目标文件夹存在
#                 if not os.path.exists(target_group_dir):
#                     os.makedirs(target_group_dir)

#                 # 移动图片到目标文件夹（这里仅做演示，实际项目中请根据需求修改为移动或复制操作）
#                 new_img_path = os.path.join(target_group_dir, file)
#                 # os.rename(img_path, new_img_path)  # 移动操作
#                 # shutil.copy(img_path, new_img_path)  # 复制操作

#                 processed_images[img_features] = similar_group

# if __name__ == "__main__":
#     group_and_move_similar_images()

# 在Python中，要实现将一个文件夹内内容相似的图片分组并移动到新建的文件夹中，通常需要经过以下步骤：

# 加载图片。
# 计算图片间的相似度。
# 根据相似度阈值进行分组。
# 创建新的文件夹并移动图片。
# 这里是一个基于PIL和imagehash库（用于计算图片哈希）的基本示例。请注意，实际项目中可能需要更复杂的图像处理和相似度算法，例如使用深度学习模型。以下代码仅作为一个基础模板：
import os
import hashlib
from PIL import Image
from imagehash import phash
import shutil
from tqdm import tqdm

# 设置原始图片目录
original_dir = r"C:\Users\saber\Desktop\pythonscript\BackUp"
# 设置相似图片存放的基础目录
target_base_dir = r"C:\Users\saber\Desktop\pythonscript\Back"

# 阈值设置，根据实际情况调整
similarity_threshold = 5  # 这里以8位的dHash为例，0-64之间选择合适的阈值


def calculate_image_similarity(image_path1, image_path2):
    """
    计算两个图片的相似度
    """
    hash1 = phash(Image.open(image_path1))
    hash2 = phash(Image.open(image_path2))
    return hash1 - hash2  # 返回汉明距离，越小表示越相似


def group_and_move_similar_images():
    processed_images = {}  # 存储已处理图片及其对应的分组哈希
    for root, dirs, files in os.walk(original_dir):
        for file in files:  # 添加进度条:
            if file.endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                img_path = os.path.join(root, file)
                img_hash = phash(Image.open(img_path))

                # 查找已有相似图片组
                similar_group = None
                for group_hash, group_files in processed_images.items():
                    if abs(group_hash - img_hash) <= similarity_threshold:
                        similar_group = group_files
                        break

                # 如果找到了相似图片组，则添加到该组，否则创建新组
                if similar_group is not None:
                    similar_group.append(img_path)
                    target_group_dir = os.path.join(target_base_dir, str(group_hash))
                else:
                    similar_group = [img_path]
                    target_group_dir = os.path.join(target_base_dir, str(img_hash))

                # 确保目标文件夹存在
                if not os.path.exists(target_group_dir):
                    os.makedirs(target_group_dir)

                # 移动图片到目标文件夹
                new_img_path = os.path.join(target_group_dir, file)
                os.rename(img_path, new_img_path)

                # shutil.copy(img_path, new_img_path)  # 复制操作
                processed_images[img_hash] = similar_group


if __name__ == "__main__":
    group_and_move_similar_images()
