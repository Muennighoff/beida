### 第1 Quick Sort

猴子排序 / Bogo Sort
- 1) Randomly permute sequence
- 2) Check if correct
- 3) Repeat
- Worst case complexity: O(n! * n)
- Worst case: Does never find the solutin


Quicksort:
- Average case: O(nlog(n))
- Worst case: O(n^2)

练习 - Quicksort：
```python
import random

def quicksort(A):
    if len(A) <= 1:
        return A
    L, R = [], []
    pivot_idx = random.choice(range(len(A))) 
    pivot_val = A[pivot_idx]
    for i in range(len(A)):
        if i == pivot_idx:
            continue
        if A[i] < pivot_val:
            L.append(A[i])
        else:
            R.append(A[i])
    return quicksort(L) + [pivot_val] + quicksort(R)

quicksort([2,5,3,6,7,21,51,24,11,50])
```

### 第2 LinkedList

练习 - LinkedList

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, array):
        self.head = Node(array[0])

        cur = self.head
        for val in array[1:]:
            cur.next = Node(val)
            cur = cur.next

    def append(self, val):
        new_node = Node(val)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def __len__(self):
        cur = self.head
        count = 1
        while cur.next is not None:
            cur = cur.next
            count += 1
        return count

    def __repr__(self):
        out = f"{self.head.val}"
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            out += f", {cur.val}"
        return f"[{out}]"

    def get(self, idx):
        """
        idx should be zero-indexed - i.e. first node: idx=0
        """
        cur = self.head
        for _ in range(idx):
            cur = cur.next
        return cur.val

    def delete(self, idx):
        cur = self.head
        pre = None
        for _ in range(idx):
            pre = cur
            cur = pre.next
        if pre:
            pre.next = cur.next
            del cur
        # Do not handle zero-element LinkedLists for now
            


array = [2, 3, 5, 4]
ex = LinkedList(array)

assert ex.get(1) == array[1]
assert str(ex) == str(array)
ex.append(5)
assert ex.get(4) == 5
assert len(ex) == 5
ex.delete(4)
assert str(ex) == str(array)
```


### 第3 Binary Search Tree

- BST:
- Key Operations - All O(Height) = O(N)
    - Search: May take O(N) if completely 斜 
    - Insert: O(N), as needs to be inserted at bottom
    - Delete: 3 Cases: 
        - No child: Delete directly
        - One child: Replace with child
        - Two children: Replace with smallest 
    - In Order Traversal > Get a sorted list right away

```
def inOrderTraersal():
    if x!= NULL:
        inOrderTraersal(x.left)
        print(x.key)
        inOrderTraersal(x.right)
```

- If we can balance it --> (log(n))
    - 完美平衡： 每个节点都有两个子节点
    - 红黑树 - Requirements：
        - Each node is red/black
        - All NIL (=final hypothetical) nodes are black
        - A red node does not have a red child
        - Every path from a given node to a descendant NIL node goes through the same num of black nodes (> Will make it balanced) 
        - [The root is black]
    - 红的节点越少越平衡
    - 高度： $2\log(n+1)$


