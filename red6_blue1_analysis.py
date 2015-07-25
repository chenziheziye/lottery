#!/usr/bin/env python2.7
# -- coding:utf-8 --
# __author__ = 'chenziheziye'

import matplotlib.pyplot as plt
import numpy as np

f = open('/Users/chenziheziye/Documents/history_data.txt', 'r')

#data content(per line): six red num(1~33) + one blue num(1~16)

def ColdHot():
    """冷热号分析

    1.持续5期以上不出现为温号，持续10期为冷号，5期以内为热号(可以绘制出冷热号趋势表或散点图)
    2.10期内1次未出为冷号，10期内只出现1～2次为温号，10期内连出3次或最近5期开出2次以上为热号
    """
    fileLineCount = len(f.readlines())#总期数，即文件的行数
    timeCount = 0#彩票的期数,从0开始
    redHitNum = np.zeros((fileLineCount, 33), dtype=np.int)
    blueHitNum = np.zeros((fileLineCount, 16), dtype=np.int)
    redTraitNum = np.zeros((fileLineCount, 33), dtype=np.int)
    blueTraitNum = np.zeros((fileLineCount, 16), dtype=np.int)

    for line in f:
        dataList = line.split()
        timeCount += 1

        for i in range(1, len(dataList) - 2):#遍历红号，并对出现次数累加
            redHitNum[int(dataList[i]) - 1, timeCount-1] += 1

            if timeCount > 5:
                redTraitNum[timeCount - 1, int(dataList[i]) - 1] += int(dataList[i])#前后5期均为热号
            else:


        blueHitNum[int(dataList[6])-1][timeCount-1] += 1



def calc_num_ratio():
    """计算数字的出现率

    1.计算数字出现率的变化曲线，期数*每期出现的数字个数（6）累加后作为分母，以考察数字作为分子
    2.
    """
    for line in f:
        curList = line.split()

#test area
#ColdHot()

l1 = np.zeros((10, 10), dtype=np.int)
l1[0, 0] = 3
l1[0, 0] += 1
print l1

x = [1, 2, 3, 4, 5, 6]
y = [t**2 for t in x]
#plt.scatter(x, y)
#plt.show()