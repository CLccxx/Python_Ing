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

局部变量与全局变量

局部变量：在函数内定义的变量叫局部变量，局部变量只能在函数内使用，不能在函数外使用。
全局变量：全局变量可以在不同函数内使用。如果需要修改全局变量的值，需要使用 `global` 对变量修饰，之后进行修改



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
# *args 表示任何多个无名参数，各个值之间用“,”隔开。
# sep 表示当输入多个打印的值时，各个值之间的的分割方式，默认是“ ”，我们可以通过为sep赋值来自定义分割方式
# end 控制print中传入值输出完后结束符号，默认为换行，可以通过为end赋值设置为其他自定义结束方式
# file 设置输出设备以及把print中的值打印到什么地方，默认输出到准端，可以设置file = 文件储存对象，把内容存到该文件中。

f = open(r'a.txt', 'w')
print('python is good', file=f)
f.close()
```

输入

```
def input(*args， **kwargs):
# *args， **kwargs 都是Python中的可变参数
# *args表示任何多个无名参数，它本质是一个tuple； 
# **kwargs表示关键字参数，它本质上是一个dict； 
# 如果同时使用*args和**kwargs时，*args参数列必须在**kwargs前面。

示例：
def fun(*args，**kwargs):
    print('args=', args)
    print('kwargs=',kwargs)
fun(1,2,3,4,A='a',B='b',C='c',D='d')

输出：
args= (1， 2， 3， 4)
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
# 根据指定数据查找其第一次出现的下标，如果没有该数据则直接crash，可以指定查找的范围
str.index("h")

# 同index(), 从右边开始
str.rindex("o")

# 根据指定数据查找其第一次出现的下标，find如果没有找到数据返回的是-1，可以指定查找的范围
str.find("z", start = 0, end = len(str))

# 同find(), 从右边开始找
str.rfind("z")

# 统计字符串的长度
len(str)

# 统计某个字符出现的次数，并且可以指定范围
str.count("l", start = 0, end = len(str))

# 替换指定的数据，如果没有则不替换，可以指定最多替换多少次。
str1 = str.replace("l","x",str.count(str1))

# 分割数据（将分割的数据装入列表里面，对应分割出来的字符就是列表中的元素），如果没有对应的分割符，则会将整个分割为一个
str_list = str.split("，")

# 是否以指定数据开头
str.startswith("http") 

# 是否以指定数据结尾
str.endswith("xxx")

# 把字符串的第一个字符大写
str.capitalize()

# 把字符串以空格分开的每个字符串第一个字符大写并返回改字符串
str.title()

# 把字符串中所有大写字符转为小写
str.lower()

# 把字符串中所有小写字符转为大写
str.upper()

# 返回一个与原字符左对齐，并使用空格填充至长度width的新字符串，如果width本来就小于字符串长度则不做补充。
str.ljust(width)

# 返回一个与原字符右对齐，并使用空格填充至长度width的新字符串，如果width本来就小于字符串长度则不做补充。
str.rjust(width)

# 返回一个与原字符串居中，并使用空格填充至长度width的新字符串
str.center(width)

# 把字符串以指定字符分割成三部分，如果不存在指定字符串则分为整体和两个空字符串
str.partition("bb")

# 同partition(), 从右边开始
str.rpartition("bb")

# 根据指定字符串拼接数据，my_str中每个字符之间插入一个flag_str，插入列表页可以
flag_str = "-"
my_str = "abc"
result = flag_str.join(my_str)
print(result)

# 去除指定参数，如果不传参数则默认去除空格，只能去除两边的数据
str.strip()
# 去除左边空格
str.lstrip()
# 去除右边空格
str.rstrip()

# 按照行分割, 返回一个包含各行作为元素的列表
str.splitlines()

# 如果str所有字符都是字母, 则返回True, 否则返回False
str.isalpha()

# 如果str只包含数字则返回True, 否则返回False
str.isdigit()

# 如果str所有字符都是字母或数字则返回True, 否则返回False
str.isalnum

# 如果str只包含空格, 则返回True, 否则返回False
str.isspace()

# 在str中每个元素后面插入insertStr, 返回新字符串
str.join(insertStr)

```

### 循环语句
while 循环

```
num = 0
while num <=5:
    num +=1
    print("hello world")
```

for 循环: 有三个参数，起始数据：默认为0，终止数据：默认不打印，以及跳跃数据（步长，默认为1）

```
for value in range(1,6,2):
    print(value)
# 打印内容：1，3，5
```

for循环和whlie循环可以结合else使用:循环结束之后执行

### 列表
Python中的列表就是数组，列表中可以存放任意类型数据。

```
# 定义一个列表
my_list = [1, 3.14, "hello world", True]

# 获取列表的长度
len(my_list)

# 给列表增加指定数据
my_list.append(5)

# 列表指定位置插入数据
my_list.insert(1, "abc")

# 可以使用-1做索引，直接获取最后一个元素
my_list[-1]

# 将另一个集合中的元素逐一添加到列表中
my_list.extend(my_list1)

# 修改数据，直接通过下标进行修改
my_list[0] = "4"

# 根据元素的值进行删除，如果数组中该数据则会crash
my_list.remove("abc")

# 根据下标删除，下标要合法，否则会crash
del my_list[0]

# 返回被删除的值，如果不传下标则默认删除最后一个元素
remove_item = my_list.pop(0)
print(remove_item)

# 判断指定数据是否在列表当中，返回bool值
result = "abc" in my_list

# 判断不存在
result = "abc" not in my_list

# 根据数据获取其对应的下标，数据不存在会crash
result = my_list.index("草莓")

# 根据指定数据获取数据在列表中的个数
result = my_list.count("a")

# 将列表按照特定的顺序排序，默认为由小到大，可以设置参数reverse = True改为倒序排序，由大到小。
my_list.sort()

# 将列表翻转，逆向
my_list.reverse()
```

可以使用运算符对列表直接进行相应的操作(+ , *)

```
[1,2] + [3,4]  -> [1,2,3,4]
["go"] * 3 -> ["go","go","go"]
```

### 元组
与列表类似，以小括号形式存储的数据集合，可以存储任意数据类型，可以根据下标获取数据，但是不能对元组进行数据修改。

元组不可变，所以代码更安全，如果可以满足需求，尽量使用tuple代替list。

```
# 注意：如果元组只有一个数据，则无法构成元组，其类型为该数据的类型
# tuple = (1) 其实是int类型的。
# 如果想创建只有一个数据的元组可以这样 tuple = (1，) 但是这样做并没有什么意义。
my_tuple = (1, 3.14, "abc", True)

# 根据下标取值
my_tuple[1]
```

元组同样适用于列表中判断数据是否在元组中，以及获取数据在元组中的下标及个数。

元组内的数据不可以进行修改，但是我们可以对元组中的列表内的数据进行修改

### 字典
字典：以大括号表现形式的键值对数据组合，字典是无序的，通过key来获取value。

```
my_dict = {"name":"cc", "age":17}

# 通过key获取value
value = my_dict["name"]
# 如果字典中没有该key则会crash，可以通过使用get()来避免这个问题，如果没有key则会返回NONE
my_dict.get("sex")

# 为字典添加键值对，如果字典中存在该key，则修改value的值，如果不存在则添加该键值对
my_dict["name"] = "李四"

# 删除(key和value同时存在)
del my_dict["age"]

# 删除整个字典
del my_dict

# 清空整个字典
my_dict.clear()

# 随机删除键值对
my_dict.popitem()

# 删除指定的键值对
my_dict.pop("sex")

# 获取字典里面所有的key
result = my_dict.keys()

# 获取所有的value
result = my_dict.values()

# 遍历字典的项
for item in my_dict.items():
    # item 为元组
    print(item)
    
for key,value in my_dict.items():
    print(key,value)

# 判断key 是否存在字典当中
result = "age" in my_dict

```

### 集合
set集合:以大括号表现形式的数据集合，集合里面不能有重复的数据，集合可以根据下标获取数据，可以添加和删除。

```
my_set = {1, 3.14, "hello", "world"}

#删除数据，不能删除不存在的数据，否则会crash
my_set.remove("hello")

# 也可以删除数据，这种方式即使没有数据也不会crash
my_set.discard(12221)

# 列表转集合，用于去重
my_list = [1, 2, 3, 3, 5, 5]
my_set = set(my_list)
```

### for循环
for循环获取容器类型中的所有元素，获取容器类型中的每一个元素(字符串，列表，元组，字典，集合)

```
for value in list 的格式

for value in my_list:
    print(value)

# 如果需要遍历值和下标可以使用enumerate()封装列表
for index，value in enumerate(my_list):
    print(value)

# 遍历字典
# 默认打印key
for key in my_dict:
    print(key)
# 遍历value:
for value in my_dict.values():
    print(value)

#遍历出来字典所有的key和value
for key，value in my_dict.items():
    print(key，value)

```
