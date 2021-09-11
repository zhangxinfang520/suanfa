# -*- coding:utf-8 -*-
#@Time : 2021/9/11 14:38
#@Author: zxf_要努力
#@File : 电信云2.py
import sys


class Soluction:
    total = 0
    def get_count(self,target):
        if target == 0:
            return 0
        nums = [1,5,10,20,50,100]
        n = len(nums)
        def dp(target,index):
            if target == 0:
                self.total +=1
                return
            for i in range(index,n):
                if target - nums[i] >= 0:
                    dp(target-nums[i],i)
        dp(target,0)
        return self.total



if __name__ == "__main__":
    # 读取第一行的n
    target = int(sys.stdin.readline().strip())
    #target = 10
    print(Soluction().get_count(target))