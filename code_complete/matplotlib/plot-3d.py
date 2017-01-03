from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
pi = np.pi
t = np.linspace(-pi, pi, 100)
z = np.cos(t)
y = np.linspace(0,20, 40)
# y2为100行y的2darray,z2为40列z的2d-array
y2, z2 = np.meshgrid(y, z)
y2, t2 = np.meshgrid(y, t)
# y2, t2, z2 = np.meshgrid(y, t, z) 
# 添加画布，子图
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# rstride:从x轴上看线条的稀疏度， cstride从y轴看
ax.plot_wireframe(t2, y2, z2, rstride=5, cstride=2)
# 设置坐标轴
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()


