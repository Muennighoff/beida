# 学习小结 20211013

#### 尹哲良

## 选课系统数据库设计

### 存储的数据对象

学生、老师、教务、课程 四个类

### 需要实现的功能

学生选课：看到课程信息、执行选课操作

选课限制：学分限制、时间限制、名额限制

学生应用：查看选课信息

教师开课：获取教室情况、开课时间、开课地点

教师运营：查看选课名单、录入成绩

## SQL

### 语法特征

+ 空格忽略
+ 分号隔开语句
+ 注释：##，--， /*
+ 大小写不敏感

### 具体语句

#### 创建

create database 数据库名

create table 表名

#### 删除

drop table 表名

drop table if exists 表名

#### 表内操作

指定某张表：alter table 表名

添加列：add c3 int(3)

主键：学号，个体的主要标识

### 数据表

#### 数据结构

set：非重复集

multiset：可重复集，sql的底层逻辑

数据表中每一个数据值都是简单数据类型（Atomic types）

#### 数据表模式

键：若干数据属性用来确定个体，可以有多列，但属性数目需要尽量少

SFW query

#### 数据查询

单表查询：SELECT (ATTRIBUTE) FROM (TABLE) WHERE (CONDITION)

多表查询：SELECT (ATTRIBUTE) FROM (TABLE1,TABLE2) WHERE (CONDITION)

如果不同表中有相同的属性，写数据表前缀 TABLE1.name

多表查询将所有满足要求的结果都列出来

外连接：声明主表，主表中有的元素都会出现在查询表中

作用：组织不同的表。例如，查询学生选了什么课

## Python SQLite

## Tkinter

### 性质

GUI：用户使用的图形界面

Button：按钮设置

Entry：输入设置

Label：显示
