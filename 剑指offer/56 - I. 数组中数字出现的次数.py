# -*- coding:utf-8 -*-
#@Time : 2021/10/9 19:09
#@Author: zxf_要努力
#@File : 56 - I. 数组中数字出现的次数.py

'''
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。
要求时间复杂度是O(n)，空间复杂度是O(1)。

输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
'''
from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        x, y, n, m = 0, 0, 0, 1
        for num in nums:         # 1. 遍历异或
            n ^= num
        while n & m == 0:        # 2. 循环左移，计算 m
            m <<= 1
        for num in nums:         # 3. 遍历 nums 分组
            if num & m: x ^= num # 4. 当 num & m != 0
            else: y ^= num       # 4. 当 num & m == 0
        return x, y 

if __name__ == '__main__':
    nums = [3,3,2,2,1,1,44,5,44]
    print(Solution().singleNumbers(nums))