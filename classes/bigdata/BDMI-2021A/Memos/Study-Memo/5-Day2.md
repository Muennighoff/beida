# 学习小结 20210922

#### 尹哲良

## Python 语法补充

### Python 文件操作

#### 打开、关闭函数

显式读取

```python
file=open(file_path,'r')
file.close()
```

#### 路径函数

```python
os.path.realpath('file_io.ipynb') #返回某文件所在的文件夹
os.path.dirname(current_file) #返回文件所在文件夹的上级
data_dir=os.path.join(os.path.dirname(current_dir),'data') #返回data文件夹
```

#### 写入函数

```python
file.write(str)
```

#### 课堂示例：写入、追加写入

```python
import os

#将路径指向data文件夹
current_file=os.path.realpath('test_9_22.ipynb')
current_dir=os.path.dirname(current_file)
data_dir=os.path.join(os.path.dirname(current_dir),'data')

#创建data文件夹
if not os.path.exists(data_dir):
    os.makedirs(data_dir)
   
#打开并写入文件内容（隐式读取）
new_file_path=os.path.join(data_dir,'new_file.txt')
with open(new_file_path,'w') as my_file:
    my_file.write('This is my first file that I write with Python.\n')

#追加文件内容
with open(new_file_path,'a+') as my_file:
    my_file.write('This is my second file that I write with Python.\n')
```

#### 课堂示例：写入、读取随机数

```python
import random

#生成随机数并写入
number_file_path=os.path.join(data_dir,'number_file.txt')
with open(number_file_path,'w') as f:
    for i in range(20):
        f.write('{} '.format(random.randint(0,100)))

#读取文件并输出
with open(number_file_path,'r') as f:
    for line in f:
        print(line.split())
```

#### 文件删除函数

规范性：首先判断文件是否存在

```python
if os.path.exists(new_file_path):
	os.remove(new_file_path)
```

### 模块和包

#### 区别

包一定有\_\_init\_\_.py文件，模块只是一个扩展py源文件

#### 调用方法

```python
import A
if __name__=="__main__":
	print(A.sum(3,4))
```

```python
from A import sum
if __name__=="__main__":
	print(sum(3,4))
```

## 算法补充

### 排序算法

#### 插入排序

```python
def insertion_sort(a_list):
    b_list=a_list.copy()
    for i in range(1,len(b_list)):
        tmp=b_list[i]
        point=i-1
        while point>=0 and b_list[point]>tmp:
            b_list[point+1]=b_list[point]
            point-=1
        b_list[point+1]=tmp
    return b_list
```

#### 归并排序

```python
def merge(left,right):
    ans=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            ans.append(left[i])
            i+=1
        else:
            ans.append(right[j])
            j+=1
    ans.extend(left[i:])
    ans.extend(right[j:])
    return ans
def merge_sort(a_list):
    if len(a_list)<=1:
        return a_list
    mid=len(a_list)//2
    left=merge_sort(a_list[:mid])
    right=merge_sort(a_list[mid:])
    return merge(left,right)
```

如何证明时间复杂度？

假设
$$
n=2^k
$$
则有
$$
T(n)=2*T(n/2)+O(n)
$$
也即
$$
T(n)=O(n)+2*O(n/2)+4*O(n/4)+...+2^k*O(n/2^k)=O(n)*(k+1)=O(nlogn)
$$

### 选择算法

问题描述：返回一个数组中第k小的元素

基本思路

+ 如果数组很短，直接排序后选择
+ 如果数组很大，选择一个锚点，将数组分为两部分，进入其中一部分递归选择

选择锚点的方法

+ 随机
+ 中位数法
  + 将数组分为五组，每组计算中位数
  + 取五个中位数的中位数，作为锚点

```python
def select(a_list,k):
    small=[]
    big=[]
    for i in range(1,len(a_list)):
        if a_list[i]<a_list[0]:
            small.append(a_list[i])
        else:
            big.append(a_list[i])
    if len(small)==k:
        return a_list[0]
    elif len(small)>k:
        return select(small,k)
    else:
        return select(big,k-1-len(small))
```

### 复杂度记号

O：最坏情况，上界

\Omega：最好情况，下界

\Theta：最好、最坏情况量级相同，确界

对于小规模问题，复杂度低的算法不一定快
