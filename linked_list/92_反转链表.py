# -*- coding:utf-8 -*-
#@Time : 2021/10/9 14:01
#@Author: zxf_要努力
#@File : 92_反转链表.py
'''
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。
请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        def reverse_linked_list(head: ListNode):
            # 也可以使用递归反转一个链表
            pre = None
            cur = head
            while cur:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next

        tempNode = ListNode(-1)
        tempNode.next = head
        pre = tempNode

        for _ in range(left-1):
            pre = pre.next
        # 从 pre 再走 right - left + 1 步，来到 right 节点
        right_node = pre
        for _ in range(right - left + 1):
            right_node = right_node.next

        # 第 3 步：切断出一个子链表（截取链表）
        left_node = pre.next
        curr = right_node.next

        #切断链接
        pre.next = None
        right_node.next = None

        reverse_linked_list(left_node)

        pre.next = right_node
        left_node.next = curr
        return tempNode.next





    def reverseBetween1(self, head: ListNode, left: int, right: int) -> ListNode:
        tempNode = ListNode(-1)
        tempNode.next = head
        pre = tempNode

        for _ in range(left-1):
            pre = pre.next
        cur = pre.next

        for _ in range(right-left):
            next = cur.next
            cur.next = next.next
            next.next = pre.next
            pre.next = next
        return tempNode.next


    def reverse(self,head):
        if head.next == None:return head
        newhead = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return newhead

if __name__ == '__main__':
    head = ListNode(1)
    head1 = ListNode(2)
    head.next = head1

    print(Solution().reverseBetween(head, 1, 2).val)



