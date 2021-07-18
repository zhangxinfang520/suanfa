# -*- coding:utf-8 -*-
#@Time : 2021-07-18 14:06
#@Author: zxf_要努力
#@File : 141_环形链表.py

'''
定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，
并不会作为参数传递到函数中。

我们使用两个指针，fast 与 low。它们起始都位于链表的头部。随后，slow 指针每次向后移动一个位置，而 fast 指针向后移动两个位置。
如果链表中存在环，则 fast 指针最终将再次与 slow 指针在环中相遇。
设链表中环外部分的长度为 aa。slow 指针进入环后，又走了 bb 的距离与 fast 相遇。此时，fast 指针已经走完了环的 n 圈，
因此它走过的总距离为a+n(b+c)+b=a+(n+1)b+nc。fast 指针走过的距离都为slow 指针的 22 倍。因此，我们有
a+(n+1)b+nc=2(a+b)⟹a=c+(n−1)(b+c)
有了 a=c+(n-1)(b+c)a=c+(n−1)(b+c) 的等量关系，我们会发现：从相遇点到入环点的距离加上 n-1 圈的环长，恰好等于从链表头部到入环点的距离。

因此，当发现 low 与 fast 相遇时，我们再额外使用一个指针 ptr。起始，它指向链表头部；随后，它和 slow 每次向后移动一个位置。
最终，它们会在入环点相遇。

'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast,slow = head,head
        while True:
            try:
                slow = slow.next
                fast = fast.next.next
            except Exception as e:
                return False
            if slow == fast:
                prt = head
                while prt !=slow:
                    prt = prt.next
                    slow = slow.next
                return prt

