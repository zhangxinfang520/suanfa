# -*- coding:utf-8 -*-
#@Time : 2021-06-07 14:44
#@Author: zxf_要努力
#@File : Gradual warmup.py
from  torch.optim.lr_scheduler import _LRScheduler

class GradualWarmupScheduler(_LRScheduler):

    def __init__(self,optimizer,multiplier,total_epoch,after_scheduler=None):
        """

        :param optimizer: Wrapped optimizer.
        :param multiplier: target learning rate = base lr * multiplier
        :param total_epoch: target learning rate is reached at total_epoch, gradually
        :param after_scheduler: after target_epoch, use this scheduler(eg. ReduceLROnPlateau)

        """
        self.multiplier = multiplier
        if self.multiplier <=1:
            raise ValueError("multiplier should be greater than 1.")
        self.total_epoch = total_epoch
        self.after_scheduler = after_scheduler
        self.finished = False
        super(GradualWarmupScheduler, self).__init__()

    def get_lr(self):
        if self.last_epoch > self.total_epoch:
            if self.after_scheduler:
                if not self.finished:
                    self.after_scheduler.base_lrs = [base_lr * self.multiplier for base_lr in self.base_lrs]
                    self.finished =True
                return self.after_scheduler.get_lr()
            return [base_lr * self.multiplier  for base_lr in self.base_lrs]
        return [base_lr * ((self.multiplier - 1.) * self.last_epoch / self.total_epoch + 1.) for base_lr in self.base_lrs]

    def step(self,epoch=None):
        if self.finished and self.after_scheduler:
            return self.after_scheduler.step(epoch)
        else:
            return super(GradualWarmupScheduler, self).step(epoch)
