# encoding: utf-8
'''
@author: gaoyongxian666
@file: demo02.py
@time: 2018/5/26 19:57
'''
# numpy的运算

import numpy as np

# 条件判断
stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
a=stus_score > 80
print(a)
b=np.where(stus_score < 80, 0, 90)
print(b)


# 统计判断

# 求最大值
# 指定轴最大值amax(参数1: 数组; 参数2: axis=0/1; 0表示列1表示行)
stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
# 求每一列的最大值(0表示列)
print("每一列的最大值为:")
result = np.amax(stus_score, axis=0)
print(result)

print("每一行的最大值为:")
result = np.amax(stus_score, axis=1)
print(result)

# 指定轴最小值amin
stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
# 求每一行的最小值(0表示列)
print("每一列的最小值为:")
result = np.amin(stus_score, axis=0)
print(result)

# 求每一行的最小值(1表示行)
print("每一行的最小值为:")
result = np.amin(stus_score, axis=1)
print(result)


# 指定轴平均值mean
stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
# 求每一行的平均值(0表示列)
print("每一列的平均值:")
result = np.mean(stus_score, axis=0)
print(result)

# 求每一行的平均值(1表示行)
print("每一行的平均值:")
result = np.mean(stus_score, axis=1)
print(result)

# 方差std
stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
# 求每一行的方差(0表示列)
print("每一列的方差:")
result = np.std(stus_score, axis=0)
print(result)

# 求每一行的方差(1表示行)
print("每一行的方差:")
result = np.std(stus_score, axis=1)
print(result)

# 数组运算
# [行,列]
# 数组与数的运算
stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
print("加分前:")
print(stus_score)
# 为所有平时成绩都加5分
stus_score[:, 0] = stus_score[:, 0]+5
print("加分后:")
print(stus_score)

stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
print("减半前:")
print(stus_score)

# 平时成绩减半
stus_score[:, 0] = stus_score[:, 0]*0.5
print("减半后:")
print(stus_score)

# 数组间也支持加减乘除运算,但基本用不到
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
c = a + b
d = a - b
e = a * b
f = a / b
print("a+b为", c)
print("a-b为", d)
print("a*b为", e)
print("a/b为", f)


# 矩阵运算np.dot()(非常重要)
# 计算规则:
# (M行, N列) * (N行, Z列) = (M行, Z列)
stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
# 平时成绩占40% 期末成绩占60%, 计算结果
q = np.array([[0.4], [0.6]])
result = np.dot(stus_score, q)
print("最终结果为:")
print(result)
# 矩阵拼接
# 矩阵垂直拼接
print("v1为:")
v1 = [[0, 1, 2, 3, 4, 5],
      [6, 7, 8, 9, 10, 11]]
print(v1)
print("v2为:")
v2 = [[12, 13, 14, 15, 16, 17],
      [18, 19, 20, 21, 22, 23]]
print(v2)
# 垂直拼接
result = np.vstack((v1, v2))
print("v1和v2垂直拼接的结果为")
print(result)
# 矩阵水平拼接
print("v1为:")
v1 = [[0, 1, 2, 3, 4, 5],
      [6, 7, 8, 9, 10, 11]]
print(v1)
print("v2为:")
v2 = [[12, 13, 14, 15, 16, 17],
      [18, 19, 20, 21, 22, 23]]
print(v2)
# 垂直拼接
result = np.hstack((v1, v2))
print("v1和v2水平拼接的结果为")
print(result)

# Numpy读取数据np.genfromtxt
# 如果数值据有无法识别的值出现,会以nan显示,nan相当于np.nan,为float类型.
# 使用numpy读取数据
# np.loadtxt()用于从文本加载数据。
# 文本文件中的每一行必须含有相同的数据。
# 作用是把文本文件（*.txt）读入并以矩阵或向量的形式输出。

# loadtxt(fname, dtype=<class 'float'>, comments='#', delimiter=None, converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0)
# fname要读取的文件、文件名、或生成器。
# dtype数据类型，默认float。
# comments注释。
# delimiter分隔符，默认是空格。
# skiprows跳过前几行读取，默认是0，必须是int整型。
# usecols：要读取哪些列，0是第一列。例如，usecols = （1,4,5）将提取第2，第5和第6列。默认读取所有列。
# unpack如果为True，将分列读取。默认为flase它将会以整个数组返回。

# 在默认情况下是通过空格来分割列的，如果想通过其他来分割列则需要通过delimiter来设置。
# 如果你想跳过几列来读取则需要用usecoles来设置。
# 正常情况下该返回的是二维矩阵，若设置了unpack=True将返回各列

x, y = np.loadtxt('example.txt', delimiter=',', unpack=True)
