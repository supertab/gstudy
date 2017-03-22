import numpy as np
import os, pickle

with open('vqdict.pkl','rb') as f:
    vqdlist = pickle.load(f)
imgszie = 128
blksize = 8
img = np.zeros((imgszie, imgszie))
lim = imgszie - blksize + 1

nvq = 0

for px in range(0, lim, blksize):
    for py in range(0, lim, blksize):
        vqd = vqdlist[nvq][1]
        vqd = vqd.reshape((blksize, blksize))
        img[px:px+blksize, py:py+blksize] = vqd
        nvq += 1

import matplotlib.pyplot as plt

plt.gray()
plt.imshow(img)
plt.show()


