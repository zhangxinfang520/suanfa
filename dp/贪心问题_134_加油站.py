# -*- coding:utf-8 -*-
#@Time : 2021/10/7 17:51
#@Author: zxf_要努力
#@File : 贪心问题_134_加油站.py

'''
在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。

你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。
如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。
说明:
如果题目有解，该答案即为唯一答案。
输入数组均为非空数组，且长度相同。
输入数组中的元素均为非负数。

'''
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        for i in range(0,len(gas)):
            if self.cangoFindish(i,gas,cost) !=-1:
                return i
        return -1

    def cangoFindish(self,i,gas,cost):
        left = 0
        for x in range(i,len(gas)):
            left += gas[x]
            left -= cost[x]
            if left == 0 and x==len(gas)-1 and i==0:
                return 0
            elif left <=0:
                return -1

        for x in range(0,i):
            left += gas[x]
            left -= cost[x]
            if left < 0:
                return -1

        return -1 if left < 0 else 0

if __name__ == '__main__':
    # gas = [1, 2, 3, 4, 5]
    # cost = [3, 4, 5, 1, 2]
    # gas = [2, 3, 4]
    # cost = [3, 4, 3]
    # gas = [4, 5, 3, 1, 4]
    # cost = [5, 4, 3, 4, 2]
    gas = [3, 1, 1]
    cost = [1, 2, 2]
    print(Solution().canCompleteCircuit(gas, cost))