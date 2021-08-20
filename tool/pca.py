import numpy as np
from sklearn.decomposition import PCA as sk_PCA

class PCA(object):
    def __init__(self,n_components=3):
        self.n_components = n_components
        self.mean = None
        self.v_components = None
        self.explained_variance_ratio_ = None

    def fit(self, w):
        self.mean = w.mean(axis=0)
        mean_x = w - self.mean
        # np.linalg.svd 对矩阵mean_x 进行奇异值分解
        # np.linalg.svd(a,full_matrices=1,compute_uv=1)。
        # a 是一个形如(M,N)矩阵
        #full_matrices的取值是为0或者1，默认值为1，这时u的大小为(M,M)，v的大小为(N,N) 。
        # 否则u的大小为(M,K)，v的大小为(K,N) ，K=min(M,N)
        #compute_uv的取值是为0或者1，默认值为1，表示计算u,s,v。为0的时候只计算s。
        #返回值 u大小为(M,M)，s大小为(M,N)，v大小为(N,N)。  A = u*s*v
        # 其中s是对矩阵a的奇异值分解。s除了对角元素不为0，其他元素都为0，并且对角元素从大到小排列。
        # s中有n个奇异值，一般排在后面的比较接近0，所以仅保留比较大的r个奇异值
        u, s, v = np.linalg.svd(mean_x,full_matrices=False)
        self.v_components = v[:self.n_components]

        ratios = []
        s_sum = np.dot(s,s)
        for i in range(self.n_components):
            ratio = np.dot(s[i],s[i]) / s_sum
            ratios.append(ratio)
        self.explained_variance_ratio_ = np.array(ratios)

    def transform(self,x):
         mean_x = x - self.mean
         return np.dot(mean_x,self.v_components.T)

    def fit_transform(self,x):
        self.fit(x)
        return self.transform(x)

    @staticmethod
    def eig_transform(x):
        mean_x = x - x.mean(axis=0)
        a = np.dot(mean_x.T,mean_x)
        #numpy.linalg.eig() 计算方形矩阵的特征值和特征向量
        # w,v = numpy.linalg.eig(a)  计算方形矩阵a的特征值和右特征向量
        # w: 多个特征值组成的一个矢量。备注：多个特征值并没有按特定的次序排列。特征值中可能包含复数。
        # v: 多个特征向量组成的一个矩阵。每一个特征向量都被归一化了。第i列的特征向量v[:,i]对应第i个特征值w[i]。
        w, v = np.linalg.eig(a)
        z = np.dot(mean_x, v)
        return z

if __name__ == '__main__':
    np.random.seed(12)
    np.set_printoptions(precision=6, suppress=True, linewidth=120)
    data = np.random.random((6, 5))
    python_PCA = PCA(n_components=5)
    sk_PCA_reduction = sk_PCA(n_components=0.95)
    sk_PCA_all = sk_PCA(n_components=5)
    x = np.array(data)
    sk_reduction_out = sk_PCA_reduction.fit_transform(x)
    sk_all_out = sk_PCA_all.fit_transform(x)

    python_svg_out = python_PCA.fit_transform(x)
    python_eig_out = python_PCA.eig_transform(x)

    print("sklearn_reduction")
    print(sk_reduction_out)
    print("sklearn_all")
    print(sk_all_out)
    print("vanilla_svg")
    print(python_svg_out)
    print("python_eig")
    print(python_eig_out)
    print("sklearn_reduction_ratio")
    print(sk_PCA_reduction.explained_variance_ratio_)
    print("sklearn_all_ratio")
    print(sk_PCA_all.explained_variance_ratio_)
    print("python_all_ratio")
    print(python_PCA.explained_variance_ratio_)



