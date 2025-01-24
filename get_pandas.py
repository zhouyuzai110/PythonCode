import pandas as pd
import numpy as np

#读取桌面的tableA.csv文件,写好完整路径
df = pd.read_csv('C:/Users/saber/Desktop/tableA.csv')
# print(df)
# 查看df  结构信息
# print(df.info())
# 查看第一列和第二列的交叉频数
print(pd.crosstab(df['duixiang'], df['b']))
print(pd.crosstab(df['duixiang'], df['a']))
hebing = pd.concat([pd.crosstab(df['duixiang'], df['b']), pd.crosstab(df['duixiang'], df['a'])], axis=1)
print(hebing)
#重排列的顺序
print(hebing.reindex(['a', 'b', 'w', 'x', 'y', 'z']))
   ssh -T git@github.com