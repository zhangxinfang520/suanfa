# -*- coding:utf-8 -*-
# @Time : 2021-08-08 9:57
# @Author: zxf_要努力
# @File : test.py
import sys


class Solution:

    def test(self,values):
        n, x_1, y_1, z_1, x_2, y_2, z_2 = values
        target = [x_2, y_2, z_2]

        memo = set()

        def dp(x, y, z):
            if (x,y,z) in memo:
                return False
            else:
                memo.add((x,y,z))
            if [x, y, z] == target:
                return True
            if (x > n) or (y > n) or (z > n) or (x < 0) or (y < 0) or (z < 0):
                return False

            temp = dp(2 * y - x + 1, 2 * x - y - 1, z)

            temp = temp or dp(y, x, z)
            temp = temp or dp(x, z, y)
            temp = temp or dp(z, y, x)
            return temp
        print(dp(x_1, y_1, z_1))

values = [4, 1, 2, 1, 1,1,1]

Solution().test(values)



# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     ans = 0
#     for i in range(n):
#         # 读取每一行
#         line = sys.stdin.readline().strip()
#         # 把每一行的数字分隔后转化成int列表
#         values = list(map(int, line.split()))
#         x = values[0]
#         x_1, y_1, z_1, x_2, y_2, z_2 = values[1:]
#
#         target = [x_2, y_2, z_2]
#
#
#         def dp(x, y, z):
#             if [x, y, z] == target:
#                 return True
#             if (x > n) or (y > n) or (z > n) or (x < 0) or (y < 0) or (z < 0):
#                 return False
#
#             temp = dp(2 * y - x + 1, 2 * x - y - 1, z)
#             temp = temp or dp(y, x, z)
#             temp = temp or dp(x, z, y)
#             temp = temp or dp(z, y, x)
#             return temp
#
#
#         print(dp(x_1, y_1, z_1))
