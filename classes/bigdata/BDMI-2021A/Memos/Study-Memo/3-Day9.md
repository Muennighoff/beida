# WW9 课程总结

## TensorFlow2 Introduction
- 张量 Tensor n-dimensional array
  - 张量计算可以用来表示neuron network

- 变量 variable
  - changeable
  
- 自动微分 autodiff
  - 使用reverse mode differentiation

## 张量
  - Constructor() 张量 tf.constant()
  - 3轴 张量 2维张量的叠加
  - 末位数字是list的length，之后就是list of lists, list of lists of lists
  
- 运算
  - tf.multiply() element multiplication
  - tf.matmul() matrix multiplication
  - tf.reduce_max find the maximum
  - tf.argmax 求最大值的索引
  - tf.cast() tensor dtype转换
  - tf.reshape()
  
- Tensor 广播
  - 为了适应大张量，会对小张量进行“扩展”
  
- Tensor 索引
  - 冒号：start:stop:step，左闭右开
  
- 不规则张量
  - tf.ragged.RaggedTensor() 某个axis的length会改变
  
- 字符串张量
  - single String rank == 0
  
- 稀疏张量
  - tf.sparse.SparseTensor()
  示例：
```python
mport tensorflow as tf
print(tf.__version__)
a = tf.constant(1.0)
b = tf.constant(3.0)
c = a + b
print(c)

t1 = tf.constant(np.random.normal(size=(4,4)))
t2 = tf.constant(np.random.normal(size=(4,5,6)))
print(t1,t2)
```

## 变量 Variable
- 需要initialization
 - Constructor: ts.Variable(ts.constant)
 - shape cannot be changed
 - t.assign()
 - (2,)代表1维
- a == b 可以直接判断


## 自动微分
- Gradient type
  - constant must be added
  - tf.GradientTape.gradient(dependent variable,independent variable)
  - 设置 persistent = True 不会释放内存
- 高阶求导
```python
import tensorflow as tf
x = tf.constant(1.0)
with tf.GradientTape(persistent=True) as t:
    with tf.GradientTape(persistent=True) as t2:  
        t2.watch(x)
        y = x**3 + tf.exp(x)
    dy_dx = t2.gradient(y,x)
d2y_dx2 = t.gradient(dy_dx,x)

print(dy_dx)
del t
```