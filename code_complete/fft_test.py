# fft测试
# 画频谱图：幅频图和相频图
# 使用matplot画竖线图

# numpy知识点
# numpy中取得复数的实部和虚部
# 快速过滤： arr[abs(arr)<0.0001]=0-1j 


import matplotlib.pyplot as plt
import numpy as np

Fs = 200.0  # sampling rate
Ts = 1.0/Fs # sampling interval
ff = 5      # frequency of the signal

# t = np.linspace(0,1,Fs) # time vectori #使用linspace时幅频图出现小的波动
t = np.arange(0,1, Ts)

#frequency ff=5
# y = np.sin(2*np.pi*ff*t)+5*np.sin(2*np.pi*2*ff*t)+3*np.cos(2*np.pi*22*t)
# 加入相位
y = np.sin(2*np.pi*ff*t+ np.pi/6)+5*np.sin(2*np.pi*2*ff*t)+3*np.cos(2*np.pi*22*t)

#set frequency
n = len(y) # length of the signal
k = np.arange(n)
frq = k[range(n//2)] # one side frequency range

# Y = np.fft.fft(y) # 不做normaliztion幅值将放大为采样点数的1/2倍
Y = np.fft.fft(y)/(n/2.0) # fft computing and normalization
Y = Y[range(n//2)]

amplitude=abs(Y) # 获得幅值

threshold = 0.005 # 过滤极小值点的阈值

# 得到有用数据的索引
'''
x_vline=[]
for i, data in enumerate(amplitude):
    if data>0.0001:
        x_vline.append(i)
'''
# 使用列表推导式代替上面几行
x_vline=[i for (i, data) in enumerate(amplitude) if data > threshold]
y_amp=amplitude[x_vline]
# Y.real 得到实部，一个array; Y.imag 得到虚部，一个array
y_pha=np.arctan(-Y[x_vline].real/Y[x_vline].imag) # 获得相位
# 过滤相位中的极小值点
y_pha[abs(y_pha)<threshold]=0

# 绘图
fig=plt.figure()
ax1=fig.add_subplot(311)
ax2=fig.add_subplot(312)
ax3=fig.add_subplot(313)
fig.subplots_adjust(hspace=0.4) # 设置子图的间距

x_lim=(0,100)       # 横轴的范围即为频率范围
ax2.set_xlim(x_lim) # 设置横轴的范围
ax3.set_xlim(x_lim)
ax1.plot(t,y)
ax2.plot(x_vline, y_amp, 'ro') # 幅频图
ax2.vlines(x_vline, [0], y_amp)
ax3.plot(x_vline, y_pha, 'ro') # 相频图
ax3.vlines(x_vline, [0], y_pha)
ax1.set_xlabel('t')
ax1.set_ylabel('|Amplitude|')
ax2.set_xlabel('Frequence')
ax2.set_ylabel('|Amplitude|')
ax3.set_xlabel('Frequence')
ax3.set_ylabel('Phase')
plt.show()

# ax1.set_xlabel('Time')
# ax1.set_ylabel('Amplitude')
# fig, ax = plt.subplots(2, 1)
# ax[0].set_xlabel('Time')
# ax[0].set_ylabel('Amplitude')
# ax[0].plot(t,y)
# ax[1].set_xlabel('Freq (Hz)')
# ax[1].set_ylabel('|Y(freq)|')
# ax[1].plot(frq, amplitude, 'r') # plotting the spectrum
# ax[1].acorr(amplitude)
# ax[2].plot(frq, phase, 'r')

