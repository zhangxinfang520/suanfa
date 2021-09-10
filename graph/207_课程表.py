# -*- coding:utf-8 -*-
#@Time : 2021-08-13 10:39
#@Author: zxf_要努力
#@File : 207_课程表.py

'''
你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。
在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。
例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。
输入：numCourses = 2, prerequisites = [[1,0]]
输出：true
解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。

用队列来解决
'''
from typing import List
import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0 or numCourses == 0:
            return True
        edge = [0] * numCourses
        in_dix = collections.defaultdict(list)
        for i in range(len(prerequisites)):
            first, end = prerequisites[i]
            edge[first] += 1
            in_dix[end].append(first)
        #将入度为0的 提取出来
        que = [u for u in range(numCourses) if edge[u] == 0]
        visited = 0
        while que:
            visited +=1
            temp = que.pop(0)
            for v in in_dix[temp]:
                edge[v] -=1
                if edge[v] == 0:
                    que.append(v)
        return visited == numCourses

    def canFinish1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edge = collections.defaultdict(list)
        node = [0] * numCourses
        for i in range(len(prerequisites)):
            first, end = prerequisites[i]
            edge[end].append(first)
            node[first] += 1
        que = [u for u in node if u == 0]

        visited = 0
        while que:
            visited +=1
            temp = que.pop(0)
            for u in edge[temp]:
                node[u] -=1
                if node[u] == 0:
                    que.append(u)
        return visited == numCourses


if __name__ == '__main__':
    numCourses = 3
    prerequisites = [[1, 0],[0,1],[1,2]]
    print(Solution().canFinish1(numCourses,prerequisites))