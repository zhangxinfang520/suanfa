# -*- coding:utf-8 -*-
#@Time : 2021/9/2 11:44
#@Author: zxf_要努力
#@File : AUC.py
import numpy as np

from sklearn.metrics import roc_curve
from sklearn.metrics import auc

def auc_calculate(labels,pred):
    pos = [i for i in range(len(labels)) if labels[i] == 1]
    neg = [i for i in range(len(labels)) if labels[i] == 0]

    auc = 0
    for i in pos:
        for j in neg:
            if pred[i] >pred[j]:
                auc +=1
            elif pred[i] == pred[j]:
                auc +=0.5
    return auc / (len(pos)*len(neg))

if __name__ == '__main__':
    label = [1,0,0,0,1,0,1,0]
    pre = [0.9, 0.8, 0.3, 0.1, 0.4, 0.9, 0.66, 0.7]
    print(auc_calculate(label,pre))
    fpr,tpr,th = roc_curve(label, pre,pos_label=1)
    print(auc(fpr, tpr))
    