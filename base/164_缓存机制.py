# -*- coding:utf-8 -*-
#@Time : 2021-08-05 11:21
#@Author: zxf_要努力
#@File : 164_缓存机制.py
'''
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制 。
实现 LRUCache 类：

LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。
当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间
'''
import collections

class LRUCache:

    def __init__(self, capacity: int):
        self.list = []
        self.content = dict()
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.content.keys():
            return -1
        else:
            index = self.content[key]
            key,value = self.list[index]
            #把数值移到最后面 同时将字典中的value更新
            for i in range(index,self.size-1):
                self.list[i] = self.list[i+1]
                self.content[self.list[i][0]] -= 1
            self.list[-1] = [key,value]
            self.content[key] = self.size -1
            return value

    def put(self, key: int, value: int) -> None:
        '''
        当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间
        :param key:
        :param value:
        :return:
        '''
        if self.size == self.capacity and key not in self.content.keys():
            old_key,old_value = self.list.pop(0)
            self.content.pop(old_key)
            for old_key,old_value in  self.content.items():
                self.content[old_key] = old_value - 1
            self.list.append([key,value])
            self.content[key] = len(self.list) - 1
        elif key in self.content.keys():
            index = self.content[key]
            self.list[index][-1] = value
            self.get(key)
        else:
            self.list.append([key,value])
            self.size +=1
            self.content[key] = len(self.list) - 1

#继承collections.OrderedDict 类 通过其实现


class LRUCache1(collections.OrderedDict):
    def __init__(self,capacity):
        super(LRUCache1, self).__init__()
        self.capacity = capacity

    def get(self,key):
        if key not in self:
            return -1
        #方法move_to_end(key, last=True) ​ 该方法用于将一个已存在的key移动到有序字典的任一端。
        # 如果last为True（默认值），则移动到末尾，如果last为False，则移动到开头。如果key不存在，引发KeyError
        self.move_to_end(key)
        return self[key]

    def put(self,key,value):
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            #方法popitem(last=True)
            #​ 调用有序字典的popitem()方法会删除并返回(key, value)对。
            # 如果last为真，则以LIFO(后进先出)顺序返回这些键值对，
            # 如果为假，则以FIFO(先进先出)顺序返回。
            self.popitem(last=False)


if __name__ == '__main__':
    lru = LRUCache1(2)
    lru.put(2,1)
    lru.put(1,1)
    lru.put(2,3)
    lru.put(4,1)
    print(lru.get(1))
    print(lru.get(2))
    
