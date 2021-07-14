# -*- coding:utf-8 -*-
#@Time : 2021-07-14 11:12
#@Author: zxf_要努力
#@File : InstanceNorm.py
'''实现IN'''

import torch
import torch.nn as nn


def IN_process(p:torch.tensor,eps=1e-5):
    """

    :param p: N * C * H * W
    :param eps:
    :return:
    """
    var_mean = torch.var_mean(p,dim=[2,3],unbiased=False)
    var = var_mean[0]
    mean = var_mean[1]

    p = (p - mean[:,:,None,None]) / torch.sqrt(var[:, :,None,None] + eps)
    return p


if __name__ == '__main__':
    p = torch.randn(2,2,2,2)
    print(p.shape)
    r1 = IN_process(p)
    print(r1)
    IN = nn.InstanceNorm2d(2,eps=1e-5)
    r2 = IN(p)
    print(r2)
