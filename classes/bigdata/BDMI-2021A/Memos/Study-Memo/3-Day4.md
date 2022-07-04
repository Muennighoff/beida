# WW4 课堂总结

## 2-3-4 tree

- 可以做到完美平衡
- 是B树最简单的形式，是其过渡形式
- 特征
  - 每一个节点可以放多个key
  - a 2-node has one data element, and if internal has two child nodes;
  - a 3-node has two data elements, and if internal has three child nodes;
  - a 4-node has three data elements, and if internal has four child nodes;
  - 根节点到叶节点路径长度相等
- Search Method
  - Compare serach key against keys in node
  - find suitable interval unitil it becomes leaf node
- Insert Method
  - 使用查找方法找到插入的node
  - 如果插入后超过4-node，那么把当前节点的median key插入到parent node，然后把这个节点变成两个node，再后插入
  - 如果parent node也出现超过4-node的情况，重复上述步骤
- 保证最慢速度增长树的高度
  - worst case lg N
| Algorithm | Average | Worst Case |
| ----- | ----- | ----- |
| Space | O(n) | O(n) |
| Search | O(log(n)) | O(log(n)) |
| Insert | O(log(n)) | O(log(n)) |
| Delete | O(log(n)) | O(log(n)) |




## LLRB tree (Left-leaning red-black tree)

- 特征
  - 实现形式：2-3-4 tree -> BST
  - use red to label internal edges for 3- and 4- nodes
  - 3-nodes should be left-leaning(without right leaf)


## B+ tree

- 索引类型Index Types
  - B树
  - Hash Tables
  
- 特征

  - 每一个的node只保存keys
  - 每一个 node 有 count(keys) + 1 个pointer，分别指向子节点的首位

  - 确定d degree，每一个node 可以有 [d,2d]个key
  - leaf node 之间存在pointer，便于从左向右遍历

- 查找
  - exact key value
    - 从根一直向下查找，与2-3-4 tree 相似
  - range  key values
    - 从inferior往右遍历
  
- 可以保证以最慢的速度增长



## 桶排序与基排序

- 最好情况可以达到O(n)，但是实际需要考虑数据表现
- Bucket Sort
  - 适合 min 和 max 差距不大的情况
- Radix Sort
  - 对least significant digit 进行排序，放入桶中，之后对每一digit的桶进行排序
  - 若使用的是r进制，分配空间与r成正比，时间与r成反比

```python
def bucket_sort(A,min_value,max_value):
    buckets = [[] for i in range(min_value,max_value+1)]
    for x in A:
        buckets[x-min_value].append(x)
    sorted_arr = []
    for bucket in buckets:
        sorted_arr += bucket 
    return sorted_arr

arr =[5,1,2,7,10,3,9,4,0,6,8,12]
sorted_arr = bucket_sort(arr,0,12)
print(sorted_arr)
```

## Hash Table

- 允许更快的insert delete search方法
- 实际上是使用某种映射关系，建立hash_table
- 但是固定的function，可能会让一个bucket非常大
- 如果使用random function, 也可能出现bucket非常大的情况，并且不可重新复制
- 解决方法：可以做一个通用的表，并且使用嵌套的hash function
- 空间使用：
  - n个桶（素数）
- 时间复杂度：一次计算就可以获得位置，O(m)

```python
class HashTable():
    def __init__(self,bucket_num):
        self.buckets = [[] for i in range(bucket_num)]
    
    def insert(self,num):
        self.buckets[(num*7)%5].append(num)
    
    def search(self,num):
        bucket = self.buckets[(num*7)%5]
        for i in range(len(bucket)):
            if bucket[i] == num:
                return ((num*7)%5,i)
                break
        print('Not Find')
                       
    def delete(self,num):
        (i,j) = self.search(num)
        self.buckets[i] = self.buckets[i][0:j] + self.buckets[i][j+1::]

a = HashTable(5)
for i in [2,5,2,6,8,0,9]:
    a.insert(i)
a.search(5)
a.buckets
a.delete(9)
a.buckets
```