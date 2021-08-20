# -*- coding:utf-8 -*-
#@Time : 2021-07-25 11:21
#@Author: zxf_要努力
#@File : SGD.py
'''实现随机梯度下降'''


'''
Batch Gradient Descent（BGD，批量梯度下降）
Stochastic Gradient Descent（SGD，随机梯度下降）
Mini-Batch Gradient Descent（MBGD，小批量梯度下降）
Moment Gradient Descent（MGD，动量梯度下降）
Adaptive Gradient Descent（AdaGrad，自适应梯度下降，2011）
Adaptive Delta Gradient Descent（AdaDelta，自适应调整梯度下降, 2012）
Root Mean Square Prop（RMSProp，均方根支撑， 2012）
Nesterov Accelerated Gradient Descent（NAG，Nesterov加速梯度下降，2013）
Adaptive Moment Estimation（Adam，自适应矩估计，2014）
Adaptive Moment Estimation Max（AdaMax, 2015）
Nesterov Adaptive Moment Estimation（Nadam，Nesterov加速自适应矩估计，2016）
Adam & RMSProp Gradient Descent (AMSGrad, 2018)

'''
import numpy as np

#全批量梯度下降
class BatchGradientDescent:
    def __init__(self,eta=0.01,n_iter=10000,tolerance=0.0001):
        self.eta = eta
        self.n_iter = n_iter
        self.tolerance = tolerance

    def fit(self,X,y):
        '''

        :param X: [N,dimmension] N 代表 样本数量 dimension 代表特征维度
        :param y: 真实值 [N]
        :return:
        '''
        n_samples = len(X)
        '''
        np.r_是按列连接两个矩阵，就是把两矩阵上下相加，要求列数相等。
        np.c_是按行连接两个矩阵，就是把两矩阵左右相加，要求行数相等。
        '''
        X = np.c_[np.ones(n_samples),X] # 增加 截距项 目前明白为什么放前面 X [N,1+dimension]
        n_features = X.shape[-1]

        self.theta = np.ones(n_features) #[1+dimension] 未知数个数
        self.loss_ = [0.]

        self.i = 0
        while self.i < self.n_iter:
            self.i +=1
            errors = X.dot(self.theta) - y #误差[N，1]
            loss = 1/(2 * n_samples) * errors.dot(errors) #损失 [1]
            delta_loss = loss - self.loss_[-1] #两次更新间的误差
            self.loss_.append(loss)

            if np.abs(delta_loss) < self.tolerance:
                break
            else:
                #这里偏置为1 乘不乘结果都一样
                gradient = 1 / n_samples * X.T.dot(errors) #更新参数 [dimension,N] * [N，1]
                self.theta -= self.eta * gradient
        return self


#随机梯度下降
class StohasticGradientDescent(BatchGradientDescent):
    def __init__(self,shuffle=True,random_state=None):
        self.shuffle = shuffle
        if random_state:
            np.random.seed(random_state)
        super(StohasticGradientDescent, self).__init__()

    def fit(self, X, y):
        X = np.c_[np.ones(len(X)),X]
        n_samples, n_features = X.shape
        self.theta = np.ones(n_features)
        self.loss_ = [0]

        self.i = 0
        while self.i < self.n_iter:
            self.i +=1
            if self.shuffle:
                X,y = self._shuffle(X,y)
            errors = []
            for xi,yi in zip(X,y):
                error_i = xi.dot(self.theta) - yi
                errors.append(error_i ** 2)
                gradient_i = xi.T.dot(error_i)#单个样本梯度
                self.theta -= self.eta * gradient_i

                loss = 1/2 * np.mean(errors)
                delta_loss = loss - self.loss_[-1]
                self.loss_.append(loss)
                if np.abs(delta_loss) < self.tolerance:
                    break
        return self


    @staticmethod
    def _shuffle(X,y):
        '''np.random.permutation()：随机排列序列'''
        location = np.random.permutation(len(y))
        return X[location], y[location]


class MiniBatchGradientDescent(StohasticGradientDescent):
    def __init__(self,batch_size=2):
        self.batch_size = batch_size
        super(MiniBatchGradientDescent, self).__init__()

    def fit(self, X, y):
        X = np.c_[np.ones(len(X)),X]
        n_samples,n_features = X.shape

        self.theta = np.ones(n_features)
        self.loss_ = [0.]

        self.i = 0
        while  self.i < self.n_iter:
            self.i +=1
            if self.shuffle:
                X, y = self._shuffle(X,y)
            errors = []
            for j in range(0, n_samples, self.batch_size):
                mini_X,mini_y = X[j:j+self.batch_size], y[j: j+self.batch_size]
                error_mini = mini_X.dot(self.theta) - mini_y
                errors.append(error_mini.dot(error_mini))
                mini_gradient = 1 / self.batch_size * mini_X.T.dot(error_mini)
                self.theta -= self.eta * mini_gradient
            loss = 1 / (2 * self.batch_size) * np.mean(errors)
            delta_loss = loss - self.loss_[-1]
            self.loss_.append(loss)

            if np.abs(delta_loss) < self.tolerance:
                break

        return self


class MomentumGradientDense(MiniBatchGradientDescent):

    def __init__(self,gamma=0.9):
        self.gamma = gamma
        super(MomentumGradientDense, self).__init__()

    def fit(self,X,y):
        X = np.c_[np.ones(len(X)),X]
        n_samples,n_features = X.shape

        self.theta = np.ones(n_features)
        self.velocity = np.zeros_like(self.theta)
        self.loss_ = [0]

        self.i = 0
        while self.i < self.n_iter:
            self.i +=1
            if self.shuffle:
                X,y = self._shuffle(X,y)

            errors = []
            for j in range(0, n_samples, self.batch_size):
                mini_X,mini_y = X[j : j+self.batch_size], y[j:j+self.batch_size]
                error = mini_X.dot(self.theta) - mini_y
                errors.append(error.dot(error))
                mini_gradient = 1/ self.batch_size * mini_X.T.dot(error)
                self.velocity = self.velocity * self.gamma + self.eta * mini_gradient
                self.theta -= self.velocity

            loss = 1 / (2*self.batch_size) * np.mean(errors)
            # print(loss)
            delta_loss = loss - self.loss_[-1]
            self.loss_.append(loss)

            if np.abs(delta_loss) < self.tolerance:
                break
        return self
'''
MomentumGradientDense 动量梯度下降是利用历史情况对当前状态进行纠偏，防止过度反应；
而Nesterov加速下降则依赖于先见之明，对未来的走势进行预判，在事情发生前便进行了内部调整，避免出现极端情况
'''
class NesterovAccelerateGradint(MomentumGradientDense):
    def __init__(self):
        super(NesterovAccelerateGradint, self).__init__()

    def fit(self,X,y):
        X = np.c_[np.ones(len(X)),X]
        n_samples,n_features = X.shape

        self.theta = np.zeros(n_features)
        self.velocity = np.zeros_like(self.theta)

        self.loss_ = [0]
        self.i = 0
        while self.i < self.n_iter:
            self.i += 1
            if self.shuffle:
                X, y = self._shuffle(X, y)
            errors = []
            for j in range(0,n_samples,self.batch_size):
                mini_X, mini_y = X[j:j+self.batch_size], y[j:j+self.batch_size]
                #迭代公式
                error = mini_X.dot(self.theta-self.gamma*self.velocity) - mini_y
                errors.append(error.dot(error))
                mini_gradents = 1 / self.batch_size * mini_X.T.dot(error)
                self.velocity = self.velocity * self.gamma + self.eta * mini_gradents
                self.theta -= self.velocity
            loss = 1/(2*self.batch_size) * np.mean(errors)
            delta_loss = loss - self.loss_[-1]
            if np.abs(delta_loss) <self.tolerance:
                break
        return self
#自适应梯度下降算法
class AdaptiveGradientDescent(MiniBatchGradientDescent):
    '''
    自适应梯度下降法通过将学习率除以历史梯度值平方和的平方根得到新的学习率从而来优化程序的迭代
    学习率需为正值且其调整依赖于梯度值，这个梯度值的构成可以是历史梯度值的简单平均抑或是指数加权移动平均。
    '''
    def __init__(self,eta,n_iter,epsilon=1e-6):
        self.epsilon = epsilon
        self.eta = eta
        self.n_iter = n_iter
        super(AdaptiveGradientDescent, self).__init__()

    def fit(self, X, y):
        X = np.c_[np.ones(len(X)), X]
        n_samples, n_features = X.shape
        self.theta = np.ones(n_features)
        self.loss_ = [0.]

        gradient_sum = np.zeros(n_features)
        self.i = 0
        while  self.i <  self.n_iter:
            self.i += 1
            if self.shuffle:
                X,y = self._shuffle(X,y)
            errors = []
            for j in range(0,n_samples,self.batch_size):
                mini_X , mini_y = X[j:j+self.batch_size], y[j:j+self.batch_size]

                error = mini_X.dot(self.theta) - mini_y
                errors.append(error.dot(error))
                mini_gradent = 1 / self.batch_size * mini_X.T.dot(error)
                '''
                如果最优解需要很多次迭代，随着迭代次数的不断增加，历史梯度的平方和的平方根会越来越大，
                导致学习率会逐渐收缩到无穷小，大大降低了程序后期的运行效率
                '''
                gradient_sum += mini_gradent ** 2
                adj_gradient = mini_gradent / (np.sqrt(gradient_sum + self.epsilon))
                self.theta -= self.eta * adj_gradient

            loss = 1/(2* self.batch_size) * np.mean(errors)

            #print(loss)
            delta_loss = loss - self.loss_[-1]

            self.loss_.append(loss)
            if np.abs(delta_loss) < self.tolerance:
                break
        return self

'''
AdaDelta主要的特性在于其虽然考虑了历史的梯度值，
但其通过对历史梯度的平方进行指数加权移动平均来减缓梯度的累积效应，
进而达到了减缓学习率收缩的速度；同时，其引入了一个作用类似于动量的成分来代替原始的超参数学习率 eta ，
状态变量的自适应性加快了收敛速度
'''

class  AdaDelta(MiniBatchGradientDescent):

    def __init__(self,gamma=0.95,epsilon=1e-6):
        self.gamma = gamma
        self.epsilon = epsilon
        super(AdaDelta, self).__init__()

    def fit(self,X,y):
        X = np.c_[np.ones(len(X)),X]
        n_samples,n_features = X.shape
        self.theta = np.ones(n_features)
        self.loss_  = [0.]

        gradient_exp = np.zeros(n_features)
        delta_theta_exp = np.zeros(n_features)

        self.i = 0
        while  self.i < self.n_iter :
            self.i += 1
            if self.shuffle:
                X, y = self._shuffle(X, y)
            errors = []
            for j in range(0,n_samples,self.batch_size):
                mini_X,mini_y = X[j:j+self.batch_size], y[j:j+self.batch_size]
                error = mini_X.dot(self.theta) - mini_y
                errors.append(error.dot(error))
                mini_gradient = 1 / self.batch_size * mini_X.T.dot(error)
                gradient_exp = self.gamma * gradient_exp + (1-self.gamma) * mini_gradient ** 2
                gradient_rms = np.sqrt(gradient_exp + self.epsilon)

                delta_theta = -np.sqrt(delta_theta_exp + self.epsilon) / gradient_rms * mini_gradient
                delta_theta_exp = self.gamma * delta_theta_exp + (1-self.gamma) * delta_theta ** 2
                delta_theta_rms = np.sqrt(delta_theta_exp + self.epsilon)
                delta_theta = - delta_theta_rms / gradient_rms * mini_gradient

                self.theta += delta_theta
            loss = 1/ (2*self.batch_size)* np.mean(errors)
            delta_loss = loss - self.loss_[-1]
            self.loss_.append(loss)
            if np.abs(delta_loss) <self.tolerance:
                break
        return  self

'''
RMSProp的提出也是为了对AdaGrad进行改进，防止学习速率过快的衰减。区别于AdaGrad对历史所有梯度的平方进行累加，
RMSProp采用了对历史梯度的平方和进行指数加权移动，来减缓梯度的累积效应，而其与AdaDelta的差异仅仅在于未对学习率进行变动。
'''
class RMSProp(MiniBatchGradientDescent):
    def __init__(self,gamma=0.9,epsilon=1e-6):
        self.gamma = gamma
        self.epsilon = epsilon
        super(RMSProp, self).__init__()

    def fit(self,X,y):
        X = np.c_[np.ones(len(X)),X]
        n_samples, n_features = X.shape
        self.theta = np.ones(n_features)
        self.loss_ = [0.]

        gradient_exp = np.zeros(n_features)
        self.i = 0
        while  self.i < self.n_iter:
            self.i +=1
            if self.shuffle:
                X, y = self._shuffle(X, y)
            errors = []

            for i in range(0,n_samples,self.batch_size):
                mini_X, mini_y = X[i:i+self.batch_size], y[i:i+self.batch_size]
                error = mini_X.dot(self.theta) - mini_y
                errors.append(error.dot(error))
                mini_gradient = 1 / self.batch_size * mini_X.T.dot(error)
                gradient_exp = self.gamma * gradient_exp + (1-self.gamma)* mini_gradient ** 2
                gradient_rms = np.sqrt(gradient_exp +self.epsilon)
                self.theta -= self.eta / gradient_rms * mini_gradient
            loss = 1/ (2*self.batch_size) * np.mean(errors)
            delta_loss = loss - self.loss_[-1]
            self.loss_.append(loss)
            if np.abs(delta_loss) < self.tolerance:
                break
        return  self


class Adam(MiniBatchGradientDescent):
    def __init__(self,beta_1=0.9,beta_2=0.999,epsilon=1e-6):
        self.beta_1 = beta_1
        self.beta_2 = beta_2
        self.epsilon = epsilon
        self.eta = 10
        self.n_iter = 100
        super(Adam, self).__init__()

    def fit(self, X, y):
        X = np.c_[np.ones(len(X)), X]
        n_sampels, n_features = X.shape
        self.theta = np.ones(n_features)
        self.loss_ = [0.]

        m_t = np.zeros(n_features)
        v_t = np.zeros(n_features)
        self.i = 0
        while  self.i < self.n_iter:
            self.i +=1
            if self.shuffle:
                X, y = self._shuffle(X, y)
            errors = []
            for j in range(0,n_sampels,self.batch_size):
                mini_X,mini_y = X[j:j+self.batch_size], y[j:j+self.batch_size]
                error = mini_X.dot(self.theta) - mini_y
                errors.append(error.dot(error))
                mini_gradient = 1/self.batch_size * mini_X.T.dot(error)
                m_t = self.beta_1 * m_t + (1 - self.beta_1) * mini_gradient
                v_t = self.beta_2 * v_t + (1 - self.beta_2) * mini_gradient ** 2
                # m_t_hat = m_t / (1 - self.beta_1 ** self.i)
                # v_t_hat = v_t / (1 - self.beta_2 ** self.i )
                m_t_hat = m_t / (1 - self.beta_1 )
                v_t_hat = v_t / (1 - self.beta_2 )
                self.theta  -=self.eta / (np.sqrt(v_t_hat) + self.epsilon) * m_t_hat
            loss = 1 / (2* self.batch_size) * np.mean(errors)
            #print(loss)
            delta_loss = loss - self.loss_[-1]
            self.loss_.append(loss)
            if np.abs(delta_loss) < self.tolerance:
                break
        return self






if __name__ == '__main__':
    X = np.asarray([[2],
                    [3],
                    [1],
                    [10]])
    y = np.asarray([4.1,
                    6.1,
                    2.1,
                    20.1])
    # X = np.random.randn(4,2)
    # y = np.random.randn(4)
    print("梯度下降", BatchGradientDescent().fit(X, y).theta)
    print("小批度梯度下降",MiniBatchGradientDescent(2).fit(X, y).theta)
    print("随机梯度下降",StohasticGradientDescent().fit(X, y).theta)
    print("带动能的梯度下降", MomentumGradientDense().fit(X, y).theta)
    print("Nes带动能的梯度下降", NesterovAccelerateGradint().fit(X, y).theta)
    print("自适应梯度下降", AdaptiveGradientDescent(0.1,200000).fit(X, y).theta)
    print("AdaDelta自适应梯度下降", AdaDelta().fit(X, y).theta)
    print("RMSProp自适应梯度下降", RMSProp().fit(X, y).theta)
    print("adam自适应梯度下降", Adam().fit(X, y).theta)







