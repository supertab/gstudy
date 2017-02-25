import numpy as np
from numpy import random as rd
import gen_random_dot as dot

rand_dot= dot.data()
vector_len=len(rand_dot[0]) # 得到向量的长度
k = 3 # 设置k值
scale = 100
m_k = np.array(dot.init_k() )

init_set = []
for i in range(k):
    init_set.append([])

while True:
    # 计算欧式距离, 以欧式距离最大作为聚类原则
    for vec in rand_dot:
        max_num, i = 0
        for (index, m) in enumerate( m_k):
            tmp = np.linalg.norm(vet, m)
            if tmp > max_num:
                max_num = tmp
                i = index
        init_set[i].append(vec)

    # 计算每个集合的中心，与m_k中的每个元素对比，存在差异则更新m_k,不存在差异就判断为收敛
    # 求差，如果差小于一定范围则认为两集合的数据点相同
    if_consive = True
    tmp_m =[]
    for (index, each_set) in enumerate(init_set):
        tmp_m.append( (np.sum(each_set[0:,0])/len(each_set), np.sum(each_set[0:,1])/len(each_set)) )
        tmp_m = np.array(tmp_m)
        distance_x = np.abs(np.sum(tmp_m[0:,0]), np.sum(m_k[0:,0]) )
        distance_y = np.abs(np.sum(tmp_m[0:,1]), np.sum(m_k[0:,1]))
        if distance_x> 1e-4 and distance_y > 1e-4:
            m_k = m
            if_consive = False

    if if_consive: 
        break

m_k = [m_k]
dot.dot_plot( init_set, col='o')
dot.dot_plot( m_k, col='o')

