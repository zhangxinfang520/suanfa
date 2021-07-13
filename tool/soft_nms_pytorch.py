# -*- coding:utf-8 -*-
#@Time : 2021-07-10 11:10
#@Author: zxf_要努力
#@File : soft_nms_pytorch.py
import torch

def soft_nms_pytorch(p:torch.tensor,thresh_iou,thresh_score,sigma,method):
    """

    :param p:
    :param thresh_score:
    :param sigma:
    :param method: 1 or 2 一个是线性的 一个高斯的
    :return:
    """
    x1 = p[:,0]
    y1 = p[:,1]
    x2 = p[:,2]
    y2 = p[:,3]

    area = ( x2 - x1 ) * ( y2 - y1)
    keep = []
    scores = p[:,-1]
    keep_new_score = []

    scores_cp = scores.clone()

    order = scores_cp.argsort()

    size = len(order)
    for i in range(size):
        index = order[-1]
        order = order[:-1]
        keep.append(p[index])
        keep_new_score.append(scores_cp[index])

        xx1 = torch.index_select(x1,0,index=order)
        xx2 = torch.index_select(x2,0, index=order)
        yy1 = torch.index_select(y1,0, index=order)
        yy2 = torch.index_select(y2,0, index=order)

        xx1 = torch.max(xx1,x1[index])
        yy1 = torch.max(yy1,y1[index])
        xx2 = torch.min(xx2,x2[index])
        yy2 = torch.min(yy2,y2[index])

        w = torch.clamp(xx2-xx1,min=0)
        h = torch.clamp(yy2-yy1,min=0)

        inter = w * h
        res_areas = torch.index_select(area,0,index=order)
        out = res_areas - inter + area[index]

        iou = inter / out

        if method == 1:
            x = torch.ones(len(order)) - iou
            y = torch.ones(len(order))
            weight = torch.where(iou > thresh_iou,x,y)
        else:
            weight = torch.exp(-iou*iou/sigma)

        num = weight.size()[0]
        for i in range(num):
            scores_cp[order[i]] *= weight[i]

        end = len(order)
        order = scores_cp.argsort()

        order = order[0:end]


    num = len(keep_new_score)
    print(keep_new_score)

    keep_f = [keep[i] for i in range(num) if keep_new_score[i] > thresh_score]
    return keep_f


P = torch.tensor([[500.0, 500.0, 1000.0, 1000.0, 0.85],
                 [615.0, 600.0, 1115.0, 1100.0, 0.95],
                 [550.0, 375.0, 1050.0, 875.0, 0.75],
                 [800.0, 700.0, 1300.0, 1200.0, 0.80]])

keep = soft_nms_pytorch(P, thresh_iou=0.30, thresh_score=0.50, sigma=0.5, method=2)
n = len(keep)
for i in range(n):
    print(keep[i][-1])
