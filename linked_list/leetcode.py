# -*- coding:utf-8 -*-
#@Time : 2021-05-07 21:06
#@Author: zxf_要努力
#@File : leetcode.py
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def generator_link(list:List)->ListNode:

    if len(list) == 1:
        return ListNode(list[-1])
    head = ListNode(list[0])
    pre = head
    for node in list[1:]:
        pre.next = ListNode(node)
        pre = pre.next
    return head


def travel(head:ListNode):

    while head:
        print(head.val,end='')
        head = head.next

