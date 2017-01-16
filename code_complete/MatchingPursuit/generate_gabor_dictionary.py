#############################################################
# 功能:
# 生成原子长度为N的 gabor 过完备原子库, 文件名为 data.pickle 保存在当前目录中
# gabor函数:
# Gr(t)=1/sqrt(s) * G((t-u)/s) * cos(vt+w) -- r=(s, u, v, w)
# G(t) = e^(-pi*t^2)
#############################################################

import numpy as np
import pickle

temp=[]
# 参数根据参考文献中数据设置
N=128
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

for j in np.arange(j_min, j_max+1):
    for p in np.arange(p_min, N*2**(-j+1)+1):
        for k in np.arange(k_min, 2**(j+1)+1):
            for i in np.arange(i_min, i_max+1):
                s=a_base**j
                u=p*s*u_base
                v=k*(1.0/s)*v_base
                w=i*w_base
                # t=np.array([i for i in range(0,N)])
                t=np.arange(0,N)
                t=(t-u)/(s*1.0)
                g=(1.0/np.sqrt(s))*np.exp(-np.pi*t*t)*np.cos(v*t+w) # gabor function 离散化
                #print ("raw g: ", g)
                g=g/np.sqrt(np.sum(g*g)) #对向量单位化
                temp.append(g)

print('writing file ...')
with open('data.pickle', 'wb') as f:
    pickle.dump(temp, f)

f.close()
