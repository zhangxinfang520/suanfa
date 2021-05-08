# -*- coding:utf-8 -*-
#@Time : 2021-05-08 20:22
#@Author: zxf_要努力
#@File : 160_相交链表.py
'''
找到两个单链表相交的起始节点
intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Reference of the node with value = 2
输入解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
解释：这两个链表不相交，因此返回 null。

意思 两个链表有相同的结尾
'''
from linked_list.leetcode import generator_link,travel

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not  headA or not headB:
            return
        pre_A = headA
        pre_B = headB
        re = headB
        while pre_A:
            while pre_B:
                x = pre_B
                if pre_B == pre_A:
                    while pre_B and pre_A:
                        if pre_B == pre_A:
                            pre_B = pre_B.next
                            pre_A = pre_A.next
                    if not pre_A and not pre_B:
                        return x
                else:
                    pre_B = pre_B.next
            pre_B = re
            pre_A = pre_A.next
        return

listA = [4,1,8,4,5]
listB = [5,0,1,8,4,5]
linkA = generator_link(listA)
linkB = generator_link(listB)
travel(Solution().getIntersectionNode(linkA,linkB))
