# -*- coding:utf-8 -*-
#@Time : 2021-07-20 15:45
#@Author: zxf_要努力
#@File : EMA.py
'''
数滑动平均。 它的意义在于利用滑动平均的参数来提高模型在测试数据上的健壮性。
'''
import math

import torch
import torch.nn as nn


class EMA(nn.Module):

    def __init__(self,mu,update=0):
        super(EMA, self).__init__()

        self.update = update
        self.shadow = {}
        self.mu = lambda x: mu * (1-math.exp(-x / 2000))

    def register(self,name,val):
        self.shadow[name] = val

    def forward(self,name,x):
        assert  name in self.shadow
        self.update += 1
        d = self.mu(self.update)
        new_average = (1. - d) * x + d * self.shadow[name]
        self.shadow[name] = new_average.clone()
        return new_average

model = ""
ema = EMA(0.999)
for name,param in model.name_parameters():
    if param.required_grad:
        ema.register(name,param)
#optimizer.step()
for name,parm in model.name_parameters():
    if param.required_grad:
        param.data = ema(name,parm.data)

