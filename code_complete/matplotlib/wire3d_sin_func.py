# x,y,z都是二维数组
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(211, projection='3d')
X, Y, Z = axes3d.get_test_data(0.05)

ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

xt = np.linspace(1,10,10) 
yt = np.linspace(-np.pi, np.pi,50)
zt = np.sin(yt)
x, y = np.meshgrid(xt, yt)
x, z = np.meshgrid(xt, zt)
ax2 = fig.add_subplot(212, projection='3d')
ax2.plot_wireframe(x, y, z, rstride=5)

# fig2=plt.figure()
# atx = fig2.add_subplot(131)
# aty = fig2.add_subplot(132)
# atz = fig2.add_subplot(133)
# atx.plot(X)
# aty.plot(Y)
# atz.plot(Z)

plt.show()
