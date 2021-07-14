# -*- coding:utf-8 -*-
#@Time : 2021-07-14 10:01
#@Author: zxf_要努力
#@File : LayerNormalization.py
'''实现layer Normalization'''
'''在Pytorch的LayerNorm类中有个normalized_shape参数，
可以指定你要Norm的维度（注意，函数说明中the last certain number of dimensions，指定的维度必须是从最后一维开始）。
比如我们的数据的shape是[4, 2, 3]，那么normalized_shape可以是[3]（最后一维上进行Norm处理），
也可以是[2, 3]（Norm最后两个维度），也可以是[4, 2, 3]（对整个维度进行Norm），但不能是[2]或者[4, 2]'''

import torch
import torch.nn as nn


def layer_norm_process(feature:torch.tensor,beta=0.,gamma=1.0,eps=1e-5):
    '''

    :param feature: N * C * H * W
    :param beta:
    :param gamma:
    :param eps:
    :return:
    '''
    var_mean = torch.var_mean(feature,dim=[1,2,3],unbiased=False)
    var = var_mean[0]
    mean = var_mean[1]

    #ln归一化
    feature = (feature - mean[:,None,None,None]) / torch.sqrt(var[:,None,None,None]+eps)
    feature = gamma * feature + beta
    return feature

if __name__ == '__main__':
    p = torch.randn(2,2,2,2)
    r1 = layer_norm_process(p)
    print(r1)
    m = nn.LayerNorm(p.size()[1:],eps=1e-5)
    r2 = m(p)
    print(r2)
