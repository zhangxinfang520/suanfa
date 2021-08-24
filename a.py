# -*- coding:utf-8 -*-
# @Time : 2021-07-01 16:54
# @Author: zxf_要努力
# @File : a.py
from typing import List

import numpy as np
# def quick_sort(nums):
#     def sort(l, r):
#         if l >= r: return
#         i, j = l, r
#         temp = nums[i]
#         while i < j:
#             while i < j and nums[j] > temp:
#                 j -= 1
#             if i < j:
#                 nums[i] = nums[j]
#                 i += 1
#             while i < j and nums[i] < temp:
#                 i += 1
#             if i < j:
#                 nums[j] = nums[i]
#                 j -= 1
#         nums[i] = temp
#         sort(l, i - 1)
#         sort(i + 1, r)
#
#     sort(0, len(nums) - 1)
#     return nums
from  linked_list.leetcode import generator_link,travel
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Partition:
    def partition(self, pHead, x):
        if not pHead:
            return None
        head = pHead
        re = ListNode(0)
        re_head = re
        pre,post = head,head
        while post:
            if post.val < x:
                temp = post.next
                re.next = ListNode(post.val)
                re = re.next
                pre.next = post.next
                post = temp
            else:
                pre = post
                post = post.next
        re.next = head

        return re_head.next

import random
def foo(n):
    random.seed()
    c1 = 0
    c2 = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        r1 = x * x + y * y
        r2 = (1 - x) * (1 - x) + (1 - y) * (1 - y)
        if r1 <= 1 and r2 <= 1:
           c1 += 1
        else:
           c2 += 1
    return   c1 / c2

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def trackback(track,idx):
            res.append(track[:])
            for i in range(idx,n):
                track.append(nums[i])
                trackback(track,i+1)
                track.pop()
        trackback([],0)
        return res


# def test():
#     for i in range(10):
#         print(i)
#         i +=1

if __name__ == '__main__':
    nums = [1,2,3]
    print(Solution().permuteUnique(nums))
    # a = "abec"
    # b = "abcdd"
    # print(a  in b)

    # nums = [7, 1, 5, 4, 2, 8, 6, 5]
    # pnode = generator_link(nums)
    # travel(Partition().partition(pnode,5))
    # a = "123456"
    # for i in range(len(a)):
    #  print(a[0:i]+"s"+a[i:len(a)])
    # a = 3
    # c = a ^ 2 ^ a
    # print(c)
    #
    # b = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
    # a = b[1:10:2]
    # print(a)
    # a = 2
    # print("%.2f"%a)
    #print(foo(100000))


    # res = map(lambda n:n>5,range(10))
    # print(list(res))
    #
    # res2 = filter(lambda x:x>5 ,range(10))
    # print(list(res2))

    #
    # a = np.repeat(np.arange(5).reshape([1, -1]), 10, axis=0) + 10.0
    # b = np.random.randint(5, size=a.shape)
    # c = np.argmin(a * b, axis=1)
    # b = np.zeros(a.shape)
    # b[np.arange(b.shape[0]), c] = 1

    #print(b)


