# -*- coding:utf-8 -*-
#@Time : 2021/9/26 20:11
#@Author: zxf_要努力
#@File : 腾讯1.py
import  sys

def get_zhishu(n,x):
    if x == 1:
        return [6]
    re = []
    for j in range (1,n+1):
        if j % 2 == 0:
            continue
        if n%j == 0:
            if len(re):
                if j - re[-1] >= x:
                    re.append(j)
                    if len(re) == 4:
                        return re
                else:
                    return False
            else:
                re.append(j)
    if len(re) < 4:
        return False
    return re


def get_nums(x):
    i = 1
    flag = True
    while flag:
        res = get_zhishu(i,x)
        if res == False:
            i +=1
        else:
            flag = False
    return res



if __name__ == '__main__':
    # T = int(sys.stdin.readline().strip())
    # for _ in range(T):
    #     x = int(sys.stdin.readline().strip())
        print(get_nums(7)[-1])