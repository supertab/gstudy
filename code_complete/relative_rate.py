# -*- coding: utf-8 -*- 
import numpy as np
import matplotlib.pyplot as plt
## 测试正弦信号能否被恢复
# 正弦函数构造的字典：
# 振幅：a(1,5) 频率：f(0.1, 10) 相位：pha(-pi,pi)
#################################################
# 计算相关比
# 实验记录:
# 思考：原始信号已经完全被噪声淹没的一段信号，与完全由噪声组成的一段信号如何区别它们？
# 回答：他们之间肯定是存在区别的，一个例子：假如我一个人在一个小镇里，周围的人都是讲的当地的方言，因此即使人们在我耳边交谈我也不会产生什么反应，因为我听不懂他们的方言。这时从人群里传来熟悉的声音，普通话！即使这个声音比其他声音小的多但是我还是能够听清其中的内容。这是为什么呢？哦～因为我从小就学习普通话，我的大脑中已经建立了普通话这种语言的记忆区，所以当我听到普通话的时候我能够识别它。  
# 其中方言对于我来说就是完全噪声，方言中含有普通话就是噪声与有用信号混合信号。在现实生活中我们可以识别第二类信号。现在有没有一种方法让机器能够区分完全噪声信号和混合信号？
# 类比人可以识别普通话，是因为我们学过普通话，因此让机器能够识别信号的前提使机器进行学习生成原子库或字典。
# 经过学习后需要通过相应的方法建立信号与字典之间的联系，就像人学会普通话后通过大脑中神经元之间的联系让我听懂普通话，因此在机器上也需要一种方法来建立信号与字典之间的联系
# 
# 我的方法：
# 得到原子库的方法：K-SVD算法
# 原子库和信号之间的联系：MP算法 
#
# 
# 1.计算了输入信号与原子库
#
#
#
#################################################

###
# global pi=np.pi

def select(signal, a_min, a_max, f_min, f_max, pha_min, pha_max):
    N=len(signal)
    signal_len=np.sqrt(np.sum(signal*signal))
    relative_rate=0
    print ('signal_length:', signal_len)
    c=0
    proj=0
    (amplitude, freq, phase)=(0, 0, 0)
    for a in np.arange(a_min, a_max, 1):
        for f in np.arange(f_min, f_max, 0.1):
            for p in np.arange(pha_min, pha_max, 0.1):
                t=np.arange(0, 2, 0.005)
                g=a*np.sin(2*np.pi*f*t+p)
                g=g/np.sqrt(np.sum(g*g))
                proj_tmp=np.sum(signal*g)
                
                if abs(proj_tmp) > abs(proj):
                    proj = proj_tmp
                    amplitude, freq, phase = a, f, p
                    
                r_tmp=abs(proj_tmp)/(1.0*signal_len)    
                if r_tmp > relative_rate:
                    relative_rate=r_tmp
                #c+=1
    #print("times: ",c)
    return (proj, relative_rate, amplitude, freq, phase)

a, f, p = 1, 1.7, 0.3*np.pi
print ('parameters of original signal:',a,f,p)
sup = 2 # 范围上限

# generate noise
peek=10
noise=[peek*np.random.random() for x in np.arange(0,sup,0.01)]
noise_neg=[-peek*np.random.random() for x in np.arange(0,sup,0.01)]
noise[len(noise):len(noise)]=noise_neg # 噪声信号
np.random.shuffle(noise)
noise=np.array(noise)
print ('max of noise:', max(noise))

t=np.arange(0, sup, 0.005)
signal=a*np.sin(2*np.pi*f*t+p) # 干净信号

signal_noise=signal+noise # 掺噪信号

data=signal_noise#重构信号选择：signal，signal_noise, noise

lenth_of_signal=np.sqrt(np.sum(data*data))
print ('length of input signal:',lenth_of_signal)

# set parameter
a_min, a_max=1, 5
f_min, f_max=0.1, 10
pha_min, pha_max=(-np.pi, np.pi)
# select best atom

(proj, relative_rate, amplitude,\
freq, phase)=select(data, a_min, a_max, f_min, f_max, pha_min, pha_max)
# print('parameter:', amplitude, freq, phase)
print ('the max relative rate is:', relative_rate)
#re_signal=amplitude*np.sin(2*np.pi*freq*t+phase)
#lenth_of_signal2=np.sqrt(np.sum(re_signal*re_signal))
#print(lenth_of_signal2)

#reconstruct signal
g=amplitude*np.sin(2*np.pi*freq*t+phase)
#print('init:',g)
g=g/np.sqrt(np.sum(g*g))
signal_recon=proj*g
lenth_of_signal3=np.sqrt(np.sum(signal_recon*signal_recon))
print ('length of reconstruct signal:',lenth_of_signal3)
err = signal-signal_recon
print ('max error:', max(err))

# plt.subplot(221) 
# plt.plot(signal[0:150]) # 干净信号
# plt.subplot(222)
# plt.plot(data[0:150]) # 待处理信号
# plt.subplot(223)
# plt.plot(signal_recon[0:150]) #重构信号
# plt.subplot(224)
# plt.plot(err[0:150])
# plt.show()


