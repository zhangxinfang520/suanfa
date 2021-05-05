# -*- coding:utf-8 -*-
#@Time : 2021-05-05 16:47
#@Author: zxf_要努力
#@File : 19_删除链表的倒数第 N 个结点.py
'''
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

进阶：你能尝试使用一趟扫描实现吗？
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]

输入：head = [1], n = 1
输出：[]
输入：head = [1,2], n = 1
输出：[1]

只用循环一遍的思路 就是 两个指针 遍历整个链表 二者的差距为 k（倒数第几个）
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        q = head
        #判读只有一个node的时候 并且删除它
        if n == 1 and not q.next:
            return
        while n > 0 and q:
            q = q.next
            n -= 1
        #越界情况
        if n > 0:
            return head
        #恰好把第一个节点删除
        if n == 0 and not q:
            head = head.next
        #删除中间的节点
        p = head
        pre = p
        while q:
            q = q.next
            pre = p
            p = p.next
        #删除节点
        pre.next = p.next

        return head

node_1 = ListNode(1)
Solution().removeNthFromEnd(node_1,1)