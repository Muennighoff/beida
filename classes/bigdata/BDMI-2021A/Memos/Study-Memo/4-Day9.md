# Tensorflow 2 Practice

## Tensor 张量

Tensor即N维数组，1维tensor向量，2维矩阵，多维可通过组合低维得到。

张量不可变，多作为参数。无法更新张量的内容，只能创建新的张量。

```python
#%% 张量创建
a = tf.constant([1,2,3])
b = tf.constant(4)
c = tf.constant(([5,6],
                [7,8],
                [9,10]))
d = tf.ones((4,5,6)) # 4x5x6 的全是1的张量
print(a)
print(b)
print(c)
print(d)
#Output
tf.Tensor([1 2 3], shape=(3,), dtype=int32)
tf.Tensor(4, shape=(), dtype=int32)
tf.Tensor(
[[ 5  6]
 [ 7  8]
 [ 9 10]], shape=(3, 2), dtype=int32)
```

基本运算：

```python
#%% 基本运算
e = tf.ones((2,2),dtype=tf.float32)
f = tf.constant(([1,2],
                [3,4]),dtype=tf.float32)
print(tf.add(e,f)) #对应元素加
print(tf.multiply(e, f)) #对应元素乘
print(tf.matmul(e, f)) #矩阵运算
```

注意在使用1维向量相乘时，依然会得到矩阵（逻辑与线性代数运算一致）。这被称为广播乘法。

稀疏矩阵：如果矩阵中有大量的0或null值，为了节约空间，可以使用稀疏矩阵。

```python
sparse_tensor = tf.sparse.SparseTensor(indices=[[0,0],[1,2]], 
                                       values=[1,2], 
                                       dense_shape=[3,4])
print(sparse_tensor)
print(tf.sparse.to_dense(sparse_tensor))
```

此时输出结果如下。注意可以通过*to_dense*把矩阵还原为普通矩阵。

```python
SparseTensor(indices=tf.Tensor(
[[0 0]
 [1 2]], shape=(2, 2), dtype=int64), values=tf.Tensor([1 2], shape=(2,), dtype=int32), dense_shape=tf.Tensor([3 4], shape=(2,), dtype=int64))
tf.Tensor(
[[1 0 0 0]
 [0 0 2 0]
 [0 0 0 0]], shape=(3, 4), dtype=int32)
```

## Variable 变量

和张量一致，变量也无法改变形状，reshape会生成一个新张量。

变量的值可以修改，方法为assign。

```python
#%% 变量的操作
print(tf.debugging.set_log_device_placement) #得到变量存储位置
my_tensor = tf.constant([[1.0,2.0],[3.0,4.0]])
my_variable = tf.Variable(my_tensor)
print(my_variable)
# 可以使用assign来改变其值
b = tf.Variable(my_variable)
my_variable.assign([[0,0],[0,0]]) 
#assign 方法可以改变变量值，但不能改变形状。dtype必须一致。
print(my_variable)
print(b)
```

## 自动微分

一个简单的求导过程如下：

对函数$y=x^2+e^{x}$求导，求其在$x=1$处导数：

```python
#%% 一个简单求导过程
x = tf.constant(1.0)
with tf.GradientTape() as t:
    t.watch(x)
    y = x*x + tf.exp(x)
dy_dx = t.gradient(y,x)
print(dy_dx)
```

































