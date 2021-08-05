# -*- coding:utf-8 -*-
#@Time : 2021-07-09 10:09
#@Author: zxf_要努力
#@File : nms_pytorch.py

import torch
import numpy as np

from  ensemble_boxes import  *


def pytorch_nms(p:torch.tensor,threshold:float):
    '''
    求解 iou
    :param p: [N,5] 
    :param threshold:float 
    :return: 
    '''
    x1 = p[:, 0]
    y1 = p[:, 1]
    x2 = p[:, 2]
    y2 = p[:, 3]
    area = (y2-y1) * (x2-x1)
    scores = p[:,4]
    order = scores.argsort()
    
    keep = []
    while len(order):
        idx = order[-1]
        keep.append(p[idx])
        order = order[:-1]
        if len(order) == 0:
            break
        xx1 = torch.index_select(x1,dim=0,index=order)
        yy1 = torch.index_select(y1,dim=0,index=order)
        xx2 = torch.index_select(x2,dim=0,index=order)
        yy2 = torch.index_select(y2,dim=0,index=order)

        xx1 = torch.max(xx1,x1[idx])
        yy1 = torch.max(yy1,y1[idx])
        xx2 = torch.min(xx2,x2[idx])
        yy2 = torch.min(yy2,y2[idx])

        w = torch.clamp(xx2 - xx1,min=0)
        h = torch.clamp(yy2 - yy1,min=0)

        # 根据oreder获取预测框的面积
        rem_areas = torch.index_select(area,0,index=order)

        Inter = w * h

        out = rem_areas - Inter + area[idx]

        IOU = Inter / out
        order = order[IOU < threshold]

    return keep


def pytroch_soft_nms(p:torch.tensor,thresh_iou=0.75,
                     thresh_score=0.001,sigma=0.4,method=1):
    '''
      应用soft-nms算法提取出最佳的目标框。
        1. 从P中提取预测框的边界信息和分数;
        2. 计算P中每个预测边界框的面积;
        3. 提取置信度最大的预测边界框，记为S, 添加至keep;
        4. 计算S与P中其他预测边界框T的交并比;
        5. 根据method方法计算新的score, 并更新score, 缩短order的范围(去除已经确定的预测框信息);
        6. 跳转至步骤3,直至遍历所有预测框;
        7. 使用thresh_score筛选出最佳目标框;

    :param p:图片中目标的预测框和置信度，Shape：[num_boxes, 5];
    :param thresh_iou:(float)用于抑制不必要预测框的阈值;
    :param thresh_score:区分最优目标框的置信度阈值;
    :param sigma:soft_nms算法高斯加权的参数;
    :param method:现soft-nms的方法, 0:表示传统的nms;1:表示线性加权;2:表示高斯加权;
    返回值：
    :return:最佳预测框;
    '''
    x1 = p[:,0]
    y1 = p[:,1]
    x2 = p[:,2]
    y2 = p[:,3]

    areas = (x2-x1) * (y2-y1)

    scores = p[:,4]
    keep = []
    scores_cp = scores.clone()
    order = scores_cp.argsort()
    keep_new_score = []  # 存储最佳预测框更新之后的分数

    size = len(order)
    for i in range(size):
        # 3.提取置信度最大的预测框
        # 传统nms算法情况
        if method != 1 and method !=2:
            if len(order) == 0 : break
            S_idx = order[-1]
            keep.append(p[S_idx])
            order = order[:-1]
        else:
            S_idx = order[-1]  # 获取置信度最高的预测框下标
            order = order[:-1]
            keep.append(P[S_idx])  # 把置信度最高的预测框存储到keep中
            keep_new_score.append(scores_cp[S_idx])
        # 4.计算S与P中其他预测边界框T的交并比;
        # 根据下标提取数据组织成新的tensor
        xx1 = torch.index_select(x1, dim=0, index=order)
        xx2 = torch.index_select(x2, dim=0, index=order)
        yy1 = torch.index_select(y1, dim=0, index=order)
        yy2 = torch.index_select(y2, dim=0, index=order)

        # 计算交集的边界框
        xx1 = torch.max(xx1, x1[S_idx])
        yy1 = torch.max(yy1, y1[S_idx])
        xx2 = torch.min(xx2, x2[S_idx])
        yy2 = torch.min(yy2, y2[S_idx])

        # 计算交集的宽、高，注意非重叠部分会是负值，需要设置为0
        w = torch.clamp(xx2 - xx1, min=0.0)
        h = torch.clamp(yy2 - yy1, min=0.0)

        # 计算交集面积 ==> shape: tensor([n-1,1])
        inter = w * h
        rem_areas = torch.index_select(areas, dim=0, index=order)
        # 计算并集面积, shape: tensor([n-1,1])
        union = (rem_areas - inter) + areas[S_idx]
        # 计算 S 与 P中其他预测框的 IoU, shape: tensor([n-1,1])
        IoU = inter / union
        print(IoU)

        if method == 1 or method == 2:
            if method == 1:
                x = torch.ones(len(order)) - IoU
                y = torch.ones(len(order))
                weight = torch.where(IoU>thresh_iou, x, y)
            else:
                weight = torch.exp(-(IoU*IoU)/sigma)

            # 更新score_cp的分数
            num = weight.size()[0]
            for i in range(num):
                scores_cp[order[i]] *= weight[i]
            # print("更新 scope_cp: {}".format(scores_cp))

            # 重新进行排序
            end = len(order)
            order = scores_cp.argsort()

            order = order[0:end]
        else:
            order = order[IoU < thresh_iou]

    # 7.使用thresh_score筛选出最佳目标框
    if method == 1 or method == 2:
        num = len(keep_new_score)
        keep_f = [keep[i] for i in range(num) if keep_new_score[i] > thresh_score]
        return keep_f
    else:
        return keep


array_list =[[0.500, 0.500, 1.0, 1.0, 0.85],
                 [0.615, 0.600, 1.0, 1.0, 0.95],
                 [0.550, 0.375, 1.0, 0.875, 0.75],
                 [0.80, 0.70, 1.0, 1.0, 0.80]]



def a(nums):
    return  nums / 2000

# a = list(map(a,array_list[0]))
# print(a)
P = torch.tensor(array_list)
#
#
keep = pytroch_soft_nms(P, thresh_iou=0.30, thresh_score=0.50, sigma=0.5, method=1)
print(keep)
#
print(nms(P[:, :-1].numpy().reshape(1,-1,4), P[:, -1:].numpy().reshape(1,-1,1), [np.ones(len(array_list))], iou_thr=0.5))

