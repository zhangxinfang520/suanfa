# -*- coding:utf-8 -*-
#@Time : 2021-08-13 14:58
#@Author: zxf_要努力
#@File : 210_课程表 II.py
'''
在你总共有 n 门课需要选，记为 0 到 n-1。

在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]

给定课程总量以及它们的先决条件，返回你为了学完所有课程所安排的学习顺序。

可能会有多个正确的顺序，你只要返回一种就可以了。如果不可能完成所有课程，返回一个空数组。
输入: 2, [[1,0]]
输出: [0,1]
解释: 总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。
'''
import collections
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edge = collections.defaultdict(list)
        node = [0] * numCourses
        for i in range(len(prerequisites)):
            first,end = prerequisites[i]
            edge[end].append(first)
            node[first] +=1
        que = [u for u in range(numCourses) if node[u] == 0]
        res = []
        visited = 0
        while que:
            visited +=1
            temp = que.pop(0)
            res.append(temp)
            for u in edge[temp]:
                node[u] -=1
                if node[u] == 0:
                    que.append(u)
        if visited != numCourses:
            return []
        return res

if __name__ == '__main__':
    # numCourses = 4
    # prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    numCourses = 3
    prerequisites = [[1,0],[1,2],[0,1]]
    print(Solution().findOrder(numCourses, prerequisites))
