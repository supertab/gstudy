import numpy as np
import numpy.linalg as linalg
import mahotas as mh
import matplotlib.pyplot as plt
from scipy.sparse import coo_matrix

# 使用im2col的一个原因：
# 经过im2col后矩阵中每列的长度由窗口决定，而不是输入图像本身决定
# 因此字典中每个原子的长度只要与窗口的长度符合就行了
def im2col_sliding_strided(A, BSZ, stepsize=1):
    # Parameters
    # A 转入矩阵，BSZ: 窗的大小
    # 窗口按行滑动，每个小窗内的数据，按行拼接后作为新矩阵的列
    # bug: stepsize不等于1的时候结果不符合预期
    m,n = A.shape
    s0, s1 = A.strides    
    nrows = m-BSZ[0]+1
    ncols = n-BSZ[1]+1
    shp = BSZ[0],BSZ[1],nrows,ncols
    strd = s0,s1,s0,s1
    out_view = np.lib.stride_tricks.as_strided(A, shape=shp, strides=strd)
    return out_view.reshape(BSZ[0]*BSZ[1],-1)[:,::stepsize]


def construct_image(im_size,blocks, bb):
    # 重构图像
    # genrate pos of every pixes by Image and blocks
    x_lim = im_size[0] - bb
    y_lim = im_size[1] - bb
    # padding
    recon_image = np.zeros(im_size)
    weight = np.zeros(im_size)
    col= 0
    for x_pos in range(x_lim+1):
        # for y_pos,each_block in zip(range(y_lim+1), blocks): # lead Error
        for y_pos in range(y_lim+1):
            # padding block
            recon_image[x_pos:x_pos+bb, y_pos:y_pos+bb] += blocks[:,col].reshape((bb,bb))
            # record weight
            weight[x_pos:x_pos+bb, y_pos:y_pos+bb] += np.ones((bb,bb))
            col += 1
    return recon_image / weight


'''
#test split and construct_image
sizeA = (4,8)
A = np.arange(32).reshape((4,8))
bb = (2,2)
blocks = im2col_sliding_strided(A, bb)
B = construct_image(sizeA, blocks, bb[0])
'''

def GenDCT(bb ,Pn=16):
    dct = np.zeros((bb,Pn))
    bb = np.arange(bb)
    for k in range(Pn):
        V = np.cos(bb*k*np.pi/Pn)
        if k>0:
            V = V-np.mean(V)
        dct[:,k] = V/linalg.norm(V)
        DCT= np.kron(dct,dct)
    return DCT


'''
D - dictionary(normalized)
X - signals to represent
L - the max number of coefficients for each signal
'''
def MP(D,X,L):
# n: the length of very vector
# P: the number of vector in X
# K: the number of vector in D
    x_shape = X.shape
    if len(x_shape) > 1:
        n, P = x_shape
    else:
        n, P = x_shape[0], 1
    K = D.shape[1]
    # 系数矩阵，行数等于D中向量的个数，列数等于X中向量的个数
    A = np.zeros((K, P))
    D_T = D.T

    for k in range(P):
        indx = []
        cofficient = []
        x = X[:,k]
        residual = x
        for j in range(L):
            proj = np.dot(D_T, residual)
            # get max lenth of project and pos
            if abs(proj.min()) >= abs(proj.max()):
                maxL = proj.min()
            else:
                maxL = proj.max()
            pos = np.where(proj==maxL)[0]
            indx.append(pos.tolist()[0]) # array.tolist()转array为数组
            cofficient.append(maxL)
            # bug: D[:,indx[0:j+1]]会出现3个维度，原因是indx里面是array型数据
            x_reconstruct = np.dot(D[:,indx[0:j+1]],np.array( cofficient))
            residual = x - x_reconstruct
            if (residual**2).sum() < 1e-6:
                break
        
        # 将系数存入系数矩阵A中
        for i,j in zip(indx,cofficient):
            A[i][k] = j # k为信号矩阵的第k个向量
    return A

def SparseCodeing(im, block_size, codebook):
    blocks = im2col_sliding_strided(im, [block_size,block_size])
    iter_accout = 2
    Coef = MP(codebook, blocks, iter_accout)
    return Coef

def Decode(coef, im_size, block_size, codebook):
    blocks = np.dot(codebook, coef)
    im = construct_image(im_size, blocks, block_size)
    return im

im = mh.imread('lena200.jpg')
# 转化为灰度图
im= mh.colors.rgb2gray(im)
bb = 8 # 方形窗口[bb,bb]
codebook = GenDCT(bb)
coeff = SparseCodeing(im, bb, codebook)
sparse_coef = coo_matrix(coeff) # compress sparse matrix by scipy.sparse's function
recovery_im = Decode(coeff, im.shape, bb, codebook)
plt.gray()
plt.imshow(recovery_im)
plt.show()
