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


### 返回函数
高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。

首先我们来看一个简单的求和函数

```
def sum(*args):
    sum_num = 0
    for n in args:
        sum_num += n
    return sum_num

result = sum(3,5,6,7)
print(result)
```

如果不需要立刻求和，而是在后面的代码中根据需要在计算，那么可以使用返回函数，不返回求和的结果，而是返回求和的函数。

```
def lazy_sum(*args):
    def sum():
        sum_num = 0
        for n in args:
            sum_num += n
        return sum_num
    return sum

# 此时sum_func就是返回的sum函数，调用函数即可
sum_func = lazy_sum(3,5,6,7)

print(sum_func())
```

在上述例子中，在lazy_sum函数中定义了sum函数，并且sum函数内部使用了lazy_sum函数的参数，因此当lazy_sum函数中return sum函数时，相关参数和变量都保存在返回函数中，这种称为“闭包”。

需要注意的是：当调用lazy_sum函数时，每次调用都会返回一个新的函数，即使传入的参数是相同的。

### 闭包
形成闭包有两个必要条件

1. 函数嵌套，并且内部函数使用了外部函数的参数或者变量。
2. 返回值为内部函数。

那么返回的内部函数就叫做闭包。

需要注意的是：返回的函数并没有立刻执行，而是直到调用时才执行。来看一个例子

```
def count():
    fs = []
    for i in [1,2,3]:
        def f():
            return i * i
        fs.append(f)
    return fs

f1,f2,f3 = count()
print(f1())
print(f2())
print(f3())

输出
9
9
9
```

上述例子可以看出，每次循环都创建了一个新的函数，然后把创建的3个函数都返回了，但是打印内容都是9，原因在于返回的函数引用了变量i，单是返回函数并非立刻执行。等到3个函数都返回时，他们所引用的变量i已经变成了3，因此最终结果为9。

因此，在返回闭包时需要注意：返回函数不要引用任何循环变量，或者后续会发生变化的变量，否则结果可能会和我们预期不同。

如果一定要引用循环变量，可以在创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不会变。

```
def count():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs

f1,f2,f3 = count()
print(f1())
print(f2())
print(f3())

输出
1
4
9
```

上述代码中，g函数中使用的是f函数中的参数j，并且f函数被立刻执行，因此g函数中保存的就是当前被传入的值。

### 匿名函数
当我们在将函数当做参数时，不需要显示地定义函数，直接传入匿名函数更方便。

匿名函数的定义 lambda (参数): (返回值)

```
lambda x : x*x
实际上就是

def f(x):
    return x * x

```

匿名函数不需要要return，且只能有一个表达式，返回值就是该表达式的结果。因为匿名函数没有名字，因此不必担心函数名冲突，因此匿名函数也是一个函数对象，可以把匿名函数赋值给一个变量。

```
f = lambda x : x * x
f(6)
```

也可以将匿名函数作为返回值返回

```
def build(x,y):
    return lambda: x * x + y *y

f = build(3,4)
print(f())
```


### 装饰器
在代码运行期间动态增加功能的方式，称之为装饰器Decorator。装饰器Decorator本质上就是一个返回函数的高阶函数。首先看下面的例子

```
# 如果想在函数运行之前先打印函数的名字，但是又不想修改函数的内部代码。
# 可以使用返回函数的高阶函数，将要修改的函数封装为一个新的函数返回并调用

def show():
    print("AAA")

def decorator(func):
    def inner():
        print("fun_name: %s()" % func.__name__)
        func()
    return inner
# 将新的函数赋值为show
show = decorator(show)
show()

```

上述例子中，我们可以看出在decorator函数中传入show函数，返回经过封装之后的函数并重新复制给show。

接下来可以看使用装饰器Decorator简化后的代码

```
def decorator(func):
    def inner():
        print("fun_name: %s()" % func.__name__)
        func()
    return inner

# @decorator 当在show函数的定义出，相当于执行了语句 show = decorator(show)
@decorator
def show():
    print("AAA")

show()
```

上述代码看起来很完善，但是此时当打印`show.__name__`就会发现此时show的name其实是高阶函数返回的函数

```
print(show.__name__)
# 打印内容
inner
```
此时如果依赖函数名去做一些判断就会出错。因此可以使用`functools.wraps`修改函数的名称。下面是一个完整的装饰器写法

```
import functools
def decorator(func):
    # 修改函数名
    @functools.wraps(func)
    def inner():
        print("fun_name: %s()" % func.__name__)
        func()
    return inner

@decorator
def show():
    print("AAA")

show()
print(show.__name__) # 此时在打印函数名为show
```

如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数。下面代码为例

```
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def inner():
            print("%s fun_name: %s()" % (text,func.__name__))
            func()
        return inner
    return decorator

# 相当于 
@log("log: ")
def show():
    print("AAA")

show()
print(show.__name__)

打印内容：show = log("log: ")(show)
log:  fun_name: show()
AAA
show
```

上述代码中，log函数传入参数返回了一个decorator函数，调用decorator函数，参数是show函数，最终返回的是inner函数。但是函数中使用了@functools.wraps()将函数名进行了修改，因此函数名字是show。

### 偏函数
通过上面函数的参数介绍，我们知道可以通过设定参数的默认值，来降低函数调用的难度，偏函数也可以做到这一点。

```
# 以int()函数为例, int()函数可以把字符串转为整数，当仅传入字符串时，int()函数默认转化为十进制函数。
int("998")
# 同时也可以指定base参数来指定转化的进制
int("110", base = 2) # 2进制110转化为10进制

# 但是如果要转化大量的二进制，这样每次指定进制就显得稍有繁琐，因此可以专门写一个函数用来做2进制的转化

def int2(x):
    return int(x, base = 2)

print(int2("110"))

# 这样调用int2("110")就可以快速进行2进制转化了。
```

python提供了专门的方法来帮助我们创建上述int2()函数。

functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义。functools.partial作用就是把一个函数的某些参数给固定住(也就是设置默认值)，并返回一个新的函数，调用这个函数会更简单。

```
int2 = functools.partial(int ,base = 2)
print(int2("110"))
# 输出：6
```

需要注意的是 functools.partial仅仅是把base的参数重新设定默认值为2，但是我们同样可以在调用int2的时候为base传入其他的值。

```
int2 = functools.partial(int ,base = 2)
print(int2("110", base = 10))
# 输出：110
```

当创建偏函数时，实际上可以接受`函数对象，*args和**kw`这三种参数的

```
int2 = functools.partial(int ,base = 2)

# 下面函数同上面是等价的
kw = {"base":2}
int("100", **kw)

max2 = functools.partial(max , 10)
print(max2(5,6,7))
# 打印内容 10
# 相当于为max函数添加了一个默认值10
```


偏函数的作用：当函数的参数个数过多时，使用functools.partial创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。



