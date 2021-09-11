# -*- coding:utf-8 -*-
#@Time : 2021/9/11 21:50
#@Author: zxf_要努力
#@File : 在一个先增长后减小的数组中找到最大值.py

class Solution:
    def findTop(self,nums):
        n = len(nums)
        return self.findPeakutils(0,n-1,nums)


    def findPeakutils(self,low,high,nums):
        mid = (low + high) // 2
        if ( mid == 0 or nums[mid-1] < nums[mid]) and (mid == len(nums)-1 or nums[mid+1]<nums[mid]):
            return mid
        
        elif (mid>0 and nums[mid-1] > nums[mid]):
            return self.findPeakutils(low,mid-1,nums)
        else:
            return self.findPeakutils(mid+1,high,nums)

if __name__ == '__main__':
    nums = [1,2,3,5,6,67,5,4,2,1]
    print(Solution().findTop(nums))