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
__kernel void brazil_filter(__read_only image2d_t input,
                              __write_only image2d_t output){
   
   const sampler_t sampler = CLK_FILTER_NEAREST |
                             CLK_NORMALIZED_COORDS_FALSE |
                             CLK_ADDRESS_CLAMP_TO_EDGE;

   const int2 size = get_image_dim(input);

   int2 coord = (int2)(get_global_id(0),get_global_id(1));
   
   float4 src_rgba = read_imagef(input,sampler,coord);
   
   float xBlockSize = 0.01*0.1;
   float yBlockSize = xBlockSize * size.x / size.y;  // mutiply ratio
   float xCoord = (floor((coord.x-0.5)/xBlockSize)+0.5) * xBlockSize+0.5;
   float yCoord = (floor((coord.y-0.5)/yBlockSize)+0.5) * yBlockSize+0.5;
   float arg = 0.5f;
   
   float4 color = read_imagef(input,sampler,convert_int2((float2)(xCoord,yCoord)));
   color = (float4)(color.xyz+arg * 2.0f - 1.0f, color.w);
   
    float sum = (color.x + color.y + color.z) / 3.0f;

    float3 white  = (float3)(255.0f, 255.0f, 255.0f) / 255.0f;
    float3 yellow = (float3)(242.0f, 252.0f,   0.0f) / 255.0f;
    float3 green  = (float3)(  0.0f, 140.0f,   0.0f) / 255.0f;
    float3 brown  = (float3)( 48.0f,  19.0f,   6.0f) / 255.0f;
    float3 black  = (float3)(  0.0f,   0.0f,   0.0f) / 255.0f;

    if      (sum < 0.110f) color = (float4)(black,  color.w);
    else if (sum < 0.310f) color = (float4)(brown,  color.w);
    else if (sum < 0.513f) color = (float4)(green,  color.w);
    else if (sum < 0.965f) color = (float4)(yellow, color.w);
    else                  color = (float4)(white,  color.w);
   
  write_imagef(output,coord,color);
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
prg.brazil_filter(queue,globalWorkSize,localWorkSize,img1,output)


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