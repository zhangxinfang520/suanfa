# -*- coding:utf-8 -*-
#@Time : 2021-07-17 13:56
#@Author: zxf_要努力
#@File : 23_合并多个链表.py
'''
给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表
'''
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        m = log2 n
        """
        if len(lists) == 0:
            return []
        if len(lists) == 1:
            return lists[-1]
        mid = len(lists) // 2
        left = len(lists) % 2 # 判断list的长度为奇数还是偶数 
        l1 = lists[0:mid]
        l2 = lists[mid :2*mid]
        r1 = self.mergeKLists(l1)
        r2 = self.mergeKLists(l2)
        r = self.merge(r1, r2)
        if left:
            r = self.merge(r,lists[-1])
        return r
    def merge(self,node1,node2):
        '''合并两个链表'''
        head = ListNode(0)
        re = head
        while node1 and node2:
            if node1.val < node2.val:
                re.next = node1
                node1 = node1.next
            else:
                re.next = node2
                node2 = node2.next
            re = re.next
        if node1:
            re.next = node1
        if node2:
            re.next = node2
        return head.next


from  linked_list.leetcode import generator_link,travel

list1 = [1,4,5]
list2 = [1,3,4]
list3 = [2,6]
#list4 = [1,4,4]
node1 = generator_link(list1)
node2 = generator_link(list2)
node3 = generator_link(list3)
#node4 = generator_link(list4)

re = Solution().mergeKLists([node1,node2,node3])

travel(re)