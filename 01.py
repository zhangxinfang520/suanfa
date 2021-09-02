# -*- coding:utf-8 -*-
#@Time : 2021/8/30 15:26
#@Author: zxf_要努力
#@File : 01.py
import string


def get_letters(nums,target=3):
    res = []
    track = []

    def dp(target,track):
        if target == 0:
            res.append(track[:])
            return
        for i in range(len(nums)):
            if target > 0 :
                track.append(nums[i])
                dp(target-1,track)
                track.pop()
    dp(3,track)
    return res

if __name__ == '__main__':
    # A = list(string.ascii_letters)
    # print(len(get_letters(A, 3)))
    # import random
    # a = random.randint(1,2)
    #
    # print(a)
    print(1e9+7)
    # A = [1,2,3,3,3,2,2,2]
    # b = {}
    # b = b.fromkeys(A)
    # print(list(b))