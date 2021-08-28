# -*- coding:utf-8 -*-
#@Time : 2021/8/25 18:22
#@Author: zxf_要努力
#@File : 006排序数值中两个数字之和.py
'''
定一个已按照 升序排列  的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target 。
函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 0 开始计数 ，
所以答案数组应当满足 0 <= answer[0] < answer[1] < numbers.length 。

输入：numbers = [1,2,4,6,10], target = 8
输出：[1,3]

解释：2 与 6 之和等于目标数 8 。因此 index1 = 1, index2 = 3 。
输入：numbers = [2,3,4], target = 6
输出：[0,2]

输入：numbers = [-1,0], target = -1
输出：[0,1]
'''
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i = 0
        while i < n:
            if i != 0 and numbers[i-1] == numbers[i]:
                continue
            if numbers[i] > target:
                break
            end = target - numbers[i]
            j = n - 1
            while j > 0 and j > i:
                if end == numbers[j]:
                    return [i,j]
                if end < numbers[j]:
                    j -= 1
                else:
                    i +=1
                    break
    def twoSum1(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i, j = 0, n-1
        while i < j:
            temp =numbers[i] + numbers[j]
            if temp < target:
                i +=1
            elif temp > target:
                j -=1
            else:
                return [i,j]



if __name__ == '__main__':
    numbers = [1, 2, 4, 6, 10]
    target = 8
    print(Solution().twoSum(numbers,target))
