# -*- coding:utf-8 -*-
#@Time : 2021-08-04 10:28
#@Author: zxf_要努力
#@File : 148_排序链表.py
'''
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
进阶：
你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
输入：head = [4,2,1,3]
输出：[1,2,3,4]
输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]
'''
from  linked_list.leetcode import generator_link,travel
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return []
        re = head.next

        head.next = None
        while re:
            temp = head
            pre = temp
            if re.val < temp.val:
                re_temp = re.next
                re.next = temp
                head = re
                re = re_temp
                continue

            while temp and  re.val > temp.val :
                  pre = temp
                  temp = temp.next
            if temp :
                re_temp = re.next
                pre.next = re
                re.next = temp
                re = re_temp
            else:
                re_temp = re.next
                pre.next = re
                re.next = None
                re = re_temp
        return head

    #归并排序
class Solution1:
    def sortList(self, head: ListNode) -> ListNode:
        h, length, intv = head, 0, 1
        while h: h, length = h.next, length + 1
        res = ListNode(0)
        res.next = head
        # merge the list in different intv.
        while intv < length:
            pre, h = res, res.next
            while h:
                # get the two merge head `h1`, `h2`
                h1, i = h, intv
                while i and h: h, i = h.next, i - 1
                if i: break  # no need to merge because the `h2` is None.
                h2, i = h, intv
                while i and h: h, i = h.next, i - 1
                c1, c2 = intv, intv - i  # the `c2`: length of `h2` can be small than the `intv`.
                # merge the `h1` and `h2`.
                while c1 and c2:
                    if h1.val < h2.val:
                        pre.next, h1, c1 = h1, h1.next, c1 - 1
                    else:
                        pre.next, h2, c2 = h2, h2.next, c2 - 1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0: pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = h
            intv *= 2
        return res.next


if __name__ == '__main__':

    head = [5,3,4,0,2]
    head = generator_link(head)
    travel(Solution1().sortList(head))



