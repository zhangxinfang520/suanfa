# -*- coding:utf-8 -*-
#@Time : 2021/9/11 21:50
#@Author: zxf_要努力
#@File : 在一个先增长后减小的数组中找到最大值.py
#在一个数组中获取最大值

# class Solution:
#     def findTop(self,nums):
#         n = len(nums)
#         return self.findPeakutils(0,n-1,nums)
#
#
#     def findPeakutils(self,low,high,nums):
#         mid = (low + high) // 2
#         if ( mid == 0 or nums[mid-1] < nums[mid]) and (mid == len(nums)-1 or nums[mid+1]<nums[mid]):
#             return mid
#
#         elif (mid>0 and nums[mid-1] > nums[mid]):
#             return self.findPeakutils(low,mid-1,nums)
#         else:
#             return self.findPeakutils(mid+1,high,nums)

import sys

#时间复杂度 logn
#修改左右边界 就是那个等号的左右相等的时候 修改一下
#再用二分查找去？？？ （logn）
def get_target(nums,target):
    if not nums:
        return -1
    l, r = 0, len(nums) - 1
    #二分查找
    while l <= r:
        #获取中间值
        mid = (l + r) // 2
        if nums[mid] == target:
            #在这里几个一个while吧
            # if mid == 0:
            #     return mid
            # while mid >= 0 and nums[mid-1] == nums[mid]:
            #     mid -=1
            return mid
        if nums[0] < nums[mid]:
            #判断target是否在升序子数组中

            if nums[0] < target <= nums[mid]:
                #如果在右指针左移
                r = mid - 1
            else:
                #不在 左指针右移动
                l = mid + 1
        else:
            #在降序数组中
            if nums[mid] <= target < nums[len(nums) - 1]:
                l = mid + 1
            else:
                r = mid - 1
    return -1
#冒泡排序
def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums



#调试 写输入 输入是两行 第一行 4 5 7 0 1 2 按照空格隔开
#第二行为一个target
if __name__ == '__main__':
    #输入 4 5 7 0 1 2
    # 0
    # nums = list(map(int,sys.stdin.readline().strip().split(" ")))
    # target = int(sys.stdin.readline())
    nums = [4,5,7,7,7,0,0,0,0,1,2,2,2,2]
    target = 0
    print(get_target(nums,target))