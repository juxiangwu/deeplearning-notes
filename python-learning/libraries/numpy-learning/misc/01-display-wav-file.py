# -*-coding:utf-8 -*-
# 加载WAV音频文件
import scipy
import matplotlib.pyplot as plt

sample_rate,data = scipy.io.wavfile.read('datas/test.wav')

#plt.subplot(2,1,1)
plt.title('Original')
plt.plot(data)
plt.show()
