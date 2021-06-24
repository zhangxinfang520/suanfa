# -*- coding:utf-8 -*-
#@Time : 2021-06-24 20:47
#@Author: zxf_要努力
#@File : 77_组合.py
'''
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k > n:
            return [[]]

        res = list()
        track = list()

        self.all_sort(n,k,1,track,res)

        return res

    def all_sort(self, n, k, start, track, result):
        if len(track) == k:
            if track[::-1] not in result :
                result.append(track[:])
            return
        for i in range(start,n+1):
            if i in track:
                continue
            track.append(i)
            self.all_sort(n,k,start+1,track,result)
            track.pop()

class Solution1:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]  #存放符合条件结果的集合
        path=[]  #用来存放符合条件结果
        def backtrack(n,k,startIndex):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(startIndex,n-(k-len(path))+2):  #优化的地方
                path.append(i)  #处理节点
                backtrack(n,k,i+1)  #递归
                path.pop()  #回溯，撤销处理的节点
        backtrack(n,k,1)
        return res




print(Solution1().combine(4, 3))