# -*- coding:utf-8 -*-
#@Time : 2021/8/31 9:55
#@Author: zxf_要努力
#@File : 学习率调整.py

import torch
import torch.nn as nn


class LR(nn.Module):

    def __init__(self,in_channel):
        super(LR, self).__init__()
        self.liner = nn .Linear(in_channel,1)
        self.sigmod = nn.Sigmoid()

    def forward(self,x):
        return self.sigmod(self.liner(x))


input  = torch.randn(1,2)
target = torch.tensor([[1]],dtype=torch.float32)


net = LR(2)
# out = net(input)

loss_fuc = nn.BCELoss()

#优化器 学习利率
# print(loss_fuc(out, target))

#优化器 trick
#--------------- 指数衰减 
# optimizer = torch.optim.SGD(net.parameters(),lr=0.1)
#
# #指数衰减控制器
# ExpLR = torch.optim.lr_scheduler.ExponentialLR(optimizer,gamma=0.98)
#
# for epoch in range(50):
#     out = net(input)
#     loss = loss_fuc(out, target)
#     print(loss)
#     loss.backward()
#     optimizer.step()
#     print(optimizer.state_dict()['param_groups'][0]['lr'])
#     ExpLR.step()
#     print(optimizer.state_dict()['param_groups'][0]['lr'])

#固定步长衰减
# optimizer = torch.optim.SGD(net.parameters(),lr=0.1)
#
# StepLR = torch.optim.lr_scheduler.StepLR(optimizer,10,gamma=0.65)
#
# for epoch in range(100):
#     prob = net(input)
#     loss = loss_fuc(prob,target)
#     print(loss)
#     loss.backward()
#     optimizer.step()
#     print(optimizer.state_dict()["param_groups"][0]['lr'])
#     StepLR.step()
#     print(epoch)
#     print(optimizer.state_dict()["param_groups"][0]['lr'])

#多步长衰减
# optimizer = torch.optim.SGD(net.parameters(),lr=0.1)
# # 0 - 10不跟新 20-30 30-40 40-50 的右侧都进行一次更新
# Multi = torch.optim.lr_scheduler.MultiStepLR(optimizer,milestones=[10,20,30,40,50],gamma=0.8)
#
# for epoch in range(50):
#     prob = net(input)
#     loss = loss_fuc(prob,target)
#     loss.backward()
#     print(loss)
#     optimizer.step()
#     print(optimizer.state_dict()['param_groups'][0]['lr'])
#     #print(optimizer.state_dict())
#     print(epoch)
#     Multi.step()
#     print(optimizer.state_dict()['param_groups'][0]['lr'])
#余弦退火

optimizer = torch.optim.SGD(net.parameters(),lr=0.1)
#参数T_max表示余弦函数周期；eta_min表示学习率的最小值，默认它是0表示学习率至少为正值
CosineLR = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=150, eta_min=0)
for epoch in range(50):
    prob = net(input)
    loss = loss_fuc(prob,target)
    loss.backward()
    optimizer.step()
    print(epoch)
    print(optimizer.state_dict()['param_groups'][0]['lr'])
    CosineLR.step()

    print(optimizer.state_dict()['param_groups'][0]['lr'])


