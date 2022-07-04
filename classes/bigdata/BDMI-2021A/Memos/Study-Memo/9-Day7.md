# 第7次课笔记
课后作业：读《机器学习实战》1-4、10章。

# 1 Python numpy
numpy和scipy

## 1.1 使用array创建数组：
```python
import numpy as np
c = np.array([[1,2,3],[4,5,6]])
```
array可以接受序列，tuples，还可以用dtype = 来设置数据的类型（例如整形，复数等等）

## 1.2 算术运算
### 1.2.1 数组和标量的运算：
```python
import numpy as np
a = np.arange(4)
#a = [0,1,2,3]
a + 4
#array([4,5,6,7])
a*2
#array([0,2,4,6])
b = np.arange(4,8)
#b = array([4,5,6,7])
a + b
#array([4,6,8,10])
a*b
#array([0,5,12,21])
```

### 1.2.2 数组和函数的运算：
```python
a*np.sin(b)
a*np.sqrt(b)
```

### 1.2.3 矩阵乘积：
```python
A = np.arange(0,9).reshape(3,3)
B = np.ones((3,3))
#A = array([[0,1,2],[3,4,5],[6,7,8]])
#B = array([[1,1,1],[1,1,1],[1,1,1]])
A*B#仅仅得到各同位置元素相乘的结果

#np.dot可以实现矩阵的代数相乘。要保证A矩阵的列数等于B矩阵的行数。
np.dot(A,B)
```

### 1.2.4 数组变形：
```python
a.reshape(3,4)
a.shape = (3,4)
a.reval()
a.transpose()
```

## 1.3 pdb调试代码
```python
import pdb
pdb.set_trace()
```

# 2 Deep learning

## 2.1 深度学习1：人工神经元

单个神经元的能力：进行二元分类，模拟布尔运算。

### 2.1.1 单个人工神经元（Artificial Neuron）
对一组数组的线性加权叠加，做非线性变换后，进行输出
$$
y=f(\sum^N_{i=1}W_ix_i+b)
$$
画图时，把求和\sum、函数f操作写到一起，写作F。
有哪些函数？

**激活函数**
sigmoid函数、tanh函数、ReLU函数等等

**最简单的神经元：整流线性单元-RuLU单元**
eg：
y = max(0, -0.21\*x1 + 0.3\*x2 + 0.7\*x3)
F = ReLU(y)
代码：
```python
def ReLU(x):
    if x > 0:
        return x
    else:
        return 0

def ReLU_cell(x):
    w = array([-0.21, 0.3. 0.7])
    return ReLU(np.dot(x,w))
#print(ReLU_cell([1,0,1]))
```

### 2.1.2 布尔运算
布尔运算是计算机的基础能力。
与（AND）、或（OR）、非（NOT）、与非（NAND）、异或（XOR）

逻辑斯提回归单元是最常用的。因为输出的范围是[0, 1]，可以表示一个二元概率。
**如何用逻辑斯提回归单元来模拟布尔运算？**
取不同的权重和偏置即可：
```python
import numpy as np
def sigmoid(x):
    return 1/(1+np.exp(-x))

def And(x):
    w = [20,20]
    b = -30
    return sigmoid(np.dot(x,w)+b)

x = np.array([[0,0],[0,1],[1,0],[1,1]])
print("And:")
for i in range(4):
    print(And(x[i]))

def Or(x):
    w = [20,20]
    b = -10
    return sigmoid(np.dot(x,w)+b)
print("Or:")
for i in range(4):
    print(Or(x[i]))

def Not(x):
    w = -20
    b = 10
    return sigmoid(x*w+b)
print("Not:")
print(Not(0))
print(Not(1))

def NAND(x):
    w = [-20,-20]
    b = 30
    return sigmoid(np.dot(x,w)+b)
print("NAND:")
for i in range(4):
    print(NAND(x[i]))

def XOR(x):#需要两层结构
    w = [20,20]
    b = -30
    x1 = Or(x)
    x2 = NAND(x)
    return sigmoid(x1*w[0]+x2*w[1]+b)
print("XOR:")
for i in range(4):
    print(XOR(x[i]))
```

## 2.2 深度学习2：多层神经网络
模拟布尔运算、解决异或问题等等。。
多层神经网络，最简单的就是两层网络。能做什么？
eg：用三个神经元，两层网络，解决异或问题。

**机器学习：根据输入数据构建（训练）预测模型**
**数据集：**
训练集：用于训练模型
验证集：从训练集分离而来，用于验证学习效果
测试集：用于在模型经由验证集的初步验证之后，来测试模型
**应用：**
分类任务（Classification）、预测任务（regression）

**监督式机器学习（supervised machine learnin）**
学习方法：给定输入、输出对（x,y），学习映射f。
训练数据集由样本组成，每个样本上都有对应的标签（label），用来指导学习过程。
两个阶段：训练（train）、推断（inference）。

**深度学习：**
即深度神经网络，又称多层神经网络。
而神经网络方法，属于监督学习的一种。

**更多层数的深度神经网络：**
输入层（输入数据集的特征）、隐藏层（有神经元）、输出层（有神经元）

**softmax处理：概率向量归一化**
```python
import numpy as np
def softmax(x):
    return(np.exp(x)/np.sum(np.exp(x)))
print(softmax([1,2,3,4,5,6,7,8,9]))
```
