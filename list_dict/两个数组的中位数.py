# -*- coding:utf-8 -*-
#@Time : 2021/8/22 19:28
#@Author: zxf_要努力
#@File : 两个数组的中位数.py
'''
给两个排序好的数组
求排序好的中位数

'''

class Solution:
    def find_median_soreted_arrays(self,A,B):
        m, n = len(A), len(B)
        #如果数组A的长度大于数组B
        if m > n:
            self.find_median_soreted_arrays(B,A)
        if n == 0:
            return
        start, end, half =0, m , (m+n+1)/2#为什么加一 因为考虑到奇数
        while start < end:
            i = (start + end) / 2
            j = half - i
            if i < m and B[j-1] > A[i]:
                #i 设置小了
                start = i + 1
            elif i > 0 and A[i-1] > B[j]:
                end = i - 1
            else:
                #i 刚好 或者i已到达数组边界
                if i==0:
                    max_of_left = B[j-1]
                elif j==0:
                    max_of_left = A[i-1]
                else:
                    max_of_left = max(A[i-1],B[j-1])
                if (m+n)%2 == 1:
                    return max_of_left
                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i],B[j])
                return (max_of_left + min_of_right) / 2.0

