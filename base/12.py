# -*- coding:utf-8 -*-
#@Time : 2021-07-14 12:43
#@Author: zxf_要努力
#@File : 12.py
'''
读入字符串并丢弃无用的前导空格
检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。 确定最终结果是负数还是正数。 如果两者都不存在，则假定结果为正。
读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。
将前面步骤读入的这些数字转换为整数（即，"123" -> 123， "0032" -> 32）。如果没有读入数字，则整数为 0 。必要时更改符号（从步骤 2 开始）。
如果整数数超过 32 位有符号整数范围 [−231,  231 − 1] ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 −231 的整数应该被固定为 −231 ，大于 231 − 1 的整数应该被固定为 231 − 1 。
返回整数作为最终结果。
'''
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0
        digits = []
        begin = 0
        flag = 1
        if s[begin] == " ":
            while s[begin] == " ":
                begin += 1
                if begin == n:
                    return 0
        if s[begin] == "-":
            flag = -1
            begin += 1
        elif s[begin] == "+":
            begin += 1
        if begin == n:
            return 0
        if s[begin] in "1234567890":
            while s[begin] in "1234567890":
                digits.append(s[begin])
                begin += 1
                if begin == len(s):
                    break
        else:
            return 0

        if len(digits) == 0:
            return 0
        j = 0
        while digits[j] == '0':
                j += 1
                if j == len(digits):
                    return 0
        if j == len(digits):
            return 0
        x = 1
        sum = 0
        for i in range(len(digits)-1 ,j-1,-1):
            sum += int(digits[i]) * x
            x *= 10
        if flag * sum > pow(2,31) - 1:
            return pow(2,31) - 1
        if flag * sum < -pow(2,31):
            return -pow(2, 31)

        return flag * sum

str =" "

print(Solution().myAtoi(str))


