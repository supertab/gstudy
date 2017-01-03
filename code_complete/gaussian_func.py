import numpy as np
import matplotlib.pyplot as plt
import time

def gaussian_func(a, T):
    '''a为窗函数的宽度，T为中轴的位置'''
    t = np.arange(1000)
    return np.exp(-a*((t-T)**2)/2)

a=0.01
for i in np.arange(0,1000,200):
    plt.plot( gaussian_func(a, i) )
plt.show()
