# import math
# import sys
#
# while True:
#     n,m = sys.stdin.readline().strip().split()
#     sum_ = int(n)
#     if int(n) < 0 or int(m) < 0:
#         print(0)
#     res = []
#     for i in range(0,int(m)):
#         res.append(sum_)
#         sum_ = round(math.sqrt(sum_),2)
#
#     re = sum(res)
#     print(round(re,2))

import math
import sys

while True:
    m,n = sys.stdin.readline().strip().split()
    n, m = int(n),int(m)
    if n < 100 or m < 100:
        print("no")
    else:
        res = []
        for i in range(m,n):
            gh = i % 10
            sh = (i - gh)// 10 % 10
            bh = i // 100
            if (gh**3 + sh**3 + bh**3) == i:
                res.append(i)
        if len(res):
            for re in res:
                print(re,end="")
        else:
            print("no")



