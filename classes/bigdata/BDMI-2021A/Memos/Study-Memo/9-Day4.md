# 第4次课堂笔记

## 4.1回顾了第三次课的内容
快速排序，链表，有序数组，二分查找树，红黑树
课程目标：认识到排序和查找结构是大数据系统的基本模块；了解机器智能系统的基本原理和操作

## 4.2 2-3-4树
2-3-4树能做到完美平衡（perfect balance）——从根节点到任何叶节点通过的路径都是相等的。
### 结构：
是对BST的推广，允许每个节点有1、2、3个值，从而有2、3、4个子节点。分别称之为2-node，3-node，4-node。这也是2-3-4树名字的来由。
### 查找：
首先和根节点的keys相比，根据比较结果，前往相应的子节点。直到找到结果为止。
### 插入：
**1.**首先，对要插入的值进行查找。
**2.**找到后，将位于底部的2-node变为3-node；将位于底部的3-node变为4-node。
**3.**如果找到发现底部就是4-node呢？此时没有空间留给这个值了，需要旋转-平衡操作。
具体的，有不同算法来应对：
3.1当4-node上方是2-node时。将4-node的中间值拉上去，这个4-node变成了3-node；上方的2-node变成了3-node。之后再将下方的已变成3-node的节点又拆分成两个2-node，再将新值插到其中一个node中。
3.2当4-node上方是3-node时。将4-node的中间值拉上去，这个4-node变成了3-node；上方的3-node变成了4-node。之后再将下方的已变成3-node的节点又拆分成两个2-node。
### 高度：
最坏的情况，也就是log_2 N。（全是2-node）
最好的情况，是log_4 N。（全是4-node）
### LLRB Trees：
将2-3-4树变为RBT的算法。具体的，就是将3-node、4-node拆分成2-node。
### B+树
组织数据：排序
索引：帮助查到数据的数据结构。图书馆里对书籍进行组织，排列的常用结构。
**B+树**就是一种索引类型。对排好的数据，非常适合范围查询。
精确查找：从根节点开始，往下查找，直到叶子节点。
范围查找：先找最小值，然后从小到大进行遍历。

## 4.3桶排序与基排序（Bucket and Radix Sort）
在比较好的情况下，甚至达到O(n)的复杂度，这是最理想的复杂度。
### Bucket Sort
建造从最小值到最大值之间的“桶”，将数字塞进各个桶里（一次遍历），再将各个桶串联在一起（一次常数规模），就完成了排序。
问题：比较适合的数据进行桶排序是合理的。数据的最小值和最大值差距特别大时，不适合桶排序。
**代码实现：**
```python
#桶排序
def bucket_sort(A, min_value, max_value):
    buckets = [[] for _ in range(min_value, max_value + 1)]
    for x in A:
        buckets[x - min_value].append(x)
    sorted_arr = []
    for bucket in buckets:
        sorted_arr += bucket
    return sorted_arr
arr = [5,1,2,7,3,9,4,0,6,8]
print(bucket_sort(arr,0,9))
```
### Radix Sort
**方法：**先对个位数进行桶排序。然后，依次对十位、百位……进行桶排序。多次桶排序后（取决于最大数字的位数），能完成排序。
当最大位数为d时，算法复杂度为：O(nd)。
通常情况下，d随着n增大而增大。增加的速度通常也是log(n)，所以Radix排序退回到Merge Sort的速度。
**改进：**可以依据数据的特点来改变进制。换用更大的r进制：一方面，每次桶排序需要更大数量的桶；另一方面，可以减少排序迭代的次数。
数组的最大最小值，会影响排序效果。

## 4.4哈希结构（Hashing）
哈希表是一种可以对数据进行快速插入、删除、寻找的数据结构。
哈希表的背后，是哈希族。Universal hash family更有magic。
哈希函数（hash function），决定每个元素应该去哪个桶，然后组成哈希表。
**平凡的哈希函数：**
例如，依据末位数字进行分类：h(13) = 3，h(43) = 3，h(9) = 9。
（或者选取别的进制，例如，模5，乘7模5，等等）
但容易发生坏情况：数据集中在某一个桶里。而且，对于deterministic hash fuction，很坏的情况总是存在的。这被称为**“哈希爆炸”**。
**随机哈希函数：**
为了减小哈希爆炸的概率，引入non-deterministic hash function（随机性），即随机哈希函数。
思路1：对应关系选取uniformly random distribution function，**可行吗？**
缺点：需要把h(x)也记录下来。并且，不能保证桶是平衡的。
思路2：额外加限制条件，例：限制每个桶的元素不超过2个。这样可以满足桶是平衡的，每个链表不会太长。
**哈希族：**
可以从一族哈希函数随机选取哈希函数。这个哈希函数的集合就是哈希族。
通用哈希族的作用：可以减小发生碰撞的概率。
例如，对数据做变换（例如，a\*x + b）后再输入哈希函数，而对a、b的随机选取则构成了哈希族。

下面是对实现哈希结构的代码学习记录（copy）：

```python
#定义哈希表
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from random import choice
%matplotlib inline

class HashTable:
    def __init__(self, h, n):
        #n是buckets的数目
        self.h = h#哈希函数的定义
        self.buckets = [[] for i in range(n)]
    def insert(self, x):
        self.buckets[self.h(x)].append(x)#向哈希函数h指向的buckets存入x
    def delete(self, x):
        bucket = self.buckets[self.h(x)]#找到x所在的bucket
        for i in range(len(bucket)):
            if bucket[i] == x:
                return bucket.pop(i)
        return None
    def find(self, x):
        bucket = self.buckets[self.h(x)]
        for i in range(len(bucket)):
            if bucket[i] == x:
                return bucket[i]
        return None

#再定义一个取个位数的哈希函数
def xModn(x, n = 10):
    return x%n
#实现一个哈希表的实例
HT = HashTable(xModn, 10)
x = 1234567
y = 76554334234
HT.insert(x)
#检验是否可行
if HT.find(x) == x:
    print("OK!")
else:
    print("Wrong!")
if HT.find(y) == None:
    print("OK!")
else:
    print("Wrong!")

#尝试一个均匀分布的哈希函数
#def randomFn(x, n = 10):
#    return choice(range(n))#随机把x映射到一个函数上，但是，显然这样是不行的。因为，存入和查找时调用哈希函数，随机得到不同的结果！！！

#生成一个均匀分布的哈希函数，从range(M)映射到range(n)
def generateUniformlyRandomHashFunction(M, n = 10):
    fnTable = [ None for i in range(M)]#fnTable有M个缺省值
    for x in range(M):
        fnTable[x] = choice(range(n))#用fnTable记录M个值对应的函数值
    def randomFn(x):
        return fnTable[x]#定义了一个查询哈希函数的函数
    return randomFn#返回上面这个查询函数
#然后生成一个函数：
randomFnTake2 = generateUniformlyRandomHashFunction(1000, 10)#只调用一次，生成一个从1000映射到10的哈希函数
HT2 = HashTable(randomFnTake2, 10)#这个哈希表肯定是OK的，

#现在的问题是，如果想要哈希函数有很大的定义域怎么办？
#例如：140位的字符串。由于ASCII码表有128个，所以定义域高达128**140
#下面介绍Universal Hash Families
#从一族函数里，随机选择一个成为哈希函数
#一个不好的哈希族：
def leastSigDig(x, n = 10):#得到x的个位数
    return x%n
def mostSigDig(x, n = 10):#得到x的最高位数
    if x == 0:
        return 0
    while x > 0:
        last = x%n
        x = (x/n).__trunc__()#向下取整，直到x只剩下最高位时，会得到0，终止循环
    return last
#一个好一点的哈希族：
def generateUniversalHashFn(a, b, p, n = 10):
    def f(x):
        r = (a*x + b)%p
        return r%n#f的返回值是一次函数ax+b，再求对p余数，再求个位数
    return f#返回函数名f

#哈希爆炸的概率
def getCollisionProbabilities(hashFamilyFn, M, trials = 100):
    data = []
    for x in range(M):#M是定义域
        for y in range(x + 1, M):
            countxy = 0
            for t in range(trials):#t是试验次数
                h = hashFamilyFn()
                if h(x) == h(y):
                    countxy += 1
            data.append(countxy/trials)
    return data

#尝试一个实例：
M = 100
n = 10
p = 101#大于100的最小质数
#现在，从三个哈希族里分别选取一个哈希函数
def drawFromBadHashFamily():
    return choice([leastSigDig, mostSigDig])#选“取个位”“取最高位”之一
def drawFromGoodHashFamily():
    a = choice(range(1,p))#选一个非零的数做位比例
    b = choice(range(p))#选一个常数
    return generateUniversalHashFn(a,b,p)
def drawFromBestHashFamily():
    return generateUniformlyRandomHashFunction(M, n)
dataBad = getCollisionProbabilities(drawFromBadHashFamily, M, trials = 1)
dataGood = getCollisionProbabilities(drawFromGoodHashFamily, M, trials = 1)
#dataGreat = getCollisionProbabilities(drawFromBestHashFamily, M, trials=100)
#print(dataBad)
#print(dataGood)
#print(dataGreat)
```