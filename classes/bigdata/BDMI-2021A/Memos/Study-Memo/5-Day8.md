# 学习小结 20211027

#### 尹哲良

## Pandas基础

### 数据结构

+ Series
+ DataFrame
+ Panel

### 使用数据库

```python
from sqlalchemy import create_engine

engine = create_engine('sqlite:///test.db') 
df_classmates.to_sql('tb_test',con=engine) #将DataFrame写入到SQL
with engine.connect() as conn, conn.begin():
    data = pd.read_sql_table('tb_test', conn) #从SQL读取数据到DataFrame
```

## TensorFlow2基础

### 参数设置

+ 学习率：越大收敛越快，但可能不稳定
+ noise：数据中噪声的大小
+ 正则化比率：预防过拟合

## 机器学习相关概念

### 反向传播

本质上为求损失函数对每个参数的偏导数

问题：保存过多中间变量

### 梯度下降

$$
\theta_{i+1}=\theta_i-\alpha*\frac{\partial J(\theta)}{\partial \theta}
$$

随机梯度下降：每次迭代随机抽取一个样本点

### 小批量训练

将训练集分为多个batch（min-batch）
