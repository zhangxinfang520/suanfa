# -*- coding:utf-8 -*-
#@Time : 2021-03-05 20:20
#@Author: zxf_要努力
#@File : 232.py
'''请你仅使用两个栈实现先入先出队列。队列应当支持一般队列的支持的所有操作（push、pop、peek、empty）：
实现 MyQueue 类：
void push(int x) 将元素 x 推到队列的末尾
int pop() 从队列的开头移除并返回元素
int peek() 返回队列开头的元素
boolean empty() 如果队列为空，返回 true ；否则，返回 false
 
说明：

你只能使用标准的栈操作 —— 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
'''

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mystack1 = []
        self.mystack2 = []


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.mystack1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        pop = self.mystack1[0]

        self.mystack1.remove(self.mystack1[0])
        for i in range(0,len(self.mystack1)):
            self.mystack2.append(self.mystack1[i])
        print(len(self.mystack1),len(self.mystack2))
        for i in range(0,len(self.mystack2)):
            self.mystack1[i] = self.mystack2[i]
        self.mystack2 = []

        return pop


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.mystack1[0]


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.mystack1) == 0:
            return True
        else:
            return False


queue = MyQueue()
queue.push(1)
queue.push(2)
# queue.push(3)
# queue.push(4)
queue.peek()
queue.pop()
queue.empty()

