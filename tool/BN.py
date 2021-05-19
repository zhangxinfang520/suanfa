# -*- coding:utf-8 -*-
#@Time : 2021-05-18 15:17
#@Author: zxf_要努力
#@File : BN.py
import torch
import torch.nn as nn

def batch_norm(x,gamma,beta,moving_mean,moving_var,eps,momentum):
    #eps 和 momentu为超参数 Hyperparameter
    #测试和训练的均值方差计算是不同的
    if not torch.is_grad_enabled():
        #测试的时候直接使用全局的
        x_hat = (x-moving_mean ) / torch.sqrt(moving_var+eps)
    else:
        assert (x.shape) in (2,4)
        if (x.shape) == 2:#liner
            mean = x.mean(dim=0)
            var = ((x-mean)**2).mean(dim=0)
        else:#cnn
            mean = x.mean(dim=(0,2,3),keepdim=True)
            var = ((x-mean)**2).mean(dim=(0,2,3),keepdim=True)
        x_hat = (x-mean ) / torch.sqrt(var+eps)
        #然后更新 moving_mean_var
        moving_mean = moving_mean*momentum + mean*(1-momentum)
        moving_var = moving_var * moving_var + var*(1-momentum)

    y = gamma*x_hat +beta
    return y,moving_mean,moving_var

class BatchNorm(nn.Module):
    def __init__(self,num_features,num_dims,**kwargs):
        super(BatchNorm, self).__init__()
        self.batch_norm = batch_norm
        if num_dims==2:#如果是liner bn后的shape
            res_shape = (1,num_features)
        else:#卷积的bn后的shape
            res_shape = (1,num_features,1,1)
        #学习的参数gamma_beta
        self.gamma = nn.Parameter(torch.ones(res_shape))
        self.beta = nn.Parameter(torch.ones(res_shape))

        #均值方差
        self.moving_mean = torch.zeros(res_shape)
        self.moving_var = torch.zeros(res_shape)

    def forward(self,x):
        #device
        if x.device != self.moving_mean.device:
            self.moving_mean = self.moving_mean.to(x.device)
            self.moving_var = self.moving_var.to(x.device)
        Y,self.moving_mean,self.moving_var = self.batch_norm(x,self.gamma,self.beta,
                                                             self.moving_mean,self.moving_var)
        return Y