#########################################
# 说明：
# 在混合信号中添加白噪声后恢复信号
#########################################

import numpy as np
import matplotlib.pyplot as plt
import multi_signal as signal

sampling_count = 1024
t, db_sin = signal.Signal(sampling_count).sine_db()
t, noise = signal.Signal(sampling_count).white_noise(amplitude=6)
y1=np.sin(2*np.pi*2*t+np.pi/3)
y2=np.sin(2*np.pi*5*t+np.pi/6)
y = y1+y2+noise
y_rem =y

y_result = []
for n in range(2):
    proj, index = 0, 0 # initialize the projection
    for i, vec in enumerate(db_sin):
        temp = np.sum(y_rem * vec)
        proj, index = (temp, i) if temp>proj else (proj, index)

    y_cons =  proj * db_sin[index] 
    y_rem = y_rem-y_cons
    y_result.append(y_cons)

# 使用向量的长度表示重构误差
get_error= lambda y0, y1 : np.sqrt( np.sum((y0-y1)*(y0-y1)))
err1 = get_error(y1, y_result[0])
err2 = get_error(y2, y_result[1])
print( 'err1: %s, err2: %s'%(err1, err2) )

f, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2,3, sharex='col')
f.subplots_adjust(wspace=0.4, hspace=0.2)
ax1.set_title('y1(1, 2, pi/3)')
ax1.plot(t, y1)
ax2.set_title('y2(1, 5, pi/6)')
ax2.plot(t, y2)
ax3.set_title('y1+y2+noise')
ax3.plot(t, y)
ax4.set_title('y1_construct')
# ax4.axis([0, 1.2, -3, 3])
ax4.plot(t, y_result[0])
ax5.set_title('y2_construct')
ax5.plot(t, y_result[1])
ax6.set_title('remained signal')
ax6.plot(t, y_rem)

# 定义画图函数
# plot y1 y3 y y_result y_rem
def my_plot(x, y, title='fig', layout=111):
    plt.subplot(layout)
    plt.title(title)
    plt.plot(x, y)

plt.show()
