# -*- coding:utf-8 -*-
# @Time : 2021/8/28 18:38
# @Author: zxf_要努力
# @File : 荣耀01.py

import sys


def get_first(persons):
    if len(persons) == 0:
        return 0
    dict_nums = dict()
    for person in persons:
        if person.isalpha():
            if len(person) == 1 and person[0].isupper():
                if person in dict_nums.keys():
                    dict_nums[person] += 1
                else:
                    dict_nums[person] = 1
            elif person[0].isupper() and person[1:].islower():
                if person in dict_nums.keys():
                    dict_nums[person] += 1
                else:
                    dict_nums[person] = 1
            else:
                return 0
        else:
            return 0
    sort_list = sorted(dict_nums.items(), key=lambda x: (-x[1]))

    max_ = sort_list[0][1]
    res = sort_list[0][0]

    for i in range(1, len(sort_list)):
        if max_ == sort_list[i][1]:
            if len(res) > len(sort_list[i][0]) and res[:len(sort_list[i][0])] == sort_list[i][0]:
                res = sort_list[i][0]
            elif (ascii(res) > sort_list[i][0]):
                res = sort_list[i][0]
            else:
                pass
        else:
            break
    return res


if __name__ == "__main__":
    # 读取第一行的n
    #list_person = sys.stdin.readline().strip().split(",")
    list_person = ["Lily","Tom","Lucy","Lucy","Jack","Abc","Tom","Tom","Tomy","Tomy","Tomy","Lucy"]
    res = get_first(list_person)
    if res == 0:
        print("error.001")
    else:
        print(res)
