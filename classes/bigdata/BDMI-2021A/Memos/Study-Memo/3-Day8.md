# WW8 课堂总结

## pandas

- 数据类型 一维series 二维dataframe 三维panel
  - pd.Series(data) - data: dict,ndarray
  - pd.DataFrame(data, index,columns) - data: dict, list of lists)
- 操作csv文件
  - pd.read_csv()
  - df.to_csv()
- 生成时间序列
  - pd.date_range(periods)
- interact with sql
```python
from sqlalchemy import create_engine
engine = create_engine('sqlite:///test.db') 
df_classmates.to_sql('tb_test',con=engine)
with engine.connect() as conn, conn.begin():
    data = pd.read_sql_table('tb_test', conn)
```

## Tensorflow
- 正则率Regularization Rate
  - to deal with overfitting
- 归一化 logit
  - 是sigmoid的反函数
- 网络层数越多，表达能力增强，权重数量增加
- automized weight ascertainment
  - 过程 确定loss function; initialization; back propagation; weight adjusting
  - loss function
    - loss: 输出值和标签的diff
    - 两种类型
      - MSE：linear regression
      - CE: logistic regression 多用于classification
  - 反向传播
    - gradient:direction that increases the most
    - 最优化算法:梯度下降，取gradient的相反方向
    - 对于神经网络，分割成单个算子进行计算
      - 利用chain rule，右边第二项为上一步计算得的数值，
$$
\frac{\partial{J}}{\partial{f_{n-1}}} = \frac{\partial{J}}{\partial{f_{n}}}\frac{\partial{f_{n}}}{\partial{f_{n-1}}}
$$
  - 梯度算子 - 权重更新
    - gradient descent -> weights of outer layer of neurons -> 算子往后推到底
  - 正则化 - deal with overfitting
    - normally used: dropout regularization
  - 实际过程
    - 一个整个训练集batch切分成多个大小相同的子集mini-batch，送入训练
    - 认为model合理后，将训练结果固化

```python
def MSE(Xp,Xr):
    sum = 0
    for i in range(len(Xp)):
        sum += (Xp[i] - Xr[i])**2
    result = sum/len(Xp)
    return result
MSE([72,94,79,83,65,81,73,67,85,82],[80]*10)
```


## 示例：二元分类问题
- 采用单个人工神经元,权重表示不同特征对判断结果的贡献率；激活函数：Sigmoid；输出Y 概率

