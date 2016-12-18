## mp自适应分解的应用
去噪，波形的参数估计，特征提取

## 字典库
Gaussian and chirplet dictionaries, 高斯字典适合分解对称信号，chirplet字典能够分解非对称信号, （这里的高斯字典就是gabor字典）

## 处理lamb波
在mp算法中选择chirplet字典，应用在lamb上，可以得到chirp rate，通过chirp rate可以识别lamb波的模态A0还是S0


## 时频分析方法
- 短时傅立叶变换（STFT）
通过窗函数来得到时频图，即在一段时间内做傅立叶变换，分段傅立叶变换来得到时频图，STFT的窗函数是固定的，因此它时频图的没段的时间宽度相同
如果使用的是高斯窗STFT就变成了Gabor变换
- 其他的方法论文未介绍

## gabor原子库与chirplet原子库
- gabor库
原子为实函数,给出了离散化方案，方便编程。参数三元组（s，u，w）分别为尺度scaling，传播translating，调制modulating因子。对应sin函数就是：s为振幅，u为时间，w为频率
还有一个相位因子phi，可以选为0
缺点：只能处理对称信号（什么是对称信号）

- chirplet库
为复函数，没有给出离散化方案（还是不能离散化？）在gabor函数的基础上增加了c(chirp rate)参数
使用Matlab的LASTWAVE库
可以处理非对称信号（如何处理）
