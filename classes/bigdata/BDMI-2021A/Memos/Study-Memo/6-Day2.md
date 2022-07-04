### 第1 Python Paths

Get full path:
```python
import os
os.path.realpath('xyz.txt)
```

练习1：
```python
classmates = ["张", "林", "陈"]
with open("myclassmates.txt", 'w') as f:
    f.write("\n".join(classmates))

with open("myclassmates.txt", 'a') as f:
    f.write("\n王")
```


练习2：
```python
import random
nums = []
for x in range (0, 100):
    nums.append(random.randint(0, 9999))
with open("random_nums.txt", "w"):
    f.write("\n".join(nums))
```


### 第2 Sorting

Insertion Sort 插入排序:
- 每次都要调用位置
- Running time O(n^2) 

Merge Sort 合并排序:
- Divide & Conquer
- Break the list down until units of 1 (If just 1 always sorted)
- Compare 1 by one and build it back up sorted
- Running time O(nlogn)

```python
def merge_sort(list):
    # 1. Store the length of the list
    list_length = len(list)

    # 2. List with length less than is already sorted
    if list_length == 1:
        return list

    # 3. Identify the list midpoint and partition the list into a left_partition and a right_partition
    mid_point = list_length // 2

    # 4. To ensure all partitions are broken down into their individual components,
    # the merge_sort function is called and a partitioned portion of the list is passed as a parameter
    left_partition = merge_sort(list[:mid_point])
    right_partition = merge_sort(list[mid_point:])

    # 5. The merge_sort function returns a list composed of a sorted left and right partition.
    # > The fed in lists are already sorted! (i.e. at the beginning [X], [Y], then [X, Z], [W, Y])
    return merge(left_partition, right_partition)


# 6. takes in two lists and returns a sorted list made up of the content within the two lists
def merge(left, right):
    # 7. Initialize an empty list output that will be populated with sorted elements.
    # Initialize two variables i and j which are used pointers when iterating through the lists.
    output = []
    i = j = 0

    # 8. Executes the while loop if both pointers i and j are less than the length of the left and right lists
    while i < len(left) and j < len(right):
        # 9. Compare the elements at every position of both lists during each iteration
        if left[i] < right[j]:
            # output is populated with the lesser value
            output.append(left[i])
            # 10. Move pointer to the right
            i += 1
        else:
            output.append(right[j])
            j += 1
    # 11. The remnant elements are picked from the current pointer value to the end of the respective list
    output.extend(left[i:])
    output.extend(right[j:])

    return output

A = [8,7,5,2,3]
B = [2,5,1,5,7,1,2]

merge_sort(A+B)
```

作业：
>>> 必做题: Sorting的作业
>>> 选做题：ooo作业
