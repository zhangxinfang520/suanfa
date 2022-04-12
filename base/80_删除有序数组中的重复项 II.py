# encoding: utf-8
"""
@author: zxf_要努力
@file: 80_删除有序数组中的重复项 II.py
@time: 2022/4/12 10:32
"""
'''
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 最多出现两次 ，返回删除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

输入：nums = [1,1,1,2,2,3]
输出：5, nums = [1,1,2,2,3]
解释：函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。 不需要考虑数组中超出新长度后面的元素。

输入：nums = [0,0,1,1,1,1,2,3,3]
输出：7, nums = [0,0,1,1,2,3,3]
解释：函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。 不需要考虑数组中超出新长度后面的元素
'''


class Solution(object):
    def removeDuplicates(self, nums):
        j = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[j - 2]:
                nums[j] = nums[i]
                j += 1
        return j


    def removeDuplicates1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (n:=len(nums)) <= 2:
            return len(nums)
        count,begin  = 0,0
        while begin < n:
            right,len_ = self.bin_sort_bound_right(begin, nums[begin], nums)
            if len_ > 2:
                count +=2
            else:
                count += len_
            begin = right + 1
        return count

    def bin_sort(self,left,target,nums):
        begin = left
        right = len(nums) - 1
        while left <= right:
            mid = left + ((right-left) >> 1)
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid -1
            else:
                return mid

    def bin_sort_bound_left(self,left,target,nums):
        begin = left
        right = len(nums) - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                right = mid - 1
        #检查越界情况
        if left >= len(nums) or nums[left] !=target:
            return -1
        return left


    def bin_sort_bound_right(self,left,target,nums):
        begin = left
        right = len(nums) - 1
        if left == right:
            return right,1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            #锁定边界
            else:
                left = mid + 1

        #检查边界
        #if right < 0 or nums[right] != target:
        #   return -1
        if right == begin or nums[right] != target:
            return right,1
        else:
            return right,right-begin + 1

if __name__ == '__main__':
    
    #nums = [0,0,1,1,1,1,2,3,3,3,4,4,4,4,5,5,5,5]
    nums = [0,0,1,1,1,1,2,3,3]
    s = Solution()
    #print(s.bin_sort_bound_right(7, 3, nums))
    print(s.removeDuplicates(nums))





