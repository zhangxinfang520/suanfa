# -*- coding:utf-8 -*-
# @Time : 2021-05-05 13:50
# @Author: zxf_要努力
# @File : 单向循环列表.py
'''
单向循环列表
'''


class Node(object):

    def __init__(self, item, next=None):
        self.item = item
        self.next = next


class SingleCycLinkList():

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head == None

    def length(self):
        # 头部为空
        if self.is_empty():
            return 0
        else:
            count = 1
            cur = self._head
            while cur != self._head:
                count += 1
                cur = cur.next
            return count

    def travel(self):
        if self.is_empty():
            return
        cur = self._head
        print(cur.item, end=' ')
        while cur.next != self._head:
            cur = cur.next
            print(cur.item, end=' ')

    def add(self, item):

        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = node

        else:
            node.next = self._head
            # 将链表末尾指向新节点
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
            # 头插法 把head 指向头结点
            self._head = node

    def append(self, item):
        # 插在尾部
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = node
        else:
            node.next = self._head
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            cur.next = node

    def remove(self, item):
        cur = self._head
        pre = None
        if self.is_empty():
            return
            # 移出的首项
        if item == self._head.item:
            # 链表只有一项
            if self.length() == 1:
                self._head = None
            # 头部和尾部 指移出项的next
            else:
                while cur.next != self._head:
                    cur = cur.next
                cur.next = self._head.next
                self._head = self._head.next
        else:
            pre = self._head
            while cur.next != self._head:
                if cur.item == item:
                    pre.next = cur.next
                    return
                pre = cur
                cur = cur.next
            # 删除尾部
            if cur.item == item:
                pre.next = self._head

    def insert(self, pos, item):
        # pos 超出链表项
        if pos >= self.length():
            self.append(item)
        elif pos <= 0:
            self.add(item)
        # 中间位置
        else:
            node = Node(item)
            cur = self._head
            count = 0
            while count < (pos - 1):
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def search(self,item):
        if self.is_empty():
            return False
        cur = self._head
        if item == cur.item:
            return True
        while cur.next != self._head:
            cur = cur.next
            if cur.item == item:
                return True

        return  False


def main():
    li = SingleCycLinkList()
    print(li.is_empty())
    li.add(1)
    li.add(23)
    li.append(4)
    li.travel()
    li.remove(4)
    li.remove(56)
    li.travel()
    li.insert(0, 11)
    li.insert(2, 5)
    li.insert(6, 8)
    li.travel()
    print(li.length())
    print(li.search(9))
    print(li.search(5))

if __name__ == '__main__':
    main()

