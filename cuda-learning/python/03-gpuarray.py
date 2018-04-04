# -*-coding:utf-8 -*-

import pycuda.gpuarray as gpuarray
import pycuda.driver as cuda
import pycuda.autoinit
import numpy

a = numpy.asarray([
    [1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]
])

# 将数据复制到设备
a_gpu = gpuarray.to_gpu(a.astype(numpy.float32))
# 执行kernel并将数据复制到主机
a_doubled = (2*a_gpu).get()
print (a_doubled)
print (a_gpu)