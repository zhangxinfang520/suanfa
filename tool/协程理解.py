# encoding: utf-8
"""
@author: zxf_要努力
@file: 协程理解.py
@time: 2022/4/6 16:00
"""
import asyncio

#协程是一种特殊的线程，它可以跟线程比较像，但是它没有线程的执行上下文，
# 协程的执行上下文是由调用者提供的，协程的执行上下文是由调用者提供的，
# 因为协程是一个线程执行，那怎么利用多核CPU呢？
# 最简单的方法是多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。
import threading
import time


def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

#异步IO
#异步IO是从线程切换到线程的方式，即在一个线程中执行一个任务，然后切换到另一个线程继续执行另一个任务，

async def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    await asyncio.sleep(10)
    print("Hello again!")




async def hello1():
    print(f"Hello world 01 begin,my thread is:{threading.currentThread()}")
    await asyncio.sleep(6)
    print("Hello again 01 end")


async def hello2():
    print(f"Hello world 02 begin,my thread is:{threading.currentThread()}")
    await asyncio.sleep(5)
    print("Hello again 02 end")

async def hello3():
    print(f"Hello world 03 begin,my thread is:{threading.currentThread()}")
    await asyncio.sleep(1)
    print("Hello again 03 end")


class async_generator:
    def __init__(self,stop):
        self.i = 0
        self.stop = stop
    def __aiter__(self):
        return self
    async  def __anext__(self):
        i = self.i
        self.i += 1
        if i <= self.stop:
            await asyncio.sleep(1)
            return i*i
        else:
            raise StopAsyncIteration

async def main():
    async for i in async_generator(5):
        print(i)

# class async_generator:
#     def __init__(self, stop):
#         self.i = 0
#         self.stop = stop
#
#     def __aiter__(self):
#         return self
#
#     async def __anext__(self):
#         i = self.i
#         self.i += 1
#         if self.i <= self.stop:
#             await asyncio.sleep(1)
#             return i * i
#         else:
#             raise StopAsyncIteration
#
#
# async def main():
#     async for i in async_generator(3):
#         print(i)

if __name__ == '__main__':
    # c = consumer()
    # produce(c)
    # 获取EventLoop:
    a = time.time()
    loop = asyncio.get_event_loop()
    # 执行coroutine
    tasks = [hello1(),hello2(),hello3()]
    #tasks = [hello3()]

    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

    b = time.time()
    print('---------------------------------------')
    print(b - a)






