MOD: 一种字典训练算法
## 算法
1. 初始化字典F0, 大小NxK， N与输入的向量的长度一致，K远大于N; 设置用于表示向量的原子数目m（即OMP算法的迭代次数，OMP每次迭代一次就从字典中选出一个原子），初始化计数器i
2. 用选出的原子组合，得到逼近向量x'和残差r=x-x'
3. 通过x'和r调整字典F0->F'
**论文重点：**调整字典的方法：目标是减小r，通过公式推导，得到调整系数
4. 使用新字典F'来表示向量x，如果不满足停止条件，则跳转到第3步, 计数器i+1
停止条件：可以是设定迭代次数，或者当MSE基本不变的时候停止


