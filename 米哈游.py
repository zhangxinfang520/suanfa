# import sys
#
# def get_sample(target):
#     new_target = ""
#     j = 0
#     while j <= len(target) - 1:
#         if (j+1 !=len(target)) and target[j] == "a" and target[j+1] == "b":
#             j = j + 2
#         else:
#             new_target += target[j]
#             j += 1
#     return new_target
#
# def is_get_target(target):
#     temp = target
#     new_target = get_sample(target)
#     while temp != new_target:
#         temp = new_target
#         new_target = get_sample(new_target)
#         if new_target == "" :
#             return True
#     target = new_target
#     if len(target) != 0:
#         return False
    # if len(target) % 2 :
    #     return False
    # if len(target) < 2:
    #     return False
    #
    # right = len(target) // 2
    # left = right - 1
    # while left>=0 and right < len(target):
    #     if target[left] != target[right]:
    #         return True
    #     else:
    #         left -=1
    #         right +=1
    # return False
    # modu = "ab"
    # if target == modu:
    #     return True
    # def backtrack(con):
    #     if con == target:
    #         return True
    #     if len(con) >= len(target):
    #         return False
    #     flag = False
    #     for i in range(len(con)):
    #         flag = flag or  backtrack(con[0:i]+modu+con[i:len(con)])
    #         if flag:
    #             return flag
    #     return flag
    #
    # return backtrack("ab")

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        '''每一行变为目标'''
        # 把每一行的数字分隔后转化成int列表
        values = list(map(str, line.split()))
        for value in values:
            if len(value) < 2:
                print("NO")
                continue
            if is_get_target(value):
                print("YES")
            else:
                print("NO")
