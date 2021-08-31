# -*- coding:utf-8 -*-
#@Time : 2021/8/31 11:41
#@Author: zxf_要努力
#@File : merge_sort.py

class Megre:
    def merge_sort(self,nums):
        if len(nums)<=1:
            return nums
        mid = len(nums) // 2
        #left = len(nums) % 2
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])
        return self.merge_2_one(left,right)

    def merge_2_one(self,left,right):
        res = []
        i,j = 0, 0
        while i<len(left) and j < len(right):
            if left[i] <right[j]:
                res.append(left[i])
                i +=1
            else:
                res.append(right[j])
                j +=1
        res += left[i:]
        res += right[j:]
        return res

if __name__ == '__main__':
    nums = [2,5,6,8,4,6,32,4,9]
    print(Megre().merge_sort(nums))
