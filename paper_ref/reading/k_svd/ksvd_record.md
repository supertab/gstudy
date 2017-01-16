## 一些稀疏模型??
* Principal-Component-Analysis
* Anisotropic diffusion
* Markov Random Field
* Wienner Filtering
* **DCT(discrete cosine trains) and JPEG**: jpeg格式的图片就是使用了离散余弦变换
* **Wavelet and JPEG-2000** jpeg2000是小波变换在图像压缩中的应用
* Picec-Wise-Smooth
* C2-smoothness
* Besov-Space
* Total-Variation
* Beltrami-Flow

稀疏信号：信号中只有少数非零值，类似于原子，原子的能量全部集中在原子核中

- 为什么能够使用稀疏分解处理信号？
因为信号具有一定的内部结构，而噪声不具备这些结构，因此通过特定的原子库可以保留有用信号去除噪声

## 困难与解决方法
2. 给出一个信号，如何从原子库中找出最合适的一组原子来表示信号？
原子库中不同原子的排列组合过于庞大
栗子：从2000个原子的库中选择15个原子共有2.4e37种可能，从这些原子中找出最佳原子是不可能的
**解决方法:** 使用近似算法,解需要足够的稀疏
1. 记录了许多信号，如何从这些信号中得到原子库
**解决方法:** 使用k-svd学习字典
