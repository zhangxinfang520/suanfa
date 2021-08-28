# -*- coding:utf-8 -*-
#@Time : 2021/8/27 9:22
#@Author: zxf_要努力
#@File : ResNetX.py
import torch
import torch.nn as nn


class BottleNeck(nn.Module):
    expansion = 2
    def __init__(self,in_channel,channel,stride=1,C=32,downsample=False):
        super().__init__()
        self.conv1 = nn.Conv2d(in_channel,channel,
                               kernel_size=1,stride=stride,bias=False)
        self.bn1 = nn.BatchNorm2d(channel)

        self.conv2 = nn.Conv2d(channel,channel,
                               kernel_size=3,stride=1,padding=1,bias=False,groups=C)
        self.bn2 = nn.BatchNorm2d(channel)

        self.conv3 = nn.Conv2d(channel,channel*self.expansion,
                               kernel_size=1,stride=1,bias=False)
        self.bn3 = nn.BatchNorm2d(channel*self.expansion)

        self.relu = nn.ReLU(False)

        self.downsample = downsample
        self.strides = stride

    def forward(self,x):
        residual = x
        out = self.relu(self.bn1(self.conv1(x)))
        out = self.relu(self.bn2(self.conv2(out)))
        out = self.relu(self.bn3(self.conv3(out)))

        if self.downsample !=None:
            residual = self.downsample(residual)

        out += residual

        return self.relu(out)


class RexNetX(nn.Module):
    def __init__(self,block,layers,num_classes=1000):
        '''
        @param block: 模块名称 一般都是Bottleneck
        @param layers: list列表 比如ResNet50为[3,4,6,3]
        @param num_classes: 最后全连接层的输出数

        '''
        super().__init__()
        self.in_channels = 64
        
        self.conv1 = nn.Conv2d(3,64,
                               kernel_size=7,stride=2,padding=3,bias=False)
        self.bn1 = nn.BatchNorm2d(64)
        self.relu = nn.ReLU(False)
        
        self.maxpool = nn.MaxPool2d(kernel_size=3,stride=2,
                                    padding=0,ceil_mode=True)
        
        #layer
        self.layer1 = self._make_layer(block,128,layers[0])
        self.layer2 = self._make_layer(block,256,layers[1],stride=2)
        self.layer3 = self._make_layer(block,512,layers[2],stride=2)
        self.layer4 = self._make_layer(block,1024,layers[3],stride=2)

        #classifier
        self.avgpool = nn.AdaptiveAvgPool2d(1)
        self.classifier = nn.Linear(1024*block.expansion,num_classes)
        self.softmax = nn.Softmax(-1)

    def forward(self,x):

        out = self.relu(self.bn1(self.conv1(x)))
        out = self.maxpool(out)

        out = self.layer1(out)
        out = self.layer2(out)
        out = self.layer3(out)
        out = self.layer4(out)

        out = self.avgpool(out)
        out = out.reshape(out.shape[0], -1)
        out = self.classifier(out)
        out = self.softmax(out)

        return out


    def _make_layer(self,block,channel,blocks,stride=1):
        """
        主要来处理 H（x） = f（x） + x
        @param block: 模块名称
        @param channel: 输出通道
        @param blocks: 块的数量
        @param stride:
        """
        downsample = None
        if (stride !=1 or self.in_channels!= channel *block.expansion):
            self.downsample = nn.Conv2d(self.in_channels,channel*block.expansion,
                                        stride=stride,kernel_size=1,bias=False)
        #第一部分 一般可能需要downsample
        layers = []
        layers.append(block(self.in_channels,channel,downsample=self.downsample,stride=stride))
        self.in_channels = channel*block.expansion

        for _ in range(1,blocks):
            layers.append(block(self.in_channels,channel))
        return nn.Sequential(*layers)

def ResNeXt50(num_classes=1000):
    return RexNetX(BottleNeck,[3,4,6,3],num_classes=num_classes)


def ResNeXt101(num_classes=1000):
    return RexNetX(BottleNeck,[3,4,23,3],num_classes=num_classes)


def ResNeXt152(num_classes=1000):
    return RexNetX(BottleNeck,[3,8,36,3],num_classes=num_classes)

if __name__ == '__main__':
    input = torch.randn(8,3,224,224,device="cuda:0")
    net  = ResNeXt50().cuda()
    out = net(input)
    print(out)