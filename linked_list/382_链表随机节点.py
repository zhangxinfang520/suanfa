# -*- coding:utf-8 -*-
#@Time : 2021-07-13 14:14
#@Author: zxf_要努力
#@File : 382_链表随机节点.py
'''给定一个单链表，随机选择链表的一个节点，并返回相应的节点值。保证每个节点被选的概率一样。'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import random
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.l = []
        pr = head
        while pr:
            self.l.append(pr.val)
            pr = pr.next

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        x = random.randint(0,len(self.l)-1)
        return self.l[x]


# Your Solution object will be instantiated and called as such:

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

obj = Solution(head)
param_1 = obj.getRandom()
print(param_1)