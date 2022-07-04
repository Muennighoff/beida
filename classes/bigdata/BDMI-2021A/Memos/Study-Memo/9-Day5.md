# 第5次课堂笔记
# 1.课程管理系统讨论
教务系统、学生界面、教师界面

讨论结果：![课程管理系统讨论](D:\学业相关资料\大四上\大数据与机器智能\课程管理系统讨论.png)

思考，这个系统的核心是什么？

数据，数据结构，以及对数据的操纵。

# 2.SQL学习
Structured Query Language
是一种高级编程语言，是查询和操作数据库的标准语言。
**SQL有哪些？**
数据定义语言（definition，DDL语言）；
数据操作语言（manipulation，DML语言）；
数据控制语言（control，DCL语言）

## 2.1一些SQL基础语法
多条SQL语句以分号分隔。可以写到一行，也可以写成多行。
空格被忽略。
三种注释方式：##注释、--注释、/\*注释\*/。
命令不区分大小写：Create，Drop Table
输入值区分大小写：‘Seattle’, 'seattle', ...（这里，用单引号表示常数）

## 2.2 SQL上手
### 2.2.1 创建数据库（DDL语句）
CREATE DATABASE testdb;

### 2.2.2创建、删除、修改数据表（DDL语句）
CREATE TABLE 表名(列名 列类型, ...);
常见的列类型：bool, int, real, text, timestamp, ...
**示例代码：**
CREATE TABLE table1(c1 int, c2 int)
**删除表：**
DROP TABLE table1;
DROP TABLE if exists table1;
**添加列：**
ALTER TABLE table1
ADD c3 int(3);
**修改类型：**
ALTER TABLE table1
MODIFY COLUMN c3 tinyint;
**删除列：**
ALTER TABLE table1
DROP COLUMN c3;
**指定主键：**
ALTER TABLE table1
ADD PRIMARY KEY(c1);
**删除主键：**
ALTER TABLE table1
DROP PRIMARY KEY;

### 2.2.3添加数据（DML语句）
INSERT INTO 表名[(列名,...)] VALUES(列值, ...), ...
**例如：**
INSERT INTO table1
VALUES
(1,2),
(2,3),
(3,4);
**添加单条数据到数据表：**
INSERT INTO table1 VALUES(1,2);
**添加多条数据到数据表：**
INSERT INTO table1 VALUES(1,2),(2,3);
**指定要添加的列：**
INSERT INTO table1(c1) VALUES(1);

### 2.2.4查询数据（DML语句）
SELECT语句
**查询所有行，所有列：**
SELECT * FROM table1;
**查询所有行的c1,c2列：**
SELECT c1, c2 FROM table2;
**查询满足条件c1 = 1的行：**
SELECT * FROM table1 WHERE c1 = 1;

### 2.2.5更改数据（DML语句）
UPDATE语句
**语法：**
UPDATE 表名 SET 列名 = 值, [WHERE 条件]
**示例：**
**更新所有行的c1列为1：**
UPDATE table1 SET c1 = 1;
**附加更新条件的情况：**
UPDATE table1
SET c1 = 1
WHERE c2 = 2;

### 2.2.6删除数据（DML语句）
**删除数据表中的所有行：**
DELETE FROM table1;
**删除满足条件的行：**
DELETE FROM table1
WHERE c1 = 1;

### 2.2.7连接数据（关联查询）
JOIN
**包括哪些连接？**
内连接（INNER JOIN），
左连接（LEFT JOIN），
右连接（RIGHT JOIN），
全连接（FULL JOIN）
**操作：**
**内连接：**
SELECT * from A inner join B on(A.c1 = B.c1);
取满足条件的笛卡尔积
**左连接：**
SELECT * from A left join B on(A.c1 = B.c1);
满足条件的，取笛卡尔积；如果不满足条件，则B表的列，用空值补充
**右连接：**
SELECT * from A right join B on(A.c1 = B.c1);
满足条件的，取笛卡尔积；不满足条件的，用空值补充A表的列
**全连接：**
SELECT * from A full join B on(A.c1 = B.c1);
满足条件的，返回笛卡尔积；不满足条件的，表A和表B的行都用空值补充

### 2.2.8索引操作（Index）
**创建单列索引：**（基于表的一个列来创建）
CREATE INDEX index_name ON table_name(column_name);
示例：create index idx_c on table1(c1);
**创建组合索引：**（基于一个表的两个或多个列来创建）
CREATE INDEX index_name ON table_name(c1, c2);
示例：create index idx_c on table(c1, c2);
**删除索引：**
DROP INDEX index_name;

### 2.2.9视图（View）
视图是可视化的表，但是是虚拟的表，本身不包含数据，不能进行索引操作
可以像对普通的表一样进行操作：
CREATE VIEW bigger_10_view AS
SELECT c1, c2
FROM table1
WHERE c1 > 10

DROP VIEW bigger_10_view;

### 2.2.10事务操作（TxB）
包含多条SQL语句，形成执行块。要么全部执行成功，要么全不执行。
BEGIN TRANSACTION:
COMMIT:
ROLLBACK:

### 2.2.11键约束（Key constraints）
键，是属性的最小子集。
主键：Primary key
外键：Foreign key
代码示例：
CREATE TABLE A(c1 INT, c2 INT, PRIMARY KEY(c1));
CREATE TABLE B(c1 INT, c2 INT, PRIMARY key(c1), Foreign key(c2) references A(c2))

INSERT INTO A VALUES(1,4),(2,5),(3,6);
INSERT INTO A VALUES(2,4),(3,5),(4,6);

## 2.3 SQL学习2.0
### 2.3.1集合代数
连表List：[1,1,2,3]
集合Set：{1,2,3}
多集Multiset：允许重复元素的集合：{1,1,2,3}
合并运算：针对集合的。如果是Set，就是通常意义上的并集；如果是Multiset，就是弄成一个Multiset，重复的元素仍然重复。
交叉积：类似于矩阵的外积

### 2.3.2数据表Table/Relation
是由元组构成的多集。那么，元组是什么？
**元组或行：**（Tuple/Row/Record）
是数据表中的单个数据条目。例如，一个Product表，每条数据都包含：
"PName"、"Price"、"Manuf"等属性。
**属性或列：**（Attribute/Column）
是表头中，指定了类型的数据项。
**基数和元数：**（cardinality/arity）
元组的数目：基数；
属性的个数：元数

### 2.3.3数据表模式：（Table Schemas）
是指：表名称(表的属性:属性的类型,...)
例如：Product(Pname: string, Price: float, Category: string, Manufacturer: string)

### 2.3.4键值和约束：（ Key constraints）
Key是一种属性，一个表的Key，应该是指值唯一的。就如同元组的“身份证号”一样。
键会加下划线。
也因此，Key是表的属性的最小子集。因为有了Key，可以唯一映射元组。
例如，学生的学号，可以作为key。

### 2.3.5模式声明：（Declare Schemas）
相当于对表进行初始化
**例如：**
Students(sid:string, name:string, gpa:float)
将学号sid作为键值，怎么声明呢？
**代码如下：**
CREATE TABLE Students(
sid CHAR(20),
name VARCHAR(50),
gpa float,
PRIMARY KEY(sid) --这是对键值的指定
)

### 2.3.6空值和非空值：（NULL， NOT NULL）
对于不知道的值，不能空着，要赋一个”NULL“值。
但是决不能每个属性都有空值，否则就没有意义了。比如说，表中的”name“属性。
**空值的意义何在？**
筛选时需要考虑空值，例如：
SELECT \*
FROM Person
WHERE age < 25 OR age >= 25
OR age IS NULL
如果没有最后这句NULL，那么，年龄未知的明显属于”全年龄“，但不会被筛选出来。

### 2.3.7单表查询
**查询（Query）语句的SFW形式：**
SELECT \*：应该选出整个元组（整个行），包括了所有的属性；
FROM <一个表，或多个表>
WHERE <满足查询所需的条件>

--如果是SELECT attribute1, attribute2，那么选出的结果就只包含两个属性。即，投射到某几个属性（Projection），这样做，将生成原表的子集。

查询返回的结果，仍然是表。只不过，此时的属性由查询时的语句进行了选择，并且不再具有Key的信息。

WHERE 后面进行条件说明时，除了确定性的条件，还可以进行字符串匹配：
**字符串匹配：LIKE**
s LIKE p
PName LIKE ‘%gizmo%’
PName LIKE '\_yifan%'
用%表示任意长度字符串，下划线表示一个字符

如果想查询，例如：这个表的Category属性，不希望有重复的结果，可以消除重复：
**消除重复：DISTINCT**
SELECT DISTINCT Category
FROM .Product

如果希望返回的查询结果可以排好序（例如查成绩，价格等等），可以：
**查询后排序：ORDER BY**
SELECT Pname, Price, Manufacturer
FROM Product
WHERE Category = 'gizmo' AND price > 50
ORDER by Price, PName

### 2.3.8多表查询
需要用到连接。
例如，对于两个有关联的表，Product的制造商（Manufacturer），就是Company的公司名字（Pname）。
**连接：JOINS**
Product(PName, Price, Category, Manufacturer)
Company(CName, StockPrice, Country)
将Product的Manufacturer，和Company的CName对应起来，去查找”产地在日本的，价格低于$200的所有产品：
**代码如下：**
SELECT PName, Price
FROM Product
JOIN Company
ON Manufacturer = Cname
WHERE Price <= 200 AND Country = 'Japan'
**或者：**
SELECT PName, Price
FROM Product, Company
WHERE Manufacturer = CNAME AND Country = 'Japan' AND Price <= 200

但如果，两个表的属性出现同名呢？
**多表元组变量的含糊性：**
Product(name, Price, Category, Manufacturer)
Company(name, StockPrice, Country)
都有name，怎么办？两种解决方法：
**代码1：**
SELECT DISTINCT Product.name, Company.name
From Product, Company
WHERE Product.Manufacturer = Company.name
**代码2：**
SELECT DISTINCT p.name, c.name
FROM Product p, Company c
WHERE p.Manufacturer = c. name

### 2.3.9连接的语义：
基于交叉积运算；
然后，根据WHERE条件，进行过滤；
然后，根据SELECT给定的范围，进行投影（仅返回部分数据）；
（那幅连接语义的示例图，就能说明问题了）

# 3. Tkinter GUI
Tkinter是Python中最常用的图形化编程库。
发现，在Jupyter notebook中，只使用“from tkinter import * ”不太行，要具体地引用如下：
```python
from tkinter import Label
from tkinter import Button
from tkinter import Tk
```
才能正常运行代码。

## 3.1练习一
创建一个窗口，有Press me按钮。点击后，按钮变蓝，字变白，并显示按下了按钮的信息。
```python
from tkinter import Label
from tkinter import Button
from tkinter import Tk
def call():
    msg = Label(window, text = "You press the button")#标签
    msg.place(x = 30, y = 50) #msg被创建之后的位置
    button['bg'] = 'blue'#控制背景色
    button['fg'] = 'white'#控制字体颜色
                
#窗口建立：
window = Tk()
window.geometry("200x110")#这里是小写的x
button = Button(text = "press me", command = call)#Button是按钮类
button.place(x = 30, y = 20, width = 100, height = 30)#控制button的位置和尺寸大小
window.mainloop()#检测窗口的状态，不断刷新和显示
```
运行结果：

![image-20211017151746824](C:\Users\dell\AppData\Roaming\Typora\typora-user-images\image-20211017151746824.png)

## 3.2练习二
在窗口中的一个输入框输入名字，按下按钮后，下方的文本框会变色，并显示名字。
```python
from tkinter import *

def click():
    name = textbox1.get()##从输入框接受name
    message = str("Hello\n" + name)##将要在textbox输出的消息
    textbox2["bg"] = "yellow"
    textbox2["fg"] = "red"
    textbox2["text"] = message
    #在执行了click操作之后，将会把textbox2变成如下的样子

window = Tk()
window.geometry("500x200")

label1 = Label(text = "Enter your name:\n")
label1.place(x = 30, y = 20)

textbox1 = Entry(text = "")#创建一个输入框
textbox1.place(x = 150, y = 20, width = 200, height = 25)
textbox1['justify'] = 'center'#控制在输入框输入文本时，文本的显示位置（居中）
textbox1.focus()

button1 = Button(text = 'Press me', command = click)#按钮
button1.place(x = 30, y = 50, width = 120, height = 25)

textbox2 = Message(text = "")#控制textbox2在click操作之前，这个文本框的属性
textbox2.place(x = 150, y = 50, width = 200, height = 50)
textbox2["bg"] = "white"
textbox2["fg"] = "black"

window.mainloop()
```
运行结果：

![image-20211017155653328](C:\Users\dell\AppData\Roaming\Typora\typora-user-images\image-20211017155653328.png)

## 3.3练习三

在输入框可以输入名字后，点击按钮把名字载入到下方的文本显示框里。并且可以点击另一个按钮清除掉显示框中的名字。
```python
from tkinter import *

def add_name():
    name = name_box.get()
    name_list.insert(END, name)#add_name的功能：按一次，在name_list中的最后一行，增加一次name_box中输入的名字，并清除掉name_box中刚刚输入的名字
    name_box.delete(0,END)
    name_box.focus()
    
def clear_list():
    name_list.delete(0, END)#清除掉name_list中所有的名字
    name_box.focus()
    
window = Tk()#控制窗口的名字和大小
window.title("Name list")
window.geometry("400x300")

label1 = Label(text = "Enter your name:\n")
label1.place(x = 10, y = 20, width = 100, height = 30)

name_box = Entry(text = 0)#提供名字的输入框
name_box.place(x = 120, y = 20, width = 100, height = 30)
name_box.focus()

button1 = Button(text = 'Add name to list', command = add_name)#提供载入名字的按钮
button1.place(x = 250, y = 20, width = 100, height = 25)

name_list = Listbox()#提供显示已载入名字的文本框
name_list.place(x = 120, y = 50, width = 100, height = 60)

button2 = Button(text = "Clear list", command = clear_list)#提供删除名字的按钮
button2.place(x = 250, y = 50, width = 100, height = 25)

window.mainloop()
```
运行结果：

![image-20211017155738833](C:\Users\dell\AppData\Roaming\Typora\typora-user-images\image-20211017155738833.png)
