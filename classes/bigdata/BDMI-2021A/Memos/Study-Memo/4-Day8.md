# Tensorflow: 梯度下降与Loss Function

## 损失

即输出值与标签的差异。

输入：$x$	标签：$y$	输出值：$\hat{y}$	损失：$loss(y_i,\hat{y_i})$，

不同$loss(y_i,\hat{y_i})$使用场景：

* 线性回归中损失使用均方误差MSE，逻辑回归中常使用交叉熵。

* 回归任务：使用MSE；分类任务：使用交叉熵CE公式

## 梯度下降法

核心：$\min loss(y_i,\hat{y_i})$

方法：反向传播算法

1. 求loss偏导数。
2. 将loss的偏导数再依次对前一层的每一个分量求偏导
3. k层对k-1层每个分量求偏导，直至第一层

实现方法：自动微分

单个算子（Operator）反向传播：将深度网络分解为一系列算子的运算，再对单个算子进行反向传播运算。（具体操作可参考课件内容）

## 一些函数实现

这里主要记录课程上的softmax，logit function，loss function实现。

```python
#%% softmax
def Softmax(x):
    array = np.array([np.exp(i) for i in x])
    sum = array.sum()
    result = np.array([j/sum for j in array])    
    return result

#%% Logit Function
def logit(x):
    return np.log(x/(1-x))
print(logit(np.array([0.5,0.8,0.9,0.999999])))
#%% MSE loss function
def MSE(pre:list,real:float) -> float:
    temp = [(i-real)**2 for i in pre]
    mse = np.average(temp)
    return mse

#%% Cross Entropy
def CE(y,yhat)->float:
    return -np.sum(y * np.log(yhat))
```

