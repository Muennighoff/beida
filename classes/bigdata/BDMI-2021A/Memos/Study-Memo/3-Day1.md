# 第一周课程小结

## Python 基础知识
因为笔者对Python使用频率较高，所以对课程讲述内容比较熟悉，现总结如下：
- 基本内建类型：字符串、整数、浮点数、布尔值
  - str.strip() 从字符串中移除输入的字符
- 基本数据结构：字符串、列表、集合、字典
- 基本语法：条件语句、循环语句（for、while）
- 函数：lambda等
  - lambda 匿名函数，是一个表达式，可以与map连用
- 类：类、对象、属性、方法、参数、实例化

## Matplotlib画图实践
课程讲解如何绘制散点图、线图、柱状图、3D图，以及相应的参数配置

## 圆周率计算、算法实践
- 讲解了圆周率的计算意义、算法发展过程
  示例：
```python
  def pical(times=10000):
    pi = 0
    currenttime = 1
    while currenttime <= times:
    pi += ((-1)**(currenttime-1))/(2*currenttime-1)
    currenttime += 1
    pi = pi*4
    return pi
  
  pi = pical()
  print("pi approximately equals to {}".format(pi))
```

- 讲解了算法的定义和特征
  示例：
  
```python 
  def equation_solving(a,b,c):
      x1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
      x2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
      return x1,x2
  x1,x2 = equation_solving(2,24,22)
  print(x1,x2)
```

##  Markdown 语法
因为笔者之前多使用Latex，所以对Markdown的使用方法并不是十分熟悉，但是通过本节课的讲授学习了Markdown的基本语法，掌握了文本格式、图片插入、数学公式等功能。

示例：
- <font color = red size = 2> 我是红色的字</font>
- <img src = '/Users/adam/Desktop/Senior Autumn/Big data/shanghai.jpg' style='zoom:50%'>
- 
$$
\pi = 4 * \sum_{n=0}^{\infty} \frac{(-1)^{n-1}}{2n-1}
$$

## Git的使用
课程讲解了Git的概念和使用方法