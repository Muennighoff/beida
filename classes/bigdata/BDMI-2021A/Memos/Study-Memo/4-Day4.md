# Day 4 Summary

[TOC]

## 2-3-4 tree

性质：Perfect Balance, Every path from root to leaf has same length

* 2-node: 1 key, 2 children
* 3-node: 2 keys, 3 children
* 4-node: 3 keys, 4 children

Tree height:

* worst case: $lg(N)$ [all 2-nodes]
* Best $log(4N)$ [all 4-nodes]
* Between 10 and 20 for 1 million nodes
* Between 15 and 30 for 1 billion nodes (较低的高度能储存足够多的数)

Transfer: need to convert a 4-node into a combination of 2 and 3 nodes if a new node is added to a 4-node.

## B+ Tree

Index 索引

B tree是如今数据库系统中的基本形式。2-3-4 tree是B tree的最简单形式。B+ tree 是B tree的变种。

each node can have $d\le number \le 2d$ keys

### 查找B+ tree：

* 精确查找：  start at root node and process down
* 范围查找：search a certain node, and there traverse

## Bucket and Radix Sort 桶排序和基排序

Bucket Sort 桶排序：

```python
#%% bucket sort
def bucket_sort(A, min_value, max_value):
    buckets = [[] for _ in range(min_value,max_value+1)] #创建从min到max每个值的bucket
    for x in A:
        buckets[x-min_value].append(x) #把数值放入对应的bucket
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)   #把所有bucket合起来
    return sorted_arr

list = [5,1,2,7,3,9,4,0,6,8]
print(bucket_sort(list, 0, 9))
```

Radix Sort 基数排序：依次对个位、十位、百位进行bucket sort

复杂度：O(nd) d为最大数字的位数。注意此时已经受到最大值影响，而一般排序不会。

注意代码中略去了一些函数。

```python
def radix_sort(A, n_digits, base):
    B = [ myInt(x, base=base) for x in A ]
    for j in range(n_digits):
        for x in B:
            x.updateKeyDigit(j)
        B = bucketSortBase(B, base)
    B = [x.getValue() for x in B]
    return B
```

 ## Hash 表

查找极快，但空间需要大（$O(n log(M))$的空间大小），最优可以在$O(1)$时间内查找。一次计算，即可找到位置

结合之前在数据结构算法课内容，下给出一个简单的Hash实现：

需要关注的点：

* 要有Hash函数来编码，该编码决定了bucket要如何设置
* 需要有一个rehash的过程解决冲突，比如课件中的随机数

```python
class HashingTable:         
    def __init__(self,size = 11):
        self.size = size
        self.data = [None]*self.size
        self.slots =[None]*self.size

    def hashfunction(self,key):     #hash值生成规则为：取11的余数
        return key % self.size

    def rehash(self,oldhash):
        # return (oldhash+1) % self.size
        return  oldhash + 1     #用来解决原先找到size末尾后会回到开头的问题。
    #取1其实会导致ppt中所说数据过于集中的问题，实际操作时应当取3、5等数字来保证数据相对分散，以提升效率。此处取1是为了方便阐述

    def put(self,key,data):
        realSize = self.size
        Lambda = self.len()/realSize        #负载因子。单独设置一个realSize来记录不断变化的列表长度
        if Lambda >= 0.5:                   #负载因子大于0.5则分别给slots和data列表后面添上一个新的元素。这个临界值其实可以修改，
                                            # 但要保证不会出现"添加一个已经无法解决问题"的情况，即lambda不能太过贴近1
            self.slots.append(None)
            self.data.append(None)
            realSize += 1

        hashvalue = self.hashfunction(key)
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data     #若对应列表为空，那么直接放入
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data #replace
            else:
                nextslot = self.rehash(hashvalue)
                while self.slots[nextslot] != None and \
                    self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot)
                if self.slots[nextslot] == None:
                    self.slots[nextslot]=key
                    self.data[nextslot]=data
                else:
                    self.data[nextslot] = data #replace

    def __setitem__(self, key, value): #可以调用H[2]=4形式
        self.put(key,value)

    def get(self,key):
        startslot = self.hashfunction(key)
        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and \
            not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position)
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, item):
        return self.get(item)

    def __delitem__(self, key):
        hashvalue = self.hashfunction(key)
        for i in self.slots[hashvalue:]:
            if i == key:
                dataindex = self.slots.index(i)
                self.slots.remove(i)
                self.data.pop(dataindex)
            else:
                return None     #不确定，现实中del方法在删去不存在的元素时会直接报错，这里填一个None来解决一下。


    def len(self):
        total = 0
        for i in range(self.size):
            if self.slots[i] != None:
                total += 1
        return total

    def __contains__(self, key):
        if self.get(key) == None:
            return False
        else:
            return True
          
H = HashingTable()
H.put(7,'Alice')
H.put(18,'Bob')
H[8] = 'Andrew'
H[1] = 'X'
H[12] = 'Y'
H[23] = 'J'
H[34] = 'J'
H[45] = 'J'
H[56] = 'J'
H[67] = 'J'
H[78] = 'J'
H[89] = 'K'
print(H.get(89))
# H[100] = 'J'
# H[111] = 'J'
print(H.slots)
```

