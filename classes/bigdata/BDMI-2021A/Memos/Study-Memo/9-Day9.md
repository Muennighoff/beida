# 第9次课笔记

# TensorFlow2

有开源的活跃的Github项目：https://github.com/tensorflow/tensorflow
一些基础知识模块：
https://tensorflow.google.cn/guide/tensor
https://tensorflow.google.cn/guide/variable
https://tensorflow.google.cn/guide/autodiff
模块：
https://tensorflow.google.cn/guide/intro_to_modules
计算图：
https://tensorflow.google.cn/guide/intro_to_graphs
训练流程：
https://tensorflow.google.cn/guide/basic_training_loops

## 1 张量

张量（tensor）：可用若干指标表示其元素。可理解为多维数组。
0阶张量就是一个标量；1阶张量相当于向量；2阶张量相当于矩阵……
可以尝试用np.random.rand(2,3,4)，来生成一个2\*3\*4的三阶张量。

```python
import numpy as np
import random
c = np.array([[[0,1,2,3],[4,5,6,7],[8,9,10,11]],[[12,13,14,15],[16,17,18,19],[20,21,22,23]]])
print(np.shape(c))
a = np.random.randn(2,3,4)
print(a)
```

## 1.1 张量表示神经网络的运算

输入层X、隐藏层H、输出层N、softmax层输出Y，均为张量；
从X到H、从H到N，这个运算过程的表示：W1、W2，也是张量；
输出层之前的运算，都是张量运算；softmax操作，是张量操作。
归结起来，网络的运算，就是对张量的操作（TensorFlow）。

```python
X = [22,35,86]
W1 = np.random.rand(3,3)
W2 = np.random.rand(3,2)
H = np.dot(X,W1)
N = np.dot(H,W2)
print(W1)
print(H)
print(W2)
print(N)
```

## 1.2 tensor in TensorFlow

### 1.2.1 张量的创建

张量是不可变的，相当于python中的字符串一样。不能改变张量的元素，只能创建新的张量。

创建一个0维张量：
```python
rank_0_tensor = tf.constant()
print(rank_0_tensor)
```

创建一个1维张量：
```python
rank_1_tensor = tf.constant([2.0, 3.0, 4.0])
print(rank_1_tensor)
```

创建一个2维张量(3\*2)：
```python
rank_2_tensor = tf.constant([1, 2], [3, 4], [5, 6], dtype = float16)
print(rank_2_tensor)
```

创建一个3维张量(3\*2\*5)：
```python
rank_3_tensor = tf.constant([[1,2,3,4,5],[6,7,8,9,10]],[[11,12,13,14,15],[16,17,18,19,20]],[[21,22,23,24,25],[26,27,28,29,30]], dtype = int32)
print(rank_3_tensor)

rank_3_tensor = tf.ones((4,5,6))
print(rank_3_tensor)
```

### 1.2.2 张量的运算

**张量转化为数组：**
```python
np.array(rank_2_tensor) #张量赋值给数组
rank_2_tensor.numpy() #用数组形式调用张量
```

**对应元素加法、对应元素乘法、矩阵乘法：**
```python
#元素加法
tf.add(a,b)
a + b
#元素乘法
tf.multiply(a,b)
a * b
#矩阵乘法
tf.matmul(a,b)
a @ b
```

**运算符（op）运算：**
```python
#最大值
tf.reduce_max()
#最大值的索引
tf.argmax()
#归一化
tf.nn.softmax()
```

**数据类型和转换：**


**形状的变换：reshape**
保持元素总个数不变的情况下，变换张量的形状：
```python
aa = tf.contant([[1],[2],[3]])#是3*1的二维张量
bb = tf.reshape(aa, [1,3])#变成1*3的二维张量
```

**广播：**
有时候张量的指标不满足运算匹配条件时，可以对小张量进行“扩展”。
```python
x = tf.constant([1,2,3])
y = tf.constant(2)
z = tf.constant([2,2,2])

#下面三种运算结果相同
print(tf.multiply(x,2))
print(x * y)
print(x * z)

x = tf.constant([[1],[2],[3]])#3*1的张量
y = tf.constant([1,2,3,4])#1*4的张量
print(x * y)#结果得到3*4的张量
```

### 1.2.3 张量的索引

从0开始编号，左闭右开的原则。
```python
rank_1_tensor[2: 7]#从第2个元素，到第6个元素
```

### 1.2.4 其他特殊张量

**不规则张量：**
张量某个轴上的元素个数可变。使用tf.ragged.RaggedTensor来生成。

**字符串张量：**
可以是一种不规则张量。
tf.string

**稀疏张量：**
只需要确定有数值的位置，就可以构成张量。
可以实现稀疏矩阵和稀疏张量的转化。
```python
sparse_tensor = tf.sparse.SparseTensor(indices = [[0,1],[1,2]], values = [1,2], dense_shape = [3,4])
print(sparse_tensor)
print(tf.sparse.to_dense(sparse_tensor))
```
# 2 变量

先建立初始值，然后再建立变量。
```python
my_tensor = tf.constant([[1,2],[3,4]])
my_variable = tf.Variable(my_tensor) #从张量来创建变量
```
变量的数据类型不限，可以是bool值、复数，等等。

## 2.1 变量的结构

shape查询、dtype查询、变为numpy、转化为张量：
```python
my_variable.shape
my_variable.dtype
my_variable.numpy
tf.convert_to_tensor(my_variable)
```
## 2.2 变量的运算

变量的值可以通过assign函数更改，但形状不能更改。
```python
a = tf.Variable([2.0,3.0])
a.assign([5,6])#用整形去填入浮点型，是ok的
#加减法：
a.assign_add([2,3])
a.assign_sub([7,9])
```

## 2.3 变量的使用

可以给变量赋名字（可以同名，但是不建议），来追踪一个变量的变化。
```python
my_tensor = tf.constant([[1.0,2.0],[3.0,4.0]])
a = tf.Variable(my_tensor, name = "Mark")
b = tf.Variable(my_tensor + 1, name = "Mike")
print(a == b)
```

# 3 自动微分

详细内容见相应的ipynb文件
