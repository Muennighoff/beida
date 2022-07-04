# WW7 课程总结

## Numpy

- Numpy 用于矩阵运算

- Scipy 科学计数运算，based on numpy

- 创建数组 

  - np.array(tuples,lists,...)

- 数组与scalar的计算

  - 对每一个element做一个运算
  - np.array.reshape(row_num,col_num)

- A * B 对每一个相同坐标的element相乘,输出矩阵

- array.dot(array) 点乘

- 增减算符 Operators += -=

- 数组变形

  - ravel( ) 向量化
  - transpose() 转置

- Others

  - np.zeros() np.ones() 创建全部为0 全部为1的矩阵
  - np.arange(start,end) 创建[start,end) 步长为1 的向量array
  - np.identity() 创建单位方阵
  - np.vstack() np.hstack() 垂直、水平叠加array

- Numpy 调试
  - import pdb pdb.set_trace()
  示例：
```python
import numpy as np
S = np.array((['s','t'],['e','f']))
T = np.arange(4,10).reshape(2,3)
U = np.arange(5,11).reshape(2,3)
product = T*U
product.ravel()
```

## Deep Learning

- 人工神经元
  - 单个人工神经元（Artificial Neuron）
    - input的线性加权求和（加上常数 bias）
    - 经过一个非线性变换（函数f）输出
      - Activation Function：sigmoid（logistic function）、tanh、ReLU
```python
import numpy as np
def sigmoid(x):
    result = 1/(1+np.exp(-x))
    return result
sigmoid(float('inf'))
```
- 布尔运算——以logistic为例
    - 通过adjust weight实现AND OR NOT NAND 等逻辑运算
```python
def logistic(x):
    result = 1/(1+np.exp(-x))
    return result
OR = lambda x1,x2 : round(logistic(x1*20+x2*20-1*10))
print(OR(0,1))
print(OR(0,0))
print(OR(1,1))
```
- 多个神经元的能力
  - e.g. 解决XOR（异或）运算

- 多层神经网络
  - 知识准备
    - stochastic gradient descent...
    - machine learning ——对input进行一种预测
      - 三种范式：
        - 监督学习1: decision tree；监督学习2: neuron network
        - 非监督学习 e.g. PCA
        - 强化学习
      - 数据集
        - training set 数据集的子集、训练模型
        - validation set (part of training set) 验证model的有效性，做model的选择
        - test set 推广能力验证
    - supervised machine learning
      - 需要labeled sample
      - (x,y) -> f，model 就是f的表示方式
      - phase：train & inference
    - 迁移学习 transfer learning
      - 信息从一个机器学习任务迁移到另一个机器学习任务
  - 多层神经网络举例

    - 两层网络结构 XOR
    - 更多层数
      - 存在输入层、隐藏层、输出层
      - Softmax（）——常用的归一化方法
$$
g(z_{m}) = \frac{e^{z_{m}}}{\sum_{k}e^{z_{k}}}
$$
```python
import numpy as np
Softmax = lambda X : [round(np.exp(x)/sum(np.exp(X)),3) for x in X]
Softmax([1,2,3,4,5,6,7,8,9])
```

