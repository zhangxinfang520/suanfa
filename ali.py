# -*- coding:utf-8 -*-
#@Time : 2021/9/22 9:02
#@Author: zxf_要努力
#@File : ali.py
import re
import sys

def get_(s:str):

    temp = []
    res = []
    for i in range(len(s)-1,1,-1):
        if s[i].isdigit():
            temp.append(int(s[i]))
        elif s[i] in ["+","-","*","/"]:
            flag = get_res(temp,s[i])
            if not flag:
                return "invalid epression"
            elif flag =="zero":
                return "division expression"
            else:
                res.append(flag)
            temp = []
    res = get_res(res,s[1])
    return res


def get_res(lists,op):
    if op == "+":
        if len(lists) == 0:
            return False
        return sum(lists)
    elif op == "*":
        if len(lists) == 0:
            return False
        res = 1
        for num in lists:
            res *=num
        return res
    elif op == "/":
        if len(lists) != 2:
            return False
        if lists[0] == 0:
            return "zero"
        return lists[-1] // lists[0]
    else:
        if len(lists) != 2:
            return False
        return lists[-1] - lists[0]




if __name__ == "__main__":
    # 读取第一行的n
    # t = int(sys.stdin.readline().strip())
    # for i in range(t):
    #     # 读取每一行
    #     n, k = list(map(int,sys.stdin.readline().strip().split()))
    #     in_list = list(map(int,sys.stdin.readline().strip().split()))
    #     out_list = list(map(int,sys.stdin.readline().strip().split()))
    #
    #     res = get_ot_nums(n,k,in_list,out_list)
    #     print(res)
    s  = "(+ (* 1 2 3 4) (/ 6 2) (- 1 4 ))"
    res = get_(s)
    print(res)

