# -*- coding:utf-8 -*-
#@Time : 2021-03-13 21:34
#@Author: zxf_要努力
#@File : 18.py
'''
四数之和
给定一个包含 n 个整数的数组 nums 和一个目标值 target，
判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组

示例 1：

输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
示例 2：
输入：nums = [], target = 0
输出：[]
四个指针
first second third end
我使用的暴力简单的
first second third 放在数组前面
end 从后往前遍历

另一种方法
first second 放在前面
third end 放在后面 镜像遍历
'''
class Solution(object):
    def fourSum(self, nums, target):
        if len(nums) ==0:
            return []
        nums.sort()
        n = len(nums)
        result = list()
        for first in range(n):
            if first!=0 and nums[first] ==nums[first-1]:
                continue

            for second in range(first+1,n):
                if second != (first+1) and nums[second] == nums[second - 1]:
                    continue
                for third in range(second+1,n):
                    end = n - 1
                    aim = target - nums[first]-nums[second]-nums[third]
                    if third !=(second+1) and nums[third] ==nums[third-1]:
                        continue
                    while end > third and nums[end] > aim:
                        end -= 1
                    if end == third:
                        continue
                    if nums[end] == aim:
                        result.append([nums[first],nums[second],nums[third],nums[end]])
        return result




nums = [-3,-2,-1,0,0,1,2,3]
target = 0
a = Solution()
print(a.fourSum(nums, target))
