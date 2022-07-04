# 学习小结 20211027

#### 尹哲良

## Numpy

### 安装

启动CMD，输入 `pip install numpy`

### 数组基本功能

创建

运算

函数运算 `np.sin` `np.sqrt` `np.ones` `__array__.reshape`

### 矩阵运算

`np.matnul(mat_a,mat_b)` 或 `mat_a.dot(mat_b)` 或 `np.dot(mat_a,mat_b)` 或 `mat_a @ mat_b` ：矩阵乘积或向量欧式内积

`mat.reshape()` 或 `mat.shape=tuple()` ：改变维度

`mat.ravel()` ：展开成一维

`mat.transpose()` ：转置

## Deap Learning

### 人工神经元

特征权重+激活函数

激活函数常用者有：`sigmoid` 、 `tanh` 、 `relu` 

### 逻辑运算

利用 `sigmoid` 的单调性，通过定义不同的权重，得到近似0或1的结果

与、或、非、与非：均可通过一个神经元实现

## Pandas

## Deep Learning

### 机器学习的分类

监督学习（分类+预测）

非监督学习

强化学习

### 方法

`softmax` ：将一列数组归一化，将大的数值和小的数值两极分化
