# encoding: utf-8
"""
@author: zxf_要努力
@file: 001_整数除法.py
@time: 2022/3/21 15:24
"""


# 给定两个整数 a 和 b ，求它们的除法的商 a/b ，要求不得使用乘号 '*'、除号 '/' 以及求余符号 '%'
# 整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231, 231−1]。本题中，如果除法结果溢出，则返回 231 − 1

class Solution(object):
    def divide(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

        if a > (pow(2,31)-1):
            a = (pow(2,31)-1)
        if a < -(pow(2,31)):
            a = -(pow(2,31))
        if a ==0:return 0
        flag = 0
        if (a > 0 and b>0) or (a< 0 and b < 0) :
            flag = 1
        else:
            flag = -1
        if a < 0 :
            a = -a
        if b < 0:
            b = -b
        if b == 1:
            return flag * a if flag * a < (pow(2,31)-1)  else (pow(2,31)-1)
        res = 0

        while a >= b:
            a -=b
            res +=1
        return  res * flag if res * flag < (pow(2,31)-1) else (pow(2,31)-1)

    def divide2(self, a: int, b: int) -> int:
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
        if a == INT_MIN and b == -1:
            return INT_MAX

        ans = 0

        # 处理边界，防止转正数溢出
        if b == INT_MIN:  # 除数绝对值最大，结果必为 0 或 1
            return 1 if a == b else 0
        if a == INT_MIN:  # 被除数先减去一个除数
            a -= -abs(b)
            ans += 1

        sign = -1 if (a > 0) ^ (b > 0) else 1

        a, b = abs(a), abs(b)
        for i in range(31, -1, -1):
            if (a >> i) - b >= 0:
                a = a - (b << i)
                # 代码优化：这里控制 ans 大于等于 INT_MAX
                if ans > INT_MAX - (1 << i):
                    return INT_MIN
                ans += 1 << i
        # bug 修复：因为不能使用乘号，所以将乘号换成三目运算符
        return ans if sign == 1 else -ans


if __name__ == '__main__':
    print(Solution().divide2(147483648,7))
