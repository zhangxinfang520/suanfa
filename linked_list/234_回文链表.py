# -*- coding:utf-8 -*-
#@Time : 2021-05-11 9:53
#@Author: zxf_要努力
#@File : 234_回文链表.py
'''
请判断一个链表是否为回文链表。
输入: 1->2
输出: false
输入: 1->2->2->1
输出: true
我自己的思路 就是遍历到字典中
答案得的是放到数组中
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or  not head.next:
            return True
        cut = 0
        result =dict()
        while head:
            result[cut] = head.val
            head = head.next
            cut +=1
        if cut % 2 == 1:
            low = cut//2 - 1
            high = cut//2 + 1
        else:
            low = cut // 2 -1
            high = cut //2
        while low >=0:
            if result[low] != result[high]:
                return False
            else:
                low -= 1
                high  +=1

        return True


from  linked_list.leetcode import generator_link
list_node = [1,2]
print(Solution().isPalindrome(generator_link(list_node)))