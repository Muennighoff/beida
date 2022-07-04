# 4-Summary Day 2 

这次课程的核心代码操作有两类：文件操作和排序。

## 1. 文件操作

文件操作的基本package是os模块。它可以方便地处理地址：

```python
#%%
import os
current_file = os.path.realpath("4-Day1.md") #返回路径
current_dir = os.path.dirname(current_file) #得到文件所在文件夹路径
file_path = os.path.join(current_dir,'simple_file.txt') #合称为一个地址
```

进而可以对文件进行操作：

```python
new_file = open('myclassmates.txt', 'w')
new_file.close()
with open('myclassmates.txt', 'a+') as f:
    f.write('Andrew')
with open('myclassmates.txt','a+') as simple_file:
    simple_file.write('张三 01')
#使用with不必再close文件
```

### example1: classmates

```python
#%%加入随机数
import random
with open('myclassmates.txt', 'w') as f:
    for i in range(20):
        num = random.randint(0, 100)
        f.write(str(num))
        f.write(' ')
with open('myclassmates.txt','r') as f:
    print(f.read())
```

> 注意上述代码可以直接生成myclassmates.txt, 无需手动操作

### example2: package导入

```python
from lecture2_sorting import naiveInsertionSort
A = [6,4,3,8,5]
B = naiveInsertionSort(A)
print(B)
```

可以导入其他代码处的包

## 练习：merge sort

一种使用分治思想的排序方法，这里基于上课讲解内容进行了实现。

```python
def merge1(L,R):
    i = 0 #L
    j = 0 #R
    result = []
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            result.append(L[i])
            i += 1
        else:
            result.append(R[j])
            j += 1
    result.extend(L[i:])
    result.extend(R[j:])
    return result
M = [1,2,4]
N = [3, 5, 6]
print(merge1(M,N)) 
def mergeSort(A):
    n = len(A)
    if n <= 1:
        return A
    L = mergeSort(A[:round(n/2)])
    R = mergeSort(A[round(n/2):n])
    return merge(L,R)
            
```

