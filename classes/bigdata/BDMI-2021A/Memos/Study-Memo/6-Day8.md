### 第1 Python Pandas


- See pandas.ipynb


### 第2 TF2


- https://playground.tensorflow.org/
- 需要几个神经元解决XOR问题？
    - 5 （第一层：3；第二层：2）


```python
import numpy as np
def mse(x, y):
    return np.mean((x - y) ** 2)
X = np.array([72, 94, 79])
y = np.array([80, 80, 80])
mse(X, y)
```

```python
def crossentropy(y_hat, y, e=1e-12):
    return -np.sum(y * np.log(y_hat + e)) / len(y_hat)

y_hat = np.array([0.8, 0.2])
y = np.array([1, 0])
crossentropy(y_hat, y)
```
