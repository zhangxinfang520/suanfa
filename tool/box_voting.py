# -*- coding:utf-8 -*-
#@Time : 2021-04-27 20:23
#@Author: zxf_要努力
#@File : box_voting.py
import numpy as np

def box_voting(top_dets, all_dets, thresh, scoring_method='ID', beta=1.0):
    """Apply bounding-box voting to refine `top_dets` by voting with `all_dets`.
    See: https://arxiv.org/abs/1505.01749. Optional score averaging (not in the
    referenced  paper) can be applied by setting `scoring_method` appropriately.
    """
    # top_dets is [N, 5] each row is [x1 y1 x2 y2, sore]
    # all_dets is [N, 5] each row is [x1 y1 x2 y2, sore]
    top_dets_out = top_dets.copy()
    top_boxes = top_dets[:, :4]
    all_boxes = all_dets[:, :4]
    all_scores = all_dets[:, 4]
    top_to_all_overlaps = bbox_overlaps(top_boxes, all_boxes)
    for k in range(top_dets_out.shape[0]):
        inds_to_vote = np.where(top_to_all_overlaps[k] >= thresh)[0]
        boxes_to_vote = all_boxes[inds_to_vote, :]
        ws = all_scores[inds_to_vote]
        top_dets_out[k, :4] = np.average(boxes_to_vote, axis=0, weights=ws)
        if scoring_method == 'ID':
            # Identity, nothing to do
            pass
        elif scoring_method == 'TEMP_AVG':
            # Average probabilities (considered as P(detected class) vs.
            # P(not the detected class)) after smoothing with a temperature
            # hyperparameter.
            P = np.vstack((ws, 1.0 - ws))
            P_max = np.max(P, axis=0)
            X = np.log(P / P_max)
            X_exp = np.exp(X / beta)
            P_temp = X_exp / np.sum(X_exp, axis=0)
            P_avg = P_temp[0].mean()
            top_dets_out[k, 4] = P_avg
        elif scoring_method == 'AVG':
            # Combine new probs from overlapping boxes
            top_dets_out[k, 4] = ws.mean()
        elif scoring_method == 'IOU_AVG':
            P = ws
            ws = top_to_all_overlaps[k, inds_to_vote]
            P_avg = np.average(P, weights=ws)
            top_dets_out[k, 4] = P_avg
        elif scoring_method == 'GENERALIZED_AVG':
            P_avg = np.mean(ws**beta)**(1.0 / beta)
            top_dets_out[k, 4] = P_avg
        elif scoring_method == 'QUASI_SUM':
            top_dets_out[k, 4] = ws.sum() / float(len(ws))**beta
        else:
            raise NotImplementedError(
                'Unknown scoring method {}'.format(scoring_method)
            )

    return top_dets_out