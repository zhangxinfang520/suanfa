# -*- coding:utf-8 -*-
#@Time : 2021-05-10 15:21
#@Author: zxf_要努力
#@File : 206_反转链表.py
'''
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
答案 递归
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


    def reverselist(self,head:ListNode):
        if  head.next==None : return head
        newnode = self.reverselist(head.next)
        head.next.next = head
        head.next = None
        return newnode

head = [1,2,3,4,5]
travel(Solution().reverselist(generator_link(head)))

