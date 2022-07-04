### 第1 NumPy


```python
import numpy as np
a = np.arange(0, 10)
print(a + a)

A = np.arange(0,9).reshape(3,3)
B = = np.ones((3,3))
# element-wise matrix multiplication (Hadamard Product)
print(A * B)
# dot product
print(A @ B)
# Turn into just 1-dim vector
print(A.ravel())
```

- **pdb**: Useful for testing & tracing python code


### 第2 神经网络基本概念


```python
import numpy as np

def tanh(x):
    return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

def relu(x):
    return max(x, 0) 

def sigmoid(x):
    return 1 / (1 + exp(-x))

def logistic_reg(x, w):
    return sigmoid((x @ w.T).sum())

x = np.array([1, 0, 1])
w = np.array([-0.21, 0.3, 0.7])
print(logistic_reg(x, w))
```


```python
import numpy as np

and_operation = lambda x: 1 / (1 + np.exp(-(20 * x[0] + 20 * x[1] - 30)))
or_operation = lambda x: 1 / (1 + np.exp(-(20*x[0] + 20 * x[1] - 10)))
not_operation = lambda x: 1 / (1 + np.exp(-(-20 * x + 10)))
nand_operation = lambda x : 1 / (1 + np.exp(-(-20 * x[0] - 20 * x[1] + 30)))

x = np.array([0, 1])
print(and_operation(x))
print(or_operation(x))
print(nand_operation(x))
print(not_operation(1))
```
