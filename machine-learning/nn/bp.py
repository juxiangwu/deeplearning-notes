# -*- coding:utf-8 -*-

'''
BP算法实现
'''

import numpy as np
import math

#定义数据文件读取函数
def LoadFile(filename):
    data=sio.loadmat(filename)
    data=data[filename[0:-4]]
    return data

#定义Sigmoid函数
def get(x):
    act_vec=[]
    for i in x:
        act_vec.append(1/(1+math.exp(-i)))
    act_vec=np.array(act_vec)
    return act_vec

#训练BP神经网络
def TrainNetwork(sample,label):
    sample_num = len(sample)
    sample_len = len(sample[0])
    out_num = 10
    hid_num = 8
    w1 = 0.2 * np.random.random((sample_len, hid_num)) - 0.1
    w2 = 0.2 * np.random.random((hid_num, out_num)) - 0.1
    hid_offset = np.zeros(hid_num)
    out_offset = np.zeros(out_num)
    input_learnrate = 0.2
    hid_learnrate = 0.2
    for i in range(0,len(sample)):
        t_label=np.zeros(out_num)
        t_label[label[i]]=1
        #前向的过程
        hid_value=np.dot(sample[i],w1)+hid_offset #隐层的输入            
        hid_act=get(hid_value)                 #隐层对应的输出                                 
        out_value=np.dot(hid_act,w2)+out_offset
        out_act=get(out_value)    #输出层最后的输出                                 

        #后向过程
        err=t_label-out_act
        out_delta=err*out_act*(1-out_act) #输出层的方向梯度方向                         
        hid_delta = hid_act*(1 - hid_act) * np.dot(w2, out_delta)   
        for j in range(0,out_num):
            w2[:,j]+=hid_learnrate*out_delta[j]*hid_act
        for k in range(0,hid_num):
            w1[:,k]+=input_learnrate*hid_delta[k]*sample[i]

        out_offset += hid_learnrate * out_delta   #阈值的更新                    
        hid_offset += input_learnrate * hid_delta

    return w1,w2,hid_offset,out_offset

#测试过程
def Test():
    train_sample=LoadFile('mnist_train.mat')
    train_sample=train_sample/256.0
    train_label=LoadFile('mnist_train_labels.mat')
    test_sample=LoadFile('mnist_test.mat')
    test_sample=test_sample/256.0
    test_label=LoadFile('mnist_test_labels.mat')
    w1,w2,hid_offset,out_offset=TrainNetwork(train_sample,train_label)
    right = np.zeros(10)
    numbers = np.zeros(10)
    for i in test_label:
        numbers[i]+=1
    print(numbers)
    for i in range(0,len(test_label)):
        hid_value=np.dot(test_sample[i],w1)+hid_offset     
        hid_act=get(hid_value)                             
        out_value=np.dot(hid_act,w2)+out_offset            
        out_act=get(out_value)                             
        if np.argmax(out_act) == test_label[i]:            
          right[test_label[i]] += 1
    print(right.sum()/ len(test_label))

if __name__ == '__main__':
    Test()