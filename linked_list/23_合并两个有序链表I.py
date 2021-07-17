# -*- coding:utf-8 -*-
#@Time : 2021-07-17 11:19
#@Author: zxf_要努力
#@File : 23_合并两个有序链表I.py
from linked_list.leetcode import generator_link,travel
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution(object):
    def mergeTwoLists(self, l1:ListNode, l2:ListNode):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return l1
        if not l1 :
            return l2
        if not l2:
            return l1
        head = ListNode(0)
        re = head

        while l1 and l2:
            if l1.val < l2.val:
                re.next = l1
                l1 = l1.next
            else:
                re.next = l2
                l2 = l2.next
            re = re.next
        if  l1:
            re.next = l1
        if  l2:
            re.next = l2

        return head.next


    
list1 = [1,2,4]

list2 = [1,3,4]

l1 = generator_link(list1)
l2 = generator_link(list2)

re = Solution().mergeTwoLists(l1,l2)


travel(re)





