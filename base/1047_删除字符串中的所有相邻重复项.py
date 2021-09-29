# -*- coding:utf-8 -*-
#@Time : 2021/9/18 12:13
#@Author: zxf_要努力
#@File : 1047_删除字符串中的所有相邻重复项.py

'''
给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
在 S 上反复执行重复项删除操作，直到无法继续删除。
在完成所有重复项删除操作后返回最终的字符串。答案保证唯一
输入："abbaca"
输出："ca"
解释：
例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。
之后我们得到字符串 "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。
'''
class Solution:
    def removeDuplicates(self, s: str) -> str:
        n = len(s)
        if n  == 1 or n == 0 :
            return s
        s_list = list(s)
        if len(set(s_list)) == 1:
            return s[0]
        stack = []

        while len(s_list):
            if not stack:
                stack.append(s_list.pop(0))
            else:
                if stack[-1] == s_list[0]:
                    temp = stack[-1]
                    j = 0
                    while j < len(s_list):
                        if s_list[j] == temp:
                            j += 1
                        else:
                            break
                    stack.pop()
                    s_list = s_list[j:]
                else:
                    stack.append(s_list.pop(0))
        return "".join(stack)

    def removeDuplicates1(self, s: str) -> str:
        stk = list()
        for ch in s:
            if stk and stk[-1] == ch:
                stk.pop()
            else:
                stk.append(ch)
        return "".join(stk)

if __name__ == '__main__':
    s = "aaaaaaaaa"
    print(Solution().removeDuplicates(s))
