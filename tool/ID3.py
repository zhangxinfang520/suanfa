# -*- coding:utf-8 -*-
#@Time : 2021/8/31 9:53
#@Author: zxf_要努力
#@File : ID3.py
import math


class Solution:
    def choose_best_feature(self , dataSet ):
        # write code here
        numfeatures = len(dataSet[0]) - 1
        baseBCE = self.Shang(dataSet)
        bestBCE = 0.0
        index = -1
        for i in range(numfeatures):
            #遍历所有特征
            featList = [example[i] for example in dataSet]
            value = set(list(featList))
            newBCE = 0.0
            for val in value:
                new_dataset = self.splitDataSet(dataSet, i, val)
                prob = len(new_dataset) / len(dataSet)
                newBCE += prob * self.Shang(new_dataset)
            temp = baseBCE - newBCE
            if temp > bestBCE:
                index = i
                bestBCE = temp
        return index

    def splitDataSet(self,dataset,axis,value):
        ret = []
        for feature in dataset:
            if feature[axis] == value:
                ret_vec = feature[:axis]
                ret_vec.extend(feature[axis+1:])
                ret.append(ret_vec)
        return ret

    def Shang(self,dataSet):
        """求熵"""
        numlables = len(dataSet)
        lablecounts = {}
        for feature in dataSet:
            curlable = feature[-1]
            if curlable not in lablecounts.keys():
                lablecounts[curlable] = 1
            else:
                lablecounts[curlable] += 1
        ent = 0.0
        for lable in lablecounts.keys():
            prop = float(lablecounts[lable]) / numlables
            ent -= (prop * math.log(prop,2))
        return ent


if __name__ == '__main__':
    dataSet = [[1,1,1,1],[1,0,0,1],[0,1,1,0],[0,1,1,0]]
    print(Solution().choose_best_feature(dataSet))