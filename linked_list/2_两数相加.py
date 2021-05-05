# -*- coding:utf-8 -*-
#@Time : 2021-05-05 15:10
#@Author: zxf_要努力
#@File : 2_两数相加.py
'''
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头

输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
输入：l1 = [0], l2 = [0]
输出：[0]
输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]

思路 : 先将 列表反转过来 然后逐步遍历
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = l1.val + l2.val
        count = 0
        if temp >= 10:
            temp -= 10
            count = 1
        res = ListNode(temp)
        l1 = l1.next
        l2 = l2.next

        while l1 and l2:
            temp = l1.val + l2.val + count
            if temp >= 10:
                temp -= 10
                count = 1
            else:
                count = 0
            temp_node = ListNode(temp)
            temp_node.next = res
            res = temp_node
            l1 = l1.next
            l2 = l2.next
        if l1 and not l2:
            while l1:
                temp = l1.val +count
                if temp >= 10:
                    temp -= 10
                    count = 1
                else:
                    count = 0
                temp_node = ListNode(temp)
                temp_node.next = res
                res = temp_node
                l1 = l1.next
        if not l1 and l2:
            while l2:
                temp = l2.val +count
                if temp >= 10:
                    temp -= 10
                    count = 1
                else:
                    count = 0
                temp_node = ListNode(temp)
                temp_node.next = res
                res = temp_node
                l2 = l2.next
        if count == 1:
            node =ListNode(1)
            node.next = res
            res = node
        res = self.resverListNode(res)
        return res

    def resverListNode(self,listnode):
        q = listnode
        p = listnode.next
        q.next = None
        while p:
            temp = p.next
            p.next = q
            q = p
            p = temp
        return q




# node_2 = ListNode(2)
# node_4 = ListNode(4)
# node_3 = ListNode(3)
# node_4.next = node_3
# node_2.next = node_4
# l1 = node_2
# node_4 = ListNode(4)
# node_6 = ListNode(6)
# node_5 = ListNode(5)
#
# node_6.next = node_4
# node_5.next = node_6
# l2 = node_5

# node_9_1 = ListNode(9)
# node_9_2 = ListNode(9)
# node_1 = ListNode(1)
# node_9_2.next = node_1
# node_9_1.next = node_9_2
# l1 = node_9_1
l2 = ListNode(5)
l2 = ListNode(5)
d = Solution().addTwoNumbers(l2,l2)
print(d.val)

