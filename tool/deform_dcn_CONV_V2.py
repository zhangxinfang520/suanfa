# -*- coding:utf-8 -*-
#@Time : 2021-05-20 17:00
#@Author: zxf_要努力
#@File : deform_dcn_CONV_V2.py
'''
可变卷积 操作
'''
import torch
import torch.nn as nn

class DeformConv2d(nn.Module):
    def __init__(self,inc,outc,kernel_size=3,padding=1,
                 stride=1, bias=None, modulation=False):
        super(DeformConv2d, self).__init__()

        self.kernel_size = kernel_size
        self.padding = padding
        self.stride = stride
        self.zero_padding = nn.ZeroPad2d(padding)
        self.conv = nn.Conv2d(inc,outc,kernel_size=kernel_size,
                              stride=stride,bias=bias)

        self.p_conv = nn.Conv2d(inc,2*kernel_size*kernel_size,
                                kernel_size=3,padding=1,stride=stride)
        nn.init.constant_(self.p_conv.weight,0)

        self.p_conv.register_backward_hook(self._set_lr)

        self.modulation = modulation
        if modulation:
            self.m_conv = nn.Conv2d(inc,kernel_size*kernel_size,
                                    kernel_size=3,padding=1,stride=stride)
            nn.init.constant_(self.m_conv.weight,0)
            self.m_conv.register_backward_hook(self._set_lr)

    @staticmethod
    def _set_lr(module,grad_input,grad_output):
        grad_input = (grad_input[i] * 0.1 for i in range(len(grad_input)))
        grad_output = (grad_output[i] * 0.1 for i in range(len(grad_output)))

    def forward(self,x):
        offset = self.p_conv(x)
        if self.modulation:
            m = torch.sigmoid(self.m_conv(x))
        dtype = offset.data.type()
        ks = self.kernel_size
        N = offset.size(1) // 2

        if self.padding:
            x = self.zero_padding(x)
        # (b, 2N, h, w)
        p = self._get_p(offset,dtype)
        #(b,h,w,2N)
        p = p.contiguous().permute(0,2,3,1)
        q_lt = p.detach().floor()
        q_rb = q_lt + 1
        q_lt = torch.cat([torch.clamp(q_lt[..., :N], 0, x.size(2) - 1), torch.clamp(q_lt[..., N:], 0, x.size(3) - 1)],
                         dim=-1).long()
        q_rb = torch.cat([torch.clamp(q_rb[..., :N], 0, x.size(2) - 1), torch.clamp(q_rb[..., N:], 0, x.size(3) - 1)],
                         dim=-1).long()
        q_lb = torch.cat([q_lt[..., :N],q_rb[..., N:]], dim=-1)
        q_rt = torch.cat([q_rb[..., :N],q_lt[..., N:]], dim=-1)

        



    def _get_p_n(self,N,dtype):
        pass
    def _get_p_0(self,h,w,N,dtype):
        pass
    def _get_p(self,offset,dtype):
        pass
    def _get_x_p(self,x,q,N):
        pass

    @staticmethod
    def _reshape_x_offset(x_offset, ks):
        pass
