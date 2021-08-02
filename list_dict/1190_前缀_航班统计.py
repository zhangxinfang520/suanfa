# -*- coding:utf-8 -*-
#@Time : 2021-08-02 13:54
#@Author: zxf_要努力
#@File : 1190_前缀_航班统计.py
'''
这里有 n 个航班，它们分别从 1 到 n 进行编号。
有一份航班预订表 bookings ，表中第 i 条预订记录 bookings[i] = [firsti, lasti, seatsi] 
意味着在从 firsti 到 lasti （包含 firsti 和 lasti ）的 每个航班 上预订了 seatsi 个座位。
请你返回一个长度为 n 的数组 answer，其中 answer[i] 是航班 i 上预订的座位总数。

输入：bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
输出：[10,55,45,25,25]
解释：
航班编号        1   2   3   4   5
预订记录 1 ：   10  10
预订记录 2 ：       20  20
预订记录 3 ：       25  25  25  25
总座位数：      10  55  45  25  25
因此，answer = [10,55,45,25,25]
输入：bookings = [[1,2,10],[2,2,15]], n = 2
输出：[10,25]
解释：
航班编号        1   2
预订记录 1 ：   10  10
预订记录 2 ：       15
总座位数：      10  25
因此，answer = [10,25]
'''
from typing import List


class Solution:
    '''此方法超时'''
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        re = [0] * (n+1)
        re_hash = dict()
        for (first,last,seats) in bookings:

            for i in range(first,last+1):
                temp = re[i]
                re[i] = temp + seats
        return re[1:]
    '''构造差分数组'''
    def corpFlightBookings1(self, bookings: List[List[int]], n: int) -> List[int]:
        '''
        构建差分数组
        n = len(nums)
        diff = [0] * n
        diff[0] = nums[0]
        for i in range(1,n):
            diff[i] = nums[i] - nums[i-1]
        从差分数组还原回原数组
        or_nums = [0] * n
        or_nums[0] = diff[0]
        for i in range(1,n):
            or_nums[i] = or_nums[i-1] + diff[i]
        '''
        nums = [0] * n
        d = Difference(nums)
        for (first, last, seats) in bookings:
            #注意索引
            d.inccrement(first-1,last-1,seats)
        return d.get_ori_nums()


class Difference:

    def __init__(self,nums):
        n = len(nums)
        assert  n > 0
        self.diff = [0] * n
        self.diff[0] = nums[0]
        for i in range(1,n):
            self.diff[i] = nums[i] - nums[i-1]

    def inccrement(self,i,j,val):
        '''对 区间 i，j进行加/减 值 '''
        self.diff[i] +=val
        if(j+1) <len(self.diff):
            self.diff[j+1] -=val

    def get_ori_nums(self):
        res = [0] * (len(self.diff))
        res[0] = self.diff[0]
        for i in range(1,len(self.diff)):
            res[i] = res[i-1] + self.diff[i]
        return res


bookings = [[1,2,10],[2,3,20],[2,5,25]]
n = 5
# nums = [1,2,3,4,5]
# d = Difference(nums)
# d.inccrement(0,2,3)
# print(d.get_ori_nums())
print(Solution().corpFlightBookings(bookings, n))
