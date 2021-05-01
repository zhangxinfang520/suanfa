# -*- coding:utf-8 -*-
#@Time : 2021-04-05 19:09
#@Author: zxf_要努力
#@File : 88.py
'''

 

示例 1：

输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
示例 2：

输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]
 

提示：
nums1.length == m + n
nums2.length == n

'''


def merge(nums1, nums2):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    nums1.sort(reverse=False)
    print(nums1)
    len_nums1 =len(nums1)
    len_nums2 =len(nums2)
    x1 = len_nums2
    x2 = 0
    z = 0
    while z < len_nums1+ len_nums2-2 and x2<len_nums2 and x1 < len_nums1:
        if nums1[x1] < nums2[x2]:
            nums1[z] = nums1[x1]
            z +=1
            x1 +=1
        else:
            nums1[z] = nums2[x2]
            x2 +=1
            z +=1
    if x1 == len_nums1 and x2!=len_nums2 :
        while z < len_nums1:
            for i in range(x2, len_nums2):
                nums1[z] = nums2[i]
                z += 1
    return nums1


nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

print(merge(nums1, nums2))

