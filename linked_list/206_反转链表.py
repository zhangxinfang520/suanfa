# -*- coding:utf-8 -*-
#@Time : 2021-05-10 15:21
#@Author: zxf_要努力
#@File : 206_反转链表.py
'''
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
'''
from linked_list.leetcode import generator_link,travel


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return
        if not head.next:
            return head
        p = head
        pre = None
        post = p.next
        while post:
            temp = post.next
            post.next = p
            p.next = pre
            pre = p
            p = post
            post = temp

        return p

head = [1,2]
travel(Solution().reverseList(generator_link(head)))

