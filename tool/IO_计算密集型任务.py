# encoding: utf-8
"""
@author: zxf_要努力
@file: IO_计算密集型任务.py
@time: 2022/4/9 16:26
"""
import multiprocessing
import threading
import time

'''
多线程：多线程即在一个进程中启动多个线程执行任务。一般来说使用多线程可以达到并行的目的，
但由于Python中使用了全局解释锁GIL的概念，导致Python中的多线程并不是并行执行，而是“交替执行”
Python中的多线程适合IO密集型任务，而不适合计算密集型任务。

多进程：
由于Python中GIL的原因，对于计算密集型任务，Python下比较好的并行方式是使用多进程，
这样可以非常有效的使用CPU资源。当然同一时间执行的进程数量取决你电脑的CPU核心数
Python中的进程模块为mutliprocess模块，提供了很多容易使用的基于对象的接口。另外它提供了封装好的管道和队列，可以方便的在进程间传递消息。
Python还提供了进程池Pool对象，可以方便的管理和控制线程。
'''
# 定义全局变量Queue
g_queue = multiprocessing.Queue()
g_search_list = list(range(10000))


# 定义一个IO密集型任务：利用time.sleep()
def task_io(task_id):
    print("IOTask[%s] start" % task_id)
    while not g_queue.empty():
        time.sleep(1)
        try:
            data = g_queue.get(block=True, timeout=1)
            print("IOTask[%s] get data: %s" % (task_id, data))
        except Exception as excep:
            print("IOTask[%s] error: %s" % (task_id, str(excep)))
    print("IOTask[%s] end" % task_id)
    return


# 定义一个计算密集型任务：利用一些复杂加减乘除、列表查找等
def task_cpu(task_id):
    print("CPUTask[%s] start" % task_id)
    while not g_queue.empty():
        count = 0
        for i in range(10000):
            count += pow(3*2, 3*2) if i in g_search_list else 0
        try:
            data = g_queue.get(block=True, timeout=1)
            print("CPUTask[%s] get data: %s" % (task_id, data))
        except Exception as excep:
            print("CPUTask[%s] error: %s" % (task_id, str(excep)))
    print("CPUTask[%s] end" % task_id)
    return task_id


def init_queue():
    print("init g_queue start")
    while not g_queue.empty():
        g_queue.get()
    for _index in range(10):
        g_queue.put(_index)
    print("init g_queue end")
    return


if __name__ == '__main__':
    print("cpu count:", multiprocessing.cpu_count(), "\n")

    print("========== 直接执行IO密集型任务 ==========")
    init_queue()
    time_0 = time.time()
    task_io(0)
    print("结束：", time.time() - time_0, "\n")

    print("========== 多线程执行IO密集型任务 ==========")
    init_queue()
    time_0 = time.time()
    thread_list = [threading.Thread(target=task_io, args=(i,)) for i in range(8)]
    for t in thread_list:
        t.start()
    for t in thread_list:
        if t.is_alive():
            t.join()
    print("结束：", time.time() - time_0, "\n")

    print("========== 多进程执行IO密集型任务 ==========")
    init_queue()
    time_0 = time.time()
    process_list = [multiprocessing.Process(target=task_io, args=(i,)) for i in range(multiprocessing.cpu_count())]
    for p in process_list:
        p.start()
    for p in process_list:
        if p.is_alive():
            p.join()
    print("结束：", time.time() - time_0, "\n")

    print("========== 直接执行CPU密集型任务 ==========")
    init_queue()
    time_0 = time.time()
    task_cpu(0)
    print("结束：", time.time() - time_0, "\n")

    print("========== 多线程执行CPU密集型任务 ==========")
    init_queue()
    time_0 = time.time()
    thread_list = [threading.Thread(target=task_cpu, args=(i,)) for i in range(8)]
    for t in thread_list:
        t.start()
    for t in thread_list:
        if t.is_alive():
            t.join()
    print("结束：", time.time() - time_0, "\n")

    print("========== 多进程执行cpu密集型任务 ==========")
    init_queue()
    time_0 = time.time()
    process_list = [multiprocessing.Process(target=task_cpu, args=(i,)) for i in range(multiprocessing.cpu_count())]
    for p in process_list:
        p.start()
    for p in process_list:
        if p.is_alive():
            p.join()
    print("结束：", time.time() - time_0, "\n")

    exit()

