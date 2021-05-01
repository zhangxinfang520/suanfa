# -*- coding:utf-8 -*-
#@Time : 2021-04-17 20:57
#@Author: zxf_要努力
#@File : 56.py
'''
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

示例 1：
输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例 2：
输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。

'''
def megre(intervals):
    sort_list = sorted(intervals,key=lambda x:(x[0],-x[1]))
    temp = []
    for i in range(len(sort_list)-1):
        if sort_list[i][0]<=sort_list[i+1][0] and sort_list[i][1] >= sort_list[i+1][1]:
            sort_list[i + 1][0] = sort_list[i][0]
            sort_list[i + 1][1] = sort_list[i][1]
            temp.append(i)
        elif sort_list[i][1] >= sort_list[i+1][0]:
            sort_list[i + 1][0] = sort_list[i][0]
            temp.append(i)
    if len(temp)== 0:
        return intervals
    else:
        for i in sorted(temp,reverse=True):
            sort_list.pop(i)
        return sort_list
#a = [[1,3],[2,6],[8,10],[15,18]]
a = [[1,4],[0,2],[3,5]]
print(megre(a))
