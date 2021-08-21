# -*- coding:utf-8 -*-
#@Time : 2021/8/21 10:19
#@Author: zxf_要努力
#@File : 有赞.py

import sys
if __name__ == "__main__":
    # 读取第一行的n #不能去除空格
    word = sys.stdin.readline().strip("")
    n = len(word)
    if n == 0:
        print("")
    stack = []
    i = 0
    while i < n:
        if not word[i].isalpha():
            stack.append(word[i])
            i +=1
        else:
            j = i
            temp = ""
            while j < n and word[j].isalpha() :
                if word[j].isalpha():
                    temp += word[j]
                    j += 1
            i = j
            stack.append(temp)
    res = ""
    for i in range(len(stack)-1,-1,-1):
        res += stack[i]
    print("%s"%res)

