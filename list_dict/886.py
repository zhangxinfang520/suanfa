# -*- coding:utf-8 -*-
#@Time : 2021-04-20 12:15
#@Author: zxf_要努力
#@File : 886.py
'''
给定一组 N 人（编号为 1, 2, ..., N）， 我们想把每个人分进任意大小的两组。
每个人都可能不喜欢其他人，那么他们不应该属于同一组。
形式上，如果 dislikes[i] = [a, b]，表示不允许将编号为 a 和 b 的人归入同一组。
当可以用这种方法将所有人分进两组时，返回 true；否则返回 false。
示例 1：
输入：N = 4, dislikes = [[1,2],[1,3],[2,4]]
输出：true
解释：group1 [1,4], group2 [2,3]
示例 2：
输入：N = 3, dislikes = [[1,2],[1,3],[2,3]]
输出：false
示例 3：
输入：N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
输出：false
'''
import collections
from typing import List


# class Solution:
#     def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
#         print(N,dislikes)


class Solution(object):
    def possibleBipartition(self, N, dislikes):
        graph = collections.defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        color = {}
        def dfs(node, c = 0):
            if node in color:
                return color[node] == c
            color[node] = c
            return all(dfs(nei, c ^ 1) for nei in graph[node])

        return all(dfs(node)
                   for node in range(1, N+1)
                   if node not in color)




N = 5
dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
solution = Solution()
solution.possibleBipartition(N,dislikes)
