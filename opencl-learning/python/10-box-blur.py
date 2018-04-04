# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function
import numpy as np
import pyopencl as cl
import cv2
from PIL import Image

def RoundUp(groupSize, globalSize):  
    r = globalSize % groupSize;  
    if r == 0:  
        return globalSize
    else:  
        return globalSize + groupSize - r

# 创建Context
# 如果有多个设备，则会提示选择
ctx = cl.create_some_context()
# 创建CommandQueue
queue = cl.CommandQueue(ctx)

mf = cl.mem_flags

# 通过字符串内容编译OpenCL的Program
prg = cl.Program(ctx, """
__kernel void box_blur_filter(__read_only image2d_t input,
                              __write_only image2d_t output){
   
   const sampler_t sampler = CLK_FILTER_NEAREST |
                             CLK_NORMALIZED_COORDS_FALSE |
                             CLK_ADDRESS_CLAMP_TO_EDGE;

   const int2 size = get_image_dim(input);

   int2 coord = (int2)(get_global_id(0),get_global_id(1));
   
   float blurSize =256.0f; 
   float imageWidth = size.x;
   
   float4 sum;
   
   for(int i = 0; i < 40; i++){
      sum += read_imagef(input,sampler, coord + (int2)(0, convert_int((i-20) * blurSize / imageWidth)));
   }
  /*
   for(int i = 0; i < 40; i++){
      sum += read_imagef(input,sampler, coord + (int2)(convert_int((i-20) * blurSize / size.y),0));
   }
   */
   sum = sum / 40;
   
   write_imagef(output,coord,sum);
}
""").build()

# 打开图片文件
src1 = Image.open('temp/images/f2.png')
print(src1.size)
dist = Image.new('RGBA',(640,480),(255,255,255))

# OpenCL处理的图片文件格式RGBA,unit8
imageFormat = cl.ImageFormat(cl.channel_order.RGBA,cl.channel_type.UNSIGNED_INT8)

# 将图片从Host复制到Device
img1 = cl.Image(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR,imageFormat,src1.size,None,src1.tobytes())
output = cl.Image(context=ctx,flags=mf.WRITE_ONLY,format=imageFormat,shape=src1.size)

# 根据图片大小定义WorkSize
localWorkSize = ( 8, 8 )  
globalWorkSize = ( RoundUp(localWorkSize[0], src1.size[0]),  
                    RoundUp(localWorkSize[1], src1.size[1]))
# 执行Kernel
prg.box_blur_filter(queue,globalWorkSize,localWorkSize,img1,output)


buffer = np.zeros(src1.size[0] * src1.size[1] * 4, np.uint8)  
origin = ( 0, 0, 0 )  
region = ( src1.size[0], src1.size[1], 1 )  
# 将处理好的图片从设备复制到HOST 
cl.enqueue_read_image(queue, output,
                        origin, region, buffer).wait()
# 保存图片
dist = Image.frombytes("RGBA",src1.size, buffer.tobytes())
dist.save('temp/images/cl-output.png')
dist.show()