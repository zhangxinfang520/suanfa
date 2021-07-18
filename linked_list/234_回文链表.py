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
        result = dict()
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

    def othermethod(self, head: ListNode) -> bool:
        '''第二种方法 先找到 中间节点 然后将后半部分链表反转 然后进行比较'''
        if not head and not head.next:
            return True
        #快慢指针
        fast , slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        #如果fast 不为空 证明listNode的长度为奇数
        if fast:
            slow = slow.next
        slow = self.reverse(slow)
        fast = head
        while slow:
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next
        return True

    def reverse(self,head):
        res = ListNode(0);
        while head:
            temp = head.next
            head.next = res.next
            res.next = head
            head = temp
        return res.next




from  linked_list.leetcode import generator_link
list_node = [1,2,1]
print(Solution().othermethod(generator_link(list_node)))