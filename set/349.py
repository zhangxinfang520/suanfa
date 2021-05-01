'''
给定两个数组，编写一个函数来计算它们的交集
'''
class Solution:
    def intersection(self, nums1, nums2):
        set_list01 = set(nums1)
        set_list02 = set(nums2)
        result = set_list01.intersection(set_list02)
        return list(result)