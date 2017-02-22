MSE(mean squared error) 均方差

sectionII: 稀疏表示的最常见方法
在字典库已经存在的情况下,选择原子

寻找伪逆？
最好的表示信号：用最少的原子，最精确的表示信号
ksvd: 寻找一个字典，对集合中的没个信号都能有最好的表示

基追踪BP：凸优化，用l1泛数替换l0泛数
FOCUSS:
MAP:
k

## PART3 现有的字典设计方法
- 泛化的k-means
稀疏表示看作是泛化的VQ
因此可以借鉴k-means算法来生成学习字典
从整体来看，字典的设计和k-means的步骤相同：
第一步：在字典中选择合适的因子（初步选择）-稀疏编码
第二步：更新这些因子

- 最大似然法（maximum likelihood methods)
- MOD(Method of Optimal Directions)
提供了一种简便的更新字典的方法
上面两种方法使用了二次型更新字典, 这两种方法都需要对字典中的每列进行单位化
- MAP( Maximum A-posteriori Probability Approach) 后验法？
- Unions of orthogonal bases


