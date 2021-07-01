# -*- coding:utf-8 -*-
#@Time : 2021-06-29 21:23
#@Author: zxf_要努力
#@File : 752.py
'''
你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字：
'0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。
每个拨轮可以自由旋转：例如把 '9' 变为 '0'，'0' 变为 '9' 。
每次旋转都只能旋转一个拨轮的一位数字。
锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。
列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，
这个锁将会被永久锁定，无法再被旋转。
字符串 target 代表可以解锁的数字，你需要给出解锁需要的最小旋转次数，
如果无论如何不能解锁，返回 -1 。
输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202"
输出：6
解释：
可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，
因为当拨动到 "0102" 时这个锁就会被锁定。
'''
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target in deadends:
            return -1
        queue = []
        visited = []
        queue.append('0000')
        visited.append('0000')
        count = 0
        while queue:
            len_num = len(queue)
            for i in range(len_num):
                temp = queue.pop(0)
                if temp in deadends:
                    continue
                if temp == target:
                    return count
                visited.append(temp)
                for j in range(4):
                    Up_temp = self.UP(temp,j)
                    if Up_temp not in visited:
                        queue.append(Up_temp)
                    Down_temp = self.Down(temp,j)
                    if Down_temp not in visited:
                        queue.append(Down_temp)
            count +=1
        return -1

    def openLock1(self, deadends: List[str], target: str) -> int:
        if target in deadends:
            return -1
        queue1 = []
        queue2 = []
        visited = []
        queue1.append('0000')
        queue2.append(target)
        count = 0

        while queue1 and queue2:
            if (len(queue1) > len(queue2)):
                tempq = queue1
                queue1 = queue2
                queue2 = tempq

            temp = []
            len_num = len(queue1)
            for i in range(len_num):
                temp1 = queue1.pop(0)
                if temp1 in deadends:
                    continue
                if temp1 in queue2:
                    return count

                visited.append(temp1)
                for j in range(4):
                    Up_temp = self.UP(temp1,j)
                    if Up_temp not in visited:
                        temp.append(Up_temp)
                    Down_temp = self.Down(temp1,j)
                    if Down_temp not in visited:
                        temp.append(Down_temp)
            count +=1
            queue1 = queue2
            queue2 = temp

        return -1

    def UP(self,Str,j):
        str_list = list(Str)
        if str_list[j] == '9':
            str_list[j] = str(0)
        else:
            temp = str_list[j]
            str_list[j] = str(int(temp)+1)
        return "".join(str_list)

    def Down(self,Str,j):
        str_list = list(Str)
        if str_list[j] == '0':
            str_list[j] = str(9)
        else:
            temp = str_list[j]
            str_list[j] = str(int(temp) - 1)
        return "".join(str_list)
deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
target = "8888"
print(Solution().openLock1(deadends, target))