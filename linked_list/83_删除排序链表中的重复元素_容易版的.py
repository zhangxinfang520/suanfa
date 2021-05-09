# -*- coding:utf-8 -*-
#@Time : 2021-05-08 20:02
#@Author: zxf_要努力
#@File : 83_删除排序链表中的重复元素_容易版的.py
'''
存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除所有重复的元素，使每个元素 只出现一次
输入：head = [1,1,2]
输出：[1,2]

输入：head = [1,1,2,3,3]
输出：[1,2,3]
'''
from linked_list.leetcode import generator_link,travel
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return
        p = head
        while p and p.next:
            if p.val ==p.next.val:
                x = p.val
                while p.next and p.next.val==x:
                    p.next = p.next.next
            else:
                p = p.next
        return head
#思路
a = [1,1,2,3,3]
link_list = generator_link(a)
travel(Solution().deleteDuplicates(link_list))
