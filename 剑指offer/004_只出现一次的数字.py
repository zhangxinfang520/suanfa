# -*- coding:utf-8 -*-
#@Time : 2021/8/23 14:25
#@Author: zxf_要努力
#@File : 004_只出现一次的数字.py
'''
给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。
请你找出并返回那个只出现了一次的元素。
输入：nums = [2,2,3,2]
输出：3
输入：nums = [0,1,0,1,0,1,100]
输出：100
快速选择 快排算法里面的分区。
随机从nums中选取pivot,利用快速排序算法里面的分区函数，分成2个区，<pivot的 和 >=pivot的。如果其中一个分区大小不是3的整数倍，
说明目标元素出现在那个分区。需要继续对分区进行再分区。重复分区过程，直至有分区大小==1，则返回该分区的数。

思路二 利用状态机和位运算，
one = (one^x)&~two 只保留出现一次的数
two = (two^x)&~one 只保留出现2次的数
'''
from typing import List


class Solution:
    def singleNumber1(self, nums: List[int]) -> int:
        #快排思想
        n = len(nums)
        def quicksort(l,r):
            if l < r:
                i, j = l, r
                temp = nums[i]
                while i < j:
                    while i<j and nums[j] >= temp:
                        j -=1
                    if i <j:
                        nums[i] = nums[j]
                        i +=1
                    while i < j and nums[i] < temp:
                        i +=1
                    if i < j:
                        nums[j] = nums[i]
                        j -=1
                nums[i] = temp
                if (i) % 3 == 0:
                    quicksort(i,r)
                elif (n-i) % 3 == 0:
                    quicksort(l,i-1)
                else:
                    return temp

        return quicksort(0,n-1)

    def singleNumber(self, nums: List[int]) -> int:
        one, two = 0, 0
        for x in nums:
            one = (one ^ x) & ~two # 只保留出现一次的数
            two = (two ^ x) & ~one #只保留出现2次的数
        return one



if __name__ == '__main__':
    nums = [4,1,2,3,3,2,1,2,3,4,4,6,5,5,5,1]
    print(Solution().singleNumber1(nums))