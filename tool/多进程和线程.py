# -*- coding:utf-8 -*-
# @Time : 2021-06-29 9:33
# @Author: zxf_要努力
# @File : 多进程和线程.py
'''
线程与进程
进程：一个程序的执行实例就是一个进程，每一个进程提供执行程序所需的所有资 源。
    （进程本质上是资源的集合），操作系统管理在其上面运行的所有进程，并为这些进程公平的分配时间。
线程：是操作系统能够进行运算调度的最小单位。它被包含在进程之中，是进程中的实际运作单位。
    一条线程指的是进程中一个单一顺序的控制流，一个进程中可以并发多个线程，每条线程并行执行不同的任务
'''
from time import ctime, sleep
import time


# 单线程
def music(func):
    for i in range(2):
        print("i am %s and i love  %s" % (func, ctime()))


def movie(func):
    for i in range(2):
        print("i was at the %s!%s" % (func, ctime()))


# 多线程
"""
Python的标准库提供了两个模块：_thread和threading，
_thread是低级模块，它不支持守护线程，当主线程退出时，
所有子线程都会被强行退出。threading是高级模块，
对_thread进行了封装，支持守护线程，绝大多数情况下，
我们只需要使用threading这个高级模块。
"""

import threading


def music1(func, loop):
    for i in range(loop):
        print("I was listening to %s. %s" % (func, ctime()))
        sleep(1)


def movie1(func, loop):
    for i in range(loop):
        print("I was at the %s! %s" % (func, ctime()))
        sleep(5)


# 创建线程组
threads = []
# 创建线程1 添加到线程组中 目标函数 以及参数
t1 = threading.Thread(target=music1, args=(u"zxf", 3))
threads.append(t1)
# 创建线程2
t2 = threading.Thread(target=movie1, args=(u"wmx", 2))
threads.append(t2)

# 多进程
'''
多进程multiprocessing模块提供远程与本地的并发，
在一个multiprocessing库的典型使用场景下，
所有的子进程都是由一个父进程启动起来的，
这个父进程成为madter进程，这个父进程非常重要，
他会管理一系列的对象状态，一旦这个进程退出，
子进程很可能处于一个不稳定的状态，
这个进程最好尽可能做最少的事情，以便保持其稳定性。

Process([group [, target [, name [, args [, kwargs]]]]])
    group分组，实际上不使用
    target表示调用对象，你可以传入方法的名字
    args表示给调用对象以元组的形式提供参数，比如target是函数a，他有两个参数m，n，那么该参数为args=(m, n)即可
    kwargs表示调用对象的字典
    name是别名，相当于给这个进程取一个名字
'''
import multiprocessing

# 创建进程组
threads1 = []
# 创建进程1
t11 = multiprocessing.Process(target=music1, args=(u"zxf", 3))
threads1.append(t11)

# 创建进程2
t22 = multiprocessing.Process(target=music1, args=(u"wmx", 2))
threads1.append(t22)

# 线程池
import os
from datetime import datetime
from multiprocessing import Pool, Queue, Process


def funcpool():
    # 主进程
    print("这是主进程，进程编号：%d" % os.getpid())
    t_start = datetime.now()
    pool = Pool()
    # for i in range(os.cpu_count()):
    #     pool.apply_async(music1,args=(u"zxf",3))
    #     pool.apply_async(movie1,args=(u"wmx",2))
    pool.apply_async(music1, args=(u"zxf", 3))
    pool.apply_async(movie1, args=(u"wmx", 2))
    pool.close()  # 调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
    pool.join()  # 对Pool对象调用join()方法会等待所有子进程执行完毕
    t_end = datetime.now()
    print('主进程用时：%d毫秒' % (t_end - t_start).microseconds)


def proc1(pipe):
    pipe.send('zxf love wmx')
    print('procl rec:', pipe.recv())


def proc2(pipe):
    print('proc2 rec:', pipe.recv())
    pipe.send('hello too')


def func_thread_communication():
    multiprocessing.freeze_support()
    pipe = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=proc1, args=(pipe[0],))
    p2 = multiprocessing.Process(target=proc2, args=(pipe[1],))

    p1.start()
    p2.start()
    p1.join()
    p2.join()


# Queue类与Pipe相似，都是先进先出的结构，
# 但是 Queue类允许多个进程放入，
# 多个进程从队列取出对象。Queue类使用Queue（maxsize）创建，maxsize表示队列中可以存放对象的最大数量。

# 写数据进程执行的代码
def write(q):
    print("Process to write: %s" % os.getpid())
    for value in ['i', 'love', 'wmx']:
        print('Put %s values to queque' % value)
        q.put(value)
        time.sleep(10)


# 读数据
def read(q):
    print('Process to read:%s' % os.getpid())
    while True:
        value = q.get(True)
        print("I get value of %s" % value)


def test_queque():
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程 pw 写入
    pw.start()
    # 启动子进程
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()


if __name__ == '__main__':
    '''单线程          '''
    # music(u"zxf")
    # movie(u"wmx")
    # print("all over %s" % ctime())
    '''------------------'''
    # 多线程
    # for  t in threads:
    #     t.start()
    # #守护进程
    # for t in threads:
    #     #join 的作用是 等待每个线程终止
    #     t.join()
    # 多进程
    for t in threads1:
        t.start()
    # #守护进程
    # for t in threads1:
    #     #join 的作用是 等待每个线程终止
    #     t.join()
    # print("all over %s" % ctime())
    # 进程池
    # funcpool()
    # 进程通讯
    # func_thread_communication()
# test_queque()
