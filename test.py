import torch
import math


# from deform_dcn_CONV_V2 import DeformConv2d
#
# input = torch.randn(2,64,128,128).cuda()
# dcn = DeformConv2d(64,64,kernel_size=3,stride=1,padding=1).cuda()
# out = dcn(input)
#
# print(out.shape)

# p = torch.tensor([[-1.5650,  2.0415, -0.1024, -0.5790]]
#        )
# print(p.shape)
# print(p[:,::])
# mean = torch.var_mean(p,dim=[0])[1]
# print(mean)

# input = torch.randn(2,3,512,512)
# #dal = torch.nn.Conv2d(3,64,3,1,0)
# dal = torch.nn.Conv2d(3,64,3,1,0,2)
#
# out = dal(input)
# print(out.shape)
# 
# a = 10
# b = 15
# out = math.gcd(a,b)
# print(out)
#
def backetsort(nums):
    max_values = max(nums)
    n = len(nums)
    backerNum = max_values + 1
    count = [0] * backerNum
    temp = [0] * n
    for i in range(n):
        count[nums[i]] +=1
    for i in range(1,max_values+1):
        count[i] = count[i-1] + count[i] #把计数容器count内的单个容器数值，遍历成依次叠加的
    for i in range(n-1,-1,-1):
        temp[count[nums[i]] - 1 ] = nums[i]
        count[nums[i]] -=1  #计数器中对应的元素开始递减，完成循环后与初始计数器（每个元素的数量）保持一致。

    return temp


if __name__ == '__main__':
    nums = [2, 6, 4, 5, 1, 2, 3, 6]
    print(sum(nums))
    # print(backetsort(nums))
