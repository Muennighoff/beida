### 第1 B+树


- B+ Tree or just B-Tree
    - Generalization of BST, allowing for nodes with >2 children
    - Useful in systems where large blocks of data need to read/written
    - All leaves are at same lowest level (balanced)
    - SEARCH/INSERT/DELETE: O(log(n))
    - Space: O(n)


### 第2 Bucket & Radix Sort

- 复杂度最低 - O(n) (This is the theoretical lower limit for sorting)

- Bucket Sort: Just put elements in respective buckets
    - Problem: Need to know value distribution ahead of time
        - > Else we might need millions of buckets
        - Trades time for space

```python
def bucket_sort(A, min_value, max_value):
    buckets = [[] for _ in range(min_value, max_value+1)]
    for x in A:
        buckets[x].append(x)
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend([num for num in bucket])
    return sorted_arr

arr = [5, 1, 2]
sorted_arr = bucket_sort(arr, 0, 5)
sorted_arr
```



- Radix Sort: Put elements in buckets based on their digits, starting with the last digit
    - > Will only need 10 buckets for base 10
    - O( num_digts * n )
    - How to choose the base?
        > The higher the more space required as more buckets
        > The lower the more iterations required as less buckets


```python
def getDigits(x, base):
    digits = []
    while x > 0:
        digits.append( x % base )
        x = (x / base).__trunc__()
    return digits
        

class myInt:
    def __init__(self,x, base=10, keyDigit=0):
        self.digits = getDigits(x, base)
        self.keyDigit = keyDigit
        self.value = x
        
    def key(self):
        if len(self.digits) > self.keyDigit:
            return self.digits[self.keyDigit]
        return 0
    
    def updateKeyDigit(self,p):
        self.keyDigit = p
        
    def getValue(self):
        return self.value

def bucketSortBase(A, base):
    buckets = [[] for _ in range(base)]
    for x in A:
        buckets[x.key()].append(x)
    sorted_arr = []
    for bucket in buckets:
        sorted_arr = sorted_arr + bucket
    return sorted_arr

def radix_sort(A, n_digits, base):
    B = [ myInt(x, base=base) for x in A ]
    for j in range(n_digits):
        for x in B:
            x.updateKeyDigit(j)
        B = bucketSortBase(B, base)
    B = [x.getValue() for x in B]
    return B

arr = [99999,888,5555,77777,8888888]
sorted_arr = radix_sort(arr, 7, 10)
print(sorted_arr)
```



### 第3 Hash函数


- Hash Table
    - Array of n buckets with each bucket storing a linked list
    - Example of Hash Func: Store by least significant digit (bad hash function but works)
    - INSERT/SEARCH/DELEATE in O(1) expected time
    - With O(n log(M)) required space
        - O(n) buckets
        - O(n) items with log(M) bits per item
        - O(log(M)) to store the hash functions
        - Hashing a universe of size M into n buckets, where at most n of the items in M ever show up



```python
class HashTable:
    """
    Args:
      h: Hash Function
      n: Number of buckets
    """
    def __init__(self, h, n):
        self.h = h
        self.buckets = [ [] for i in range(n) ]
        
    def insert(self, x):
        self.buckets[self.h(x)].append(x)
        
    def delete(self,x):
        bucket = self.buckets[self.h(x)]
        # O(n) to look for x in the bucket.
        for i in range(len(bucket)):
            if bucket[i] == x:
                return bucket.pop(i)
        return None
        
    def find(self,x):
        bucket = self.buckets[self.h(x)]
        # O(n) to look for x in the bucket.
        for i in range(len(bucket)):
            if bucket[i] == x:
                return bucket[i]  
        return None


# 乘以7模5
def hash_func(x):
    return (7*x)%5


HT = HashTable(hash_func, 10)

array = [7,5,3,4,1,2,8]

x = 9
y = 4

HT.insert(x)
HT.delete(y)

print(HT.find(x) == x)
print(HT.find(y) == y)
```
