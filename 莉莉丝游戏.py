# -*- coding:utf-8 -*-
#@Time : 2021-08-11 18:55
#@Author: zxf_要努力
#@File : 莉莉丝游戏.py

# class Solution:
#     def minMonSum(self, room_grid):
#         # write code here
#         m = len(room_grid)
#         n = len(room_grid)
#         if m < 0 or n < 0:
#             return 0
#         memo = [[-1] * n for _ in range(m)]
#
#         def dp(grid, i, j):
#             if i >= m or j >= n or j < 0 or i < 0:
#                 return float('inf')
#             if i == m - 1 and j == n - 1:
#                 return grid[i][j]
#             if memo[i][j] != -1:
#                 return memo[i][j]
#             memo[i][j] = min(dp(grid, i + 1, j), dp(grid, i, j + 1)) + grid[i][j]
#             return memo[i][j]
#
#         return dp(room_grid, 0, 0)
#
# nums = [[1,3,1],[1,5,1],[4,2,1]]
# print(Solution().minMonSum(nums))

class Solution:
    def can_tasks_finish(self, task_count, task_request):
        # write code here
        if len(task_request) == 0:
            return True
        # 先进行排序
        task_request = sorted(task_request, key=lambda x: (x[0], -x[1]))
        re = list()
        re.append(task_request.pop(0))
        while len(task_request):
            if re[-1][1] == task_request[0][0]:

                if re[-1][0] == task_request[0][1]:
                    return False
                else:
                    re.append(task_request.pop(0))
            else:
                task_request.pop(0)

if __name__ == '__main__':
    nums = [[1,0],[0,1],[0,3]]
    Solution().can_tasks_finish(2,nums)