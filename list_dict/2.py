# -*- coding:utf-8 -*-
#@Time : 2021-04-06 22:37
#@Author: zxf_要努力
#@File : 2.py
# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
#
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
#
# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1 = {}
        for i in range(len(l1)):
            pass



    def resverListNode(self,listnode:ListNode):
        temp = ListNode(1,None)

        while temp.next !=None:
            pass



list1 = [ListNode(2,1),ListNode(4,2),ListNode(3,None)]
list2 = [ListNode(5,1),ListNode(6,2),ListNode(4,None)]


a = Solution()
a.addTwoNumbers(list1,list2)