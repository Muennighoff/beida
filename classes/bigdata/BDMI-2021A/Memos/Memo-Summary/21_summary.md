# DAY1课程小结Memo
> 此前并未过多的接触过Python等相关知识，学习起来较为吃力，但一节课下来收获颇丰，也非常感谢助教及老师的热情指导，如下即为第一节课学习内容的简要总结。

- <font color = red size = 6>1.学习了程序语言Python的基本操作与应用</font>
- 1.Python语言的由来
+ 2.Python运行环境配置
* 3.Python语言使用
- <font color = red size = 6> 2.通过课程 *路线图（Roadmap）*了解了课程的基本知识框架</font>
>> <img src="C:\Users\崔丽千\Desktop\人工智能相关课程\大数据与机器智能\知识框架图.png"style="zoom:50%;"/>

- <font color = red size = 6> 3.熟悉Markdown的==基本语法、画图、数学公式==等并进行相关练习</font>
- <font color = red size = 6>4.了解π计算的不同历史时期的计算历程</font>
- <font color = red size = 6>5.学习Matplotlib画图</font> <font color = blue size = 5>（其中后面的pygal仿真并没有太明白）</font>
- >> 散点图、线图、柱状图、3D图
- <font color = red size = 6>6.进一步学习Python数据类型与结构</font>
- <font color = pink size = 4>1.Python数据类型与结构</font>
>>List、Set、Dictionary、Tuple
>>if-elif-else条件语句
>>for循环
>>While循环
- <font color = pink size = 4>2.Python函数</font>
- <font color = pink size = 4>3.Python类</font>
- <font color = pink size = 4>小结：Python程序的组成</font>
>>-Python的程序形式上分解为程序块、语句、表达式和对象
>>- 程序由程序块（Block）构成
>>- 程序块包含语句（statement）
>>- 语句包含表达式（expression）
>>- 表达式建立并处理对象（object）
- <font color = pink size = 4>4.Python模块</font>
>>- 代码组织、模块、包
- <font color = red size = 6>7.了解并学习Git、Gitee使用</font>
- <font color = red size = 6>8.算法学习与案例了解</font>
>>- AI-Khwarizmi解法
>>根式法
## 感想：
> 虽然学习过程略感吃力，上课时感到有些烧脑，但经过课后的复习收获良多，继续努力~
# DAY2课程小结Memo
## 上节课内容回顾
>> Python基本内建类型：字符串（string）、整数（int）、浮点数（float）、布尔值（bool）
>> Python基本数据结构：List、Set、Dictionary
>> 模块（modules）与包（package）
## 一、
### Python3语言基础

## 二、
### Python File IO
>> Python文件操作：打开函数、关闭函数
>>
>> >> 主要函数：读取函数（with函数，用则是隐式读取，不用则是显式读取）

###  Modules and packages
>> >> 模块和包（可重复、结构清晰、 可维护性高）
>> >> 使用方法

## 三、
### 插入排序算法（InsertionSort)：
>>新元素插入原有排序的列表当中去。——归纳

### 插入排序算法实验sorting算法
## 四、
### 合并排序算法（MergeSort）
>>Divide and Conquer
>>递归——合并（算法的基本思想）——大问题变小问题——小问题恢复为最大的问题
>>如何Merge——拆分、比较、合并

### 合并排序算法实验sorting算法
## 五、
### 算法的复杂度记号
## 六、
### Median and Selection
# DAY3课程小结Memo
## 上节课内容回顾
>> 上节课的关键词：插入排序，合并排序，递归，分治
>> 课程起头和回顾、Python语言-文件读写、模块与包、插入排序和合并排序、k-选择和中值

## 课程感想
一开始就不小心翻到了课堂习题的答案版本，就开始自行研究了，实操还比较顺利，但上课的时候有些课外的事情让自己分神了，此处检讨。之后的课必须认真听讲，跟着老师的节奏来学习。
## 本节课内容
### 快速排序Quick sort
>> 分治、递归思路
>> QuickSort（快速排序） vs MergeSort(归并排序)
>> 实际上是可以faster than onlog（n），排列方法按照物理性质
>> 归并排序的时间复杂度是n log n

### 基本数据结构1：链表与有序数组

### 基本数据结构2：二分查找树（掌握）
>> some data structures for storing objects like(aka,nodes with keys)无序状态的链表结构nodes with keys;search and delete 
>> 每次的选择的节点不同，产生的树不同，和二分查找发类似，与排序算法有关。

#### 节点类
class Node:
    # 用类成员函数进行节点初始化
    def __init__(self, value):
        self.value = value
        self.lchild = None
        self.rchild = None

#### BST树类
class BST:
    # 用类成员函数进行BST初始化
    def __init__(self, node_list):
        self.root = Node(node_list[0])
        for value in node_list[1:]:
            self.insert(value)
    # 搜索拥有某值的节点操作
    def search(self, node, parent, value):
        if node is None:
            return False, node, parent
        if node.value == value:
            return True, node, parent
        # 小的在左孩子，大于等于的在右孩子
        if node.value > value:
            return self.search(node.lchild, node, value)
        else:
            return self.search(node.rchild, node, value)

    # 插入某值的节点操作
    def insert(self, value):
        flag, n, p = self.search(self.root, self.root, value)
        if not flag:
            new_node = Node(value)
            if value > p.value:
                p.rchild = new_node
            else:
                p.lchild = new_node
    
    # 删除某值的节点
    def delete(self, value):
        flag, n, p = self.search(self.root, self.root, value)
        if flag is False:
            print("Can't find the key! Delete failed!")
        else:
            #当左子树为空时
            if n.lchild is None:
                if n == p.lchild:
                    p.lchild = n.rchild
                else:
                    p.rchild = n.rchild
                    
            #当右子树为空时
            elif n.rchild is None:
                if n == p.lchild:
                    p.lchild = n.lchild
                else:
                    p.rchild = n.lchild
            else:
                #当左右都不为空时，选择右子树
                pre = n.rchild
                if pre.lchild is None:
                    #如果左子树为空，直接将右子树上移
                    n.value = pre.value
                    n.rchild = pre.rchild
                else:
                    #如果左子树不为空，直接迭代到左子树根节点
                    next = pre.lchild
                    while next.lchild is not None:
                        #迭代，在这里写代码，写代码时候删除pass
                        pass
                    n.value = next.value
                    pre.lchild = next.rchild
    # 先序遍历
    def pre_order_traverse(self, node):
        if node is not None:
            print(node.value)
            self.pre_order_traverse(node.lchild)
            self.pre_order_traverse(node.rchild)
    
    # 中序遍历
    def in_order_traverse(self, node):
        if node is not None:
            self.in_order_traverse(node.lchild)
            print(node.value)
            self.in_order_traverse(node.rchild)


    # 后序遍历
    def post_order_traverse(self, node):
        if node is not None:
            self.post_order_traverse(node.lchild)
            self.post_order_traverse(node.rchild)
            print(node.value)
### 了解红黑树，2-3-4树和B+树
### 桶排序（Bucket Sort）与哈希结构
# DAY4课程小结Memo
## 课后作业
>> 读：·CLRS：第10、11、12章和第13章
>> 读：·FCDB:第1章和第2章（下节课）

## 上节课内容回顾
>> 快速排序Quick sort
>> 基本数据结构1：链表与有序数组
>> 基本数据结构2：二分查找树（掌握）
>> 了解红黑树，旋转，自平衡

## 课程感想
哈希函数部分前半部分比较明白，后面逐渐复杂后感到还是有点理解不能，课下还是要去看看。
讲到B+树的时候启发了我在建筑设计上的一些思考，如下：
>>对空间给予某种系数（重要程度？使用频率？面积？）进行排序，然后进行组织，在后续的空间序列形成中形成空间之间的联系，有好几个空间节点应运而成，之后再不停的细分空间，空隙空间可以更加灵活的添加使用功能,然后逐渐生成一个大的综合体..
>>解决的问题可能是：1、动线静线连贯性问题；2、空间可达性及到达效率问题；3、不同功能空间的组织整合问题；这样的组织结构有点就是：快速、精确的进行范围查找
>>期待可以机器学习在建筑领域有更有效且广泛的应用。

## 本节课内容
### RBTree-->2-3-4 Tree
>>Perfect balance.Every path from root to leaf has same length.
>>Search 查找的时间就是树的高度；
>>Insert Search to bottom for key 
n节点n+1三节点,树的高度并没有改变（特点），超出四节点后吧四节点的中间节点放在上一级，把两侧节点分开成两个二节点；如果再上一级还是四节点，有两个方式来解决：
>>>>Top-down
>>>>Bottom-up
>>优点：根节点到叶节点长度一样
>>Direct implementation of 2-3-4 trees
>>红黑树是2-3-4树的变种←→2-3-4树转换为红黑树（（Left-leaning）左倾红黑树）

### B+ tree
>>数据的组织、查找与更新
>>>>组织数据——排序、组织
>>>>查找数据——属性结构、哈希
>>>>更新数据
>>>>图书馆找书——索引——杜威十进制系统，常用的图书馆数据分类系统
>>索引类型Index Types:B树
>>>>>>>>>>>>>>>>数据结构之间的真是差别巨大，操作成本决定了你选择何种索引及其理由
>>>1.非常适合范围查询（对排好序的数据）
>>>2.Very good for range queries,sorted data
>>>3.我们主要用B+树
>>>4.We will look at a variant called B+ Trees
>>哈希表 Hash Tables
>>Summary:
>>>B树是一种数据结构，能够支持快速的精确和范围查找和插入，基于高扇出
>>>B+ Trees are one index data structure which support very fast exact and range search&insertion via high fanout

### 桶排序BucketSort与基排序Radix Sort
>>Radix Sort 多次桶排序
>>整体算法复杂度O(nd)——不同的进制不一样，进制越大，桶越多，迭代次数越少。

### 查找结构：哈希表与哈希函数族，Hashing，Hashing！
>>another sort of data structure that allows fast INSERT/DELETE/SEARCH

### 哈希表实验
# Day5课程小结Memo

## 课程回顾
## 课程感想
## 课后作业
>> 读：CLRS:第10、11、12章和13章
>> 读：FCDB：第1章和第2章
>> 练习CMS项目

## 选课系统管理系统设计——教学互动20min
（course management system,CMS)
>>我们需要考虑什么？
>>>>教务系统：学生注册，课程开设，维护学生选课机制正常运行......
>>>>学生：选课，获得课程信息......
>>>>教师：提交课程，期末给出成绩......
>>>>具体到代码的实现：怎样的数据结构，如何对其操作（插入，删除，赋值等）
>>>>从用户角度出发：
>>>>教师可以录入成绩、教室地点时间冲突

## SQL语言
>>SQL是一种高级编程语言，是查询和操作数据的标准语言，语法类似英语
>>Data Definition Language(DDL)
>>Dara Manipulation Language(DML)
>>Data Control Language(DCL)

### 创建索引——Index
### 视图--View
### 事务操作（TRANSACTION)：BEGIN REANSACTION\COMMIT\ROLLBACK
### 键约束（Key Constraints）

## SQLite
## 数据库客户端Dbeaver
## Python Tkinter
>>图形化用户接口
>>Graphical User Interface,GUI
>>控件Widgets：Menu\Button\Canvas\Checkbutton\Entry\Lable\Frame
>>几何形状与位置（Geometry,Place)
# DAY6课程小结Memo
## 课程回顾
## 课程感想
>>>>特别感谢老师和助教在课堂上的指导，收获很大~
## 课后作业
>>读：FCDB第一章和第二章，第六章：The Database Language SQL
>>写：学习小结
>>练：CMS项目

## SQL语言第三部分及相关实践
### Set operators&nested queries 集合算子和嵌套查询
>>>>集合代数Set algebra
>>>>在Python中如何计算
>>>>显示集合运算 交集
>>>>显示集合运算 并集
>>>>显示多集运算 多集并
>>>>聚合与分组

#### 嵌套查询Nested Query
>>>>嵌套查询 子查询返回关系 SELECT DISTINCT去掉返回结果的重复
>>>>HAVING子句

### Aggregation&GROUP BY集合函数：SUM,Court，MIN,MAX,AVG
### GROUP BY 子句、Having子句
## Python SQLite练习

## 第三次大作业介绍
## 数据系统
>>>>数据库，一个巨大的、综合的数据集合
>>>>建模一个真实的设施
>>>>数据库管理系统（DBMS）（简称数据库管理系统）是一个用于存储额和管理数据的软件！没有离开数据管理软件的数据库，因此数据库即指的是数据。

### 基本概念与术语
>>>>示例-课程管理系统
## 数据库postgresql
>>>>安装
>>>>数据访问postgresql参考代码
# Day7课程小结Memo

## 课程回顾
## 课程感想
## 课后作业
>>>>读：《机器学习实战》（Hands-on Machine Learning with Scikit-Learn, Keras,TensorFLow2)第1-4章，第10章

## Numpy/Scipy介绍
>>>>Numpy矩阵运算、数组形状变形、Debugging
>>>>http://numpy.org/
>>>>http://www.scipy.org/

### 创建数组和数据类型定义
>>>>创建数组、算术运算、函数运算、矩阵乘积、数组变形（transpose)

### Numpy实践
#### Numpy 使用
>>>> np.matmul 矩阵相乘（Matrix multiply)
>>>> np.zeros 创建零矩阵(Create a matrix filled with zeros(np.ones))
>>>> np.arange 定义范围（开始，停止，步长）（Start,stop,step size(np.linspace))
>>>> np.identity创建一个单位矩阵（Create an identity matrix)
>>>> np.vstack 垂直叠加2阵列（Vertically stack 2 arrays(np.hstack))

#### Numpy调试
>>>> Numoy方法 Description
>>>> array.shape 得到numpy数组的形状（Get shape of numpy array）
>>>> array.dtype 检查数组的数据类型（Check data type of array(for precision for weird behavior))
>>>> type(stuff) 获取变量的类型（Get type of a variable)
>>>> import pdb;pdb.set_trace() 设置断点（Set a breakpoint)
>>>> print(f'My name is {name}'')

## 深度学习1：人工神经元
### 人工神经元（带权重的函数）
>>>>单个人工神经元（Artificial Neuron):
1.一组输入的线性加权叠加
2.经过一个非线性变换进行输出

#### 激活函数（activation function)
#### 练习代码numpy_activation_function.ipynb
>>>>激活函数有sigmoid函数，tanh函数，ReLU函数等

##### tanh函数：
>>>>import numpy as np
>>>>exp = np.exp
>>>>max = np.max
>>>>def tanh(x):
    return(exp(x) - exp(-x))/(exp(x)+exp(-x))
>>>>def relu(x):
    return max(x,0)
>>>>print(tanh(5),relu(5))

##### ReLU单元：
>>>>def ReLU(x):
    return np.maximum(0,x)
>>>>ReLU(-1)
>>>>ReLU(5)
>>>>weight=np.array([-0.21,0.3,0.7])
>>>>ReLU(np.dot([1,0,1],weight))

### 人工神经元2-逻辑斯提回归单元
>>>>所有输入线性加权叠加，经过一个非线性函数（激活函数）输出
>>>>逻辑斯提回归单元（Logistic Regression Unit）是最简单人工神经元结构之一。
>>>>逻辑斯提回归单元的激活函数采用sigmoid函数或罗季斯提函数
>>>>自己实现一个relu单元和逻辑斯提单元：参数的设置可以有多种方式

### 单个人工神经元能力-模拟布尔运算
>>>>布尔运算是现代计算机的基础能力
>>>>>>>>1.与运算（AND）、或运算(OR)、非运算(NOT)
>>>>>>>>2.与非（NAND）、异或（XOR)
>>>>import numpy as np
>>>>def sigmoid(x):
    return 1/(1+np.exp(-x))
>>>>arr = np.array([[0,0],[0,1],[1,0],[1,1]])
>>>>w = np.array([20,20])
>>>>b_and=-30
>>>>b_or=-10
>>>>print("and:")
>>>>print(sigmoid(np.dot(arr,w)+b_and).reshape(2,2))
>>>>print('or:')
>>>>print(sigmoid(np.dot(arr,w)+b_or).reshape(2,2))

### 多个人工神经元能力-解决XOR问题
#### XOR运算
##### 实现1 X1 XOR X2={X1 OR X2}AND{NAND{X1,X2}}
##### 实现2 X1 XOR X2={X1 OR X2}AND{(NOT X1)OR(NOT X2)}
*XOR运算可以由AND运算；NOT运算；OR运算组合完成；

*### 拓展思考-理论如何落实到实践
>>1、布尔运算构建了计算的体系，实际中用布尔门电路实现
>>>>什么是计算？
>>>>布尔门电路，可以由晶体管电路实现
>>2、理论上讲，用人工神经元作为基本的 计算单元，能力不逊于计算机。
>>>>问题1：实际中有用人工神经元电路的方式来实现么？
>>>>问题2：你认为这种方法的最大的挑战是什么呢？

## activation Funcation:numpy实现
## Pandas准备
## pandas练习

## 深度学习2：网络训练
### 名词术语（中英文对照）
*机器学习、监督学习、深度学习；分类、二元分类；回归、逻辑斯提回归（分类）；网络训练、网络推断；批量训练、小批量训练；时代、迭代；多维数组、张量；Softmax、logit分对数；损失函数、度量函数、均方误差、交叉熵；导数、梯度、梯度下降法；算子操作、链式求导法则；自动微分、反向传播；权重更新
*随机梯度下降方法（stocastic gradient descent,SGD);批量训练（batch training）；小批量训练（mini-batch）；迭代（iteration）；时代（epoch）；前馈网络（Feedforward Network);多层全连接网络（FCN)；多层感知机（MLP）；多个密集层网络（Dense）


## 深度学习-多层神经网络（机器学习监督学习的方法）
### 机器学习
Machine Learning，简称ML，根据输入数据构建（训练）预测模型。
>>>>利用学到的模型，根据从数据中提取的分布中，对新数据（以前从未见过的数据，与训练模型时使用的同一分布）进行实用的预测。
>>>>机器学习的主要三种范式为：
>>>>·监督学习-1：决策树、决策森林、支撑向量机、贝叶斯分类器、核方法逻辑回归；
>>>>·监督学习-2：神经网络、全连接网络、卷积网络、循环网络；
>>>>·非监督学习：降维方法（PCA，自动编码器，主题模型）、聚类；
>>>>·强化学习：策略梯度、深度Q网络、Actor-Critic算法；

### 数据集
>>>>·训练集（training set）：数据集的子集，用于训练模型。
>>>>·验证集（validation set）：数据集的一个子集，从训练集分离而来，用于验证学习效果。
>>>>·测试集（test set）：数据集的子集，用于在模型经由验证集的初步验证之后测试模型。

### 机器学习的应用
>>>>·机器学习主要用于解决两类任务：
>>>>分类任务、探测任务

### 监督式机器学习（supervised machine learning）
>>>>根据输入数据及其对应的标签来训练模型。
>>>>模型（model）是机器学习系统从训练数据学到的内容的表示形式。
>>>>在监督式学习中，有标签样本（labeled example）包含特征和标签的样本。在监督式学习中，标签指样本的“答案”或“结果”部分。
>>>>有标签数据集中的每个样本都包含一个或多个特征以及一个标签。
>>>>比如:在垃圾邮件检测数据集中，特征可能包括主题行、发件人以及电子邮件本身，而标签可能是“垃圾邮件”或“非垃圾邮件”。

### 监督学习的两阶段
·训练（Train）和推断（Inference）
·监督学习特点
>>>>训练数据集由样本（sample）组成，每个样本上都有对应的标签（label），用来指导学习过程。
>>>>根据训练数据集（data set）中的样本（sample）进行学习，然后推断新的实例。

### 迁移学习（transfer learning)
>>>>将信息从一个机器学习任务迁移到另一个机器学习任务。
>>>>迁移学习涉及将从较简单任务的解决方案迁移到较复杂的任务或者将从数据较多的任务迁移到数据较少的任务。
>>>>迁移学习是迈向通用人工智能的一小步。
>>>>大多数机器学习系统都只能完成一项任务。在通用人工智能中，单个程序可以完成多项任务。

## 深度学习2：网络训练示例-二元分类示例
## 深度学习：网络训练猜测性别（Logistic回归）
*用python代码描述一下Softmax函数（提示可以用Numpy）
>>>>def softmax(x):
    exp_x=np.exp(x)
    return exp_x/np.sum(exp_x)
>>>>softmax([i for i in range(1,10)])

## TensorFlow初步
### TensorFlow\TensorFlow-basic
### Tensor操作实验
### TensorFlow PlayGround介绍
# DAY8课程小结Memo
## 回顾上节课，介绍本节课内容
### 上节课教学内容：
>>Python Numpy
>>Deep learning:人工神经元

### 本节课教学内容：
>>Python Pandas
>>TensorFlow2 Playground
>>Deep Learning II
>>二元分类（逻辑思提回归）
>>TensorFlow2基础

## Q&A
>>第11周，结队分组
>>第8-15周，AI邀请赛（分类）

## 课后作业
>>读：
>>>>《机器学习实战》（Hands-on Machine Learning with Scikit-Learn,Keras,TensorFlow2)第1-4章，第10章
>>>>Deep Learning，nature，2015
>>>>Machine Learning，scinence 2015
>>>>Automatic differentiation in machine learning a survey,2018
>>写：
>>>>学习小结

## Pandas学习
### pandas基础：
>>一维数据Series s=pd.Series(data,index=index) 如果data是个ndarray，那么index的长度必须跟data一致
>>

## TensorFlow2基础：张量、变量、自动微分、即刻执行
### 分对数logit
>>分对数（logit）模型
>>把区间（0，1）内的数值，变换到区间（-∞，+∞）
>>与sigmoid函数互为反函数


## TensorFlow2基础：计算量、模型、训练流程

## 多层神经网络
### 回归任务的损失度量函数-均方差
>>方差（variance)
>>标准差(standard deviation)
>>均方误差（mean squared error,MSE)
>>均方误差的开放叫均方根误差（Root Mean Squared Error,RMSE)
>>注：均方误差不同于标准差（均方差）
>>练习：用Python表述一下MSE，然后计算一下结果
>>>>一组预测值X=[72,94,79,83,65,81,73,67,85,82]
>>>>真实值（标签值）=80

### 分类问题的损失的度量函数-交叉熵
### 损失：输出值与标签的差异
## 反向传播算法
### 多层网络（深度网络）
### 损失函数的计算过程
### 回顾一下：导数与梯度
### 梯度计算-示例
### 最优化算法：梯度下降法
### 反向传播算法-损失函数对权重的梯度计算
## 反向传播的实际计算
### 单个人工神经元
### 单个算子（Operator）的反向传播的原理
### 反向传播的计算
## 权重更新-随机梯度下降法
### 梯度算法-权重更新与学习率
### 权重值更新-随机梯度下降法
## 模型训练过拟合解决方法
### 正则化
### 丢弃正则化
### 神经网络的实际训练-小批量训练（mini-batch）
### 神经网络的应用-推断（inference）
### 神经网络运用的一般流程
>>准备数据集
>>搭建网络模型
>>训练模型
>>测试模型

## 实际示例
>>用逻辑斯提回归单元进行二元分类案例
>>逻辑斯提回归实验（Logistic Regression)二元分类演示实验
>>>>步骤一：获取训练数据
>>>>步骤二：搭建模型
>>>>步骤三：定义损失函数
>>>>步骤四：运行训练数据，从目标值计算损失
>>>>步骤五：优化器来调整权重变量
>>>>步骤六：结果评估-预测

## 作业
>>作业一：有序数组的平方
>>作业二：使用Tkinter为第一题制作一个GUI



## 课程小结，展望下节课

# 课程小结Memo
## 教学目标
>>学习TensorFlow2基础
>>>>张量、变量
>>>>计算图、即刻执行
>>>>计算图
>>>>模型
>>>>训练循环
>>>>自动微分（原理）
>>学习Keras
>>>>总体介绍

## 课后作业
>>读：
>>《机器学习实战》
>>Deep Learning,nature,2015
>>Machine Learning,science 2015
>>Automatic differentiation in machine learning a survey,2018
>>写：
>>学习小结
>>练习：
>>课堂中的“想一想，练一练”（二元分类）实践
>>课外作业3-CMS选课系统练习
>>准备大作业4-时频谱图分类

## TensorFlow2基础：张量、变量、自动微分、即刻执行
### 神经网络运用的一般流程
>>数据集准备
>>网络模型搭建
>>模型训练/模型测试
>>模型应用-推断

### 用张量表示神经网络
>>张量的概念：张量（Tensor）的实质是N维数组，是计算机处理离散的数值的组织方式
>>实际例子
>>>>多层全连接网络有5个神经单元
>>>>有3个输入，2个输出，中间有1个隐藏层，有1个输出层

## TensorFlow2基础：计算图、模型、训练流程
>>TensorFlow2基础知识汇总：http://tensorflow.google.cn/guide
>>Github目录：http://github.com/tensorflow/docs-|10n/tree/master/size/zh-cn/guide

### 张量是具有同一类型（称为dtype）的多维数组
>>>>张量有形状。
>>>>下面是几个相关术语：
>>>>形状shape、秩rank、轴axis或维度dimension、大小size

### 变量
>>tf.Variable 表示张量，对它执行运算可以改变其值
>>TensorFlow变量
>>

### Tensor创建
>>用python描述一个4×4的二维张量
>>一个4×5×6的三维张量
>>

### Tensor运算
>>tf.add
>>tf.multiply
>>tf.matmul

#### 张量运算符（op）运算
>>tf.reduce_max 寻找元素最大值
>>tf.argmax 求最大值的索引
>>tf.nn.softmax对元素进行归一化处理

#### DTypes详解
>>使用Tensor.dtype属性可以检查tf.Tensor的数据类型
>>从Python对象创建tf.Tensor时，可以选择指定数据类型
>>如果不指定，TensorFlow会选择一个可以表示您的数据的数据类型。
>>>>TensorFlow将Python整数转换为tf.int32,将Python浮点数转换为tf.float32
>>>>另外，当转换为数组时，TensorFlow会采用与NumPy相同的规则

#### Tensor reshape
#### Tensor广播
#### Tensor索引
#### 特殊张量
##### 不规则张量
##### 字符串张量

### 自动微分Autodiff
x=tf.constant(1.)
with tf.GradientTape() as t:
    t.watch(x)
    y=x*x+tf.exp(x)
t.gradient(y,x).numpy()

import tensorflow as tf
import numpy as np
import math
x=tf.Variable(1.0)

with tf.GradientTape() as t:
    y=x*x+tf.exp(x)
    dy_dx=t.gradient(y,x)
    print(dy_dx.numpy())
# DAY10课程小结Memo
## 回顾上节课
>>上节课关键词：人工神经元、多层网络
>>上节课的知识点：TensorFlow2的张量、变量、自动微分
>>上节课的小练习：Numpy张量计算，2层网络张量计算
https://qn-st0.yuketang.cn/Fs3O88lhrfKDyO2jrwmIo2f1W0v7

## Python
### 类定义与实例
### 类继承
## TensorFlow2基础：计算图、模型、训练流程
### 模块、层和模型简介：https://tensorflow.google.cn/guide/intro_to_modules
>>设置
>>import tensorflow as tf
from datetime import datetime
%load_ext tensorboard

### Graph（计算图）
#### Graph的特点
>>计算图可以显著是提高速度
>>函数tf.function并不会自动加快代码速度
>>多态性：一个函数，多种计算图
>>Graph（图）-恢复eager模式

### TensorFlow2完整训练流程
>>训练流程
>>1、获取训练数据
>>2、定义模型
>>3、定义损失函数
>>4、运行训练数据，从目标值计算损失
>>5、计算损失的梯度，并使用优化器来调整变量以适应数据。
>>6、结果评估
>>使用keras模型

### tf.data的用途
>>TensorFlow数据结构
>>用tf.data读取list

### 动态决定张量维度（补充）
## 课程大作业3-回顾
## 课程大作业5
## ML-AI邀请赛-说明
# DAY11课程小结Memo
## 回顾上节课，介绍本节课内容
## 自动微分
## 深度学习4：网络架构
## 深度学习5：卷积网络
## TensorFlow2-Keras:总体\顺序模型\模型与层\模型保存与加载
### Keras顺序模型
### Keras层和模型
### Keras模型的保存和加载
### Keras函数式API-https://tensorflow.google.cn/guide/keras/functional
### Kerasu训练和评估-https://tensorflow.google.cn/guide/keras/train_and_evaluate
### Keras训练循环-https://tensorflow.google.cn/guide/keras/writing_a_training_loop_from_scratch
### Keras遮盖与填充-https://tensorflow.google.cn/guide/keras/masking_and_padding
### Keras定制fit()内部操作-https://tensorflow.google.cn/guide/keras/customizing_what_happens_in_fit
### Keras迁移学习与细调-https://tensorflow.google.cn/guide/keras/transfer_learning
## TensorFlow2-Keras-Dense-卷积网络
### TensorFlow2-卷积网络-https://tensorflow.google.cn/tutorials/images/cnn
### TensorFlow2-图像分类（Keras高级）-https://tensorflow.google.cn/tutorials/images/classification
### TensorFlow2-tf.data和加载图片-https://tensorflow.google.cn/guide/data
### TensorFlow2-图像分类（数据增强）-https://tensorflow.google.cn/tutorials/images/data_augmentation
### TensorFlow2-图像分类（迁移学习）-https://tensorflow.google.cn/tutorials/images/transfer_learning
### TensorFlow2-图像分割（图像分割）-https://tensorflow.google.cn/tutorials/images/segmentation
## TensorFlow2-Keras-图像分类（Keras卷积网络）
# Day12课程小结Memo
## 课程回顾
## 课后作业
* 读《机器学习实战》
* Paper
## 深度学习6：循环网络
## TensorFlow2-Keras-循环网络及其应用
## 教学内容
* 循环网络的原理
* 循环网络基本结构
* 长短时记忆网络/门控循环单元网络
* 循环网络的应用
* 循环网络的扩展

## TensorFlow-开源活跃的Github项目
* 项目地址：https://github.com/tensorflow/tensorflow
## Keras2-循环网络及其应用（1）
* 理论部分
* * 循环网络的原理
* 时间部分
>> Keras2循环网络
>> Keras2单词嵌入
>> Keras2文本分类
>> Keras2文本生成

## Keras2-循环网络及其应用（2）
* 音乐生成（Keras）
* 机器翻译的注意力机制（Keras）
* 图像注解（Keras）
# Day13课程小结Memo
## 课程回顾
* 循环网络的原理
* 循环网络基本结构
* 长短时记忆网络/门控循环单元网络
* 循环网络的应用
* 循环网络的扩展
## 本节课教学内容
* 了解语音识别原理
* 了解深度学习在语音识别中的应用
* 了解语音识别应用
* 了解TensorFlow2全景
### 理论部分：
* 语音识别循环网络的应用
* 传统语音识别方法
* 端到端的深度学习语音识别
### 实践体验部分:
* 语音控制体验环节

## 下节课预告
* 了解计算机视觉的原理
* 了解深度学习在计算机视觉应用

## TensorFlow2-文本分类（Keras）
## TensorFlow2-Keras：循环网络应用-文本生成	
## 	语音识别体验
## 语音识别原理Audio
## CTC
* CTC解决的问题
* CTC原理
* CTC-loss损失函数
* CTC算法
* CTC-loss详细原理
### CTC实现
#### 开源实现
* 百度研究院开源实现warp-ctc
* TensorFlow2，CTC loss
* TensorFlow2，CTC beam search
### DeepSpeech 1-2-3
* 百度的DeepSpeech算法
* DeepSpeech2
* DeepSpeech2模型架构
* DeepSpeech2实现技巧
* DeepSpeech2模型架构
* 批归一化（Batch normalization)
* DeepSpeech开源实现
* DeepSpeech2-全中文语音识别
* TensorFlow2语音处理
# Day14课程小结Memo
## 课程回顾
* 了解语音识别原理
* 了解深度学习在语音识别中的应用
* 了解语音识别应用
* 理论部分
>>  语音识别中循环网络的应用
>>  传统语音识别方法
>>  端到端的深度学习语音识别

* 实践体验部分：
>> 语音控制体验环节

* Keras2-循环网络及其应用
>> Keras2文本分类
>> Keras2文本生成

## 本节课教学内容
* 了解计算机视觉的原理
* * 尤其是自动驾驶
* 了解深度学习在计算机视觉应用
* * 图像分类、对象检测、语义分割
* 了解TensorFlow2全景（TensorFlow2总结）（总结收尾）
* * 你是否可以自己打造一个深度学习框架？

## 时间安排
* 计算机视觉-总体
* 计算机视觉指标
* 计算机视觉-对象检测hub-OD
* TensorFlow2全景

## 课后作业
* 读：《机器学习实战》
* paper
* 附录：iCenter-AI平台-说明
* * 十几台GPU工作站
* * 统装GPU工作站——统一用AI平台软件管理：http://ai.moppas.com/
* * 散装GPU工作站——提供给bdmi课程专用的GPU工作站，供选题的同学使用。
>>环境：Jupyter notebook 服务器；
>>网址URL访问
>>链接：微信群

## 导学
* 了解人类的视觉感知系统（参考）
* 了解计算机视觉
* 了解基于深度学习的计算机视觉方法
### 名词术语
* 人类感知（Human Perception)
* 计算机视觉（computer vision)
* 计算机视觉的任务（visual task)
* 分类（image classification)
* 定位（localization)
* 对象检测（object detection)
* 语义分割（semantic segmentation)
* 自主（无人）驾驶（self-driving/driverless)
* 自动驾驶车（autonomous vehicles)
### 名词术语-2
* 精确率（Precision）
* 召回率（recall)
* 准确率（accuracy)
* PR曲线（P-R curve）
* AUC指标（area under curve)
* 平均精确率均值mAP（mean average precision)
* IOU(重叠联合比)
* R-CNN(Region-based CNN)
* YOLO(YOU Only Look Once)
* SSD(Single Shot MultiBox Detector)

### 人类视觉系统：参照
* 人类感知-视觉/听觉-Human Perception:audiovisual information processing
* 人眼视觉系统的处理从视网膜开始，有色彩处理和黑白光采集和处理系统
* 人类大脑的视觉通道
* * 人的70%的信息来自于视觉
* * 人的视觉处理依赖大脑皮层的不同区域（Cortex）

### 计算机视觉（Computer Vision)
* 计算机视觉是什么？
* know what is where by looking-计算机处理来理解图像和视频
* 计算机视觉是实现人工智能的一个重要挑战
>>自动抽取图像的信息

* 计算机视觉
>>机器视觉（Robot Vision）
>>智能监控
>>无人驾驶

* 自动驾驶
>>自主无人驾驶（Self-Driving/Driverless）：通过控制车辆的速度、方向刹车，来接替人类驾驶员，直接控制车辆。
>>辅助驾驶（ADAS)：利用车体加装的激光雷达、相机和GPS等传感器，观察周围环境，而后通过决策算法，提醒驾驶员注意道路状况的层次。
>>谷歌、特斯拉、蔚来等公司都在开发自动驾驶
>>developer.nvidia.com/blog/deep-learning-self-driving-cars/

### 计算机视觉的任务
* 计算机视觉是人工智能快速发展的一个分支
* 计算机视觉（简单来说）就是用计算机代替人眼来做测量和判断
* 计算机视觉的主要任务包括：分类、定位、检测和分割
* 分类、定位、检测、分割

### 计算机视觉-识别指标
识别的指标-精确率（Precision）
！二元分类
* 精确率（Precision）是针对预测结果而言的，它表示的是预测为正的样本中有多少是真正的正样本。预测（分类）为正有两种可能：
* * 一种是把正类预测为正类（TP)
* * 另一种是把负类预测为正类（FP）
* 精确率（precision） = TP/(TP+FP)
* 召回率（Recall）是针对原来的样本而言的，它表示的是样本中的正例有多少被预测正确了。预测（分类）为负有两种可能：
* * 一种是把原来的负类预测成了负类（TN）
* * 另一种是把原来的正类预测为负类（FN）
* 召回率（recall) = TP/(TP+FN)
* 准确率（Accuracy）是指对于给定的测定数据集，分类器正确分类的样本数与总样本数之比。
* 准确率（accuracy）= （TP+TN)/(TP+FN+FP+TN)==预测对的/所有
>>>> 举例说明-二元分类

#### 混淆矩阵（Confusion Matrix）！多元分类
>>>>举例说明
>>>>Pascal VOC比赛
* Pascal VOC Challenge——图像识别与物件分类的挑战赛
* 对象检测的识别精确率指标
* 平均精确率均值mAP（识别准确率指标之一）
* VIVA（智能交通与应用的视觉应用）
* PR曲线的AUC指标（识别准确率指标之二）

### 基于深度学习的计算机视觉
* 分类 Image Classification
* 对象检测detection
* 对象类别
* 对象类别与位置
* 分割segmentation
* 场景解析与标记

### 图像分类
卷积运算
* 二维卷积
* 三维卷积
卷积网络的层间连接
* 卷积核运算等效为局部规则连接（Locally Connected)
* 区别于全连接网络Dense的全连接（Fully Connected）
* LeNet-5：手写字体识别
* ImageNet图像分类赛
* ILSVRC图像分类挑战赛
* ImageNet图像分类赛
* AlexNet卷积网络
* face++人脸识别-商汤Sense time
* 计算机视觉-Megvii-矿石科技Face++
* * 偏重于人脸识别与计算机视觉
* * http://www.faceplusplus.com/
* 具有自主深度平台MegEngine
* 计算机视觉-人脸辨识与识别
* * 特征学习（feature learning)
* * 特征工程（feature engineering）
* * 特征学习取代了特征工程——学习得到的特征；图像化显示
### 视觉对象检测的方法
* 计算机视觉-基于深度学习的视觉对象检测方法
* 视觉对象检测方法发展
* R-CNN
* Fast R-CNN
* Faster R-CNN
* OD算法
* 国际会议：CVPR\ICCV\ECCV
### 视觉对象检测的指标
* IOU（重叠联合比）
* 视觉对象检测结果的正确性指标的计算
### R-CNN
* 
# Day15课程小结Memo
## 回顾上节课，介绍本节课内容
## 机器智能-人工智能-概览
### 人工智能的定义和发展
* 1956年的达特茅斯会议（Dartmouth Summer Research Project on Artificial Intelligence)第一次提出了“人工智能”概念
* 会议发起人：
** 约翰·麦卡锡（J·McCarthy)** 
** 马文·闵斯基（M.LMinsky）**
** 克劳德·香农（C.E.Shannon）**
** 纳撒尼尔·罗彻斯特（N.Rochester）**
* 约翰·麦卡锡将人工智能定义为：“研制智能机器的一门科学与技术”。
### AI的三次热潮
* 第三波热潮（2016-至今）：AIphaGo
* 深度学习\强化学习\迁移学习
* 大数据+算力提升+深度学习
** DeepStark**
**Lamda**
### AI的学科研究内容
* AI领域和方向
* 核心层：机器学习、强化学习、深度学习
* 应用层：语音识别、计算机视觉、自然语言处理
* 广义层：路径规划、机器人学
#### 机器智能（Machine Intelligence)
（机器智能）智能的及其和智能的软件依赖算法对观测到的数据进行分析（reason）来做出有用的预测（prediction）和决定（decision）
（机器智能）系统依赖机器学习、人工智能，组合了计算、数据、建模和算法
#### AI-ML
** 鸽子智能**
http://www.sciencemag.org/news/2015/11/pigeons-spot-canser-well-human-experts
** 观点1：人类与动物的不同，是智能程度的不同，学习能力的不同。
### AI的一些知名学派（基本技术-应用技术）
* AI-机器学习派1（Michael Jordan Tom Mitchell)
* AI-深度学习派1（ACM图灵奖2018年度）
* AI-数据科学派1（ACM图灵奖2020年度）_机器学习是统计学的分支

### 研究论文
#### 机器学习的学术会议
* AAAI-人工智能会议
* ICML-机器学习国际会议
* NeurIPS-神经信息处理系统年度会议
* IJCAL-国际人工智能联合会议
* KDD-国际国际数据挖掘与知识发现会议
* CVPR-国际计算机视觉与模拟识别会议
#### Arxiv-论文预印本
* Paperwithcode,https://paperwithcode.com/sota
#### Nature新子刊《自然-机器智能》——nature machine intelligence
* 算法与硬件研究、机器智能在多领域应用、机器智能对社会工业等领域影响，http://www.nature.com/natmathintell/

### AI生态系统与能力需求
* 人工智能启动原因——海量互联网数据、行业大数据
* 人工智能概况——计算硬件基础
* 人工智能（AI）生态系统架构（业务层、AI应用层、AI模型层、AI架构层、基础框架层）
* 人工智能（AI）技术人才（算法层、工程层、数据层）
* 深度学习-软硬件布局（热点）——DL硬件、DL软件、AI产业
* 深度学习-软件框架（热点）——TensorFlow：Google、PyTorch：Facebook_AI research、MXNET:Amazon、Baidu/PaddlePaddle
* 人工智能的普及：人工智能技术未来将无处不在，应用之广，改变之大，可以视作是一场新技术革命。
* AI is the new electricity.——吴恩达，斯坦福大学

### 手机中的AI
* 蓬勃发展的新产业-1-智能语音交互
* 蓬勃发展的新产业-2-自然语言处理NLP
* 蓬勃发展的新产业-3-计算机视觉-Megvii
* 蓬勃发展的新产业-4-自动驾驶1-Tesla、Momenta
* 蓬勃发展的新产业-5-智能机器人
## 大作业4-回顾-讲课和演示
* 课程大作业内容——数据集准备
* 时频谱图数据集
* 实验思路：使用CNN\RNN
* 数据增强：高斯噪声、校验噪声、随机旋转、随机缩放
* Dropout和正则化
* 实验思路：卷积层、池化层

## 结课
* 课程回顾
* 课程主讲人寄语
* 支持团队教师代表致辞
* 课程负责人致谢
* 互动时间

## 期终课程大作业（选题）
## 量化AL模型邀请赛
