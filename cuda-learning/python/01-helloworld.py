# -*- coding:utf-8 -*-

 
import pycuda.autoinit
import pycuda.driver as drv
import numpy as np

from pycuda.compiler import SourceModule

kernel = SourceModule(""" 
    __global__ void multiply_array(float * dest,float * a,float *b){
        const int i = threadIdx.x;
        dest[i] = a[i] * b[i];
    }
""")
multiply_array = kernel.get_function("multiply_array")

a = np.array([1,2,3,4,5,6,7,8,9]).astype(np.float32)
b = np.array([1,2,3,4,5,6,7,8,9]).astype(np.float32)

dest = np.zeros_like(a)

multiply_array(drv.Out(dest),drv.In(a),drv.In(b),block = (9,1,1),grid=(1,1))
print(dest)