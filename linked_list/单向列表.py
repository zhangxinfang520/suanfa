# -*- coding:utf-8 -*-
#@Time : 2021-05-05 11:17
#@Author: zxf_要努力
#@File : 单向列表.py
'''
链表的基础知识
'''


class Node(object):
    '''单个节点'''
    def __init__(self,item, next=None):
        #表元素
        self.item = item
        #指向下一节点的链接
        self.next = next


class SingleLinkList():
    """单链表"""
    def __init__(self):
        #初始化表头
        self._head = None

    def is_empty(self):
        #查看链表是否为空
        return self._head == None

    def length(self):
        count = 0
        #当前项指向表头
        cur = self._head
        #当项不为空是 往后移
        while cur :
            count +=1
            cur = cur.next
        return count

    def travel(self):
        '''遍历链表'''
        cur = self._head
        while cur :
            print(cur.item)
            cur = cur.next

    def add(self,item):
        #插入节点 这个属于头插法
        node = Node(item)
        node.next = self._head
        self._head = node

    def append(self,item):
        '''从尾部插入'''
        node = Node(item)
        #如果链表为空，_head指向新的节点
        if self.is_empty():
            self._head = None
        else:
            # 否则，循环到链表末尾，指向新节点
            cur = self._head
            while cur.next :
                cur = cur.next
            cur.next = node

    def insert(self,pos,item):
        """
        在某个位置 插入节点
        :param pos:
        :param item:
        :return:
        """
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            pre = self._head # pre 为 pos-1 位置的节点
            count = 0
            while count < (pos-1):
                pre = pre.next
                count +=1
            node.next = pre.next
            pre.next = node

    def remove(self,item):
        '''
        删除某个节点
        :param item:
        :return:
        '''
        cur = self._head
        pre = None
        while cur :
            #如果找到指定节点
            if cur.item == item:
                if not pre:
                    #如果是第一个节点，即删除头节点
                    self._head = cur.next
                else:
                    pre.next = cur.next
                break
            else:#链表后移
                pre = cur
                cur = cur.next

    def search(self,item):
        """
        查找元素是否存在
        :param item:
        :return:
        """
        cur = self._head
        while cur:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        return False

def main():
    link_list = SingleLinkList()
    print(link_list.length())
    link_list.add(1)
    link_list.add(4)
    link_list.append(3)
    link_list.travel()
    # link_list.insert(0, 2)
    # link_list.append(3)
    # print('是否有1: ', link_list.search(1))
    # link_list.travel()
    # print('长度: ', link_list.length())
    # link_list.remove(1)
    # link_list.travel()
if __name__ == '__main__':
    main()










