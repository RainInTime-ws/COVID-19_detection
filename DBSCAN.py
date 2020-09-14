
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

#二维聚类结果画图
def plot_2D(dict, cluster):
    x = []
    y = []
    for item in dict:
        x.append(dict[item][0])
        y.append(dict[item][1])
    size = 3
    plt.title("DBSCAN Outcome")
    plt.xlabel("death index")
    plt.ylabel("transmission index")
    plt.scatter(x, y, c=cluster, s=size)
    plt.show()

#三维聚类结果画图
def plot_3D(dict, cluster):
    x = []
    y = []
    z = []
    for item in dict:
        x.append(dict[item][0])
        y.append(dict[item][1])
        z.append(dict[item][2])
    ax = plt.subplot(projection='3d')
    plt.title("Cluster Outcome ")
    ax.set_xlabel('death index')
    ax.set_ylabel("transmission index")
    ax.set_zlabel("death speed")
    ax.scatter(x, y, z, c=cluster, s=2)
    plt.draw()
    plt.show()


#计算欧式距离
def distEuclid(x, y):
    return np.sqrt(np.sum((x - y) ** 2))


#判断两点是否在范围内
def isNeighbor(x, y, eps):
    return distEuclid(x, y) <= eps


#获取某一点邻域内的点
def getSeedPos(pos, data, eps):
    seed = []
    for p in range(len(data)):
        if isNeighbor(data[p], data[pos], eps):
            seed.append(p)
    return seed


#获取核心点列表
def getCorePointsPos(data, eps, minpts):
    cpoints = []
    for pos in range(len(data)):
        if len(getSeedPos(pos, data, eps)) >= minpts:
            cpoints.append(pos)
    return cpoints


#DBSCAN聚类步骤
def getCluster(data, eps, minpts):
    corePos = getCorePointsPos(data, eps, minpts)
    unvisited = list(range(len(data)))
    cluster = {}
    num = 0
    for pos in corePos:
        if pos not in unvisited:
            continue
        clusterpoint = []
        clusterpoint.append(pos)
        seedlist = getSeedPos(pos, data, eps)
        unvisited.remove(pos)
        while seedlist:
            p = seedlist.pop(0)
            if p not in unvisited:
                continue
            unvisited.remove(p)
            clusterpoint.append(p)
            if p in corePos:
                seedlist.extend(getSeedPos(p, data, eps))
        cluster[num] = clusterpoint
        num += 1
    cluster[-1] = unvisited
    return cluster

#二维DBSCAN聚类，直接调用库函数，以列表的形式返回聚类结果
def Dcluster_2D(dict):
    points = []
    for item in dict:
        points.append([dict[item][0], dict[item][1]])
    cluster = DBSCAN(eps=0.01, min_samples=9).fit_predict(points)
    return cluster

#三维DBSCAN聚类，用上面实现的函数，以列表的形式返回聚类结果
def Dcluster_3D(dict):
    data = []
    for item in dict:
        data.append(np.array([dict[item][0], dict[item][1], dict[item][2]]))
    clu = getCluster(data, 0.01, 10)
    cluster = [0 for i in range(0, len(dict))]
    for key in clu:
        for point in clu[key]:
            cluster[point] = key
    return cluster

#DBSCAN二维接口函数，主函数调用
def DBSCAN_2D(dict):
    cluster = Dcluster_2D(dict)
    plot_2D(dict, cluster)

#DBSCAN三维接口函数，主函数调用
def DBSCAN_3D(dict):
    cluster = Dcluster_3D(dict)
    plot_3D(dict, cluster)
