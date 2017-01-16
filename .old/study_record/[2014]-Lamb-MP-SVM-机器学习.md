- 第一步MP进行去噪，提高数据库的稀疏性？
- 第二步将处理后的信号作为机器学习的输入信号，分别使用ANN和SVM算法来检测缺陷的位置
- 第三步利用输出结果来干嘛

## 有限元仿真
使用ansys，添加白高斯噪声？信噪比SNR=130
使用两个极性相反的zirconate titanate电极(PZT)上下放置？来产生lamb波
使用A0模式对分析缺陷，它对缺陷敏感

使用Matlab “Lamb Toolbox”
[20]-Prego J L 2010 The LAMB toolbox www.mathworks.com/matlabcentral/fileexchange/28367

- lamb wave
在遇到边界或者不连续部分，将会发生模态转变，A0模态会转变成A0和S0的混合模态，A0A0A0, A0S0S0？

## mp字典的选择
通过剩余能量的多少来选择字典，剩余能量越多表示该原子库越好？ 最后选择的是symlet4


## 缺陷分类

ANN：使用matlab Neural Network Toolbox
方法：尺度共扼梯度反向传播训练法？
SVM: 选用不同的核函数分类的效果不同，文中选用的核函数为三次多项式(the third degree polynomial)

- 输入数据为一个12800x2的矩阵，第一列为速度响应，第二列为二进制数（0表示边缘反射，1表示其他），第二列用于后续处理中区别是边缘的反射波还是曲线反射波，输出数据也存在第二列，用来表示是否为边沿反射

## 缺陷检测
- firstly ascertain the reflection from the end ,find out the aeact velocity through that and then select the right mode for determining the damage location
先确定反射波是否是从边沿反射回来的，找出确切的回波，然后选择正确的模式来确定缺陷的位置
- 通常缺陷反射的回波比从边沿反射的回波小很多
- Here, velocity is calculated by ascertaining the reflection of the highest magnitude and then using the initial set of data available, i.e. the distance of the sensor from the edge
文中通过判定最大的反射回波，出现带入初始数据进行计算（如：传感器到薄板边沿的距离）

-MP算法用于去噪，减少非零点，文中输入信号为2000个数据点，经过MP算法后减少到500个点，信号的特征被保留
-  ML（机器学习）ANN,SVM进行分类
- 最后再用MP对ANN，SVM提取的特征进行去噪？？

## 结论
通过使用MP算法，去噪，减少数据点来提高效率
只能检测单个缺陷
