# -*- coding:utf-8 -*-
#@Time : 2021/9/11 14:33
#@Author: zxf_要努力
#@File : 电信云3.py


class Solution:
    def get_count(self,s,i):
        str_list = s.split(" ")
        if len(str_list) < i:
            str_list.reverse()
            return " ".join(str_list)
        else:
            str_1,str_2 = str_list[0:i],str_list[i:]
            str_1.reverse()
            str_2.reverse()
            res1 = " ".join(str_1)
            res2 = " ".join(str_2)
            return res1 + " "+res2


if __name__ == "__main__":
    # 读取第一行的n
    print(Solution().get_count("how are you? i am fine",3))