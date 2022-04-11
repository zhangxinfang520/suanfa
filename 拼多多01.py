# encoding: utf-8
"""
@author: zxf_要努力
@file: 拼多多01.py
@time: 2022/4/10 19:38
"""
import sys


def is_diff(s_list):
    n = len(s_list)
    return all([s_list[i] - s_list[i - 1] == s_list[-1] - s_list[-2] for i in range(n - 1, 0, -1)])


def get_result(n_list):
    tone_dict = dict()
    result = dict()
    for i,tone in enumerate(n_list):
        if tone in tone_dict.keys():
            temp = tone_dict[tone]
            temp.append(i+1)
            tone_dict[tone] = temp
        else:
            tone_dict[tone] = [i+1]
    for stone,s_list in tone_dict.items():
        if len(s_list) == 0 or len(s_list) == 1:
            result[stone] = 0
        else:
            if is_diff(s_list):
                result[stone] = s_list[1] - s_list[0]
    return result




if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    n_list = list(map(int,sys.stdin.readline().strip().split(" ")))
    result = get_result(n_list)

    result = sorted(result.items(),key=lambda x:x[0])

    for key,value in result:
        print(str(key)+" "+str(value))

