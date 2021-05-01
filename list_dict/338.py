# -*- coding:utf-8 -*-
#@Time : 2021-03-03 21:11
#@Author: zxf_要努力
#@File : 338.py

#给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
# 输入: 2
# 输出: [0,1,1]
# 输入: 5
# 输出: [0,1,1,2,1,2]

# class Solution(object):
#     def countBits(self, num):
#         """
#         :type num: int
#         :rtype: List[int]
#         """
#         a = []
#         for i in range(0,num+1):
#             a.append(self.get_ont_count(i))
#         print(a)
#     def get_ont_count(self,num):
#         count = 0
#
#         while num :
#             if num % 2 ==1:
#                 count += 1
#             num = int(num / 2)
#         return count
#
# Solution().countBits(2)


class Solution(object):

    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        a = [0]
        for i in range(1,num+1):
            if i % 2 == 1:
                a.append( a[i-1] +1)
            else:
                a.append( a[ int(i/2) ] )
        return a

Solution().countBits(5)




