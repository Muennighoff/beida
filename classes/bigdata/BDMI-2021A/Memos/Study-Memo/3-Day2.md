# Week2 课程小结

## python的基础操作（文件操作、模块和包）

- 打开关闭函数
  - open(file_path,"r") "r"是功能选项，r+读写指针在开头，w+覆盖写， a+指针在末尾
  - os.path.realpath('.ipynb') 返回带文件名的路径
  - os.path.dirname(current_file) 返回文件目录
  - os.path.join(data_dir,'file_name')
  - 
- 读取函数
  - 利用with语句，**隐式**读取
- 写入函数
  - file.write()
- 删除函数
  - os.remove(file_path)
```python
import os.path
lst = ["A","B","C"]
txt = open("myclassmates.txt","w+")
for item in lst:
    txt.write(item+"\n")
txt.close()

with open("myclassmates.txt","a+") as txt2:
    txt2.write("D")
txt2.close()
```
```python
import random
lst_num = [random.randint(0,100) for i in range(20)]
with open("data.txt","w+") as txt2:
    for item in lst_num:
        txt2.write(str(item)+" ")
with open("data.txt",'r')  as txt2:
    print(txt2.readline())
```
- 文件删除函数
- 模块和包
  - 包 可复用 结构清晰 可维护性高
  - 调用方式

## 插入排序和合并排序
- Insertion Sort
  - 从第二个item开始，取出待排序的item，然后从第A.index(item)-1个开始往后挪（节省内存空间），直到j成为current的阻碍
  - 可以考虑sorted list，将待排序的数插入到list中
  - 时间复杂度：
$$
O(n^{2})
$$
```python
def InsertSort(A):
    for i in range(1,len(A)):
        current = A[i]
        j = i - 1
        while j >= 0 and A[j] < current:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = current
    return A
```


- Merge Sort
  - 思想：recursion & merge
  - 步骤：Break up - Merge
  - 时间复杂度：
  - Recursion tree:level log(n)+1 Merge: n
  - 
$$
O(nlog(n))
$$
```python
def Merge(x,y):
    i = 0
    j = 0
    newlst = []
    while i < len(x) and j < len(y):
        if x[i] < y[j]:
            newlst.append(x[i])
            i += 1
        else:
            newlst.append(y[j])
            j += 1
    while i < len(x):
        newlst.append(x[i])
        i += 1
    while j < len(y):
        newlst.append(y[j])
        j += 1
    return newlst
C = Merge(A,B)
print(C)

def MergeSort(lst):
    if len(lst) == 1:
        return lst
    else:
        L = MergeSort(lst[0:len(lst)//2]) # the input variables are supposed to the recursed ones 
        R = MergeSort(lst[len(lst)//2:])
        new_lst = Merge(L,R)
        return new_lst
```
## K选择问题

- description: return k-smallest number
- rough solution : A = Mergesort(A) , return A[k-1]
- first we pick a pivot and  separate the list into two parts (less than and larger than the pivot, no need to sort)
  - how to select pivot
    - 最好让len（L） len（R）在 3n/10  7n/10 之间，证明使用**Master Theorem**
    - 分成 size <= 5 的小数组，get the medians, aggregate all the medians and obtain the median of the median list
  - O(n) O(nlog(n))不一定谁比谁小,take notice for actual value of n


## 复杂度记号

  - 大O表示时间的**最坏**情况
  - Ω表示最好情况，Θ表示确界
  - theta 表示确界

## Project
  - 负数全部放在一个列，正数全部放在一个列，负数正数顺序不同，是否可以递归
  - 需要交的作业是两道必做题，一到选做题
  - 小测

## Tips

 - zip(A,B) 

    - cartesian product of A & B, return tuple

 - all

    - Boolean caculation

      
