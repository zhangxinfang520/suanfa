# -*- coding:utf-8 -*-
# @Time : 2021-05-13 13:57
# @Author: zxf_要努力
# @File : 匈牙利算法.py
'''
要用到深度优先遍历优先
思路:
1. 匈牙利算法
求解目标：找到二分图的最大匹配
整体思路：每一步寻找一条增广路径，取反
2. 关键步骤
二分图的顶点分为左边点集X和右边点集Y，假定遍历的点集是X。对于每一次迭代的点x_i，

搜索增广路径：遍历x_i的邻接节点y_j
如果y_j未匹配，则找到增广路
如果y_j已匹配，则寻找y_j的匹配节点的增广路径（深搜或者广搜）

取反：把增广路径中的已经匹配边改成未匹配；未匹配的改成匹配
'''


class BFS_hungary(object):

    def __init__(self, graph):
        self.g = graph  # 无向图的矩阵表示
        self.Nx = len(graph)  # 顶点集A的个数
        self.Ny = len(graph[0])  # 顶点集B的个数
        self.Mx = [-1] * self.Nx  # 初始匹配
        self.My = [-1] * self.Ny  # 初始匹配
        self.chk = [-1] * max(self.Nx, self.Ny)  # 是否匹配
        self.Q = []

    def Max_match(self):
        res = 0  # 最大匹配数
        self.Q = [0 for i in range(self.Nx * self.Ny)]
        prev = [0] * max(self.Nx, self.Ny)  # 是否访问
        for i in range(self.Nx):
            if self.Mx[i] == -1:  # A中顶点未匹配
                qs = qe = 0
                self.Q[qe] = i
                qe += 1
                prev[i] = -1
                flag = 0
                while (qs < qe and not flag):
                    u = self.Q[qs]
                    for v in range(self.Ny):
                        if flag: continue
                        if self.g[u][v] and self.chk[v] != i:  #
                            self.chk[v] = i
                            self.Q[qe] = self.My[v]
                            qe += 1
                            if self.My[v] >= 0:  #
                                prev[self.My[v]] = u
                            else:
                                flag = 1
                                d, e = u, v
                                while d != -1:  # 将原匹配的边去掉加入原来不在匹配中的边
                                    t = self.Mx[d]
                                    self.Mx[d] = e
                                    self.My[e] = d
                                    d = prev[d]
                                    e = t
                    qs += 1
                if self.Mx[i] != -1:  # 如果已经匹配
                    res += 1

        return res


if __name__ == '__main__':
    g = [[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 0, 1], [0, 0, 1, 0]]

    mm = BFS_hungary(g)

    print('res', mm.Max_match())
