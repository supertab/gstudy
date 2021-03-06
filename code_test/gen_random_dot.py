# idea:
# 旧：先在给定范围的区间中生成k个随机点（随机点之间的距离大于r）- 计算速度不确定
# 在给定范围内，根据r计算符合的中心点，中心点的选值固定
# 形成k个以随机点为中心，r为半径的小区域，小区域中随机投入n个点
import numpy as np
from numpy import random as rd

def init_k(k=3, scale=100, r=25):
    # 生成中心点
    x_range = range(0,scale,2)
    y_range = range(0,scale,2)
    dot_set = [ (x ,y) for x in x_range for y in y_range]#
    # dot_set = []
    # for x in x_range:
        # for y in y_range:
            # dot_set.append((x,y))

    temp_dot_set = dot_set.copy()
    k_pos = []
    while len(temp_dot_set)>k:
        ok = True
        c_flag = False
        i_c= rd.choice(range(len(temp_dot_set)), k, replace=False)
        center_set=[temp_dot_set[i] for i in i_c]
        temp = center_set.copy()
        while len(temp):
            center = temp.pop()
            for dot in temp:
                if np.linalg.norm(np.array(center) - np.array(dot))< r:
                    c_flag = True
                    for i in center_set:
                        temp_dot_set.remove(i)
                    break
            if c_flag:
                ok = False
                break
        if ok:
            return  center_set 

def data( k=3, n=100, r=25):
    scale =100
    k_pos = init_k(k, scale)
    s_k=[]
    for i in range(k):
        s_k.append([])
    for (index, pos) in enumerate( k_pos):
        for i in range(n):
            while True:
                x, y = r*rd.random(2)
                if x**2+y**2 < r**2:
                    s_k[index].append((x+pos[0], y+pos[1]))
                    break

    return [np.array(i) for i in s_k]

def dot_plot( result, col='ro'):
    # 形式：[ array((a,b),...,), array((a2,b2),...) ]
    import matplotlib.pyplot as plt
    plt.axis([0,120,0,120])
    k = len(result)
    for x in range(k):
        plt.plot(result[x][0:,0],result[x][0:,1], col)
    plt.show()
