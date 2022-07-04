# 第3次课堂笔记

# 3.1快速排序
## 3.1.1 BogoSort猴子排序
先假设序列A中的元素都是不一样的
**伪代码：**
```python
BogoSort(A)：
	while true:
		Randomly permuate(A)
		check if A is sorted
		if A is sorted, return A
```
显然，做一次排序需要O(n)的时间复杂度。而排序出正确结果的概率是1/n!，那么BogoSort的时间复杂度是O(n\*n!)。当然，这只是理想情况，最差的情况下，时间复杂度可以趋于正无穷。
## 3.1.2 好的快速排序方法
随机选取一个锚点（pivot）：x = A[i]，然后把序列分成两个部分，小于锚点的、大于锚点的，并且把锚点抽取出来。
采取分治、递归的思路，不断重复上述过程，直至完成排序。
**思考一个问题：**当序列中有重复元素时，怎么办？
1.如果等于锚点，也放到E里面去（和锚点放在一起）。2.不等于锚点，照常处理即可。
**代码实现：**
```python
import random
def QuickSort(A):
    if len(A) <= 1:
        return A
    L = []
    R = []
    p = random.choice(range(len(A)))#随机选择一个pivot
    E = [A[p]]
    for i in range(len(A)):
        if i == p:
            continue
        if A[i] < A[p]:
            L.append(A[i])
        else:
            R.append(A[i])
    return QuickSort(L) + E + QuickSort(R)
test_list = [6,4,2,9,3,8,5,1,7]
print(QuickSort(test_list))
```
**快速排序的时间复杂度：**理想分析的结果，最好是每次都取到中位数，时间复杂度是O(nlog(n))；最坏是每次取最小或最大值，则时间复杂度达到了O(n^2)。但实际上，随机选择锚点不会这么差。
和归并排序比较：前面分析知道，归并排序的最差情况也是O(nlog(n))。归并排序比快速排序更优。
有没有可能，我们得到比O(nlog(n))更快的排序手段？
没有。除非取巧…………例如，stick model
## 3.1.3其他排序方法
桶排序（BacketSort）、基数排序（RadixSort），第四讲会介绍。
## 3.1.4二元查找树
**决策树：**每个节点表示对某个属性的判断，节点的每个分支表示一个判断结果的输出。决策树从根节点出发，最终到达各个叶节点，表示从一个决策判断出发，经过若干次的判断-输出，得到各个分类结果。或者说，每个叶节点储存了一个分类的结果状态。
**二叉树：**至少会有n!片叶子。拥有n!个叶节点的二叉树，如果是completely balanced，则有最矮的高度log(n!)。所以，任何二叉树的最长路径不会低于log(n!)=nlog(n)。

# 3.2链表与有序数组
数据结构：用来存储数的结构组织，是带有结构特性的数据元素的集合。
## 3.2.1链表（linked list）
查找：O(n)量级、删除：O(n)量级、插入：O(1)量级
**下面是实现链表的代码学习（copy）：**
```python
#Linkedlist
#定义一个节点
class Node:
    def __init__(self, value, node = 0):
        self.value = value#节点的value元素：value
        self.next = node#节点的指针元素：next

#再实现列表类
class LinkedList:
    def __init__(self, value = 0, *args):#args表示有很多个参数，后面可以灵活地上传
        self.lenth = 0#初始化列表的长度length，并赋值0
        self.head = 0 if value == 0 else Node(value)
        #根据输入的参数value来创建表头。如果是0，则赋为空？？？？？？？？？？？？？？？？
        #否则，创建一个相应的Node？？？？？？？？？？？？？？？？
        #总而言之，self.head已经初始化为了一个node？？？？？？？？？？？？？？？？？？？
        p = self.head#定义一个指向表头的指针p，此时，p已经是一个Node？？？？？？？？？？？？？？？？？？？？？？
        for i in [*args]:#从*args中的元素开始遍历，依次创建节点Node(i)，并不断用指针指向这些节点，直到链接结束
            node = Node(i)
            p.next = node
            p = p.next
    def printLinkedList(self):
        self.p = self.head#将列表的头节点赋给列表的头指针元素
        while self.p:#当指针不为空时，进行循环
            print(self.p.value)#输出这个指针指向的节点的值
            if not self.p.next:#如果到了末尾节点，即这个尾节点的next为None，则结束循环，并且返回这个节点。
                return self.p
            self.p = self.p.next#否则，我们进入到下一个节点
    def append(self, value):
        new_node = Node(value)#先创建一个新的节点
        cur = self.head#把指针cur指向列表的头节点
        while cur.next != 0:#开始遍历列表，直到列表的末尾
            cur = cur.next
        cur.next = new_node#到末尾后，将新的节点接上
    def insert(self, value):##？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        self.head = Node(value, self.head)#建立一个新节点，并且将新节点的next指针指向原列表的节点？？？？？？？？？？？？？？？
        #而且为什么length不增加一个？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
    def insert_anywhere(self, index, value):
        if self.head is None or index <= 0:#若原列表的头
            self.head = Node(value, self.head)
        else:
            temp = self.head
            while index > 1 and temp.next != None:
                temp = temp.next
                index -= index
            temp.next = Node(value, temp.next)
            self.lenth += 1
    def searchIndex(self, value):
        temp = self.head
        index = 0
        while temp != None and value != temp.value:
            index += 1
            temp = temp.next
        return index
    def delete(self, value):
        index = self.searchIndex(value)#先找到要删除的那个值的指标
        if index <= 0 or self.head.next is None:#指标小于等于0，或没有下一个节点了
            removeItem = self.head.value
            self.head = self.head.next#将下一个节点赋给这个节点。即删除了表头节点
        else:
            temp = self.head#否则，定义一个临时指针指向表头
            while index > 1 and temp.next.next != None:#开始遍历列表，寻找要删除的点
                temp = temp.next
                index -= 1
            removeItem = temp.next.value
            temp.next = temp.next.next
        self.lenth -= 1

l = LinkedList(7,5,3,4,1,2,8)
l.printLinkedList()
print("")
l.insert(4)
l.printLinkedList()
print("")
print(l.searchIndex(4))
print("")
l.delete(4)
l.printLinkedList()
#到此为止，美中不足的是，它只能搜寻、删除单个值。不过这个链表的构建，现在本就是限制在各元素不同的前提下进行的。
```
## 3.2.2有序数组（sorted array)
查找：O(log(n))量级、删除：O(n)量级、插入：O(n)量级

# 3.3二分查找树
Binary search trees (balanced)
查找：O(log(n))量级、删除：O(log(n))量级、插入：O(log(n))量级
**特点：**
节点（node）的联结采用链表的结构，各节点有储存值（key）。
每个节点有两个points指向左右两个节点，称之为它的左右子节点（lchild，rchild）。这个节点又称为两个子节点的父节点（parent）。
没有子节点的节点（或子节点为空）称为叶节点。
**BST的要求：**
每个节点的左子节点，储存值都小于它的储存值；右节点的储存值都大于它的储存值。
如何构造？
1.选取一个数据存入根节点，依据大小关系把其他的数据分为左右两部分，开始插入子节点。
2.用递归的方法，不断进行查找-插入，在根节点的左边或右边进行“生长”。
3.不断递归，直到完成BST的构造。
*回忆，BST和快速排序算法是不是有相似之处？*
## 3.3.2 查找
从根节点开始，不断比较大小
最长时间：最长的路径（树的高度）
## 3.3.3插入
也是从根节点开始，比大小找位置。直接插到某一个数字的下面吗？可以。
## 3.3.4删除
删除操作比较复杂。分几种情况讨论，具体的在后方的代码学习里也有体现。
首先，先检查这个是否存在具有value的节点，即进行查找工作。
找到后，检查其左、右节点是否为空。**如果有，则是较为简单的情形：**左节点为空，就把右节点提上来；右节点为空，就把左节点提上来。
**如果左右节点都不为空，怎么办？**
代码提供了一种思路：前往其右子树的最左边的节点，即从右子树找最小值节点，用这个节点替换被删除的节点即可。但实现方法是比较复杂的，详见代码。
## 3.3.5代码学习
```python
#BST的实现（二元搜索树）
class Node:#先实现节点初始化
    def __init__(self,value):
        self.value = value
        self.lchild = None
        self.rchild = None

class BST:#再实现二叉树类
    #BST的初始化
    def __init__(self, node_list):
        self.root = Node(node_list[0])#直接将node_list的第一位作为根节点
        for value in node_list[1:]:#再将后面位上的数据插入到BST中
            self.insert(value)
    #搜索具有某个值的节点的操作（node是已经有值的节点，作为函数的输入。同时，这个node的母节点也要作为输入？？？？？？？？？？？？）
    def search(self, node, parent, value):#搜索函数
        if node is None:
            return False, node, parent
        if node.value == value:#这个节点的值就是value，那么就返回这个节点
            return True, node, parent
        #小于的在左边，大于等于的在右边
        if node.value > value:
            return self.search(node.lchild, node, value)
        else:
            return self.search(node.rchild, node, value)
    def insert(self, value):
        flag, n, p = self.search(self.root, self.root, value)#从根节点开始，如果根节点的值就等于value，那flag = True，将n和p分别赋值self.root，self.root，完成。
        if not flag:#否则的话，创建一个新的节点，把它挂为p的左孩子或右孩子？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
            new_node = Node(value)
            if value > p.value:
                p.rchild = new_node
            else:
                p.lchild = new_node
    def delete(self, value):
        flag, n, p = self.search(self.root, self.root, value)
        if flag is False:
            print("Can't find the key! Delete failed!")
        else:
            if n.lchild is None:#当这个节点的左子树是None时
                if n == p.lchild:
                    p.lchild = n.rchild#如果这个节点是父节点的左节点，就把它的右节点接到父节点的左节点上。下面同理
                else:
                    p.rchild = n.rchild
            elif n.rchild is None:#当这个节点的右子树是None时
                if n == p.lchild:
                    p.lchild = n.lchild
                else:
                    p.rchild = n.lchild
            else:
                #左右节点都不为空的情况，下面开始讨论。
                #先直接把右子树拿出来：
                pre = n.rchild
                if pre.lchild is None:
                    #右子树的左节点为空时，直接把右节点拿上去即可：
                    n.value = pre.value#先把原节点赋值为右节点的值
                    n.rchild = pre.rchild#再把右节点的右子树挂到右边来
                else:
                    #pre的左子树不为空怎么办？又找它的左子树，一直找，找到为空为止，然后把n的左子树挂上去
                    next_ = pre.lchild
                    while next_.lchild is not None:
                        pre = next_
                        next_ = next_.lchild#不断前往左节点
                    #到此时，next_是左节点为空的节点。pre是next的父节点
                    n.value = next_.value#next_的值，是n的右子树的最小值，但又比左子树的所有值都大。现在把它赋给n，没有破坏性质。
                    pre.lchild = next_.rchild#由于已经拿走了next_本身，所以把它的右子树接到next_的父节点上
                    #总而言之，就是在右子树中找到最小值所在的节点，把这个节点提升为原节点！！！！！！！！！！
```

# 3.4红黑树、查找、自平衡
如果BST的高度很高，不平衡，则BST的搜索速度可能退化到链表。
那么，降低BST的高度？如何把unbalanced的树变得balanced？
idea 1：旋转（rotation）：把重的那一头拎起来。
idea 2：达到近似平衡，have some proxy for balance。因为完美平衡是很难的。
而**红黑树**可以达到自动平衡。这是由于红黑树的要求决定了的，达到的结果为：在红节点不太多的情况下（红节点是稀疏的），**黑节点**是几乎平衡的。

**红黑树的条件限制：**
1.每个节点都要染色。根节点和叶节点是黑色。
2.红节点的子节点是黑色。
3.从任意一个节点出发走到空节点，经过的黑节点数目必须相同。
那么，有n个非空节点的红黑树的高度，最多是2log(n+1)。