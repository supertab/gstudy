## orthogonal matching pursuit 正交匹配追踪
匹配追踪所的到的信号残差与当前所选出的原子正交，但不能满足与之前所选出的原子正交，这就导致了残差在后续匹配的过程中有可能再次选择之前已经选择过的原子
OMP方法就是寻找一种方法使得残差与所选原子库中的每个原子都正交，再将这个残差进行继续匹配投影
对比MP算法：
MP算法在选出一个原子后，使用信号在该原子上的投影长度作为原子的系数，每次迭代得到一个原子和它对应的系数，各个原子系数之间没有关联.
OMP算法在选出一个原子后，不再使用投影长度作为原子系数，而是根据之前所选择的原子更新所有原子系数
