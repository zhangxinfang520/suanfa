# -*- coding:utf-8 -*-
#@Time : 2021/9/2 15:54
#@Author: zxf_要努力
#@File : 69_x的算法平凡根.py
'''
实现 int sqrt(int x) 函数。
计算并返回 x 的平方根，其中 x 是非负整数。
由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。


'''
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        if x<= 0:
            return 0
        left = 0
        right = x
        mid = (left +right) / 2
        y = mid * mid
        while abs(y-x)> 0.000001:
            if y > x:
                right = mid
            elif y < x:
                left = mid
            else:
                return int(mid)
            mid = (right + left) / 2
            y = mid * mid
        return int(mid)

if __name__ == '__main__':
    x = 8
    print(Solution().mySqrt(x))