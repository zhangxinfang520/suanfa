import sys


def is_zouqi(nums):
    for i in range(len(nums)-2):
        if nums[i] !=nums[i+2]:
            return False
    return True

def get_high_count(nums):
    nums_dict= {}
    for num in nums:
        if num not in nums_dict.keys():
            nums_dict[num] = 1
        else:
            nums_dict[num] += 1
    re = sorted(nums_dict.items(),key=lambda x:(-x[1]))
    return re[0][1]

def get_count_zhouqi(nums):
    first = nums[0::2]
    second = nums[1::2]

    re_first = get_high_count(first)
    re_second = get_high_count(second)
    return  len(nums) - re_first -re_second



if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    nums = list(map(int,sys.stdin.readline().strip().split()))
    if is_zouqi(nums):
        print(0)
    else:
        res = get_count_zhouqi(nums)
        print(res)