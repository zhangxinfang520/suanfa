# -*- coding:utf-8 -*-
#@Time : 2021-05-05 14:29
#@Author: zxf_要努力
#@File : 双向链表.py
'''
实现双向链表

'''


class Node(object):

    def __init__(self,item,next=None,prev=None):

        self.item = item
        self.next = next
        self.prev = prev


class DLinkList(object):

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head == None

    def length(self):
        count = 0
        cur = self._head
        while cur:
            cur = cur.next
            count += 1
        return count

    def travel(self):
        #空链表
        cur = self._head
        while cur:
            print(cur.item,end=" ")
            cur = cur.next

    def add(self,item):
        #头插法
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node

    def append(self,item):

        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self,pos,item):
        if pos >= self.length():
            self.append(item)
        elif pos <= 0:
            self.add(item)
        else:
            node = Node(item)
            cur = self._head
            count = 0
            while count < (pos-1):
                count +=1
                cur = cur.next
            node.next = cur.next
            node.prev = cur
            cur.next.prev = node
            cur.next = node

    def remove(self,item):
        if self.is_empty():
            return
        else:
            cur = self._head
            #删除首项
            if cur.item == item:
                #如果链表仅有一项
                if cur.next == None:
                    self._head =None
                else:
                    cur.next.prev = None
                    self._head = cur.next
                return
            while cur:
                if cur.item == item:
                    cur.next.prev = cur.prev
                    cur.prev.next = cur.next
                    break
                cur = cur.next

    def search(self,item):
        if self.is_empty():
            return False
        cur = self._head
        while cur:
            if cur.item == item:
                return True
            cur = cur.next
        return False

if __name__ == '__main__':
    li = DLinkList()
    print('是否是空链表:', li.is_empty())
    li.append(9)
    li.append(10)
    li.add(8)
    li.add(5)
    li.insert(-1, 6)
    li.travel()
    li.remove(6)
    li.travel()
    print('length:', li.length())
    print('是否有99:', li.search(99))
    print('是否有8:', li.search(8))






