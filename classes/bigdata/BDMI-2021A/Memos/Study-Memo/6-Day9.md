### 第1 TF2


```python
import numpy as np
X = np.random.randn(3,3,10,10)
```


```python
import numpy as np
X = np.array([22, 35, 86])

w_1 = np.random.randn(3, 3)
b_1 = np.random.randn(3)

w_2 = np.random.randn(2, 3)
b_2 = np.random.randn(2)

def softmax(x):
    denominator = sum(np.exp(x))
    return np.exp(x) / denominator

out = softmax((X @ w_1.T + b_1) @ w_2.T + b_2)
```


```python
import numpy as np
import tensorflow as tf
X = tf.constant(np.random.randn(3,3,10,10))
X = tf.ones((4,5,6))
```

```python
import tensorflow as tf

x = tf.constant([1, 2, 3])
print(x)
x = tf.reshape(x, [3, 1])
print(x) # [3, 1]
y = tf.range(1, 5) # [1, 5]
print(y)
print(tf.multiply(x,y)) # [3, 5]
```

```python
import tensorflow as tf

complex_variable = tf.Variable([1 + 5j])
```

```python
import tensorflow as tf

x = tf.Variable(1.0)

with tf.GradientTape() as tape:
  y = x ** 2 + tf.exp(x)

dy_dx = tape.gradient(y, x) # f'(x) = 2x + e**x = 2 * 1.0 + e**1.0 = 2 + e = 4.7
```

```python

with tf.GradientTape() as tape:
    with tf.GradientTape() as tape2:
        y = x * x * x   # x ^ 3
    dy_dx = tape.gradient(y, x) # 3x^2
d2y_dx2 = tape.gradient(dy_dx, x) # 6x
```


- Tensor
    - tf <> numpy
        - np.array(tensor) ; tensor.numpy()
    - tf.add == + ; tf.multiply == * ; tf.matmul == @
    - Never use tf.reshape to reorder dimensions > use tf.transpose
- Variable
    - Wrapper around tensor - Used to represent a persistent changeable tensor
    - Variables cannot be reshaped > TF will turn it into a tensor
- Autodiff
- Modules
- Graphs
- Training Loops

