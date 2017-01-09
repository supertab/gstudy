# -.- coding=utf8 -.-
import numpy as np
import matplotlib.pyplot as plt
import read_csv


def select_best(signal_r, N, a_base, j_min, j_max, u_base,\
        p_min, v_base, k_min, w_base, i_min, i_max):
    proj_trans=0
    proj=0
    size_dic=0
    for j in np.arange(j_min, j_max+1):
        for p in np.arange(p_min, N*2**(-j+1)+1):
            for k in np.arange(k_min, 2**(j+1)+1):
                for i in np.arange(i_min, i_max+1):
                    size_dic+=1
                    s=a_base**j
                    u=p*s*u_base
                    v=k*(1.0/s)*v_base
                    w=i*w_base
                    # t=np.array([i for i in range(0,N)])
                    t=np.arange(0,N)
                    t=(t-u)/(s*1.0)
                    g=(1.0/np.sqrt(s))*np.exp(-np.pi*t*t)*np.cos(v*t+w) # garbor function 离散化
                    #print ("raw g: ", g)
                    g=g/np.sqrt(np.sum(g*g)) #对向量单位化
                    proj_trans=np.sum(signal_r*g) #做内积(残差在向量上投影)
                    #print ("i:", i, "proj_trans:", proj_trans)
                    # 比较投影的长度，选出投影长度最大的原子，更新参数
                    # (scale, translation, freq, phase)
                    if np.abs(proj_trans)>np.abs(proj):
                        proj=proj_trans
                        scale=s
                        translation=u
                        freq=v
                        phase=w
    #print("size_dic: ",size_dic)
    #print("in func:",proj, scale, translation, freq, phase)
    return (proj, scale, translation, freq, phase)

# data=generate_rand(64)
tmp = read_csv.convert_csv('F0002CH1.CSV')
data =np.array( tmp[700:900])
energy_all = np.sum(np.sqrt(data*data))
iter_num= 2
N=len(data)
signal_reconstruct= np.zeros(N)
signal_r= data.copy()
# initialize
# 参数根据参考文献中数据设置
a_base=2.0
j_min=0
j_max=np.log2(N)
u_base=1.0/2
p_min=0
v_base=np.pi
k_min=0
w_base=np.pi/6.0
i_min=0
i_max=12
# set
for n in range(0, iter_num):
    # 得到最佳原子及在该原子上的投影
    (proj, scale, translation, freq, phase)=select_best(signal_r,\
            N, a_base, j_min, j_max, u_base, p_min, v_base,\
            k_min, w_base, i_min, i_max)
    print("in main:",proj, scale, translation, freq, phase)
    # t=np.array([i for i in range(0,N)])
    t=np.arange(0, N)
    t=(t-translation)/scale
    g=(1.0/np.sqrt(scale))*np.exp(-np.pi*t*t)*np.cos(freq*t+phase)
    # print ("raw g: ", g)
    g=g/np.sqrt(np.sum(g*g))
    # print ("unit g: ", g)
    # set
    signal_reconstruct+=proj*g
    signal_r-=proj*g
    print('iterate time:', n, 'remained energy:', np.sum(np.sqrt(signal_r*signal_r)), 'total energy:', energy_all)

#plt.plot(data)
plt.subplot(221)
plt.plot(data)
plt.subplot(222)
plt.plot(g)
plt.subplot(223)
plt.plot(signal_r)
plt.subplot(224)
plt.plot(signal_reconstruct)
plt.show()

