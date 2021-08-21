# -*- coding:utf-8 -*-
# @Time : 2021-07-01 16:54
# @Author: zxf_要努力
# @File : a.py

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

if __name__ == '__main__':
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
    a = 2
    print("%.2f"%a)


# nums = [7,1,3,6,8,4]
	# print(quick_sort(num
