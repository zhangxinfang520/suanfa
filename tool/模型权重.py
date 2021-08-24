# -*- coding:utf-8 -*-
#@Time : 2021/8/23 19:23
#@Author: zxf_要努力
#@File : 模型权重.py

import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision

class TheModelClass(nn.Module):
    def __init__(self):
        super(TheModelClass, self).__init__()
        self.conv1 = nn.Conv2d(3,6,5)
        self.pool = nn.MaxPool2d(2,2)
        self.conv3 = nn.Conv2d(6,16,5)
        self.fc1 = nn.Linear(16*5*5,120)
        self.fc2 = nn.Linear(120,84)
        self.fc3 = nn.Linear(84,10)

    def forward(self,x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv3(x)))
        x = x.view(-1,16*5*5)
        x = self.fc1(x)
        x = self.fc2(x)
        x = self.fc3(x)
        return x


if __name__ == '__main__':
    model = TheModelClass()
    #优化器
    optimizer = torch.optim.SGD(model.parameters(),lr=1e-4,momentum=0.9)

    print("model`s state_dict:")
    for param_tensor in model.state_dict():
        print(param_tensor,"\t",model.state_dict()[param_tensor].size())
    print("model`s state_dict:")
    for var_name in optimizer.state_dict():
        print(var_name,"\t",optimizer.state_dict()[var_name])
    # torch.save(model.state_dict(),"zxf.pt")
    torch.save({'model_state_dict':model.state_dict(),
                    'optimizer_state_dict':optimizer.state_dict()},'zxf.pt')






