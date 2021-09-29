# -*- coding:utf-8 -*-
#@Time : 2021/9/27 21:38
#@Author: zxf_要努力
#@File : 0_两分查找_查找两个边界.py


class Solution:

    def get_index(self,nums,target):
        return [self.get_left(nums,target),self.get_right(nums,target)]

    def get_left(self,nums,target):
        n = len(nums)
        left,right = 0,n-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] >= target:
                right = mid -1
            else:
                left = mid + 1
        if left == n or nums[left] !=target:
            return -1
        return left


    def get_right(self,nums,target):
        n = len(nums)
        left, right = 0, n - 1
        while left <=right:
            mid = (left+right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        if right == n or nums[right] != target:
            return -1
        return right

if __name__ == '__main__':
    nums = [1,2,3,4,4,5,6,6,6,7,8,9]
    target = 9
    se = Solution().get_index(nums,target)
    print(se)