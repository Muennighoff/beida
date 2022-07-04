# Day4 04

[TOC]

## Quick Sort

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
        elif A[i] < A[p]:
            L.append(A[i])
        else:
            R.append(A[i])
    return QuickSort(L) + E + QuickSort(R)

if __name__ == "__main__":
    test = [2,3,1,4,1,2,3,1,2]
    print(QuickSort(test))
```

### Compare with Merge Sort:

Merge Sort: $O(n\log n)$ no matter what.

Quick Sort: Worst: $O(n^2)$  Expected: $O(n\log n)$

### Steps

1. pick a pivot
2. partition the array into bigger than pivot and less than pivot
3. Do QuickSort again to "Bigger" and "Less" group.

## Data Structure: 链表(linked list)与有序数组(sorted array)

### linked list

$\square \rightarrow \square \rightarrow\square \rightarrow\square \rightarrow \square$ code: using class

```python
#%% linked list
class node:
    def __init__(self,key=None):
        self.key=key
        self.next=None
         
class linked_list:
    def __init__(self):
        self.head=node()

    # Adds new node containing 'key' to the end of the linked list.
    def append(self,key):
        new_node=node(key)
        cur=self.head
        while cur.next!=None:
            cur=cur.next
        cur.next=new_node

    # Returns the length (integer) of the linked list.
    def length(self):
        cur=self.head
        total=0
        while cur.next!=None:
            total+=1
            cur=cur.next
        return total 

    # Prints out the linked list in traditional Python list format. 
    def display(self):
        elems=[]
        cur_node=self.head
        while cur_node.next!=None:
            cur_node=cur_node.next
            elems.append(cur_node.key)
        print(elems)

    # Returns the value of the node at 'index'. 
    def get(self,index):
        if index>=self.length() or index<0: # added 'index<0' post-video
            print("ERROR: 'Get' Index out of range!")
            return None
        cur_idx=0
        cur_node=self.head
        while True:
            cur_node=cur_node.next
            if cur_idx==index: return cur_node.key
            cur_idx+=1

    # Deletes the node at index 'index'.
    def erase(self,index):
        if index>=self.length() or index<0: 
            print("ERROR: 'Erase' Index out of range!")
            return 
        cur_idx=0
        cur_node=self.head
        while True:
            last_node=cur_node
            cur_node=cur_node.next
            if cur_idx==index:
                last_node.next=cur_node.next
                return
            cur_idx+=1

    # Allows for bracket operator syntax (i.e. a[0] to return first item).
    def __getitem__(self,index):
        return self.get(index)


    #######################################################

    # Inserts a new node at index 'index' containing key 'key'.
    # Indices begin at 0. If the provided index is greater than or 
    # equal to the length of the linked list the 'key' will be appended.
    def insert(self,index,key):
        if index>=self.length() or index<0:
            return self.append(key)
        cur_node=self.head
        prior_node=self.head
        cur_idx=0
        while True:
            cur_node=cur_node.next
            if cur_idx==index: 
                new_node=node(key)
                prior_node.next=new_node
                new_node.next=cur_node
                return
            prior_node=cur_node
            cur_idx+=1

    # Inserts the node 'node' at index 'index'. Indices begin at 0.
    # If the 'index' is greater than or equal to the length of the linked 
    # list the 'node' will be appended.
    def insert_node(self,index,node):
        if index<0:
            print("ERROR: 'Erase' Index cannot be negative!")
            return
        if index>=self.length(): # append the node
            cur_node=self.head
            while cur_node.next!=None:
                cur_node=cur_node.next
            cur_node.next=node
            return
        cur_node=self.head
        prior_node=self.head
        cur_idx=0
        while True:
            cur_node=cur_node.next
            if cur_idx==index: 
                prior_node.next=node
                return
            prior_node=cur_node
            cur_idx+=1

    # Sets the key at index 'index' equal to 'key'.
    # Indices begin at 0. If the 'index' is greater than or equal 
    # to the length of the linked list a warning will be printed 
    # to the user.
    def set(self,index,key):
        if index>=self.length() or index<0:
            print("ERROR: 'Set' Index out of range!")
            return
        cur_node=self.head
        cur_idx=0
        while True:
            cur_node=cur_node.next
            if cur_idx==index: 
                cur_node.key=key
                return
            cur_idx+=1
            
if __name__ == "__main__":
    ll = linked_list()
    ll.display()
    ll.head = node(8)
    ll.insert(1,7)
    ll.insert(2,10)
    print(ll.length())
    ll.display()
```

### Sorted array

$\square \square \square \square\square \square \square \square \square$.  Notice that each following node would have to move forward if a new element is inserted.

## Data Structure: 二分查找树Binary Search Tree

Every LEFT node is smaller than the precedent node

Every RIGHT node is larger than the precedent node

Notice that everything on the LEFT should be smaller than it, vice versa.

How to build:

1. select a root node
2. select two nodes as LEFT and RIGHT
3. keep doing step2

Traverse: In-Order-Traverse a BST would return a sorted list.

Search: O(height), where height is the longest path from root to leaf

## 红黑树，2-3-4树， B+树

### 红黑树

Goal: Fast Search/Insert/Delete operation in the BST

Balanced Binary Search Tree, $O(\log(n))$ for all 3 operations

Rules:

* Root Node must be black.
* Red nodes must have black children.
* All path from any node to NIL's must have the same number of black nodes on them
* NIL is regarded as black nodes.

conjecture: the height of a red-black tree with n nodes is at most 2 log(n)



## 通排序(bucket sort)与Hash



