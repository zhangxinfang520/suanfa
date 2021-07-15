# -*- coding:utf-8 -*-
#@Time : 2021-07-14 9:14
#@Author: zxf_要努力
#@File : GroupNormalization.py
'''
实现 gn
'''
import torch
import torch.nn as nn

def group_norm(x:torch.tensor,
               num_groups:int,
               num_channels:int,
               eps:float=1e-5,
               gamma:float=1.0,
               beat:float=0.0):
    '''

    :param x: [N,C,H,W]
    :param num_groups: nums
    :param num_channels: C
    :param eps:
    :param beat:
    :return:
    '''
    assert divmod(num_channels,num_groups)[1] == 0
    channels_per_group = num_channels // num_groups
    new_tensor = []
    for t in x.split(channels_per_group,dim= 1):
        var,mean = torch.var_mean(t,dim=[1,2,3],unbiased=False)
        # var = var_mean[0]
        # mean = var_mean[1]
        t = (t-mean[:,None,None,None]) / torch.sqrt(var[:,None,None,None]+eps)
        t = t * gamma + beat
        new_tensor.append(t)
    new_tensor = torch.cat(new_tensor,dim=1)
    return new_tensor


if __name__ == '__main__':
    eps = 1e-5
    num_groups = 2
    num_channels = 4
    p = torch.randn((2, num_channels, 2, 2))
    r2 = group_norm(p, num_groups, num_channels, eps)
    print(r2)
    
    #官方的
    gn = nn.GroupNorm(num_groups=num_groups,num_channels=num_channels,eps=eps)
    r1 = gn(p)
    print(r2)



