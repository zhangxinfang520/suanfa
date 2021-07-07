# -*- coding:utf-8 -*-
#@Time : 2021-07-04 21:47
#@Author: zxf_要努力
#@File : 04_两个数组的交集II.py
'''
给定两个数组，编写一个函数来计算它们的交集。
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]
有个几个输出几个
思路 找到一个删除一个
'''
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = list()
        if len(nums1) == 0 or len(nums2) == 0:
            return result

        while nums1 and nums2:
            temp = nums1.pop()
            if temp not in nums2:
                continue
            index = nums2.index(temp)
            result.append(temp)
            nums2.pop(index)
        return result
            
nums1 = [1,2,2,1]
nums2 = [2,2]
print(Solution().intersect(nums1, nums2))