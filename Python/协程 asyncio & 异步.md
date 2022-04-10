- 异步非阻塞
- fastapi，django asgi --> 提升性能
## 1. 进程 线程 协程的通俗理解
假设现在有一个工厂生产矿泉水瓶，为了提高生产效率：

- 多进程，把这个工厂再复制一个，里面的资源，人力都复制一份，同时生产
- 多线程，在这个工厂里面增加生产流水线，从而提高生产力
- 协程，不复制工厂，不增加流水线，也不增加工人，让机器工作的同时，提高人员调度效率。比如，拧瓶盖是机器干的事，而贴标签是人干的事。原来是工人等着机器拧完瓶盖，流水线到这里再贴标签。协程就是当机器拧这个水瓶子的瓶盖的时候，工人久跑去另一个水瓶的贴标签。但是还是在这条流水线上（线程里 ），就是让人跑起来增加效率，不能让工人歇着。
## 2. 协程
协程不是计算机中真实存在的，计算机只提供了线程和进程，协程是程序设计出来的。协程也叫做微线程，它依赖于线程，其宗旨就是在程序等待的时候能够跳转到另一个任务，利用起来这个等待时间。但是它还是这个线程在做。
python 实现协程有以下几种方法：

- greenlet 早期模块
- yield 关键字
- asyncio装饰器（python 3.4）
- async await关键字(python 3.5) 推荐
### greenlet
```python
# pip install greenlet

from greenlet import greenlet
import time


def test1():
    while True:
        print("dancing.....")
        gr2.switch()
        time.sleep(1)

def test2():
    while True:
        print("singing.....")
        gr1.switch()
        time.sleep(1)


gr1 = greenlet(test1)
gr2 = greenlet(test2)

gr1.switch() # 切到1里面  

# 此程序本质是单线程，只是来回跳转，交叉运行而已
```
### gevent
greenlet 封装了yield ，而gevent 封装了greenlet，gevent 遇到延时会自动切换任务。
```python
import gevent  
import time 
from gevent import monkey
monkey.patch_all() # 打补丁 打了补丁之后，time sleep也是可用的


def dancing():
    while True:
        print("dancing.....")
        # time.sleep(1)
        gevent.sleep(1)
        

def singing():
    while True:
        print("singing.....")
        # time.sleep(2)
        gevent.sleep(1)
        

def main():
    g1 = gevent.spawn(singing)
    g2 = gevent.spawn(dancing)

    g1.join()
    g2.join()

if __name__ == '__main__':
    main()
```
### asynicoio 模块
现在更推荐asynicio模块，其使用方法如下：
```python
import asyncio
import time 


async def dancing():
    while True:
        print("dancing.....")
        await asyncio.sleep(1)


async def singing():
    while True:
        print("singing.....")
        await asyncio.sleep(1)

        

async def main():
    task1 = asyncio.create_task(singing())
    task2 = asyncio.create_task(dancing())
    await task1
    await task2
   

if __name__ == '__main__':
    asyncio.run(main())
```
## 3. 异步编程
### 3.1 事件循环
理解成为一个死循环，去检测执行某些代码，一直检测那些任务是可执行的，哪些任务是等待的，哪些任务是执行完的。
```python
import asynicio

loop = asynic.get_event_loop()
loop.run_until_complete(任务)
```
### 3.2 快速上手
协程函数 `async def ` 
协程对象，执行协程函数（）得到的就是协程对象
```python
import asyncio
async def f(): # 协程函数
    pass

result = f() # 协程对象
# ----------- 旧版本中这样运行 ---
loop = asynic.get_event_loop()
loop.run_until_complete(result)

# ------ 在现在的新版本中  -----
asyncio.run(result) #这样执行
```

### 3.3 await
async wait ，等待什么呢，等待+可等待对象（协程对象，Future，Task对象 ->IO等待 ）
```python
import asyncio

async def func():
    await asyncio.sleep(2) # 可以理解为io等待，这时就会切换任务
    
asyncio.run( func() )
```
```python
import asyncio

async def others():
    print("start")
    await asyncio.sleep(1)
    print("end")
    return "返回值"


async def main():
    # task1 = asyncio.create_task(others())
    # task2 = asyncio.create_task(others())

    # await task1
    # await task2
    response = await others() # await 就是等待，不会往下走，不会切换
    print('io 请求结果为',response)

    response1 = await others()
    print('io 请求结果为',response1)


asyncio.run(main()) # 这里顺序输出
```
### 3.4 task对象
在事件循环中，添加多个任务的。遇到io自动会进行任务切换。
可以让协程加入事件循环中，等待被调用。
```python
import asyncio
import time 


async def dancing():
    while True:
        print("dancing.....")
        await asyncio.sleep(1)


async def singing():
    while True:
        print("singing.....")
        await asyncio.sleep(1)

        

async def main():
    # 创建task对象，将当前执行函数添加到事件循环
    task1 = asyncio.create_task(singing())
    
    # 创建task对象，将当前执行函数添加到事件循环
    task2 = asyncio.create_task(dancing())
    
    # 以上会马上执行完毕，不会等待，因为只是创建对象而已
    
    await task1 # 等待task1  task1执行
    await task2
   

if __name__ == '__main__':
    asyncio.run(main())
```
示例2:
```python
import asyncio
import time 


async def dancing():
    while True:
        print("dancing.....")
        await asyncio.sleep(1)


async def singing():
    while True:
        print("singing.....")
        await asyncio.sleep(1)

        

async def main():
    task_list = [
        asyncio.create_task(singing()),
        asyncio.create_task(dancing()),
    ]
    await asyncio.wait(task_list)
   
if __name__ == '__main__':
    asyncio.run(main())
```
### 3.5 Future对象
更低级的接口，更底层，一般不会用到。
Task 继承 Future对戏那个，Task对象内部await结果的处理是基于Future对象来的。
## 4. uvloop
是asyncio的事件循环的替代方案。时间循环>默认asyncio的事件循环。
```python
import asyncio
import uvloop
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

#以下代码与asyncio的编码方式一致
```
很多支持异步，并宣称非常快的框架，甚至宣称比肩go的原因就是其内部使用了uvloop。
