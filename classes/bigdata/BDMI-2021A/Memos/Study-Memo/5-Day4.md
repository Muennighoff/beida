# 学习小结 202101006

#### 尹哲良

## 2-3-4树

### 性质

+ 完美平衡：根节点到叶节点路径长度相等
+ 一个节点可以放多个数
+ children=key+1

### 功能

+ 查找：与key比较大小进入children
+ 插入
  + 2-node和3-node叶节点增加一个key
  + 4-node叶节点把中间key递归插入到上面

### LLRB

+ 把2-3-4数转化为BST，用红边连接3/4节点
+ 左倾：保持平衡

## B+树

性质与排序数组类似

### 基础知识

+ 参数d：每个节点有至少d至多2d个key
+ 某个节点有m个key的同时又m+1个指针，前m个指向子节点，最后一个指向右兄弟节点
+ 具体信息组织在叶节点上

### 插入过程

+ 超过3个key就分裂，可能增加高度

### 范围查找

+ 例如：年龄小于等于25，与精确查找相对应
+ 精确查找到一个节点

## 桶排序和基排序

### 性质

在比较好的情况下复杂度为O(n)

### 步骤

+ 根据最小值和最大值建桶

+ 将值放入桶

+ 把桶连结起来

### 问题

数据极差很大，需要很多桶

### 基数排序

+ 先对低位排序，后对高位排序
+ 复杂度：O(d(n+r))，d是排序次数，r是桶的个数

## 哈希结构

### 简单形式

1. 数据放到一组桶里，每个桶里有一个值，问题是我们可能需要很多桶
2. 按照末位建桶，数据可能聚集在少数桶里

### 注意事项

+ 元素集合大小为M，M可以很大，需要存储的元素数量n可以很小
+ 哈希函数：元素到某一特征（末尾数字）的映射，一个元素只能有一个哈希值，进入一个桶
+ 根据元素值找元素的位置

### 随机函数

+ 目的：防止人为提供一个worst case
+ 同样可能出现worst case
+ 如果桶的数目等于元素个数，则查找某个元素，预期该桶中元素数不大于2
+ 问题：桶太多，函数也太多，都需要存储
+ 解决方案：选取随机函数的一个子集