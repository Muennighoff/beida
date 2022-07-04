# 第8次课笔记
# 1 Python Pandas学习
一维数据结构：Series。其索引为index。
调用方法：
```python
import pandas as pd
import numpy as np
#初始化这个Series
s = pd.Series(np.random.randn(5),index = ["a","b","c","d","e"])
#如果缺省index，则自动设置为0、1、2、3、4
print(s)
print(s+s)
print(s*2)
print(s[1:]+s[:-1])#切片操作
```
二维数据结构：DataFrame
```python
#初始化
d = {'one': pd.Series([1.,2.,3.],index = ['a','b','c']),'two':pd.Series([1.,2.,3.,4.], index = ['a','b','c','d'])}
df = pd.DataFrame(d)
print(df)
print(df.index)#读取行指标
print(df.columns)#读取列指标

#去字典中寻找在相应index、columns的值，找不到的值为NaN：
pd.DataFrame(d, index = ['d','b','a'], columns = ['two','three'])

#列查找
df["one"]

#查找行指标index，结果可以返回这个行指标对应的元素的列指标、元素本身
df.loc['a']

#时间序列
dates = pd.date_range('20211103',periods=6)
dates
df_data = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
```

# 2 TensorFlow2学习

一个小练习网站：
http://playground.tensorflow.org/
学习率过大引起震荡，学习率过小收敛太慢。

## 2.1深度神经网络的基础概念

### 2.1.1 什么是机器学习？

**机器学习**，是根据输入数据，来构建（训练）预测模型的。主要有三种范式：监督学习、非监督学习、强化学习。机器学习一般处理两种任务：分类任务、预测任务；相应的有对应的分类方法、回归方法。**神经网络属于监督学习的范畴。**
**监督学习**，是监督式机器学习的简称。学习方法为：给定输入x、输出y的情况下，监督学习映射f；或给定x的情况下，学习y的概率分布。分为两个阶段：（基于训练数据集（data set）的样本（sample），在样本的标签（label）的指导下进行）训练、推断。
多层的神经网络（包含一层以上的隐藏层）又称为深度神经网络。深度神经网络又称为**深度学习。**

### 2.1.2 单个神经元

可模拟布尔运算，实现二元分类。
例如：逻辑斯提回归单元（logistic regression unit）
$$
y = f(\sum^N_{i=1}W_i X_i+b)
$$
调整权重W_i和偏置b，来实现单个神经元的优化。

### 2.1.3多层神经网络

可以解决XOR问题。
$$
XOR(X1,X2) = AND(OR(X1,X2),NAND(X1,X2))
$$

**多层神经网络的结构**：输入层、隐藏层、输出层。输出层要做softmax归一化。
输出层的Softmax处理：将输出值归一化为概率向量（类似于正则配分函数）。这样使得每个输出值都是正数，且和为1。
$$
g(z_m) = \frac{e^{z_m}}{\sum_k e^{z_k}}
$$

logit函数：
把（0,1）映射到（-Infinity，+Infinity）
logit函数是sigmoid函数的反函数：
$$
\sigma^{-1}(x) = log(\frac{x}{1-x})
$$
```python
def logit(x):
    return np.log(x/(1-x))
print(logit(0.9))
print(logit(0.99))
print(logit(0.999))
print(logit(0.00000001))
```

## 2.2 神经网络的训练

对神经网络的诸神经元的权重，进行自动化的确定过程，称为神经网络的训练，或称为网络权重的学习过程。
如何训练呢？一般的流程为：
1.确定损失函数（Loss）：分为test loss，training loss。
2.权重初始化（initialization）：可采取随机初始化。
3.反向传播（back propagation）：计算损失函数对权重的梯度
4.权重修正（weights adjusting）：可采用随机梯度下降法

### 2.2.1损失函数：
损失：给网络输入带有标签的训练样本。输出值的标签y和原有标签（预期输出y'）的差异，就是损失。
这个差异，需要引入度量函数来衡量，称为：损失函数（loss）或成本函数（cost）。常用的有：
绝对值求和、平均绝对值求和、平方和误差、均方差（MSE）、交叉熵（CE）...
**对于回归任务，常用均方差（MSE：mean squared error）。对于分类任务，常用交叉熵（CE：cross entropy）。**

均方误差不同于方差（均方根误差不同于标准差）：均方误差的来源，是各个估计值和**真实值**的差异引起；方差的来源，是各个数据和**平均值**的差异引起。

**一个MSE计算的代码练习：**
```python
#MSE的计算
label = 80
predicted_value = [72,94,79,83,65,81,73,67,85,82]
def MSE(value, label):
    mse = 0.
    for i in value:
        mse += (i-label)**2
    return mse/len(value)
print(MSE(predicted_value,label))  
```

也有现成的函数可以调用：
```python
mse = tf.keras.losses.MeanSquaredError()
mse([[0.,1.],[0.,0.]],[[1.,1.],[1.,0.]]).numpy()
```

**用于分类任务的交叉熵（CE）：**
$$
H_{y'}(y) = -\sum_i y'_i log(y_i)
$$
y'是标签，y是输出。

一个练习代码：
```python
#CE的计算
def CE(y_prime,y):
    return -np.sum(y_prime*np.log(y))
print(CE([1.,0],[0.9,0.1]))
print(CE([0,1.],[0.2,0.8]))
```

也有现成的函数：
```python
tf.keras.losses.categorical_crossentropy(y_true,y_pred)
```

### 2.2.2 反向传播算法

多层的神经网络中，有一个输入层、一个输出层、n个隐藏层。

层与层之间，用函数、权重、偏置，连接起来。怎样去优化这些权重w，和偏置b呢？
核心：让损失函数为各权重的函数，计算它对权重的梯度。然后采用的最优化算法是：**梯度下降法。**这也是在神经网络上执行梯度下降的主要算法。

具体地，**先**按向前传播的方式计算、缓存每个节点的输出值；**后**按照反向传播的方式，逐层计算损失函数对每个权重的偏导数。

有一个ipynb文件可供练习。

### 2.2.3 逻辑斯提回归单元反向传播计算示例

已对课件做推导，此处略去相关介绍。
问题：中间变量保存过多。实际框架采用的是：自动微分（automatic differentiation）

### 2.2.4 权重更新——随机梯度下降算法

在初始权重\theta的基础上，沿着梯度方向移动一个步长\eta，得到新的权重的值。目的是为了让损失函数下降最快。
$$
\theta = \theta - \eta \cdot \nabla_\theta J(\theta)
$$

步长\eta：又称学习率（learning rate）。学习率过大，会引起震荡；过小，收敛过慢。

**随机梯度下降法步骤：**
随机化每个神经元的权重和偏差；
选取随机样本；
输出结果后，从最后一层开始，反向计算每层权重的偏导数，逐层调整权重；
返回第二步。
因此，核心是：**随机样本**

### 2.2.5 模型训练过拟合解决方法——正则化

可以防止过拟合。
种类有：L1正则化、L2正则化、丢弃正则化等类型。
正则化率：一个指定正则化函数的相对重要性的标量值。

L1和L2两种方法相对。分别以权重的绝对值总和、平方和总和来惩罚权重；分别可以较好地处理（几乎）不相关的特征的权重，和离群值（较大正值或较小负值）的权重。
丢弃正则化：在一个梯度步长中，移除神经网络中随机的，固定数量的单元。

# 3一些补充

本节课的一些内容还没有整理。
一个逻辑斯提回归的二元分类演示实验的代码在本节课的雨课堂PPT上有演示。日后练习需要的时候可以来参考。