## Python 基础总结

>有编程基础过一遍就可以了。

### 变量

格式： `变量名 = 值`

Python 中不需要指定数据类型，系统会自动帮助我们推导类型。

变量名采用驼峰命名法，Python中建议使用下划线分割。

Python中的关键字可以通过代码打印出来，关键字不能作为函数名，变量名使用

```
import  keyword
print(keyword.kwlist)
```

### 注释
单行注释

```
# 单行注释
```

多行注释

```
'''
多行注释
多行注释
'''
```

### 数据类型转换
通过数据类型+()的形式转化数据类型

```
str = "10"
# 将字符串转换成整型
num = int(str)
# 其他同理

```

### 输入和输出
输出 

```
def print(self, *args, sep=' ', end='\n', file=None):
# *args 表示任何多个无名参数,各个值之间用“,”隔开。
# sep 表示当输入多个打印的值时,各个值之间的的分割方式,默认是“ ”,我们可以通过为sep赋值来自定义分割方式
# end 控制print中传入值输出完后结束符号，默认为换行,可以通过为end赋值设置为其他自定义结束方式
# file 设置输出设备以及把print中的值打印到什么地方,默认输出到准端,可以设置file = 文件储存对象，把内容存到该文件中。

f = open(r'a.txt', 'w')
print('python is good', file=f)
f.close()
```

输入

```
def input(*args, **kwargs):
# *args, **kwargs 都是Python中的可变参数
# *args表示任何多个无名参数，它本质是一个tuple； 
# **kwargs表示关键字参数，它本质上是一个dict； 
# 如果同时使用*args和**kwargs时，*args参数列必须在**kwargs前面。

示例：
def fun(*args,**kwargs):
    print('args=', args)
    print('kwargs=',kwargs)
fun(1,2,3,4,A='a',B='b',C='c',D='d')

输出：
args= (1, 2, 3, 4)
kwargs= {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}
```

### if 判断语句

```
if score >= 60 and age<=80:
    print("良")
elif age > 80 and age <100:
    print("优")
else:
    print("不及格")
    
# and 等于 并 , or 等于 或
# 逻辑运算符 == , >= , <= , !=
```

### 格式化输出
```
#%s: 输出字符串
#%d: 输出int类型
#%f: 输出float类型
#%x: 输出16位进制数据
```

### 字符串的常见应用
定义字符串可以使用单引号，双引号，三引号

```
str = "hello world"
# 根据指定数据查找其第一次出现的下标，如果没有该数据则直接crash
str.index("h")

# 根据指定数据查找其第一次出现的下标，find如果没有找到数据返回的是-1.
str.find("z")

# 统计字符串的长度
len(str)

# 统计某个字符出现的次数
str.count("l")

# 替换指定的数据,如果没有则不替换
str1 = str.replace("l","x")

# 分割数据（将分割的数据装入列表里面，对应分割出来的字符就是列表中的元素）,如果没有对应的分割符，则会将整个分割为一个
str_list = str.split(",")

# 是否以指定数据开头
str.startswith("http") 

# 是否以指定数据结尾
str.endswith("xxx")

# 把字符串以指定字符分割成三部分，如果不存在指定字符串则分为整体和两个空字符串
str.partition("bb")

# 根据指定字符串拼接数据,my_str中每个字符之间插入一个flag_str，插入列表页可以
flag_str = "-"
my_str = "abc"
result = flag_str.join(my_str)
print(result)

# 去除指定参数，如果不传参数则默认去除空格
str.strip()
# 去除左边空格
str.lstrip()
# 去除右边空格
str.rstrip()

```
