#-*-coding:utf-8-*-

import pycuda.autoinit
import pycuda.driver as cuda
import numpy as np
from pycuda.compiler import SourceModule

a = np.asarray([
    [1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]
])
a = a.astype(np.float32)

a_gpu = cuda.mem_alloc(a.nbytes)

# 从主机复制数据到设备
cuda.memcpy_htod(a_gpu,a)

# kernel 函数
mod = SourceModule('''
    __global__ void doublify(float *a)
  {
    int idx = threadIdx.x + threadIdx.y*4;
    a[idx] *= 2;
  }
''')

func = mod.get_function('doublify')

# 执行 kernel函数
func(a_gpu,block=(4,4,1))

a_doubled = np.empty_like(a)
# 从设备复制数据到Host
cuda.memcpy_dtoh(a_doubled, a_gpu)
print(a)
print(a_doubled)

# 快捷方式复制数据
func(cuda.InOut(a), block=(4, 4, 1))
print(a)