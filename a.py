
a = 10
def get_index(nums):
    global a
    a +=1
print(a)
    # n = len(nums)
    # if n==1:return 1
    # dp = [1]*n
    # for i in range(1,n):
    #     for j in range(0,i):
    #         if nums[i] - nums[j] ==1:
    #             dp[i] = max(dp[i],dp[j]+1)
    # return max(dp)


if __name__ == '__main__':
    nums = [1,2, 2, 4, 5, 6, 7, 8,3,4,5,6,7,9]
    print(get_index(nums))