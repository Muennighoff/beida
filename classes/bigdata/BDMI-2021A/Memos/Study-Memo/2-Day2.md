# 第二天课堂笔记 2021/9/22

## Python 文件读写

- 打开文件
  
  ```python
  file = open('file.txt')

  with open('file.txt') as file:
    pass
  ```

  这里 open 函数的第二个参数代表打开方式，默认为 r（只读）。

  ![hello](https://www.runoob.com/wp-content/uploads/2013/11/2112205-861c05b2bdbc9c28.png)

- 读取文件

  ```python
  file.read(count)
  file.read() # to end
  ```

- 写入文件

  ```python
  file.write()
  ```

- 关闭文件

  ```python
  file.close()
  ```

- 其他

  ```python
  file.tell() # 位置
  file.seek(pos, 0) # from start
  file.seek(pos, 1) # from current
  file.seek(pos, 2) # from end
  ```

## 模块和包

模块：`.py` 文件
包：存在 `__init__.py` 的目录

```python
import module1, module2
import numpy as np

from modname import name1, name2
```

## 算法

### 插入排序

时间复杂度为 $O(n^2)$

### 归并排序

递归的思想，时间复杂度是 $O(n\log(n))$

### k-select 问题

选择列表中第 k 小的数字（或者选择列表中前 k 小的数字）

使用快速排序的思想，使用 pivot 来划分大小列表，并进一步选择一边进行递归

这里选择 pivot 时可以采用 choose_pivot() 方法，能够保证选到 $\frac{3n}{10}$ 到 $\frac{7n}{10}$ 之间的一个数

### 复杂度记号

$O$ 上界，最坏情况

$\Omega$ 下界，最好情况

$\Theta$ 确界