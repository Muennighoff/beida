<<<<<<< HEAD
# 1.1Python语言基础知识
## 1.1.1基本数据类型结构
### 字符串string
```python
my_string = 'Python is my favorite programming language!'
type(my_string)
my_new_string = my_string.replace('is','will be')
Your_string = '{} is fun'.format('Python')
my_string
my_new_string
print(Your_string)
```
### 列表List
```python
my_list = [1,2,2,3,'four']
list_of_list = [[1,2,3],[4,5,6],[7,8,9]]#二维列表
init_a_list = [i for i in range(9)]
init_a_list2 = [i**2 for i in range(9)]
init_2d_list = [[i + j for i in range(5)] for j in range(9)]
my_list.insert(0,'stuff')
print(my_list.pop(0))
print(my_list)
print(list_of_list)
print(init_a_list)
print(init_a_list2)
print(init_2d_list)
random_list = [2,12,5,6]
sorted_list = sorted(random_list)#对列表进行排序的函数
random_list2 = [(3,'A'),(12,'D'),(5,'M'),(6,'B')]
print(sorted_list)
```
### 集合Set
```python
my_set = {i**2 for i in range(10)}
aset = set([1,2,2,'3','four'])#集合，去掉重复的元素
```
### 字典Dictionary
```python
my_dict = {i: i**2 for i in range(10)}#字典是推导式地赋值
my_dict.keys()
my_dict.values()#可以获取字典的键与值
```
## 1.1.2Python语句语法
### 条件语句
if elif else
### 循环语句
for循环
while循环
## 1.1.3函数
### 定义函数：
```python
def do_something(number):
    for i in range(number):
        print(f'Hello{i}')
do_something(5)
```
## 1.1.4类
### 类定义示例-Vehicle
先定Vehicle这个类
```python
class Vehicle:
	def _init_(self, make, name, year, is_electirc = False, price = 100):
		self.name = name
		self.make = make
		self.year = year
		self.is_electric = is_electric
		self.price = price
	
		self.odometer = price
	def drive(self, distance):
		self.odometer += distance
	def compute_price(self):
		if self.is_electric:
			price = self.price / (self.odometer * 0.8)
		else:
			price = self.price / self.odometer
		return price
```
现在调用class Vehicle
```python
if _name_ == '_main_':
	family_car = Vehicle('Honda', 'Accord', '2019', price = 10000)
	print(family_car.compute_price())
	family_car.drive(100)
	print(family_car.compute_price())
```
### 类定义示例-Dog
先定义
```python
class Dog():
	def _init_(self, name, age):
		self.name = name
		self.age = age
	def sit_down(self):
		print(self.name.title() + ' is now sitting down!')
	def roll_over(self):
		print(self.name.title() + ' rolled over!')
```
再调用
```python
a_dog=Dog('tuantuan',0.2)
print(a_dog.name)
a_dog.sit_down()
a_dog.roll_over()
```
# 1.2算法启动
## 1.2.1根式法解一元二次方程
代码示例
```python
import math
def solve_equ2(a,b,c):
    val1 = b**2-4*a*c
    root1 = 0
    root2 = 0
    if val1 >= 0:
        print('there are two roots')
        root1 = (-b+math.sqrt(val1))/(2*a)
        root2 = (-b-math.sqrt(val1))/(2*a)
    else:
        print('no root')
    return root1, root2
solve_equ2(2,24,22)
```
## 1.2.2圆周率的计算
### 采用级数求和的公式进行计算
例如：
$$
\sum_{i = 0}^n \frac{1}{n^2} = \frac{\pi^2}{6}
$$
所以：
$$
\pi = \sqrt{6\sum_{i = 0}^n \frac{1}{n^2}}
$$
上述公式收敛速度和计算速度都很慢
也有其他级数求和公式，例如幂级数：
$$
\frac{\pi}{4} = 1 - \frac{1}{3} +\frac{1}{5}+...+(-1)^{n-1}\frac{1}{2n-1}+...
$$
这个幂级数求和公式收敛速度也很慢，但没有开方运算，所以计算速度比上面那个公式快了不少
### 其他算法
迭代公式算法、Monte Carol算法，等等
# 1.3画图工具
需要引入matplotlib
### 简单绘图，蓝线连接所有点示例：
```python
import matplotlib
import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
```

![下载](D:\学业相关资料\大四上\大数据与机器智能\W1pictures\下载.png)

### 也可以设置绘图的属性

```python
import matplotlib
import matplotlib.pyplot as plt
plt.axis([0,5,0,20])
plt.title('my first plot')
plt.plot([1,2,3,4],[1,4,9,16],'ro')
#Jupyter中无需调用plt.show函数
```
![下载 (1)](D:\学业相关资料\大四上\大数据与机器智能\W1pictures\下载 (1).png)

### 散点图绘制，调用scatter函数

```python
import matplotlib
import matplotlib.pyplot as plt
classA_grades = [80,85,90,95,100]
classB_grades = [30,60,40,50,80]
grades_range = [0,25,50,75,100]
plt.scatter(grades_range, classA_grades, color = 'r')
plt.scatter(grades_range, classB_grades, color = 'b')
```
![下载 (2)](D:\学业相关资料\大四上\大数据与机器智能\W1pictures\下载 (2).png)

### 绘制函数图像，实际上也是绘制点线图

```python
import numpy as np
t = np.arange(0.0, 2.0, 0.01)
s = 1+np.sin(2*np.pi*t)
fig, ax = plt.subplots()
ax.plot(t,s)
```
![下载 (3)](D:\学业相关资料\大四上\大数据与机器智能\W1pictures\下载 (3).png)

### 还可以控制函数图像的属性，加注说明等

```python
import numpy as np
t = np.arange(0.0, 2.0, 0.01)
s = 1+np.sin(2*np.pi*t)
fig, ax = plt.subplots()
ax.plot(t,s)
ax.set(xlabel = 'time(s)',ylabel = 'voltage(mV)', title = 'voltage/time')
ax.grid
```
![下载 (4)](D:\学业相关资料\大四上\大数据与机器智能\W1pictures\下载 (4).png)

### 在同一幅图上绘制多个图像，并且控制图像的属性

```python
#绘制三个正弦函数
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math
t = np.arange(0, 2.5, 0.1)
y1 = np.sin(math.pi*t)
y2 = np.sin(math.pi*t + math.pi/2)
y3 = np.sin(math.pi*t - math.pi/2)
plt.plot(t,y1,'b*',t,y2,'g^',t,y3,'ys')
plt.plot(t,y1,'b--',t,y2,'g',t,y3,'r-.')
```

![下载 (5)](D:\学业相关资料\大四上\大数据与机器智能\W1pictures\下载 (5).png)
=======
# 1.1Python语言基础知识
## 1.1.1基本数据类型结构
### 字符串string
```python
my_string = 'Python is my favorite programming language!'
type(my_string)
my_new_string = my_string.replace('is','will be')
Your_string = '{} is fun'.format('Python')
my_string
my_new_string
print(Your_string)
```
### 列表List
```python
my_list = [1,2,2,3,'four']
list_of_list = [[1,2,3],[4,5,6],[7,8,9]]#二维列表
init_a_list = [i for i in range(9)]
init_a_list2 = [i**2 for i in range(9)]
init_2d_list = [[i + j for i in range(5)] for j in range(9)]
my_list.insert(0,'stuff')
print(my_list.pop(0))
print(my_list)
print(list_of_list)
print(init_a_list)
print(init_a_list2)
print(init_2d_list)
random_list = [2,12,5,6]
sorted_list = sorted(random_list)#对列表进行排序的函数
random_list2 = [(3,'A'),(12,'D'),(5,'M'),(6,'B')]
print(sorted_list)
```
### 集合Set
```python
my_set = {i**2 for i in range(10)}
aset = set([1,2,2,'3','four'])#集合，去掉重复的元素
```
### 字典Dictionary
```python
my_dict = {i: i**2 for i in range(10)}#字典是推导式地赋值
my_dict.keys()
my_dict.values()#可以获取字典的键与值
```
## 1.1.2Python语句语法
### 条件语句
if elif else
### 循环语句
for循环
while循环
## 1.1.3函数
### 定义函数：
```python
def do_something(number):
    for i in range(number):
        print(f'Hello{i}')
do_something(5)
```
## 1.1.4类
### 类定义示例-Vehicle
先定Vehicle这个类
```python
class Vehicle:
	def _init_(self, make, name, year, is_electirc = False, price = 100):
		self.name = name
		self.make = make
		self.year = year
		self.is_electric = is_electric
		self.price = price
	
		self.odometer = price
	def drive(self, distance):
		self.odometer += distance
	def compute_price(self):
		if self.is_electric:
			price = self.price / (self.odometer * 0.8)
		else:
			price = self.price / self.odometer
		return price
```
现在调用class Vehicle
```python
if _name_ == '_main_':
	family_car = Vehicle('Honda', 'Accord', '2019', price = 10000)
	print(family_car.compute_price())
	family_car.drive(100)
	print(family_car.compute_price())
```
### 类定义示例-Dog
先定义
```python
class Dog():
	def _init_(self, name, age):
		self.name = name
		self.age = age
	def sit_down(self):
		print(self.name.title() + ' is now sitting down!')
	def roll_over(self):
		print(self.name.title() + ' rolled over!')
```
再调用
```python
a_dog=Dog('tuantuan',0.2)
print(a_dog.name)
a_dog.sit_down()
a_dog.roll_over()
```
# 1.2算法启动
## 1.2.1根式法解一元二次方程
代码示例
```python
import math
def solve_equ2(a,b,c):
    val1 = b**2-4*a*c
    root1 = 0
    root2 = 0
    if val1 >= 0:
        print('there are two roots')
        root1 = (-b+math.sqrt(val1))/(2*a)
        root2 = (-b-math.sqrt(val1))/(2*a)
    else:
        print('no root')
    return root1, root2
solve_equ2(2,24,22)
```
## 1.2.2圆周率的计算
### 采用级数求和的公式进行计算
例如：
$$
\sum_{i = 0}^n \frac{1}{n^2} = \frac{\pi^2}{6}
$$
所以：
$$
\pi = \sqrt{6\sum_{i = 0}^n \frac{1}{n^2}}
$$
上述公式收敛速度和计算速度都很慢
也有其他级数求和公式，例如幂级数：
$$
\frac{\pi}{4} = 1 - \frac{1}{3} +\frac{1}{5}+...+(-1)^{n-1}\frac{1}{2n-1}+...
$$
这个幂级数求和公式收敛速度也很慢，但没有开方运算，所以计算速度比上面那个公式快了不少
### 其他算法
迭代公式算法、Monte Carol算法，等等
# 1.3画图工具
需要引入matplotlib
### 简单绘图，蓝线连接所有点示例：
```python
import matplotlib
import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
```

![下载](D:\学业相关资料\大四上\大数据与机器智能\W1pictures\下载.png)

### 也可以设置绘图的属性

```python
import matplotlib
import matplotlib.pyplot as plt
plt.axis([0,5,0,20])
plt.title('my first plot')
plt.plot([1,2,3,4],[1,4,9,16],'ro')
#Jupyter中无需调用plt.show函数
```
![下载 (1)](D:\学业相关资料\大四上\大数据与机器智能\W1pictures\下载 (1).png)

### 散点图绘制，调用scatter函数

```python
import matplotlib
import matplotlib.pyplot as plt
classA_grades = [80,85,90,95,100]
classB_grades = [30,60,40,50,80]
grades_range = [0,25,50,75,100]
plt.scatter(grades_range, classA_grades, color = 'r')
plt.scatter(grades_range, classB_grades, color = 'b')
```
![下载 (2)](D:\学业相关资料\大四上\大数据与机器智能\W1pictures\下载 (2).png)

### 绘制函数图像，实际上也是绘制点线图

```python
import numpy as np
t = np.arange(0.0, 2.0, 0.01)
s = 1+np.sin(2*np.pi*t)
fig, ax = plt.subplots()
ax.plot(t,s)
```
![下载 (3)](D:\学业相关资料\大四上\大数据与机器智能\W1pictures\下载 (3).png)

### 还可以控制函数图像的属性，加注说明等

```python
import numpy as np
t = np.arange(0.0, 2.0, 0.01)
s = 1+np.sin(2*np.pi*t)
fig, ax = plt.subplots()
ax.plot(t,s)
ax.set(xlabel = 'time(s)',ylabel = 'voltage(mV)', title = 'voltage/time')
ax.grid
```
![下载 (4)](D:\学业相关资料\大四上\大数据与机器智能\W1pictures\下载 (4).png)

### 在同一幅图上绘制多个图像，并且控制图像的属性

```python
#绘制三个正弦函数
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math
t = np.arange(0, 2.5, 0.1)
y1 = np.sin(math.pi*t)
y2 = np.sin(math.pi*t + math.pi/2)
y3 = np.sin(math.pi*t - math.pi/2)
plt.plot(t,y1,'b*',t,y2,'g^',t,y3,'ys')
plt.plot(t,y1,'b--',t,y2,'g',t,y3,'r-.')
```

![下载 (5)](D:\学业相关资料\大四上\大数据与机器智能\W1pictures\下载 (5).png)
>>>>>>> ef1f310e44215bc72cd07152371e45bfa7c7714f
