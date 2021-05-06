# -*- coding:utf-8 -*-
# @Time : 2021-05-06 22:24
# @Author: zxf_要努力
# @File : 61_旋转链表.py
'''
给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
输入：head = [1,2,3,4,5], k = 2
输出：[4,5,1,2,3]
输入：head = [0,1,2], k = 4
输出：[2,0,1]

(我自己的思路)首先要考虑 k是不是大于 链表的长度
如果 k 等于链表的长度 直接返回head
如果大于链表的长多 k对于链表的长度取余

（官方的步骤） 构成一个环 真的巧
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or not head or not head.next:
            return head

        n = 1
        cur = head
        while cur.next:
            cur = cur.next
            n += 1

        if (add := n - k % n) == n:
            return head

        cur.next = head
        while add:
            cur = cur.next
            add -= 1

        ret = cur.next
        cur.next = None
        return ret



node1 = ListNode(1)
node2 = ListNode(2)

node1.next = node2

print(Solution().rotateRight(node1, 1).val)
