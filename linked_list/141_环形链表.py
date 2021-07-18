# -*- coding:utf-8 -*-
#@Time : 2021-07-18 14:06
#@Author: zxf_要努力
#@File : 141_环形链表.py

'''
这一题没读懂

'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast,slow = head,head
        while True:
            try:
                slow = slow.next
                fast = fast.next.next
            except Exception as e:
                 return False
            if slow == fast:
                return True

