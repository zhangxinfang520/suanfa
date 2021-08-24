# -*- coding:utf-8 -*-
#@Time : 2021/8/24 11:26
#@Author: zxf_要努力
#@File : 84_含有重复元素集合的全排列.py
'''
给定一个可包含重复数字的整数集合 nums ，按任意顺序 返回它所有不重复的全排列。
输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        path = []
        visited = [False for _ in range(n)]

        def backtrace(idx: int) -> None:
            if idx == n:
                res.append(path[:])
                return

            for i in range(0, n):
                if visited[i] == True:
                    continue
                if 0 < i and nums[i - 1] == nums[i] and visited[i - 1] == False:
                    continue
                path.append(nums[i])
                visited[i] = True
                backtrace(idx + 1)
                visited[i] = False
                path.pop()

        backtrace(0)
        return res


if __name__ == '__main__':
    nums = [1,2,3]
    print(Solution().permuteUnique(nums))
