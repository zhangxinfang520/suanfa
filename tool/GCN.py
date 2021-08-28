# -*- coding:utf-8 -*-
#@Time : 2021/8/26 16:54
#@Author: zxf_要努力
#@File : GCN.py
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn.parameter import Parameter

class CCN(nn.Module):
    def __init__(self,k_size = 3,ch=()):
        super(CCN, self).__init__()
        #self.independence = 0.7
        #self.share = 0.3
        self.w1 = Parameter(torch.ones(1) * 0.5)
        self.w2 = Parameter(torch.ones(1) * 0.5)
        w = 6
        h = 10
        self.avg_pool = nn.AdaptiveAvgPool2d((w,h))

        self.c_attention1 = nn.Sequential(nn.Conv2d(ch, ch, kernel_size=3, stride=1, padding=1, bias=True),
                                          nn.InstanceNorm2d(num_features=ch),
                                          nn.LeakyReLU(0.3, inplace=True))
        self.c_attention2 = nn.Sequential(nn.Conv2d(ch, ch, kernel_size=3, stride=1, padding=1, bias=True),
                                          nn.InstanceNorm2d(num_features=ch),
                                          nn.LeakyReLU(0.3, inplace=True))


        self.sigmoid = nn.Sigmoid()
        #self.conv1 = Conv(ch, ch, k=1)
        #self.conv2 = Conv(ch, ch, k=1)

    def forward(self, x):
        # x: input features with shape [b, c, h, w]
        b, c, h, w = x.size()

        # feature descriptor on the global spatial information
        y = self.avg_pool(x)

        y_t1 = self.c_attention1(y)
        y_t2 = self.c_attention2(y)
        bs,c,h,w = y_t1.shape
        y_t1 =y_t1.view(bs, c, h*w)
        y_t2 =y_t2.view(bs, c, h*w)

        y_t1_T = y_t1.permute(0, 2, 1)
        y_t2_T = y_t2.permute(0, 2, 1)
        M_t1 = torch.matmul(y_t1, y_t1_T)
        M_t2 = torch.matmul(y_t2, y_t2_T)
        M_t1 = F.softmax(M_t1, dim=-1)
        M_t2 = F.softmax(M_t2, dim=-1)

        M_s1 = torch.matmul(y_t1, y_t2_T)
        M_s2 = torch.matmul(y_t2, y_t1_T)
        M_s1 = F.softmax(M_s1, dim=-1)
        M_s2 = F.softmax(M_s2, dim=-1)

        x_t1 = x
        x_t2 = x
        bs,c,h,w = x_t1.shape
        x_t1 = x_t1.contiguous().view(bs, c, h*w)
        x_t2 = x_t2.contiguous().view(bs, c, h*w)

        #x_t1 = torch.matmul(self.independence*M_t1 + self.share*M_s1, x_t1).contiguous().view(bs, c, h, w)
        #x_t2 = torch.matmul(self.independence*M_t2 + self.share*M_s2, x_t2).contiguous().view(bs, c, h, w)
        x_t1 = torch.matmul(self.w1*M_t1 + (1-self.w1)*M_s1, x_t1).contiguous().view(bs, c, h, w)
        x_t2 = torch.matmul(self.w2*M_t2 + (1-self.w2)*M_s2, x_t2).contiguous().view(bs, c, h, w)
        #print("M_t1",torch.sort(M_t1[0][0]))
        #print("y_t1",torch.max(y_t1),torch.min(y_t1))
        #print("y_t2", torch.max(y_t2), torch.min(y_t2))
        return [x_t1+x,x_t2+x]


if __name__ == '__main__':
    ccn = CCN(9,256)
    x = torch.randn(8,256,32,32)
    print(ccn(x)[0].shape)