import os
import cv2
import numpy as np
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing import image
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity

# 图片文件夹路径
image_folder = 'path_to_your_images'
output_folder = 'path_to_output_clusters'

# 创建输出文件夹
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 加载预训练的ResNet50模型
model = ResNet50(weights='imagenet', include_top=False, pooling='avg')


def extract_features(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    features = model.predict(img_array)
    return features.flatten()


# 获取所有图片路径
image_paths = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

# 提取所有图片的特征
all_features = []
for path in image_paths:
    try:
        features = extract_features(path)
        all_features.append(features)
    except Exception as e:
        print(f"提取特征时出错：{e}，跳过图片 {path}")

# 转换为numpy数组
all_features = np.array(all_features)

# 使用K-means进行聚类
num_clusters = 100  # 初始聚类数量，可以根据需要调整
kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(all_features)

# 将特征分配到聚类中心
labels = kmeans.labels_

# 创建每个聚类的文件夹
for i in range(num_clusters):
    cluster_folder = os.path.join(output_folder, f'cluster_{i}')
    if not os.path.exists(cluster_folder):
        os.makedirs(cluster_folder)

# 将图片移动到对应的聚类文件夹
for i, label in enumerate(labels):
    src_path = image_paths[i]
    dest_folder = os.path.join(output_folder, f'cluster_{label}')
    dest_path = os.path.join(dest_folder, os.path.basename(src_path))
    shutil.copy(src_path, dest_path)
    print(f"图片 {src_path} 移动到 {dest_path}")

print("聚类完成，图片已分类到不同的文件夹中。")
