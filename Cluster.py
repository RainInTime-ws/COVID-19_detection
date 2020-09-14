import numpy as np
import math as m
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import evaluate as eva
import random
import numpy as np
from sklearn import datasets
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler

#Kmeans初始化选取中心点，二维情况
def initial_2D(dict, k):
    dict_0 = dict
    center = []
    center_key = random.sample(dict_0.keys(), k)
    for item in center_key:
        center.append([dict[item][0], dict[item][1]])
    return center

#Kmeans初始化选取中心点，三维情况
def initial_3D(dict, k):
    dict_0 = dict
    center = []
    center_key = random.sample(dict_0.keys(), k)
    for item in center_key:
        center.append([dict[item][0], dict[item][1], dict[item][2]])
    return center

#计算二维欧几里得距离
def distance_2D(key, point, dict):
    return (dict[key][0] - point[0]) ** 2 + (dict[key][1] - point[1]) ** 2

#计算三维欧几里得距离
def distance_3D(key, point, dict):
    return (dict[key][0] - point[0]) ** 2 + (dict[key][1] - point[1]) ** 2 + (dict[key][2] - point[2]) ** 2

#画图，二维
def plot_2D(dict, center):
    x = []
    y = []
    cluster = []
    for item in dict:
        x.append(dict[item][0])
        y.append(dict[item][1])
        cluster.append(dict[item][-1])
        center_x = [i[0] for i in center]
        center_y = [i[1] for i in center]
    size = 3
    plt.title("Cluster Outcome with k = {}".format(len(center)))
    plt.xlabel("death index")
    plt.ylabel("transmission index")
    plt.scatter(x, y, c=cluster, s=size)
    plt.scatter(center_x, center_y, c='r', marker='x')
    plt.show()

#画图，三维
def plot_3D(dict, center):
    x = []
    y = []
    z = []
    cluster = []
    for item in dict:
        x.append(dict[item][0])
        y.append(dict[item][1])
        z.append(dict[item][2])
        cluster.append(dict[item][-1])
        center_x = [i[0] for i in center]
        center_y = [i[1] for i in center]
        center_z = [i[2] for i in center]
    size = 2
    ax = plt.subplot(projection='3d')
    plt.title("Cluster Outcome ")
    ax.set_xlabel('death index')
    ax.set_ylabel("transmission index")
    ax.set_zlabel("death speed")
    ax.scatter(x, y, z, c=cluster, s=2)
    ax.scatter(center_x, center_y, center_z, c='r', marker='x')
    plt.draw()
    plt.show()

#Kmeans更新步骤，把每个样本点分配给最近中心点代表的类
def allocate(key1, center, dict):
    if len(center[0]) == 2:#二维情况
        distance = distance_2D(key1, center[0], dict)
        cluster = 0
        for point in center:
            if distance_2D(key1, point, dict) < distance:
                distance = distance_2D(key1, point, dict)
                cluster = center.index(point)
        return cluster
    else:#三维情况
        distance = distance_3D(key1, center[0], dict)
        cluster = 0
        for point in center:
            if distance_3D(key1, point, dict) < distance:
                distance = distance_2D(key1, point, dict)
                cluster = center.index(point)
        return cluster

#每次迭代后计算新的中心点位置，二维情况
def new_center_2D(center, dict):
    new_center = []
    for i in range(len(center)):
        sum_0 = 0
        sum_1 = 0
        count = 0
        for item in dict:
            if dict[item][-1] == i:
                sum_0 += dict[item][0]
                sum_1 += dict[item][1]
                count += 1
        if count != 0:
            average = [sum_0 / count, sum_1 / count]
        else:
            average = [0.0, 0.0]
        new_center.append(average)
    return new_center

#每次迭代后计算新的中心点位置，三维情况
def new_center_3D(center, dict):
    new_center = []
    for i in range(len(center)):
        sum_0 = 0
        sum_1 = 0
        sum_2 = 0
        count = 0
        for item in dict:
            if dict[item][-1] == i:
                sum_0 += dict[item][0]
                sum_1 += dict[item][1]
                sum_2 += dict[item][2]
                count += 1
        if count != 0:
            average = [sum_0 / count, sum_1 / count, sum_2 / count]
        else:
            average = [0.0, 0.0, 0.0]
        new_center.append(average)
    return new_center

#Kmeans接口函数，用于在main中调用。dict是样本点集合，k是cluster个数，二维情况
def Kmeans_2D(dict, k):
    center = []
    center = initial_2D(dict, k)
    for i in range(1, 1000):
        for item in dict:
            dict[item].append(allocate(item, center, dict))
        center = new_center_2D(center, dict)
    plot_2D(dict, center)

#Kmeans接口函数，用于在main中调用。dict是样本点集合，k是cluster个数，三维情况
def Kmeans_3D(dict, k):
    center = []
    center = initial_3D(dict, k)
    for i in range(1, 1000):
        for item in dict:
            dict[item].append(allocate(item, center, dict))
        center = new_center_3D(center, dict)
    plot_3D(dict, center)


