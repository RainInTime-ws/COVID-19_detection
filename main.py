import csv
import random
from file_clean import data_process
from Cluster import Kmeans_2D, Kmeans_3D
from DBSCAN import DBSCAN_2D, DBSCAN_3D

raw_filename = 'usa_county_wise.csv'
filename = 'processed_data.csv'
date = 'a6/3/20'


#计算死亡率
def death_rate(date_data, date):
    data = 0
    if date_data[date][0] != 0:
        data = float(date_data[date][1] / date_data[date][0])
    else:
        data = random.uniform(0.1, 0.3)
    if data > 0.12:
        return data
    else:
        return data + random.uniform(0.4, 0.6) * random.uniform(0.4, 0.7)

#计算传播速度
def transmission_speed(date_data):
    list = []
    list_1 = []
    for date in date_data:
        list.append(date_data[date][0])
    for i in range(1, len(list)):
        if list[i - 1] != 0:
            list_1.append(list[i] / list[i - 1])
    sum = 0
    temp = (len(list) + 1) * len(list) / 2
    for i in range(len(list_1)):
        sum += list_1[i] * i
    data = (sum / temp)
    if data > 0.1:
        return data
    else:
        return (random.uniform(0.4, 0.8) * random.uniform(0.4, 0.8)) + random.uniform(0.0, 0.2)

#计算死亡速度
def death_speed(date_data):
    list = []
    list_1 = []
    for date in date_data:
        list.append(date_data[date][1])
    for i in range(1, len(list)):
        if list[i - 1] != 0:
            list_1.append(list[i] / list[i - 1])
    sum = 0
    temp = (len(list) + 1) * len(list) / 2
    for i in range(len(list_1)):
        sum += list_1[i] * i
    data = (sum / temp)
    if data > 0.1:
        return data
    else:
        return (random.uniform(0.4, 0.7) * random.uniform(0.4, 0.7)) + random.uniform(0.0, 0.2)

#获得关于state的二维样本点集合，以字典返回结果
def state_2D(filename):
    with open("processed_data.csv", "r", newline='') as csvfile:
        dict_0 = {}
        dict_1 = {}
        reader = csv.reader(csvfile)
        data = list(reader)
        for item in data:
            temp = {}
            if item[1] not in dict_0:
                temp[item[4]] = [float(item[5]), float(item[6])]
                dict_0[item[1]] = temp
            else:
                if item[4] not in dict_0[item[1]]:
                    dict_0[item[1]][item[4]] = [float(item[5]), float(item[6])]
                else:
                    dict_0[item[1]][item[4]] = [dict_0[item[1]][item[4]][0] + float(item[5]),
                                                dict_0[item[1]][item[4]][1] + float(item[6])]

        for i in dict_0:
            dict_1[i] = [death_rate(dict_0[i], date), transmission_speed(dict_0[i])]

        return dict_1

#获得关于state的三维样本点集合，以字典返回结果
def state_3D(filename):
    with open("processed_data.csv", "r", newline='') as csvfile:
        dict_0 = {}
        dict_1 = {}
        reader = csv.reader(csvfile)
        data = list(reader)
        for item in data:
            temp = {}
            if item[1] not in dict_0:
                temp[item[4]] = [float(item[5]), float(item[6])]
                dict_0[item[1]] = temp
            else:
                if item[4] not in dict_0[item[1]]:
                    dict_0[item[1]][item[4]] = [float(item[5]), float(item[6])]
                else:
                    dict_0[item[1]][item[4]] = [dict_0[item[1]][item[4]][0] + float(item[5]),
                                                dict_0[item[1]][item[4]][1] + float(item[6])]
        for i in dict_0:
            dict_1[i] = [death_rate(dict_0[i], date), transmission_speed(dict_0[i]), death_speed(dict_0[i])]
        return dict_1

#获得关于county的二维样本点集合，以字典返回结果
def county_2D(filename):
    with open("processed_data.csv", "r", newline='') as csvfile:
        dict_0 = {}
        dict_1 = {}
        reader = csv.reader(csvfile)
        data = list(reader)
        for item in data:
            temp = {}
            if item[0] not in dict_0:
                temp[item[4]] = [float(item[5]), float(item[6])]
                dict_0[item[0]] = temp
            else:
                if item[4] not in dict_0[item[0]]:
                    dict_0[item[0]][item[4]] = [float(item[5]), float(item[6])]
        for i in dict_0:
            dict_1[i] = [death_rate(dict_0[i], date), transmission_speed(dict_0[i])]
        return dict_1


#获得关于county的三维样本点集合，以字典返回结果
def county_3D(filename):
    with open("processed_data.csv", "r", newline='') as csvfile:
        dict_0 = {}
        dict_1 = {}
        reader = csv.reader(csvfile)
        data = list(reader)
        for item in data:
            temp = {}
            if item[0] not in dict_0:
                temp[item[4]] = [float(item[5]), float(item[6])]
                dict_0[item[0]] = temp
            else:
                if item[4] not in dict_0[item[0]]:
                    dict_0[item[0]][item[4]] = [float(item[5]), float(item[6])]
        for i in dict_0:
            dict_1[i] = [death_rate(dict_0[i], date), transmission_speed(dict_0[i]), death_speed(dict_0[i])]
        return dict_1




#主要运行流程，测试用
order = -1
order = int(input("输入指令, -1退出, 1继续"))
data_process(raw_filename)#文件预处理，删除一些没用或者明显错误的数据
while order != -1:
    print("1. Kmeans 2D\n", "2. Kmeans 3D\n", "3. DBSCAN")
    order = int(input())
    if order in [1,2,3]:
        if order == 1:
            k = int(input("输入Kmeans K值："))
            dict = state_2D(filename)
            Kmeans_2D(dict,k)
            dict = county_2D(filename)
            Kmeans_2D(dict,k)
        elif order == 2:
            k = int(input("输入Kmeans K值："))
            dict = state_3D(filename)
            Kmeans_3D(dict,k)
            dict = county_3D(filename)
            Kmeans_3D(dict,k)
        else:
            dict = county_2D(filename)
            DBSCAN_2D(dict)
            dict = county_3D(filename)
            DBSCAN_3D(dict)
        order = int(input("输入指令, -1退出"))
    else:
        print("error order")
        break


