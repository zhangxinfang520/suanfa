# -*- coding:utf-8 -*-
#@Time : 2021-07-10 11:10
#@Author: zxf_要努力
#@File : soft_nms_pytorch.py
import torch

import torch


def pytorch_soft_nms(p: torch.tensor, thres_iou: float, thres_scores: float, sigmma=0.2, method=1):
    x1 = p[:, 0]
    y1 = p[:, 1]
    x2 = p[:, 2]
    y2 = p[:, 3]
    areas = (x2 - x1) * (y2 - y1)
    keep = []
    keep_new_scores = []
    scores = p[:, -1]
    order = scores.argsort()
    n = len(order)
    for i in range(n):
        index = order[-1]
        order = order[:-1]
        keep.append(p[index])
        keep_new_scores.append(scores[index])

        xx1 = torch.index_select(x1, 0, order)
        yy1 = torch.index_select(y1, 0, order)
        xx2 = torch.index_select(x2, 0, order)
        yy2 = torch.index_select(y2, 0, order)

        xx1 = torch.max(xx1, x1[index])
        yy1 = torch.max(yy1, y1[index])
        xx2 = torch.min(xx2, x2[index])
        yy2 = torch.min(yy2, y2[index])

        w = torch.clamp(xx2 - xx1, min=0)
        h = torch.clamp(yy2 - yy1, min=0)

        inter = w * h
        res_areas = torch.index_select(areas, 0, order)

        out = res_areas - inter + areas[index]

        Iou = inter / out
        if method == 1:
            y = torch.ones(len(order)) - Iou
            x = torch.ones(len(order))
            weight = torch.where(Iou > thres_iou, y, x)
        else:
            weight = torch.exp(-Iou * Iou / sigmma)
        len_w = weight.size()[0]
        for i in range(len_w):
            scores[order[i]] *= weight[i]
        end = len(order)
        order = scores.argsort()
        order = order[:end]
    n = len(keep_new_scores)
    keep_f = [keep[i] for i in range(n) if keep_new_scores[i] > thres_scores]
    return keep_f

P = torch.tensor([[500.0, 500.0, 1000.0, 1000.0, 0.85],
                 [615.0, 600.0, 1115.0, 1100.0, 0.95],
                 [550.0, 375.0, 1050.0, 875.0, 0.75],
                 [800.0, 700.0, 1300.0, 1200.0, 0.80]])

keep = pytorch_soft_nms(P, 0.30, 0.50, 0.5, method=2)
print(keep)
n = len(keep)
for i in range(n):
    print(keep[i][-1])
