'''我们有一个由平面上的点组成的列表 points。需要从中找出 K 个距离原点 (0, 0) 最近的点。
（这里，平面上两点之间的距离是欧几里德距离。）
'''
import math
class Solution:

    def kClosest(self, points, K):
        # distances ={}
        # a = []
        # for i,point in enumerate(points):
        #     distance = pow(point[0],2)+pow(point[1],2)
        #     distances[i] = distance
        #
        # result = sorted(distances.items(),key=lambda item : item[1])
        #
        # for i in range(K):
        #     k=result[i][0]
        #     a.append(points[k])
        # return a
        return sorted(points, key=lambda x: x[0] ** 2 + x[1] ** 2)[:K]


solution = Solution()
points = [[3,3],[5,-1],[-2,4]]
K = 2

closest = solution.kClosest(points, K)
print(closest)



