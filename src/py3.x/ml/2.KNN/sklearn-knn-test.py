#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Created on 2017-06-28
Updated on 2017-06-28
KNN: k近邻算法
Author: 小瑶
GitHub: https://github.com/apachecn/AiLearning
"""
print(__doc__)

import numpy as np
import matplotlib.pyplot as plt
from numpy import *
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets
# import warnings filter
from warnings import simplefilter
# ignore all future warnings
simplefilter(action='ignore', category=FutureWarning)


n_neighbors = 3

#  导入一些要玩的数据(鸢尾花数据集)
iris = datasets.load_iris()
X = iris.data[:, :2]  # 我们只采用前两个feature. 我们可以使用二维数据集避免这个丑陋的切片（第一个表示要多少个数据，第二个表示要几维的数据）
#第一个表示要多少条，第二个表示要多少列
y = iris.target

# print ('X=', type(X))
# print(X)
# print(iris.feature_names)
# print(len(X))
# print ('y=', type(y), len(y),y)


h = .02  # 网格中的步长

# 创建彩色的图
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])#点
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])#区域色块

for weights in ['uniform', 'distance']:
    # 我们创建了一个knn分类器的实例，并拟合数据。
    # 默认情况下kneighbors查询使用的邻居数。就是k-NN的k的值n_neighbors，选取最近的k个点，未指定的话默认值为5
    clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
    clf.fit(X, y)

    # 绘制决策边界。为此，我们将为每个分配一个颜色
    # 来绘制网格中的点 [x_min, x_max]x[y_min, y_max].
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    # 在给定间隔内返回均匀间隔的值
    # 值在半开区间 [开始，停止]内生成（换句话说，包括开始但不包括停止的区间）,返回的是 ndarray
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # 将结果放入一个彩色图中
    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

    # 绘制训练点
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.title("3-Class classification (k = %i, weights = '%s')"
              % (n_neighbors, weights))

plt.show()