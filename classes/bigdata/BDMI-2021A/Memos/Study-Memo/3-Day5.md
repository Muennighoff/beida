# WW5 课堂总结

## SQL

- 背景：
  - SQL是一种关系型数据库的结构化查询语言，是一种高级编程语言
- 优点：
  - 关系代数模型，提升用户与数据交互的抽象层次
  - 简洁，可以移植，不受系统等影响
- 缺点：
  - 存在重复数据，需要使用distinct等方式去重
- 包括：
  - DDL(Data Definition Language)：用于数据库定义，创建、修改数据表 create alter drop truncate comment rename
  - DML(Data Manipulation Language)：插入、删除 select where 
  - DCL(Data Control Language):数据库控制语言 授权、角色控制 grant revoke
  - TCL(Transaction Control)：事务控制语言 savepoint
- Tips
  - 可以一行输入多语句，语句用；隔开
  - 所有空格被忽视
  - -- /* */ 用来注释
  - 命令大小写无关，输入大小写相关
- 操作
  - 创建数据库 create database_name;
  - 删除数据库 drop database_name;
  - select * from table
  - 连接操作
    - 交叉积占据内存，可以进行筛选
    - 内连接inner join,left join, right join
      - eg. table1 join table2 on name
    - 外连接 left outer join, right outer join, full outer join
    - inner join left join right join
  - 创建索引
    - create index index_name on table_name (column name)
  - 事务操作
    - 执行包含多条sql语句，形成一个执行块
    - 要么全部执行成功，要不全部不执行
- 数据表的特征
  - 每一列称为属性
  - 表的属性必须只具有一个原子类型，不可再分
  - table 的 key应该是属性的最小子集
  - 依赖的基础数据结构：**multiset**
- 查询语句
  - 简单的字符串匹配 使用LIKE
  - 连接的语义 
    - eg （name,sex） in ()
```sql

'%gizmo%' -- % indicates sequence
'_ore' -- _ indicates character
```



## tkinter

- widgets
  - Menu 
  - Button 用于按键
  - CheckButton 可以进行多选
- 一些常用的方法
  - window.geometry() 可以用来设置窗口大小
  - button.place(x=,y=)  x y是widget左上角位置
  - listbox 
    - listbox.insert(END,item) 添加一个item在listbox的末尾
    - listbox.delete(start,end)
    - listbox.focus( ) 将光标移到开头

```python
        self.window = tk.Tk()
        self.input_frame = tk.Frame(self.window,height = 300,width = 400)
        self.input_frame.pack()
        self.input_hint = tk.Label(self.input_frame,text="Please input a sorted ascending integer array in the form like [-2,0,1]")
        self.input_hint.pack()
        self.input_box = tk.Entry(self.input_frame)
        self.input_box.pack()
        self.output_frame = tk.Frame(self.window,height = 300,width = 400)
        self.output_frame.pack()
        self.output_button = tk.Button(self.output_frame,text="Sort!",command=self.squareSort) # no need to use method()
        self.output_button.pack()
        self.var = tk.StringVar()
        self.output_label = tk.Message(self.output_frame,textvariable=self.var)
        self.output_label.pack()
```

