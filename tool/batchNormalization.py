# -*- coding:utf-8 -*-
#@Time : 2021-07-14 10:20
#@Author: zxf_要努力
#@File : batchNormalization.py
'''
实现 bn
'''

import torch
import torch.nn as nn


def bn_process(features:torch.tensor,eps=1e-5):
    '''

    :param features: N * C * H * W
    :param mean:
    :param var:
    :return:
    '''
    var_mean = torch.var_mean(features,dim=[0,2,3],unbiased=False)
    var = var_mean[0]
    mean = var_mean[1]
    
    features = (features - mean[None,:,None,None])/ torch.sqrt(var[None,:,None,None]+eps)
    return features


if __name__ == '__main__':
    p = torch.randn(2,2,2,2)
    r1 = bn_process(p)
    print(r1)

    bn = nn.BatchNorm2d(2,eps=1e-5)
    nn.InstanceNorm2d
    r2 = bn(p)
    print(r2)

    


