# -*- coding:utf-8 -*-
#@Time : 2021-07-02 10:54
#@Author: zxf_要努力
#@File : 多线程的值的返回问题.py
#查询多线程的返回值问题

import threading
import queue
import random

import numpy as np

class detect:
    def __init__(self):
        pass

    def get_result_form_frame(self,cap_id,q):
        '''

        :param cap_id: 摄像头的id 后期可以根据 id 来判别是什么任务
        :param q: 队列来存放返回值
        :return:
        '''

        img = np.random.randint((3,1080,1920))
        res_info = random.random()
        result = {cap_id:(img,res_info)}
        q.put(result)


if __name__ == '__main__':

    det = detect()
    q = queue.Queue()
    threads = [None] * 3
    result = []
    for i in range(0,3):
        threads[i] = threading.Thread(target=det.get_result_form_frame,args=(i,q))
        threads[i].start()
        result.append(q.get())
        print(result)



