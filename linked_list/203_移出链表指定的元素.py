# -*- coding:utf-8 -*-
#@Time : 2021-05-10 15:07
#@Author: zxf_要努力
#@File : 203_移出链表指定的元素.py
'''
给你一个链表的头节点 head 和一个整数 val ，
请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。

'''

from linked_list.leetcode import generator_link,travel
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return
        pre = ListNode(0)
        res = pre
        pre.next = head
        p = head
        while p:
            if p.val == val:
                pre.next = p.next
                p = p.next
            else:
                p = p.next
                pre = pre.next


        return res.next

list = [7,7,7,7]
val = 7
travel(Solution().removeElements(generator_link(list),val))
