<<<<<<< HEAD
# 第二周学习笔记

# 2.1 Python基础知识回顾

**基本数据类型：**字符串string，整数int，浮点数float，布尔值bool
**数据结构：**列表list，集合set，字典dict
**语句类型：**条件{if elif else}，循环{for}{while}，...
**函数**
**类：**初始化...
**模块与包**

# 2.2文件操作

## 2.2.1主要文件操作函数

### 打开函数：

```python
file = open(file_path,'r')
```

path是路径，'r'是要进行的操作，稍后会统一说明。

### 关闭函数：

```python
file.close() 
```

### 路径函数（利用os模块）：

```python
current_file = os.path.realpath('file_io.ipynb')#给出完整的路径
current_dir = os.path.dirname(current_file)#给出不含文件名的路径
data_dir = os.path.join(os.path.dirname(current_dir),'data')
```

### 读取函数：

```python
#用with语句进行隐式读取
file_path = os.path.join(data_dir,'simple_file.txt')
with open(file_path,'r') as simple_file:
	for line in simple_file:
		print(line.strip())
#不用with语句进行显式读取
file_path = os.path.join(data_dir,'simple_file.txt')
simple_file = open(file_path,'r')
for line in simple_file:
	print(line.strip())
simple_file.close()
```

### 写入函数：

```python
new_file_path = os.path.join(data_dir,'new_file.txt')

with open(new_file_path) as my_file:
	my_file.write('This is my first file that I wrote with Python.')
```

### 文件删除函数：

```python
if os.path.exists(new_file_path):
	os.remove(new_file_path)
```

## 2.2.2 主要文件IO模式

**t：**文本模式
**x：**写模式
**b：**二进制模式
**+：**打开一个文件进行更新（可读可写）
**w：**打开一个文件只用于写入
**r：**以只读方式打开
**a：**打开一个文件，在其结尾进行追加

## 2.2.3文件操作练习：

### 写入同学的信息：

```python
#用’x'控制，实现新建文件并进行写操作
with open('myclassmates.txt','x') as file:
	file.write('Alice 1\n')
	file.write('Bob 2\n')
	file.write('Carol 3\n')
#用'a+'控制，打开文件并在其末尾进行追加写的操作
with open('myclassmates.txt','a+') as file:
	file.write('Dave 4\n')
```

### 准备排序数据集：

```python
import random
rand_list = []
for i in range(20):
    rand_list.append(random.randint(1,100))
print(rand_list)

with open('data.txt','w') as rand_num_set:
	#用空格连接rand_list中的各个元素i，并写入到数据集中
    rand_num_set.write(' '.join([str(i) for i in rand_list]))
with open('data.txt','r') as f:
    print(f.readline())
```

# 2.3模块与包

**模块：**拓展的源文件
**包：**含有\_init\_.py文件（ 初始化）；模块和包文件的目录

### 一个包的示例：

```python
food_store/#包名
	_init_.py
	product/#模块名
		_init_.py
		fruit/
			_init_.py
			apple.py#具体的变量、函数、类等
			banana.py
		drink/
			_init_py
			juice.py
			milk.py
			beer.py
	cashier/
		_init_.py
		receipt.py
		calculator.py
```

### 在banana.py文件中定义如下函数和类

```python
def get_available_brands():
	return ['chiquita']
	
class Banana:
	def _init_(self, brand = 'chiquita'):
		if brand not in get_available_brands():
			raise ValueError('Unkown brand: {}'.format(brand))
		self._brand = brand
```

### 调用示例：

```python
from food_store.product.fruit.banana import Banana
#也可以这样调用：from food_store.product.fruit import banana

#然后创建Banana类：
my_banana = Banana()
#或者：my_banana = banana.Banana
```

# 2.4排序算法

有**插入排序**和**合并排序**等方法，今天只涉及数据都不同的排序

## 2.4.1 insertion sort

为什么叫做：插入排序？因为第i步是将第i+1位的元素，插入到前方长度为i的有序队列里。而为了排好一个长度为n的列表，需要进行n-1步操作

### 算法的可行性：

可以通过归纳法证明

### 算法效率：

朴素的排序算法，时间消耗是O(n^2)，时间消耗有两个来源：比较、交换。可以采用二分法等方法缩短比较的时间。

### 下面是插入排序的代码示例

```python
def InsertionSort(A):
	for i in range(1,len(A)):#i从1增加到len(A) - 1，排序次数是合理的
		current = A[i]
		j = i - 1
		while j >= 0 and A[j] > current:
#从i - 1位向前寻找比A[i]小的数字，找到之前，将A中的数字依次往后挪一个位置，直到找到A[i]的位置，将其放入，为止
			A[j + 1] = A[j]
			j -= 1
		A[j + 1] = current
```

## 2.4.2 merge sort

合并排序，采用**分而治之**的思想。把大问题分解成小问题分别解决，并再恢复为大问题
因此分两个重要步骤：
1.分而治之：需要反复递归。通过定义mergesort函数来实现
2.合并：需要把两个已经排好序的列表，合到一起？（即怎么去merge？答案：依次比大小）

### 算法的可行性：

1.单元素列表是排好序的
2.问题归结为，L和R都排好序时，Merge(L,R)是排好序的

### 算法效率：

**结论：**合并算法的时间消耗是O(nlog(n))。
**分析：**时间花在合并上：用2个n/2合并成n，指针遍历消耗时间是O(n)；用4个n/4分别合并成2个n/2，这一级别上，花费时间也为O(n)……总共有多少个层级呢？log(n)。所以问题的总规模为nlog(n)

### 下面是合并排序的代码示例

```python
import math
def Merge(L, R):
    i = 0
    j = 0
    ret = []
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            ret.append(L[i])
            i += 1
        else:
            ret.append(R[j])
            j += 1
    while i < len(L):
        ret.append(L[i])
        i += 1
    while j < len(R):
        ret.append(R[j])
        j += 1
    return ret

def mergesort(A):
	n = length(A)
	if n <= 1:
		return A
	L = mergesort(A[0: math.floor(n/2)])
    R = mergesort(A[math.ceil(n/2): n])
	return Merge(L,R)
```

# 2.5中值和选择

科学选择问题（k-SELECT problem），从一个数组里选出某个大小的值。

```python
select(A, k)#从A数组里，选出第k小的数
```

**讨论分析：怎么做？**
如果先排序，再选择，就回到了排序问题，复杂度为O(nlog(n))，这是不能接受的。

```python
def SELECT(A, k):
	A = mergesort(A)
	return A[k - 1]
```

朴素的选择法：不断遍历，找最小的，第二小的，以此类推，但复杂度将和O(n^2)一样！更加不能接受！
我们肯定希望找到小于O(nlog(n))的算法，甚至是O(n)的算法

### 仍然考虑分而治之的方法：

选取一个锚点（pivot），在O(n)的时间内，将原数组分解为两个数组L和R，元素分别小于或大于锚点。
然后，根据k和len(L)、len(R)的大小关系，将问题转化为在较小的数组中去找出某个数的问题。

### 代码示例：

```python
def select(A,k):
	pivot = findpivot(A)
	L, R = partition(A, pivot)
	if k == len(L) + 1:
		return pivot
	elif k <= len(L):
		return select(L,k)
	else:
		return select(R, k-len(L))
```

### 锚点的选择:

上面的代码示例中，调用了接下来将讨论的findpivot()函数，它是寻找锚点的函数。
锚点的寻找非常关键，这直接关系到分治算法的效率，如果每次都能保证10n/3 < len(L), len(R) < 10n/7，则可以实现分治算法的规模为O(n)。怎么实现呢？
1.将数组A分为5个元素一组的小组，共m = n/5个。
2.分别寻找这m个数组的中位数，记为p1,p2,p3,...pm。
3.寻找这m个中位数的中位数，记为p = SELECT([p1, p2, p3, ... pm], m/2)
4.返回p在A中的指标，这就是较好的锚点

### 现在再看看代码示例：

```python
def select(A,k):
	if len(A) < 50#当A长度较短时，采用排序-选择法更快
		A = mergesort(A)
		return A[k - 1]
	p = ChoosePivot(A)
	L, PivotVal, R = partition(A, p)
	if k == len(L) + 1:
		return Pivotval
	elif k <= len(L):
		return select(L,k)
	else:
		return select(R, k-len(L))
```

**总的复杂度来自于：**
T(n) <= O(n/5)(锚点选择) + O(7n/10)(在最大长度为7n/10的数组上做科学选择，然后返回。这个过程可以递归) + O(n)
**思考：**
O(n)的算法一定快于O(nlog(n))吗？不一定，这是渐进复杂度。
**但事实上：**
上述理论上很好的科学选择法，复杂度甚至大于归并排序（n~10^3的小规模）。
甚至，采用随机选取锚点的方法时，科学选择法有最佳的效率。

## 复杂度记号

O：最坏情况（算法的运行时间不会超过O(f(n))）
=======
# 第二周学习笔记

# 2.1 Python基础知识回顾

**基本数据类型：**字符串string，整数int，浮点数float，布尔值bool
**数据结构：**列表list，集合set，字典dict
**语句类型：**条件{if elif else}，循环{for}{while}，...
**函数**
**类：**初始化...
**模块与包**

# 2.2文件操作

## 2.2.1主要文件操作函数

### 打开函数：

```python
file = open(file_path,'r')
```

path是路径，'r'是要进行的操作，稍后会统一说明。

### 关闭函数：

```python
file.close() 
```

### 路径函数（利用os模块）：

```python
current_file = os.path.realpath('file_io.ipynb')#给出完整的路径
current_dir = os.path.dirname(current_file)#给出不含文件名的路径
data_dir = os.path.join(os.path.dirname(current_dir),'data')
```

### 读取函数：

```python
#用with语句进行隐式读取
file_path = os.path.join(data_dir,'simple_file.txt')
with open(file_path,'r') as simple_file:
	for line in simple_file:
		print(line.strip())
#不用with语句进行显式读取
file_path = os.path.join(data_dir,'simple_file.txt')
simple_file = open(file_path,'r')
for line in simple_file:
	print(line.strip())
simple_file.close()
```

### 写入函数：

```python
new_file_path = os.path.join(data_dir,'new_file.txt')

with open(new_file_path) as my_file:
	my_file.write('This is my first file that I wrote with Python.')
```

### 文件删除函数：

```python
if os.path.exists(new_file_path):
	os.remove(new_file_path)
```

## 2.2.2 主要文件IO模式

**t：**文本模式
**x：**写模式
**b：**二进制模式
**+：**打开一个文件进行更新（可读可写）
**w：**打开一个文件只用于写入
**r：**以只读方式打开
**a：**打开一个文件，在其结尾进行追加

## 2.2.3文件操作练习：

### 写入同学的信息：

```python
#用’x'控制，实现新建文件并进行写操作
with open('myclassmates.txt','x') as file:
	file.write('Alice 1\n')
	file.write('Bob 2\n')
	file.write('Carol 3\n')
#用'a+'控制，打开文件并在其末尾进行追加写的操作
with open('myclassmates.txt','a+') as file:
	file.write('Dave 4\n')
```

### 准备排序数据集：

```python
import random
rand_list = []
for i in range(20):
    rand_list.append(random.randint(1,100))
print(rand_list)

with open('data.txt','w') as rand_num_set:
	#用空格连接rand_list中的各个元素i，并写入到数据集中
    rand_num_set.write(' '.join([str(i) for i in rand_list]))
with open('data.txt','r') as f:
    print(f.readline())
```

# 2.3模块与包

**模块：**拓展的源文件
**包：**含有\_init\_.py文件（ 初始化）；模块和包文件的目录

### 一个包的示例：

```python
food_store/#包名
	_init_.py
	product/#模块名
		_init_.py
		fruit/
			_init_.py
			apple.py#具体的变量、函数、类等
			banana.py
		drink/
			_init_py
			juice.py
			milk.py
			beer.py
	cashier/
		_init_.py
		receipt.py
		calculator.py
```

### 在banana.py文件中定义如下函数和类

```python
def get_available_brands():
	return ['chiquita']
	
class Banana:
	def _init_(self, brand = 'chiquita'):
		if brand not in get_available_brands():
			raise ValueError('Unkown brand: {}'.format(brand))
		self._brand = brand
```

### 调用示例：

```python
from food_store.product.fruit.banana import Banana
#也可以这样调用：from food_store.product.fruit import banana

#然后创建Banana类：
my_banana = Banana()
#或者：my_banana = banana.Banana
```

# 2.4排序算法

有**插入排序**和**合并排序**等方法，今天只涉及数据都不同的排序

## 2.4.1 insertion sort

为什么叫做：插入排序？因为第i步是将第i+1位的元素，插入到前方长度为i的有序队列里。而为了排好一个长度为n的列表，需要进行n-1步操作

### 算法的可行性：

可以通过归纳法证明

### 算法效率：

朴素的排序算法，时间消耗是O(n^2)，时间消耗有两个来源：比较、交换。可以采用二分法等方法缩短比较的时间。

### 下面是插入排序的代码示例

```python
def InsertionSort(A):
	for i in range(1,len(A)):#i从1增加到len(A) - 1，排序次数是合理的
		current = A[i]
		j = i - 1
		while j >= 0 and A[j] > current:
#从i - 1位向前寻找比A[i]小的数字，找到之前，将A中的数字依次往后挪一个位置，直到找到A[i]的位置，将其放入，为止
			A[j + 1] = A[j]
			j -= 1
		A[j + 1] = current
```

## 2.4.2 merge sort

合并排序，采用**分而治之**的思想。把大问题分解成小问题分别解决，并再恢复为大问题
因此分两个重要步骤：
1.分而治之：需要反复递归。通过定义mergesort函数来实现
2.合并：需要把两个已经排好序的列表，合到一起？（即怎么去merge？答案：依次比大小）

### 算法的可行性：

1.单元素列表是排好序的
2.问题归结为，L和R都排好序时，Merge(L,R)是排好序的

### 算法效率：

**结论：**合并算法的时间消耗是O(nlog(n))。
**分析：**时间花在合并上：用2个n/2合并成n，指针遍历消耗时间是O(n)；用4个n/4分别合并成2个n/2，这一级别上，花费时间也为O(n)……总共有多少个层级呢？log(n)。所以问题的总规模为nlog(n)

### 下面是合并排序的代码示例

```python
import math
def Merge(L, R):
    i = 0
    j = 0
    ret = []
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            ret.append(L[i])
            i += 1
        else:
            ret.append(R[j])
            j += 1
    while i < len(L):
        ret.append(L[i])
        i += 1
    while j < len(R):
        ret.append(R[j])
        j += 1
    return ret

def mergesort(A):
	n = length(A)
	if n <= 1:
		return A
	L = mergesort(A[0: math.floor(n/2)])
    R = mergesort(A[math.ceil(n/2): n])
	return Merge(L,R)
```

# 2.5中值和选择

科学选择问题（k-SELECT problem），从一个数组里选出某个大小的值。

```python
select(A, k)#从A数组里，选出第k小的数
```

**讨论分析：怎么做？**
如果先排序，再选择，就回到了排序问题，复杂度为O(nlog(n))，这是不能接受的。

```python
def SELECT(A, k):
	A = mergesort(A)
	return A[k - 1]
```

朴素的选择法：不断遍历，找最小的，第二小的，以此类推，但复杂度将和O(n^2)一样！更加不能接受！
我们肯定希望找到小于O(nlog(n))的算法，甚至是O(n)的算法

### 仍然考虑分而治之的方法：

选取一个锚点（pivot），在O(n)的时间内，将原数组分解为两个数组L和R，元素分别小于或大于锚点。
然后，根据k和len(L)、len(R)的大小关系，将问题转化为在较小的数组中去找出某个数的问题。

### 代码示例：

```python
def select(A,k):
	pivot = findpivot(A)
	L, R = partition(A, pivot)
	if k == len(L) + 1:
		return pivot
	elif k <= len(L):
		return select(L,k)
	else:
		return select(R, k-len(L))
```

### 锚点的选择:

上面的代码示例中，调用了接下来将讨论的findpivot()函数，它是寻找锚点的函数。
锚点的寻找非常关键，这直接关系到分治算法的效率，如果每次都能保证10n/3 < len(L), len(R) < 10n/7，则可以实现分治算法的规模为O(n)。怎么实现呢？
1.将数组A分为5个元素一组的小组，共m = n/5个。
2.分别寻找这m个数组的中位数，记为p1,p2,p3,...pm。
3.寻找这m个中位数的中位数，记为p = SELECT([p1, p2, p3, ... pm], m/2)
4.返回p在A中的指标，这就是较好的锚点

### 现在再看看代码示例：

```python
def select(A,k):
	if len(A) < 50#当A长度较短时，采用排序-选择法更快
		A = mergesort(A)
		return A[k - 1]
	p = ChoosePivot(A)
	L, PivotVal, R = partition(A, p)
	if k == len(L) + 1:
		return Pivotval
	elif k <= len(L):
		return select(L,k)
	else:
		return select(R, k-len(L))
```

**总的复杂度来自于：**
T(n) <= O(n/5)(锚点选择) + O(7n/10)(在最大长度为7n/10的数组上做科学选择，然后返回。这个过程可以递归) + O(n)
**思考：**
O(n)的算法一定快于O(nlog(n))吗？不一定，这是渐进复杂度。
**但事实上：**
上述理论上很好的科学选择法，复杂度甚至大于归并排序（n~10^3的小规模）。
甚至，采用随机选取锚点的方法时，科学选择法有最佳的效率。

## 复杂度记号

O：最坏情况（算法的运行时间不会超过O(f(n))）
>>>>>>> ef1f310e44215bc72cd07152371e45bfa7c7714f
\Omega：最好情况（n足够大时，\Omega(n)给出算法的复杂度下界