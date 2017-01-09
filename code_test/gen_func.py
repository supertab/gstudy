# reference: http://www.jianshu.com/p/992f8a4671e6
# np.mod(x, y) => x%y
# np.where(condition, x, y) => [xv if c else yv for(c, xv, yv) in zip(condition, xv, yv)

# 函数功能：
# 产生周期，相位可调的三角

import numpy as np
import matplotlib.pyplot as plt
def triangle_wave(x, t, phase=0):
    '''产生幅值(-1,1), t在采样范围中的三角波, phase:相位，t=0时的值，相位与周期有关'''
    y = np.where(np.mod(x-phase,t)<t/2, -4/t*(np.mod(x-phase, t))+1, 0)
    y = np.where(np.mod(x-phase,t)>=t/2, 4/t*(np.mod(x-phase, t))-3, y)
    return y


# test

# data = triangle_wave(np.linspace(0, 5, 200), 2, 0.7) # 
# plt.plot(x, data)
# plt.show()
