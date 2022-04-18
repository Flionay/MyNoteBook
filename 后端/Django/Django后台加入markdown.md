# Django Rest FrameWork

## RESTful API

为什么要使用RESTful架构？

REST 是 Representational State Transfer的缩写，如果一个架构符合REST原则，就称它为RESTful架构

RESTful 架构可以充分的利用 HTTP 协议的各种功能，是 HTTP 协议的最佳实践

RESTful API 是一种软件架构风格、设计风格，可以让软**件更加清晰，更简洁，更有层次，可维护性更好**    

### 请求设计

![image-20220331150332296](https://pic-1300286858.cos.ap-nanjing.myqcloud.com/uPic/2022-03/image-20220331150332296.png)

### 响应设计

![image-20220331150418897](https://pic-1300286858.cos.ap-nanjing.myqcloud.com/uPic/2022-03/image-20220331150418897.png)

图片来源：https://restfulapi.cn/

### 响应状态码 含义

1. 响应状态码：由开发者（前端、后端、客户）定义，是对资源请求结果的应用层状态码，非 HTTP 响应状态码。
   - 常见字段名示例：
     - `"status"`
     - `"errcode"`
   - 常见值示例：
     - `0`: 表示操作资源成功
     - `1`: 表示操作资源失败
     - `2`: 表示操作资源成功，但没匹配结果
2. 响应状态码文字说明
   - 常见字段名示例
     - `"msg"`
     - `"message"`
3. 资源本身
   - 常见字段名示例
     - `"data"`
     - `"results"`

## Django Rest FrameWork

注意：不能直接返回的资源 (子资源、图片、视频等资源)，而是返回该资源的 url 链接

```python
from rest_framework.views import APIView, ...                      # 视图模块 - 对django原生视图类的封装
from rest_framework.response import Response, ...                  # 响应模块 - 对django原生响应类的封装
from rest_framework.request import Request, ...                    # 请求模块 - 对django原生请求类的封装
from rest_framework.serializers import Serializer, ...             # 序列化与反序列化模块
from rest_framework.settings import APISettings                    # DRF的配置文件
from rest_framework.filters import SearchFilter, ...               # RESTful API 基础功能 - 过滤
from rest_framework.pagination import PageNumberPagination, ...    # RESTful API 基础功能 - 分页
from rest_framework.authentication import TokenAuthentication, ... # RESTful API 基础功能 - 认证
from rest_framework.permissions import IsAuthenticated, ...        # RESTful API 基础功能 - 权限（是否登录）
from rest_framework.throttling import SimpleRateThrottle           # RESTful API 基础功能 - 频率
```

可以看到 DRF 在 django 原有基础上进行类封装，并实现类 RESTful API 的各大基础功能。

原生 View 不同，DRF 实现了对 json 格式的 POST 请求数据的自动解析：

- [x] form-data
- [x] x-www-form-urlencoded
- [x]  raw：包括 常见的 json、xml 等

DRF 对以上模块都尽心了重新封装，所以用到他们之后，很多方式与之前有些许不同。



## 序列化模块

```python
# DRF 常用序列化类主要有
rest_framework.serialziers.Serializer
rest_framework.serialziers.ModelSerializer
rest_framework.serialziers.ListSerializer
# 本篇介绍 rest_framework.serialziers.Serializer
```

### 用法

序列化器的使用分两个阶段：

1. 在客户端请求时，使用序列化器可以完成对数据的反序列化（就是前段往后端传递数据，反序列化之后保存数据）
2. 在服务器响应时，使用序列化器可以完成对数据的序列化（服务器取出数据，序列化之后往前段发送展示）

### 序列化服务器数据，传给前端

DRF的序列化使用流程为：根据model类创建序列化类，在视图函数中对查询数据库得出的结果进行序列化，利用.data取出具体数据。如果被序列化的数据是包含多条数据的(例如queryset数据类型)，不管是多条还是单条，需要添加`many=True` 参数

```python
user = models.User.objects.all()
user_ser =  Userserialzier(user,many=True)
```

### 反序列化：处理前端传给后端的数据

反序列化是将前天传来的数据数据存入数据库。DRF 的反序列化使用流程如下：

#### 数据验证

1. 使用序列化器进行反序列化时，需要对数据进行验证后，才能获取验证成功的数据或保存成模型类对象。
2. 在获取反序列化的数据前，必须调用 `is_valid()` 方法进行验证，验证成功返回 `True`，否则返回 `False`。
3. 验证失败，可以通过序列化对象的 `errors` 属性获取错误信息，返回字典，包含了字段和字段的错误。
4. 验证通过，可以通过序列化器对象的 `validated_data` 属性获取数据

#### 保存数据

序列化类中必须重写 `create` 方法用于新增，重写 `update` 方法用于修改。视图中使用 `create` 和 `save` 方法。

从源码可知 `save` 方法内部调用的是序列化类中的 `create` 方法，所以新增必须要在序列化类中重写 `create` 方法。

