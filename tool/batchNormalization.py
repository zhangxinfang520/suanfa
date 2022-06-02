# -*- coding:utf-8 -*-
#@Time : 2021-07-14 10:20
#@Author: zxf_要努力
#@File : batchNormalization.py
'''
实现 bn
'''

import torch
def bn_process(features:torch.tensor,eps=1e-5,gamma:float=1.0,beat:float=0.0):
    '''
    :param features: N * C * H * W
    :param mean:
    :param var:
    :return:
    '''
    var_mean = torch.var_mean(features,dim=[0,2,3],unbiased=False)
    mean = var_mean[1]
    var = var_mean[0]
    features = (features - mean[None,:,None,None])/ torch.sqrt(var[None,:,None,None]+eps)
    return gamma*features + beat


if __name__ == '__main__':
    # p = torch.randn(2,2,2,2)
    # r1 = bn_process(p)
    # print(r1)
    # 
    # bn = nn.BatchNorm2d(2,eps=1e-5)
    # 
    # r2 = bn(p)
    # print(r2)
    test = torch.randn(1)
    print(test.shape)
    print(test)
    b = torch.ones(1,1,1,1)
    print(b)
    a = test[None,:,None,None]
    print(a.shape)
    print(a)



