# python 进阶教程

> 诫言：
>
> 学东西太过皮毛，总是觉得学个大概意思就可以了。
>
> 学到99分很容易，但是满分💯才是最珍贵的。

# 数据类型

## 枚举

当一个变量有几种固定的取值时，通常我们喜欢将它定义为枚举类型，枚举类型用于声明一组命名的常数，使用枚举类型可以增强代买的可读性。

**两个特点：唯一 不可更改**

应用场景：
假设现在职称评定只有一下五个等级，我们要给每个等级定义薪资,还要定义他的中文名称。

- 高级
- 副高级
- 中级
- 初级
python3 提供了enum模块，定义类时可以继承该模块，创建一个枚举类型数据,保证其不可被更改
```python
from enum import Enum,unique
# unique 用来确保没有重复项

@unique
class TitleLevel(Enum):
    # 进阶用法 重写__new__()方法
    def __new__(cls,chinese,salary):
        obj = object.__new__(cls)
        obj.chinese = chinese
        obj.salary = salary
        return obj
    primary = "初级",5000
    intermediate = "中级",8000
    deputySenior = '副高级',10000
    advanced = '高级',13000

print(TitleLevel.primary.salary)
print(TitleLevel.intermediate.chinese)
print(TitleLevel.primary.chinese)
# 遍历
for level in TitleLevel:
    print((level.name,level.chinese,level.salary))
```
## 字节码类型
```python 
import hashlib

string = "123456"

m = hashlib.md5()       # 创建md5对象
str_bytes = string.encode(encoding='utf-8')
print(type(str_bytes))
m.update(str_bytes)   # update方法只接收bytes类型数据作为参数
str_md5 = m.hexdigest()     # 得到散列后的字符串

print('MD5散列前为 ：' + string)
print('MD5散列后为 ：' + str_md5)
```

## 静态类型标注

### 动态类型与静态类型

python作为一种动态类型语言，这使得程序不需要指定变量的类型，这一点是不会改变的。但python创始人Guido van Rossum在python3.5中引入了一个类型系统，它允许开发人员指定变量类型，主要作用是便于开发维护代码，供IDE和开发工具使用，对代码运行不产生任何影响，运行时会过滤类型信息。

1. **类型标注**
先来看一个简单的示例来了解这个新的特性
```python
def add(x: int, y: int)->int:
    return x + y


print(add(3, 4.3))
```
类型标注的使用并不复杂，只有两条规则：

使用：语句将信息附加到变量或函数参数中
				->运算符用于将信息附加到函数/方法的返回值中
通过类型标注，你很容易就了解了使用add函数时的参数要求以及函数返回值的类型，不需要添加其他注释，而这并没有增加太多工作量。尽管类型标注注明了参数y是int类型，但实际调用函数时仍然可以传入float数据，因为类型标注仅仅被当做注释来处理，而不是强制的类型要求， python并没有据此进行类型推断和验证，也没有使用类型信息来优化生成的字节码以获得安全性或性能，一言以蔽之，类型标注就是一个另类的代码注释。

**好处：**

- 易于理解代码
- 易于重构代码
- 方便协作
- 有利于大项目

### **利用mypy对python脚本进行静态检查**
`pip install mypy`

```python
# 错误代码示范：
class Stu:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '{name} {age}'.format(name=self.name, age=self.age)


stu1 = Stu('小明', 16.5)
stu2 = Stu('小刚', '17') # 将年龄传入了字符串 但是这里并不会报错

print(stu1, stu2)


# 加入类型检查可避免这些错误

class Stu:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return '{name} {age}'.format(name=self.name, age=self.age)


stu1 = Stu('小明', 16.5)
stu2 = Stu('小刚', '17')

print(stu1, stu2)
```

一般情况下ide会进行提示，但是不会影响运行，所以要使用mypy对其进行检查
```shell 
mypy demo.py
demo.py:10: error: Argument 2 to "Stu" has incompatible type "float"; expected "int"
demo.py:11: error: Argument 2 to "Stu" has incompatible type "str"; expected "int"
Found 2 errors in 1 file (checked 1 source file)
```

## python 运行时检查

### 设计一个能够检查输入输出的参数类型装饰器

```python
# 获得被装饰函数的形式参数列表

from inspect import signature

def add(x,y): 
    return x+y

sig = signature(add)
print(sig,type(sig))

bound_types = sig.bind_partial(int,int).arguments
print(bound_types) 

#(x, y) <class 'inspect.Signature'>
#{'x': <class 'int'>, 'y': <class 'int'>}
```

```python
# 获取绑定的数字
def add(x,y):
    sig = signature(add)
    bound_values = sig.bind(x,y)
    print(bound_values)
add(3,4)
#<BoundArguments (x=3, y=4)>
```

```python
from inspect import signature
from functools import wraps


def typecheck(*type_args, **type_kwargs):
    '''
    类型检查装饰器, type_args和type_kwargs都是装饰器的参数
    :param type_args:
    :param type_kwargs:
    :return:
    '''
    def decorator(func):
        sig = signature(func)
        # 建立函数参数与装饰器约定参数类型之间的映射关系
        bound_types = sig.bind_partial(*type_args, **type_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            # 获得函数执行时实际传入的数值
            bound_values = sig.bind(*args, **kwargs)
            # 进行类型检查
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(
                            'Argument {} must be {}'.format(name, bound_types[name])
                            )
            return func(*args, **kwargs)
        return wrapper
    return decorator

@typecheck(int, int)
def add(x, y):
    return x + y

add(3, 4)

```

## 字典视图对象

`dict.keys()` `dict.values()` `dict.items()`返回的对象是一个字典视图对象，类似execl视图，其是不可更改的，只读对象。

如果你想利用一个字典，且不想被人修改这个字典的信息。那么就可以创建一个字典代理对象。

```python
from types import MappingProxyType
map_dict = MappingProxyType(stu_dict)
print(map_dict)
map_dict['小红'] = 14     # 会报错
```

# Python 内存管理

更详细的信息可以访问这篇博客http://www.coolpython.net/python_senior/memory/index.html

##  变量引用

1. 变量不能单独存在，必须赋予值，也就是必须只想内存里的对象。
2. 变量是内存中数据的引用，建议使用指向这个词，更能分得清楚。初始数据类型一般就是同一个地址，但是列表等数据结构，即使值相同，也不放在同一个内存地址。
3. 如果内存中的某个数据没有被变量指向，也就是没有引用，就会被垃圾回收机制回收，释放内存。

## 深拷贝与浅拷贝

1. 浅拷贝

   拷贝规则如下

   1. 如果被拷贝对象是不可变对象，则不会生成新的对象
   2. 如果被拷贝对象是可变对象，则会生成新的对象，但是只会对可变对象最外层进行拷贝

2. 深拷贝

   拷贝规则

   1. 如果被拷贝对象是不可变对象，深拷贝不会生成新对象，因为被拷贝对象是不可变的，继续用原来的那个，不会产生什么坏的影响
   2. 如果被拷贝对象是可变对象，那么会彻底的创建出一个和被拷贝对象一模一样的新对象

# 模块概念深入学习

在python入门阶段，只需要初步了解模块的概念，能够使用import 或者from ... import ... 语法将自己需要的模块导入即可。进入到进阶阶段，需要你进一步深入思考模块是如何被导入的，导入模块时的原理和过程是什么样的？如何才能实现模块的动态加载，如何实现模块的惰性导入

## 导入模块的原理和过程是怎样的？

执行import语句时，只有两个步骤，**第一步**是搜索模块，**第二步是**将搜索结果绑定到局部命名空间。

搜索时，分为两步：

1. 搜索sys.modules
2. 搜索sys.meta_path

导入一个模块时，会将这个导入的模块以及这个模块里调用的其他模块信息以字典的形式保存到sys.modules中，如果再次导入词模块，则优先从sys.modules查找模块，你可以在脚本里执行print(sys.modules)查看已经加载的模块,我们甚至可以直接修改sys.modules里的内容

```python
import os
import sys

sys.modules['fos'] = os
import fos
print(fos.getpid())
```

执行import fos时，会先到sys.modules里查找是否有该模块，'fos'做key,找到的value是os模块，因此可以调用getpid方法。

如果在sys.modules模块中找不到目标模块，则从sys.meta_path中继续寻找。sys.meta_path是一个list，里面的对象是importer对象，importer对象是指实现了finders 和 loaders 接口的对象，输出sys.meta_path里的内容可以查看有什么

```text
<class '_frozen_importlib.BuiltinImporter'>
<class '_frozen_importlib.FrozenImporter'>
<class '_frozen_importlib_external.PathFinder'>
```

这三个importer对象分别查找及导入build-in模块，frozen模块（即已编译为Unix可执行文件的模块），import path中的模块，如果都找不到，就会报ModuleNotFoundError的错误。

## 2. sys.path

导入模块时，首先会去sys.modules里查看，如果查不到会使用sys.meta_path里的importer继续查找，这些importer首先会查找内置模块，然后查找frozen模块，最后会根据sys.path里的路径进行查找。在脚本里执行print(sys.path).

sys.path里路径的顺序决定了搜索的顺序，这里的路径分为3类

1. sys.path[0] 是当前路径，也是最先被搜索的
2. 第二类是安装python时内置进去的，比如 `/Library/Frameworks/Python.framework/Versions/3.6/lib/python36.zip/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lib-dynload/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages`
3. 最后一类就是安装的第三方模块

## 动态加载

## 1. __import__

当你使用import关键字导入模块时，底层实现默认调用的是__import__，直接使用该函数的情况很少见，一般用于动态加载。假设有这样一个场景，项目里有两份配置文件，一份是线下开发环境配置

```python
import platform

if platform.uname().system == 'Darwin':     # mac电脑
    config = __import__('offline')
else:
    config = __import__('online')

print(config.host)
```

## 2. importlib.import_module

importlib模块的import_module方法相比于__import__更加友好，使用起来更加方便。下图是项目的结构

```text
├── conf
│   ├── __init__.py
│   ├── offline.py
│   └── online.py
└── demo.py
```

在demo.py文件中根据系统来加载不同的模块，使用import_module方法的示例代码如下

```python
import platform
import importlib

if platform.uname().system == 'Darwin3':     # mac电脑
    config = importlib.import_module('conf.offline')    # 绝对导入
else:
    config = importlib.import_module('.online', package='conf')     # 相对导入

print(config.host)
```

使用相对导入时，务必在name前面加一个点.

# 高阶模块

## collections

## functools

functools模块提供了一些非常神奇的高阶函数， 其中为人熟知的有reduce，partial，wraps， 他们是作用于或返回其他函数的函数， 一般来说任何**可调用的对象**都可以用这个模块里的函数进行处理。

