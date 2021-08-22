# -*- coding:utf-8 -*-
#@Time : 2021/8/21 19:29
#@Author: zxf_要努力
#@File : 京东.py
import sys


def is_Valid(str_):
    if len(str_) == 1:
        return 1
    list_str = list(str_)
    list_str.sort()
    n = len(list_str)
    o_count = 0
    for i in range(0, n):
        if list_str[i] == '0':
            o_count += 1
        else:
            break
    l_count = n - o_count
    if o_count == 0:
        return l_count
    if l_count == 0:
        return o_count
    if l_count > o_count:
        if l_count % o_count and o_count!=1:
            return 1
        else:
            return o_count
    else:
        if l_count == 1:return 1
        if o_count % l_count and l_count!=1:
                return 1
        else:
            return l_count


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    str_ = str(sys.stdin.readline().strip())
    # n,str_ = 9, str('010100001')
    # n,str_ = 3, str('001')
    # dict_count = dict()
    if n != len(str_):
        print(0)
    else:
        for i in range(0, n):
            temp = str_[0:i + 1]
            print(is_Valid(temp), end=" ")





