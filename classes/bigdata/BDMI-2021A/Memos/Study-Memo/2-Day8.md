# 第八天课堂笔记 2021/11/3

## Pandas

Pandas：进行数据处理

Series DataFrame Panel （一二三维）

可变的数据长度

### Series

可以存储任意类型的数据

```python
pd.Series(data, index=[0,1,2])
# len(data)==len(index)
```

### DataFrame

行、列

```python
# 使用map初始化
d = {'one' : pd.Series([1.,2.,3.],index=['a','b','c']),
     'two' : pd.Series([1.,2.,3.,4.],index=['a','b','c','d'])}
df = pd.DataFrame(d)

# 使用二维数组初始化
df_data = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
```

index: 行（记录）索引

columns: 有哪些属性

I/O 交互：to_csv read_csv read_sql_table to_sql

定位一个记录：loc['index'] iloc[lino]

转置：df.T

#### 列操作

直接使用索引操作：

```python
df['three']=pd.Series([10,20,30],index=['a','b','c'])

del df['one']
```

### 行操作

```python
# 删除
df=df.drop(0)
df=df.append(df2) # 添加一个行、DataFrame
```

## 神经网络

### 分对数 logit

与 softmax 逆过程，与 sigmoid 互为反函数

```python
def logit(x):
    return np.log(x/(1-x))
```

### 多层神经网络

#### 损失函数

数值化输出和标签的差异，定义度量函数：

- 交叉熵 CE（对于分类任务）
- 均方差 MSE L2 损失函数（对于回归任务）

均方差：

```python
def MSE(x,truth):
    return np.mean(np.square(np.array(x)-truth))
```

交叉熵：

```python
def CE(predicted,truth):
    return -np.sum(np.log(predicted)*truth)
```

#### 反向传播

使用求导链式法则，使用梯度下降法，配合合适的学习率，进行参数调整。
