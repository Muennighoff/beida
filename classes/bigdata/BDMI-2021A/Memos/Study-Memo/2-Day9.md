# 第九天课堂笔记 2021/11/10

## 张量

与 numpy 中的 ndarray 相似，有一些差别，可以互相转换。是不可变的。

### 创建

```py
tf.constant(
    value[,
    dtype,
    shape,
    name,
    verify_shape]
)
```

### 转化

dtype: tf.float16 tf.float32 tf.uint8 等

```py
tf.cast(x, dtype, name)
```

注意：会产生新的张量

### 运算

```py
tf.argmax()
tf.reduce_max()
tf.nn.softmax()
a+b
a*b
a@b
```

### 其他

```py
tf.reshape(x,(1,2,-1)) # 用 -1 来代表自动计算
```

### 广播机制

### 字符串张量和分割，不规则张量，稀疏张量

## 变量

总体与张量类似，不可以 reshape

```py
a=tf.Variable()
a.assign()
a.assign_add() # 浮点数可以加整数，反之不可以
```

## 自动微分

使用 tf.GradientTape(persistent) 来记录，然后调用他的 gradient 方法获取梯度。

```py
with tf.GradientTape as t:
    t.watch(x)
    ...
dz_dx=t.gradient(z,x)
```

默认情况下只能调用一次 gradient，加上 persistent=True 后即可查看多个 Gradient 值。

### 高阶导数

通过嵌套的 GradientTape，可以二次求导。
