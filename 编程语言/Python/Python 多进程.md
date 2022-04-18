## 进程
进程时系统分配资源的单位，一个进程可以有多个线程；
进程的状态有：新建，就绪，运行，等待，死亡。
**并行：**真的多任务； **并发：** 假的多任务；

## multiprocessing
```python
import multiprocessing
import time

def singing():
    while True:
        print("singing...")
        time.sleep(1)

def dancing():
    while True:
        print("dancing...")
        time.sleep(1)

def main():
    p1 = multiprocessing.Process(target=singing)
    p2 = multiprocessing.Process(target=dancing)

    p1.start()
    p2.start()


if __name__ == "__main__":
    main()
```
多进程的创建与多线程极其相似。线程一般是共享主进程的一些变量，而进程可以理解为将主进程的资源复制一份，相比于线程，进程耗费的资源较多。
同一台电脑启动两个微信，就是两个进程。而一个微信，开多个聊天框，就是多线程。
进程是完全独立的，于线程不同，需要某个介质，实现线程之间的通信
![图片.png](https://cdn.nlark.com/yuque/0/2022/png/2637180/1648975004967-cd2dfe75-788d-4b40-9960-f7be7b378784.png#clientId=u38cd529d-be77-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=350&id=u0a1c2c12&margin=%5Bobject%20Object%5D&name=%E5%9B%BE%E7%89%87.png&originHeight=700&originWidth=1574&originalType=binary&ratio=1&rotation=0&showTitle=false&size=816559&status=done&style=none&taskId=u1da9528d-838b-4ebe-87f1-2085223063a&title=&width=787)
## 通过队列完成进程通信
队列，先进先出。
```python
from multiprocessing import Queue
##
myque = Queue(3)

myque.put(1)
myque.put(2)
myque.put(3)
myque.put(4) # 超过队列长度 ，会等待
myque.get() 
myque.get()
myque.get()
myque.get()# 先放谁 先取谁。如果为空，就会等待，阻塞
```
生产者消费者线程，利用队列进行通信
```python
from multiprocessing import Process,Queue,set_start_method,get_context
import time
def download_from_web(q):
    i=0
    while True:
        i += 1
        q.put(i)
        print(f'放入{i}')
        time.sleep(1)

def analysis_data(q):
    """处理数据"""
    watting_analysis_data = list()
    while True:
        data = q.get()
        watting_analysis_data.append(data)
        print(watting_analysis_data)
        time.sleep(4)
        # if q.empty():  # 如果放的很慢  就会停掉消费者
        #     break


    # print(watting_analysis_data)


def main():
    q = Queue(10)
    # 放入和取出 两边都while true，这样队列没有的话，不能取，会等待放入
    # 队列满了的话 不能放，会等待取出
    ctx = get_context('fork')
    p1 = ctx.Process(target=download_from_web,args=(q,))
    p2 = ctx.Process(target=analysis_data,args=(q,))
    p1.start()
    p2.start()

if __name__ == "__main__":
    main()
```
# 进程池
当要创建的进程数量不多时，可以利用multiprocessing中的Procss动态生成多个进程，但如果需要创建成千上百个目标，可以利用进程池Pool方法。
```python
from multiprocessing import Pool
import os, time, random

def work(i):
    
    time.sleep(random.random()*3)
    print("进程{} running ....".format(i),"--pid {}".format(os.getpid()))



if __name__ == '__main__':

    po = Pool(3)

    for i in range(10):
        po.apply_async(work,(i,))

    print("-----start-------")
    po.close()
    po.join()
    print("-----end-------")

```
线程池里的Queue用multiprocessing下的manager.queue
