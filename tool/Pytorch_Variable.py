# -*- coding:utf-8 -*-
#@Time : 2021-05-23 18:40
#@Author: zxf_要努力
#@File : Pytorch_Variable.py
import torch
from torch.autograd import  Variable

x_tensor = torch.ones(3)
print('张量的类型以及具体值:\n', type(x_tensor), x_tensor)
x_var = Variable(x_tensor, requires_grad = True)
print('变量的类型以及具体的值:\n', type(x_var), x_var)
# 显示的调用pytorch中的反向传播
y = x_var * x_var + 2
print(y, '\n', y.grad_fn)

y.backward(torch.FloatTensor([1, 1, 1]))
print(x_var.grad, '\n', x_var.grad_fn)