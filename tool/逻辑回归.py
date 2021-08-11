# -*- coding:utf-8 -*-
#@Time : 2021-08-10 9:22
#@Author: zxf_要努力
#@File : 逻辑回归.py
import numpy as np
import torch
import torch.nn as nn

import matplotlib.pyplot as plt

#构造数据集
n_data = torch.ones(100,2)
x0 = torch.normal(2 * n_data,1) # 生成均值为2.标准差为1的随机数组成的矩阵 shape=(100, 2)
y0 = torch.zeros(100)

x1 = torch.normal(-2 * n_data, 1)  # 生成均值为-2.标准差为1的随机数组成的矩阵 shape=(100, 2)
y1 = torch.ones(100)

#合并 xy
x = torch.cat((x0,x1),0).type(torch.FloatTensor)
y = torch.cat((y0,y1),0).type(torch.FloatTensor)

# print(x.data.numpy()[:,0])

# plt.scatter(x.data.numpy()[:,0],x.data.numpy()[:,1],c=y.data.numpy(),s=100,lw=0,cmap='RdYlGn')
# plt.show()

class LogisticRegression(nn.Module):
    def __init__(self,input,output):
        super(LogisticRegression, self).__init__()
        self.lr = nn.Linear(input,output)
        self.sigmod = nn.Sigmoid()

    def forward(self,x):
        x = self.lr(x)
        x = self.sigmod(x)

        return x

#模型初始化
log_net = LogisticRegression(2,1)
if torch.cuda.is_available():
    log_net.cuda()
#损失函数
loss = nn.BCELoss()
#优化器
optim = torch.optim.SGD(log_net.parameters(),lr=1e-3,momentum=0.9)

#开始训练
for epoch in range(10000):
    if torch.cuda.is_available():
        x = x.cuda()
        y = y.cuda()
    pred = log_net(x)
    pred = pred.squeeze(-1)
    loss_ = loss(pred,y)
    print_loss = loss_.data.item()  # 得出损失函数值
    mask = pred.ge(0.5).float()
    correct = (mask == y).sum()
    acc = correct.item() / x.size(0)  # 计算精度
    optim.zero_grad()
    loss_.backward()
    optim.step()
    if (epoch + 1) % 20 == 0:
        print('*' * 10)
        print('epoch {}'.format(epoch + 1))  # 误差
        print('loss is {:.4f}'.format(print_loss))
        print('acc is {:.4f}'.format(acc))  # 精度


# 结果可视化
w0, w1 = log_net.lr.weight[0]
w0 = float(w0.item())
w1 = float(w1.item())
b = float(log_net.lr.bias.item())
plot_x = np.arange(-7, 7, 0.1)
plot_y = (-w0 * plot_x - b) / w1
plt.scatter(x.to("cpu")[:, 0], x.to("cpu")[:, 1], c=y.to("cpu"), s=100, lw=0, cmap='RdYlGn')
plt.plot(plot_x, plot_y)
plt.show()

