# 学习小结 20210915

#### 尹哲良

注：下划线部分为今日新接触内容

## Python 基础

### 查看内置关键字

```python
import keyword as kwd
print(kwd.kwlist)
```

### 基本数据结构

列表、集合、字典

### 控制流

if-elif-else

for-while

### Python 类

类的定义：初始化、属性、方法

类的使用：实例化、调用类函数

### Python 模块

代码块 → 函数 → 类 → 包

<u>pypi：共享包，使得其可以用pip下载</u>

## 算法基础

### 概念

定义：解决问题，清晰步骤

特征

<u>举例：圆周率的计算。幂级数算\pi</u>

### 大整数相乘

分治算法：大整数分为高低位，两两相乘

<u>改进：分治时分为三个子问题，复杂度从2降为1.6</u>

## Matplotlib

基本绘图方法

<u>辅助参数设置：dashes，虚线形态</u>

```python
plt.plot(x,y,dashes=[2,2,8,2])
```

<u>绘制子图：subplot</u>

<u>pygal：更加精细的可视化方法</u>

## Markdown

标题

<u>字体格式：颜色，大小，加粗，斜体</u>

<u>段落格式：缩进、列表</u>

<u>插图</u>

<u>Latex：$$插入</u>

## Git的使用

<u>fork：项目复制为个人版本</u>

<u>pull：云端保存到本地</u>

<u>push：本地上传到云端</u>

<u>合作方式：分支合并、协调</u>

## 总体学习感受

+ 具有python和算法基础，因此前半段内容较为熟悉
+ 有关matplotlib、markdown、git的部分，需要课后练习



