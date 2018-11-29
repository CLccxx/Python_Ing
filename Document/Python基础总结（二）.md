## Python 基础总结

### 函数

函数的定义格式

```
def 函数名():
    # code
```

函数的不同格式

```
# 无参数无返回值的函数
def show_hello():
    print("hello world")

# 有参数无返回值的函数
def show_hello(name):
    print("hello:%s" % name)
    
# 无参数有返回值的函数
def show_hello():
    return "hello world"

# 有参数有返回值
def show_hello(name):
    str = "hello %s" % name
    return str

```

### 函数的参数

```
# 位置参数：调用函数时，位置参数必须按照顺序传入相应的参数
# 默认参数（缺省参数）：默认参数必须在必选参数后面。在函数定义的时候参数就有值，如果给默认参数传值就是传入的值，如果不给默认参数传值那么就使用默认值。

# 如果有必选参数和缺省参数，那么缺省参数要放到必选参数后面
def show_hello(name ,say_str = "hello"):
    print("%s,%s" % (say_str, name))
    
# 函数的传参方式
# 可以使用位置参数方式传参，位置参数方式传参必须按照函数的参数位置传入对应的值。
# 使用关键字方式传参，可以不按照参数的位置传递，但是如果前面使用的是关键字方式传参，则后面必须也使用关键字方式传参

def show(name, age):
    print(name, age)
# 位置方式传参
show("一一", 20)
# 关键字方式传参，顺序可以调换
show(age=18, name="二二")

注意：Python函数在定义的时候，默认参数的值就被计算出来了，因为默认参数也是一个变量，他指向对象，每次调用该函数时，如果改变了参数的内容，那么下载调用时，默认参数的值就改变了。不再是初次函数定义时的值了。

def add_number(num_list = []):
     num_list.append(5)
     return num_list

# 多次调用add_number函数，默认值会不同
```

### 函数的不定长参数
不定长位置参数：调用函数的时候不确定传入多少个参数，可能是0个或者多个参数，不定长位置参数会将函数传入的位置参数封装到一个元组里面，如果没有传参数，那么就是一个空数组

定义不定长位置参数：`*参数名` (通常使用*args来表示不定长位置参数)

注意：传入不定长参数时，只能使用位置参数方式传参，不能使用关键字方式传参

```
def sum_num(*args):
    print(args, type(args))
    result = 0
    for value in args:
        result += value
    return result

value = sum_num(1, 4, 5, 6)
```


定义不定长关键字参数 `**参数名` (通常使用**kwargs来表示不定长关键字参数)

注意：不定长关键字参数，必须使用关键字方式传参，不能使用位置方式传参，不定长关键字参数会把函数调用的关键字参数封装到字典里面。

不定长关键字必须放在所有参数的后面

```
def show_num(**kwargs):
    print(kwargs, type(kwargs))
    for key, value in kwargs.items():
        print(key, value)

show_num(a = 1, b = 4, c = 5, d = 6)
```

### 不定长参数的传递
如果需要传入一个不定长参数给另外一个函数，需要首先对不定长参数进行拆包后传递

```
# 不定长位置参数

def show_msg(*args):
    print(args)

def show(*args):
    # 对元组进行拆包后传递，将元组中的每一个元素作为参数传递 
    show_msg(*args)
    
    # 相当于传递的是元组，show_msg方法中会将元组再次封装到元组中
    show_msg(args)

show(10,20)

# 输出内容：
# (10, 20)
# ((10, 20),)
```


```
# 不定长关键字参数

def show_msg(**kwargs):
    print(kwargs)

#定义一个不定长位置参数
def show(**kwargs):
    # 对字典进行拆包后传递
    show_msg(**kwargs)
    
    # 直接将 a : kwargs(字典) 以字典的方式传递
    show_msg(a = kwargs)

show(a = 10,b = 20)

# 输出内容
# {'a': 10, 'b': 20}
# {'a': {'a': 10, 'b': 20}}
```


### 匿名函数
lambad 关键字修饰的函数就是匿名函数，用于简化代码，常用于简单函数的定义

```
new_func = lambda num:True if num % 2 == 0 else False
print(new_func(1))
```

匿名函数的应用(对字典列表的排序)

```
my_list = [{"name":"zs","age":19},{"name":"ls","age":12}]
# 匿名函数排序字典列表的方式
my_list.sort(key=lambda item:item["age"])
print(my_list)

def get_value(item):
    return item["age"]
# 正常方式排序列表字典(reverse = True 表示翻转)
my_list.sort(key=get_value, reverse=True)
print(my_list)
```

### 内置函数
Python创建了常用的函数，方便使用，称为内置函数

```
# 比较两个值大小 返回值 -1：小于 0：等于 1：大于
# 比较字典时优先比较键，键相同在比较值
cmp(item1,item2)

# 返回容器中元素的最大值
max(item)

# 返回容器中元素的最小值
min(item)

# 删除变量 
del(item)

# 计算容器中元素个数
len(item) 
```

### 函数注意事项
1. 函数名不能相同(否则第二个函数会把第一个函数覆盖掉)，即使参数名，参数个数不同也不可以。
2. 参数位置参考：必选参数、默认参数、可变参数、可变命名关键字参数、关键字参数。
3. 可以使用`*`强制调用者使用关键字参数。将`*`添加到强制使用关键字参数的前面并且用`,`隔开，则`*`后面的参数必须使用关键字参数方式。
4. 函数的嵌套：函数内部可以定义局部函数，只能在函数内部调用
5. 虽然函数的参数可以有多种组合，但是不要同时使用太多的组合，否则函数接口的理解性会很差
6. Python 不用指明函数返回值的类型，在函数中直接将要返回的值return即可，如果需要返回多个值，可以将值包装在集合中在返回。
