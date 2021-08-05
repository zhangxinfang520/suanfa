# -*- coding:utf-8 -*-
#@Time : 2021-08-03 14:25
#@Author: zxf_要努力
#@File : 241_运算表达式设计优先级.py
'''
给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及 * 。
输入: "2-1-1"
输出: [0, 2]
解释:
((2-1)-1) = 0
(2-(1-1)) = 2
输入: "2*3-4*5"
输出: [-34, -14, -10, -10, 10]
解释:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
'''
from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]

        res = []
        for i,char in enumerate(expression):
            # 1.分解：遇到运算符，计算左右两侧的结果集
            # 2.解决：diffWaysToCompute 递归函数求出子问题的解
            left = self.diffWaysToCompute(expression[:i])
            right = self.diffWaysToCompute(expression[i+1:])
            #合并：根据运算符合并子问题的解
            for l in left:
                for r in right:
                    if char == "+":
                        res.append(l + r)
                    elif char=="-":
                        res.append(l-r)
                    else:
                        res.append(l*r)
        return res
ex = "2-1-1"
print(Solution().diffWaysToCompute(ex))
