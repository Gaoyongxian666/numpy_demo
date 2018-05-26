# encoding: utf-8
'''
@author: gaoyongxian666
@file: demo01.py
@time: 2018/5/26 19:47
'''
# 列表变数组
# 初始化一个数组
# 获取数组的属性
# 生成1，0的矩阵
# 生成正态分布的矩阵
# 生成均匀分布的矩阵
# 元素内容和个数不变的reshape

import numpy as np

# 创建简单的列表
a = [1, 2, 3, 4]
# 将列表转换为数组
b = np.array(a)# 数据类型改变了

# 数组元素个数
b.size
# 数组形状
b.shape
# 数组维度
b.ndim
# 数组元素类型
b.dtype




# 快速创建N维数组的api函数
# 创建10行10列的数值为浮点1的矩阵
array_one = np.ones([10, 10])
# 创建10行10列的数值为浮点0的矩阵
array_zero = np.zeros([10, 10])
# 从现有的数据创建数组
# array(深拷贝)
# asarray(浅拷贝)




# Numpy创建随机数组np.random
# 均匀分布

# 创建指定形状(示例为10行10列)的数组(范围在0至1之间)
a=np.random.rand(10, 10)
print(a)
# 创建指定范围内的一个数(包含浮点数)
b=np.random.uniform(0, 100)
print(b)
# 创建指定范围内的一个整数
c=np.random.randint(0, 100)
print(c)


# 正态分布
# 给定均值/标准差/维度的正态分布
a=np.random.normal(1.75, 0.1, (2, 3))
print(a)

# 数组的索引, 切片
# 正态生成4行5列的二维数组
arr = np.random.normal(1.75, 0.1, (4, 5))
print(arr)
# 截取第1至2行的第2至3列(从第0行算起)
after_arr = arr[1:3, 2:4]
print(after_arr)
# 改变数组形状(要求前后元素个数匹配)
print("reshape函数的使用!")
one_20 = np.ones([20])
print("-->1行20列<--")
print (one_20)
one_4_5 = one_20.reshape([4, 5])
print("-->4行5列<--")
print (one_4_5)



