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


n, b = sys.stdin.readline().strip().split()
n, b = int(n),int(b)
re = []
for i in range(n):
    u, v, r = list(map(int,sys.stdin.readline().strip().split()))
    if b < (v+r):
       re.append(i)
    elif b==(v+r) and (v-r)==0:
       re.append(i)
if len(re):
    print(re[0])
else:
    print(n)








