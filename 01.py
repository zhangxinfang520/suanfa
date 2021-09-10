# -*- coding:utf-8 -*-
#@Time : 2021/8/30 15:26
#@Author: zxf_要努力
#@File : 01.py
import string


def get_letters(nums,target=3):
    res = []
    track = []
    n = len(nums)

    def dp(track,index):
        if index == n:
            return
        res.append(track[:])
        dp(track,index+1)
        track.append(nums[index])
        dp(track,index)
        track.pop()
    dp(track,0)
    return res

if __name__ == '__main__':
    # A = list(string.ascii_letters)
    # print(len(get_letters(A, 3)))
    # import random
    # a = random.randint(1,2)
    #
    # print(a)
    nums = [1,2,3,4]
    print(get_letters(nums))
    # A = [1,2,3,3,3,2,2,2]
    # b = {}
    # b = b.fromkeys(A)
    # print(list(b))