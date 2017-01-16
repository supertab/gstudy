# -*- coding: utf-8 -*- 
import numpy as np
import matplotlib.pyplot as plt
## 测试正弦信号能否被恢复
# 正弦函数构造的字典：
# 振幅：a(1,5) 频率：f(0.1, 10) 相位：pha(-pi,pi)
#################################################
# 实验记录：
# 1.采集的信号长度越大，重构精度越高
# 2.选出的最佳原子的频率能够对应上，峰值和相位不能对应
# 之间的误差很大，经过重建后的结果和原信号的误差不大。
# 3.对于最佳原子与重建信号之间的关系还需要理解
#################################################

###
# global pi=np.pi

def select(signal, a_min, a_max, f_min, f_max, pha_min, pha_max):
    N=len(signal)
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
                    
                #c+=1
    #print("times: ",c)
    return (proj, amplitude, freq, phase)

a, f, p = 3, 3.7, 0.3*np.pi
print('原信号参数:',a,f,p)  
sup = 2 # 范围上限

# generate noise
peek=5
noise=[peek*np.random.random() for x in np.arange(0,sup,0.01)]
noise_neg=[-peek*np.random.random() for x in np.arange(0,sup,0.01)]
noise[len(noise):len(noise)]=noise_neg # 噪声信号
np.random.shuffle(noise)
noise=np.array(noise)
print('噪声最大值:', max(noise))

t=np.arange(0, sup, 0.005)
signal=a*np.sin(2*np.pi*f*t+p) # 干净信号

signal_noise=signal+noise # 掺噪信号

data=signal_noise #重构信号选择：signal，signal_noise, noise

lenth_of_signal=np.sqrt(np.sum(data*data))
print('输入信号长度:',lenth_of_signal)

# set parameter
a_min, a_max=1, 5
f_min, f_max=0.1, 10
pha_min, pha_max=(-np.pi, np.pi)
# select best atom

(proj, amplitude, freq, phase)=select(data, a_min, a_max, f_min, f_max, pha_min, pha_max)
print('最佳原子参数:', amplitude, freq, phase)

#re_signal=amplitude*np.sin(2*np.pi*freq*t+phase)
#lenth_of_signal2=np.sqrt(np.sum(re_signal*re_signal))
#print(lenth_of_signal2)

#reconstruct signal
g=amplitude*np.sin(2*np.pi*freq*t+phase)
#print('init:',g)
g=g/np.sqrt(np.sum(g*g))
signal_recon=proj*g
lenth_of_signal3=np.sqrt(np.sum(signal_recon*signal_recon))
print('重构信号长度:',lenth_of_signal3)
err = signal-signal_recon
print('误差最大值:', max(err))

plt.subplot(221) 
plt.plot(signal[0:150]) # 干净信号
plt.subplot(222)
plt.plot(data[0:150]) # 待处理信号
plt.subplot(223)
plt.plot(signal_recon[0:150]) #重构信号
plt.subplot(224)
plt.plot(err[0:150])
plt.show()


