# import sys
# index = 0
#
# for line in sys.stdin:
#     print(line)
#     print(index)
#     index +=1
#     # if index == 0:
#     #     n,m = line.split()
#     #     index +=1
#     #     mxtic = [[0 for _ in range(int(m))]  for _ in range(int(n))]
#     #     row = 0
#     # if index == 1:
#     #     x1,y1,x2,y2 = line.split()
#     #     index +=1
#     # else:
#     #     loc0,loc1,loc2=line.split()
#     #     mxtic[row][0] = loc0
#     #     mxtic[row][1] = loc1
#     #     mxtic[row][2] = loc2
#     #     row +=1
#
# # def find_xy(n,m,mx,loc):
# #     for i in range(n):
# #         for j in range(m):
# #             if mx[i][j] == loc:
# #                 return i,j
# result = []
#
# def get_num(n,m,x1,y1,x2,y2,mx):
#     if x1 < 1 or y1<1 or x2<1 or y2<1:
#         return -1
#     if x1>n or x2>n or y1>m or y2>m:
#         return -1
#     #传建一个坐标轴从1，1到5,5
#     x_y = [[0 for _ in range(m)] for _ in range(n)]
#     for i in range(n):
#         for j in range(m):
#             x_y[i][j] = (i, j)
#     if go_on(x1,y1,x2,y2):
#
#         return result
#
#
#
# def go_on(x1,y1,x2,y2):
#     if x1==x2 and y1==y2:
#         return True
#     if y1+1 > n:
#         go_on(x1+1,y1,x2,y2)
#         result.append([x1+1,y1])
#     if x1+1>m:
#         go_on(x1,y1+1,x2,y2)
#     if x1==m and y1==n:
#         result.remove([(x1,y1)])
#         go_on(x1-1,y1,x2,y2)
#         go_on(x1-1,y1-1,x2,y2)
#         go_on(x1-1,y1-1,x2,y2)
# result =list()
# result.append(1)
# result.append(23)
# result.append(44)
#
# print(result)
a = [1,2,3,5,6]
print( a > 0)