# -*- coding:utf-8 -*-
#@Time : 2021-07-22 19:25
#@Author: zxf_要努力
#@File : 14_报数问题.py
'''
有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），
凡报到3的人退出圈子，问最后留下的是原来第几号的那位

'''

class Soulution:
    def getindex(self,persons):
        n = persons
        temp = n
        count = 0
        person_index = [i+1 for i in range(persons)]
        index = 0
        while n > 1:
            if person_index[index] != 0:
                count +=1
            if count == 3:
                person_index[index] = 0
                count = 0
                n -=1
            index +=1

            if index == temp:
                index = 0
        for i in range(temp):
            if person_index[i] != 0:
                print(person_index[i])


    def get_lef_index(self,persons):
        n = persons
        temp = n
        persons_list = [i+1 for i in range(n)]

        count = 0
        index = 0
        while n > 1:
            if persons_list[index] != 0:
                count += 1
            if count == 5:
                persons_list[index] = 0
                count = 0
                n -= 1
            index += 1
            if index == temp:
                index = 0
        for index in persons_list:
            if index !=0:
                print(index)


Soulution().get_lef_index(100)

