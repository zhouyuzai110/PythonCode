import numpy as np
from PIL import Image

array = np.asarray(Image.open("xzpq2.jpeg").convert('L')).astype(np.float64)

# 根据灰度变化来模拟人类视觉的明暗程度
depth = 10  # 预设虚拟深度值为10 范围为0-100
# 提取x y方向梯度值 解构赋给grad_x, grad_y
grad_x, grad_y = np.gradient(array)

# 利用像素之间的梯度值和虚拟深度值对图像进行重构
grad_x = grad_x * depth / 100
grad_y = grad_y * depth / 100

# 梯度归一化 定义z深度为1.  将三个梯度绝对值转化为相对值，在三维中是相对于斜对角线A的值
dis = np.sqrt(grad_x**2 + grad_y**2 + 1.0)
uni_x = grad_x / dis
uni_y = grad_y / dis
uni_z = 1.0 / dis

# 光源俯视角度和光源方位角度
vec_el = np.pi / 2.2
vec_az = np.pi / 4

# 光源对x、y、z轴的影响
dx = np.cos(vec_el) * np.cos(vec_az)
dy = np.cos(vec_el) * np.sin(vec_az)
dz = np.sin(vec_el)

# 光源归一化
out = 255 * (uni_x * dx + uni_y * dy + uni_z * dz)
out = out.clip(0, 255)
img = Image.fromarray(out.astype(np.uint8))

img.save('out.jpg')
