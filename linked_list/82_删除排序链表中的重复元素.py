# -*- coding:utf-8 -*-
#@Time : 2021-05-07 20:05
#@Author: zxf_要努力
#@File : 82_删除排序链表中的重复元素.py
'''
存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除链表中所有存在数字重复情况的节点，只保留原始链表中 没有重复出现 的数字。

返回同样按升序排列的结果链表
输入：head = [1,2,3,3,4,4,5]
输出：[1,2,5]
输入：head = [1,1,1,2,3]
输出：[2,3]
又是一道 我看到答案写出来的题
这道题 需要巧妙构造一个节点 放在head 前面

'''

from linked_list.leetcode import generator_link,travel


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummpy = ListNode(0,head)
        cur = dummpy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummpy.next





list_node = [1,2,2,2]

node1 = generator_link(list_node)

travel(Solution().deleteDuplicates(node1))







