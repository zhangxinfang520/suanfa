# -*- coding:utf-8 -*-
#@Time : 2021-05-24 14:50
#@Author: zxf_要努力
#@File : yolov5的输入推图像切片操作.py
'''
，对图片进行切片操作，具体操作是在一张图片中每隔一个像素拿到一个值，
类似于邻近下采样，这样就拿到了四张图片，四张图片互补，长的差不多，
但是没有信息丢失，这样一来，将W、H信息就集中到了通道空间，输入通道扩充了4倍，
即拼接起来的图片相对于原先的RGB三通道模式变成了12个通道，最后将得到的新图片再经过卷积操作，
最终得到了没有信息丢失情况下的二倍下采样特征图
'''
import torch
import torch.nn as nn


class Focus(nn.Module):
    def __init__(self,c1,c2,k=1,s=1,p=None,g=1,act=True):
        super(Focus, self).__init__()
        self.conv = nn.Conv2d(c1*4, c2, k, s, p,g,act)

    def forward(self,x):
        return self.conv(torch.cat([x[...,::2,::2],x[...,1::2,::2],x[...,::2,1::2],x[...,1::2,1::2]],dim=1))

one = torch.ones((1,3,640,640))

def a(x):
    return torch.cat([x[...,::2,::2],x[...,1::2,::2],x[...,::2,1::2],x[...,1::2,1::2]],dim=1)

two = a(one)
print(one[...,::2,::2].shape)
print(two.size())