# -*- coding:utf-8 -*-
#@Time : 2021-07-27 21:37
#@Author: zxf_要努力
#@File : 20_有效的括号.py
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
# 有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n == 0:
            return True
        if n % 2 == 1:
            return False
        str_list = list(s)
        stack = []
        while  len(str_list) > 0:
            temp = str_list.pop(0)
            if temp in ["(","{","["]:
                stack.append(temp)
            else:
                if len(stack) == 0:
                    return False
                else:
                    if (stack[-1],temp) not in [('(',')'), ('{','}'), ('[',']')]:
                        return False
                    else:
                        stack.pop()
        if len(stack) > 0:
            return False
        return True
s = "()[](()[]"
print(Solution().isValid(s))
        
