# Day 1 Summary

主要记录下今天的一些代码案例

## String

主要关注$split$和$strip$语法，比如：

```python
my_string = " First day in THU. "
print(type(my_string))
split_string = my_string.split(" ")
strip_string = my_string.strip(" ") #remove head and tail char
print(my_string)
print(strip_string)
```

> 也可以结合dict使用来生成一个电话薄

```python
telephone = {"Alice":123321442, 
             "Bob": 2233124, "James":3324123, "Kitty":22312471
             }
def get_num(name): 
    print("The telephone number of", name, "is", 
          telephone[name])
    return
get_num("Alice")
get_num("Kitty")
```

## List

比较容易混淆的是**sorted**的用法：

```python
my_list = [2,3,1,4,5]
another = [(3,2),(4,5,6),(6,2),(3,1)]
new = sorted(my_list)
print(new)
another_new = sorted(another, key = lambda x: x[0], reverse=True)
print(another_new)
```

> sorted不会修改原数据，而是生成新的变量。区分于sort

以及一些基本运用：

```python
a_list = [1,2,3,4,5]
squared_list = []
for i in a_list:
    squared_list.append(i**2)
print(a_list, "\n", squared_list)
```

如果结合**random**可以实现更好玩的操作

```python
import random
choices = ['r','p','s']
player_choice = input("your choice, print quit to quit")
while player_choice != 'quit':
    computer = random.choice(choices)
    if player_choice in choices:
        print("Computer chooses:",computer)
        if choices.index(computer) - choices.index(player_choice) == 1 or choices.index(computer) - choices.index(player_choice) == -2:
            print('Computer wins!')
        elif choices.index(computer) == choices.index(player_choice):
            print('Ties!')
        else:
            print("You wins!")
    else:
        print("Not a valid choice!")
    player_choice = input("your choice, print quit to quit")
```

## Class

着重复习类语句的设定方法：

```python
class cat:
    def __init__(self, name, year, weight, height):
        self.name = name
        self.age = year
        self.weight = weight
        self.height = height
    def bmi(self):
        return self.weight / (self.height)**2
    def tell_age(self, lovely=True):
        if self.age <= 3 and lovely == True:
            return('Pretty Kitty!',self.age,"years old!")
        else:
            return(self.age,"years old!")
bammy = cat("bammy", 2, 10, 10)
print(bammy.bmi())
print(bammy.tell_age())
print(bammy.tell_age(True))
print(bammy.tell_age(False))
```

## Matplotlib

画图的使用，也可以通过**Pygal**得到更棒的可视化包。

```python
# bo-: blue dot with lines between
# ro: red dot
import matplotlib.pyplot as plt
import numpy as np
import random
t = np.linspace(0.00,2.00,50)
s1 = 1+np.sin(2 * np.pi * t)
s2 = 1+np.cos(2 * np.pi * t)
s3 = 1+np.cos(3 * np.pi * t)
fig, ax = plt.subplots() #多个子图，fig为画布，ax为内容
ax.set(xlabel="x",ylabel="y",title='sin(x)')
ax.plot(t,s1,'bo',
        t,s2,'go-',
        t,s3,dashes=[2,2,10,2]) #2单位实线，2单位空白，10单位实线，2单位空白
```

