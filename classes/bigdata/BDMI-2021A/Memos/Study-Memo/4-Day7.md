# DeepLearning Intro

[TOC]

## Intro to Numpy

arrays

```python
import numpy as np
#%%一些numpy的使用
ones = np.ones([2,2])   #生成2x2的矩阵
print(ones)
# ones = ones.reshape(3,3) 
# cannot reshape array of size 4 into shape (3,3)
array = np.arange(9) #0,1,2,3,4,..8
```

Basic calculation:

```python
array_2 = array * 2
print(array,array_2)
array12 = array + array_2
matrix = array.reshape(3,3)
matrix2 = array_2.reshape(3,3)
print('matrix: \n',matrix)
print('matrix2: \n',matrix2)
print('matrix x matrix2: \n',matrix*matrix2) # 注意数组四则运算都是对应元素进行
#线性代数相乘应当使用dot
print('matrix.dot( matrix2 ): \n',matrix.dot(matrix2))
print('matrix @ matrix2: \n',matrix@matrix2)
```

Vstack and hstack

```python
#%%关于vstack和hstack
array1 = np.array((1,2,3))
array2 = np.array((4,5,6))
print(  np.vstack( (array1,array2) )  ) #上下叠起来
print(  np.hstack( (array1,array2) )  ) #左右拼起来
#%% 关于print f的用法
name = "Andrew"
print(f'myname is {name}')
```

## Intro to Tensorflow

三个基础激活函数：

```python
import numpy as np
#%% Functions
#激活函数
def sigmoid(x):
    return 1/(1+np.exp(-x))

def tanh(x):
    return (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))

def ReLU(x):
    return max(x,0)
```

人工神经元

```python
def ReLUCell(x,a):
    return ReLU(x@a)

def LogisticCell(x,a):
    return sigmoid(x@a)
```

逻辑门的实现：

```python
def NOT(x):
    weight = np.array([-20])
    bias = 10
    return ReLUCell(x, weight) +bias
print(NOT(np.array([10])))
```

## Supervised Machine Learning

### Definition

在给定输入和输出对(x,y)的情况下，监督学习学习映射f（或给定输入x时输出y的概率分布）

特点：根据训练集中样本进行学习，并推断新的实例。

### Steps

监督学习分为训练train和推断inference两部分。

### DeepLearning

* 神经网络方法属于监督学习
* 多层神经网络称为深度神经网络
* 深度神经网络又称为深度学习

