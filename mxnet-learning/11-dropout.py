#coding:utf-8

from mxnet import ndarray as nd

def dropout(X,drop_probability):
    keep_probability = 1 - drop_probability
    assert 0 <= keep_probability <= 1
    if keep_probability == 0:
        return X.zeros_like()
    # 随机选择一部分该层的输出
    mask = nd.random.uniform(0,1.0,X.shape,ctx=X.context) < keep_probability
    scale = 1 / keep_probability
    return mask * X * scale

A = nd.arange(20).reshape((5,4))
print(dropout(A,1.0))