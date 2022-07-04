# 第三天课堂笔记 2021/9/29

## 快速排序 Quick Sort

### 基本思想

使用分治的思想，利用递归进行排序。

选定一个 pivot 值，将此外的数字分为两部分，一部分小于等于，一部分大于。再对两部分分别进行排序。排序后进行组合即可。

此外，也可以使用交换的方法排序。首先维护一个不变量 le，这个不变量是一个下标，保证数组下标的数字和之前的数字小于等于 pivot。

对数组进行遍历，如果遇到了小于等于 pivot 的数字，则 le 前进一位，并将两者进行交换。

遍历结束之后，将 pivot 与当前 le 号数字进行交换，再进行递归即可。

### 代码

```python
def quicksort(arr, l, r):
    if l >= r:
        return
    pivot = arr[l]
    le = l  # 不变量：保证 arr[l]...arr[le] <= pivot
    for i in range(l+1, r+1):
        if arr[i] <= pivot:
            le += 1
            (arr[le], arr[i]) = (arr[i], arr[le])
    (arr[l], arr[le]) = (arr[le], arr[l])
    quicksort(arr, l, le-1)
    quicksort(arr, le+1, r)
    return
```

## 链表

### 结构

由一个个节点组成，每个节点携带数据，并且包含下一个节点的地址。

### 链表类的编写

```python
class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self) -> None:
        self.fakeHead=Node(0)

    def append(self, value):
        neoNode=Node(value)
        tail = self.fakeHead
        while(tail.next):
            tail=tail.next
        tail.next=neoNode
        
    def delete(self, value):
        last=self.fakeHead
        head=self.fakeHead.next
        while(head):
            if head.value==value:
                last.next=head.next
            (last,head)=(head,head.next)

    def print(self):
        head=self.fakeHead.next
        while head:
            print(head.value, end=' ')
            head=head.next
        print('')
```

这里注意，在定义链表类时，使用一个假的头结点，能够大幅减少代码复杂度，因为不需要去判断一个节点是否为头结点，进行特殊处理。

## 二元查找树 BST

### BST 结构

使用类似链表的结构，由一个个节点组成。存在一个根节点。

每个节点最多有两个子节点。每个节点的左子树上的数字都比这个节点小，右子树上的数字都比这个节点大。

### BST 搜索

从根节点开始，检查是否相等。相等则直接返回，否则依次检查左子树和右子树，进行递归。

如果最终也没有找到，则返回最后一个查找到的节点，便于之后的插入。

### BST 删除

首先，如果没有左右节点，直接删除即可。

如果没有左节点，则将右节点替代自己的位置。反之亦然。

如果左右节点都存在，则在右子树中找到最接近的节点来替换，并且递归删除。具体操作为：不断在右子树中找左子节点，直到一个节点 A 没有左子节点。将 A 替换到待删除的节点，原 A 节点的位置则由 A 的右子节点代替。

## 红黑树

因为 BST 树可能会有不平衡的现象发生，造成查找、插入、删除的时间复杂度增加，因此引入红黑树，能够达到自平衡。

### 旋转操作

右父亲（父亲的左子节点是自己）变成右子节点（则父亲的左子节点替换为自己原来的右子节点），或左父亲变成左子节点。

### 红黑树原则

1. 节点为红 or 黑
2. 根节点为黑
3. 空节点（占位节点、NIL）为黑
4. 红孩儿是黑
5. 对于每一个节点，到NIL的所有路径上，黑节点个数相等

### 性质

保证树的高度最多为 $2\log(n+1)$
