# WW3 课程总结



## QuickSort
- Bogosort
  - 对于一个array，重新随机打乱（在array中无放回抽取），观察是否为有序列
  - 时间复杂度 为 O (n · n! )，最差的情况是 infinite
- Quicksort
  - 选择一个pivot，分成大于和小于两个部分，然后分别对L、R进行QuickSort
  - 可以借此产生decision tree进行分析
  - 最差情况（每一次都抽到min、max）
  - 时间复杂度以及最差情况时间复杂度（每一次都抽到min、max）
$$
O(nlog(n))
$$
$$
O(n^{2})
$$


```python
import random 
def QuickSort(A):
    if len(A) <= 1:
        return A
    L = []
    R = [] 
    p = random.choice(range(len(A)))
    E = [A[p]]
    for i in range(len(A)):
        if i == p:
            continue
        if A[i] < A[p]:
            L.append(A[i])
        else:
            R.append(A[i])
    return QuickSort(L) + E + QuickSort(R)
QuickSort([2,62,79,2,9,-2])
```

- Comparison-based sorting algorithms
  - 类似decision tree的模式，通过对比进行排序
  
  - 最优时间复杂度
$$
O(log(n!)) \approx O(nlog(\frac{n}{e})) = O(nlog(n))
$$


## Linked List  & Binary Search Tree

- 链表
  - 插入操作的时间复杂度为 O(1)
  - 搜索、删除的时间复杂度为 O(n)
```python
class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

    def addNext(self,next):
        self.next = next


class LinkedList():
    def __init__(self,head):
        self.head = head
    
    def traverse(self):
        current = self.head
        lst = []
        while current is not None:
            lst.append(current.value)
            current = current.next
        return lst
        
    def add(self,node):
        nxt = self.head.next
        self.head.next = node
        node.addNext = nxt
    
    def drop(self,num):
        previous = None
        current = self.head
        nxt = current.next
        while current.value != num:
            previous = current
            current = current.next
            nxt = current.next
        previous.addNext(nxt)


a = Node(1)
b = Node(0)
c = Node(2)
d = LinkedList(a)
for i in [b,c]:
    d.add(i)
print(d.traverse())
d.drop(0)
print(d.traverse())         
```
- 有序数组
  - 插入操作 O(n)
- 二元搜索树
  - 概念：根、节点、值、叶 root node key leaves
  - 每一个node有key
  - 构建要求：一个节点的所有位于左边（以及左下）的子节点小于它，右边的子节点大于它
  - 思路：快速排序：选择pivot，变成分成大于、小于两部分 之后是递归操作
   - 产生的树并不唯一
  - 遍历的过程是O(n)级别的复杂度
  - 删除操作
    - 删除叶子结点、只有一个descendant都是简单的情况
      - 前者直接删除，后者需要把子节点提上去
      - 有两个descendants的比较复杂
      - 如果左子树为空，直接将右子树上移；如果左子树不为空，那么将右子树的左子树依次上移
  - 查找时间
    - 受到的树的高度的影响，不平衡的树甚至会达到O(n)
    - 平衡的方法
      - rotation 将左节点、右节点向右、向左旋转
        - 使用算法自动平衡
      - 红黑树 
        - 特征：黑色是好的排序的节点，红色vice versa
        - 要求：
        - 根节点必须是黑色的
        - NIL 子节点必须是黑色
        - 红节点的孩子必须是黑色的
        - 等路径条件：对于所有的node x 到NIL节点的所有path上的黑节点一样多
        - 插入/删除
          - 插入三种情况
          - 插入红节点于全部黑节点，直接插入
          - 黑——红红
```python
class Node():
    def __init__(self,value,left = None,right = None):
        self.value = value
        self.left = left
        self.right = right

    def addLeft(self,node):
        self.left = node
        
    def addRight(self,node):
        self.right = node
    
    def getValue(self):
        return self.value

class BinarySearchTree():
    def __init__(self,root):
        self.root = root
    
    def getRoot(self):
            return self.root
            
    def in_order_traverse(self,node):
        if node is not None:
            self.in_order_traverse(node.left)
            print(node.value)
            self.in_order_traverse(node.right)
            
    def pre_order_traverse(self,node):
        if node is not None:
            print(node.value)
            self.pre_order_traverse(node.left)
            self.pre_order_traverse(node.right)
    
    def post_order_traverse(self,node):
        if node is not None:
            self.post_order_traverse(node.left)
            self.post_order_traverse(node.right)
            print(node.value)
            
    
    def insert(self,node,current,parent):
            if self.root == None:
                self.root = node
            else:
                if current is not None and node.value < current.value:
                    self.insert(node,current.left,current)   
                elif current is not None and node.value >= current.value:
                    self.insert(node,current.right,current)
                if current is None and node.value < parent.value:
                    parent.addLeft(node)
                elif current is None and node.value >= parent.value:
                    parent.addRight(node)
                    
        
    
a = Node(-3)
b = Node(5)
c = Node(2)
d = BinarySearchTree(a)
for item in [b,c]:
    d.insert(item,d.root,d.root)
d.post_order_traverse(d.root)
```