# -*- coding:utf-8 -*-
#@Time : 2021-04-11 15:51
#@Author: zxf_要努力
#@File : TestNMS.py
from ensemble_boxes import  *
import numpy as np


boxes_list = [[
    [0.00, 0.51, 0.81, 0.91],
    [0.10, 0.31, 0.71, 0.61],
    [0.01, 0.32, 0.83, 0.93],
    [0.02, 0.53, 0.11, 0.94],
    [0.03, 0.24, 0.12, 0.35],
],[
    [0.04, 0.56, 0.84, 0.92],
    [0.12, 0.33, 0.72, 0.64],
    [0.38, 0.66, 0.79, 0.95],
    [0.08, 0.49, 0.21, 0.89],
]]

scores_list = [[0.9, 0.8, 0.2, 0.4, 0.7], [0.5, 0.8, 0.7, 0.3,0.2]]
labels_list = [[0, 1, 0, 1, 1], [1, 1, 1, 0]]
weights = [2, 1]



iou_thr = 0.5
skip_box_thr = 0.0001
sigma = 0.1

def single_nms(bboxes,scores,thresh=0.5):
    print(bboxes.size)


    x1 = bboxes[:,0]
    y1 = bboxes[:,1]
    x2 = bboxes[:,2]
    y2 = bboxes[:,3]
    area = (x2-x1+1) * (y2-y1+1)
    order = scores.argsort()
    order = order[::-1]

    keep = []
    while order.size > 0:
        if order.size == 1:
            i = order[0]
            keep.append(i)
            break
        else:
            i = order[0]
            keep.append(i)
        xx1 = np.maximum(x1[i],x1[order[1:]])
        yy1 = np.maximum(y1[i],y1[order[1:]])
        xx2 = np.minimum(x2[i],x2[order[1:]])
        yy2 = np.minimum(y2[i],y2[order[1:]])

        w = np.maximum(0,xx2-xx1+1)
        h = np.maximum(0,yy2-yy1+1)

        inter = w * h

        iou = inter/area[i]+area[order[1:]]+inter
        ids = np.where(iou<thresh)[0]
        if ids.size == 0:
            break
        order = order[ids+1]
    return keep


print(single_nms(bboxes=np.asarray(boxes_list[0]), scores=np.asarray(scores_list[1])))

boxes, scores, labels = nms(boxes_list, scores_list, labels_list, weights=weights, iou_thr=iou_thr)
print(scores)
# print("--------------------")
# boxes, scores, labels = soft_nms(boxes_list, scores_list, labels_list, weights=weights, iou_thr=iou_thr, sigma=sigma, thresh=skip_box_thr)
# print(scores)
# print("--------------------")
# boxes, scores, labels = non_maximum_weighted(boxes_list, scores_list, labels_list, weights=weights, iou_thr=iou_thr, skip_box_thr=skip_box_thr)
# print(scores)
# print("--------------------")
# boxes, scores, labels = weighted_boxes_fusion(boxes_list, scores_list, labels_list, weights=weights, iou_thr=iou_thr, skip_box_thr=skip_box_thr)
# print(scores)
# print("--------------------")