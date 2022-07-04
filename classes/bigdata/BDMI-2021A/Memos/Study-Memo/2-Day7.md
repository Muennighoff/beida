# 第七天课堂笔记 2021/10/27

## numpy

### 创建数组

```python
# 直接传入数组和元组
d=np.array(((1,2,3),(4,5,6)))
a=np.array([(1,2,3),(4,5,6)])
# range
a=np.arange(4)
b=np.arange(4,8)
# random
a=np.random.random(12)
# 全是 1
a=np.ones(4)
# 全是 0
np.zeros(5)
# 单位矩阵
np.identity(4)
```

### 数组组合

vstack 和 hstack：垂直和水平组合

### 数组属性

.shape 形状、维度
.dtype 数据类型

### 数组运算

```python
np.matmul(a,b) # 矩阵乘法
np.dot(a,b) # 向量点乘
## 以上两者在二维矩阵情况下是等价的
np.sin()
np.sqrt()
.reshape() # 重整
.ravel() # 展开
.transpose() # 转置
```

## pdb 调试

## 人工神经元

通过一组输入的线性组合（带有偏置），再加上一个非线性的变换。

### 非线性函数

1. sigmoid
2. tanh
3. ReLU

```python
def sigmoid(x):
    return 1/(1+exp(-x))

def tanh(x):
    return (exp(x)-exp(-x))/(exp(x)+exp(-x))

def ReLU(x):
    return max(x,0)
```

## 多层神经网络

### 机器学习

#### 监督式机器学习

给定**输入和输出对**，学习映射 f。（也称监督学习）

有标签的样本（数据集）是很重要的。

样本包括**特征和标签**

分为 Train 和 Predict 两个阶段。

#### 迁移学习

从一个学习任务中得到的信息迁移到另一个任务中。

#### 深度学习

多层的神经网络：深度神经网络，深度学习。

属于监督学习的一种。

输入层、隐藏层、输出层，最终使用 softmax 归一化为概率向量。

> Softmax：
> $g(z_m)=\frac{e^{z_m}}{\Sigma_ke^{z_k}}$
