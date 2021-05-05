# -*- coding:utf-8 -*-
#@Time : 2021-05-05 18:07
#@Author: zxf_要努力
#@File : 24_两两交换链表中的节点.py
"""

给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

输入：head = [1,2,3,4]
输出：[2,1,4,3]

输入：head = []
输出：[]

输入：head = [1]
输出：[1]

这一题主要难点 链表前民的两个节点要单独 转换一下
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return
        if not head.next:
            return head
        p = head.next
        pre,res = head,head
        #前两个节点比较特殊单独处理：

        if  not p.next:
            pre.next = p.next
            p.next = pre
            head = p
            return head
        else:
            pre.next = p.next
            p.next = pre
            head = p
            res = pre
            pre = pre.next
            p = pre.next
            if not p:
                return head
        while pre :
            q = p.next
            temp = pre
            temp.next = p.next
            p.next = temp
            res.next = p
            res = temp
            pre = q
            if not pre or not q.next:
                break
            p = q.next
        return head

    def other_answers(self,head:ListNode):
        '''答案递归调用'''
        if not head or not head.next:
            return head
        newHead = head.next
        head.next = self.other_answers(newHead.next)
        newHead.next = head
        return  newHead



node_1 = ListNode(1)
node_2 = ListNode(2)
node_3 = ListNode(3)
node_4 = ListNode(4)
node_3.next = node_4
node_2.next = node_3
node_1.next = node_2
res = Solution().swapPairs(node_1)
while res:
    print(res.val)
    res = res.next
