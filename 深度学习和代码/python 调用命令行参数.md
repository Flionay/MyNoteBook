## Python 命令解析 -argparse

### 应用场景

有时候我们需要替换Python脚本中不同的变量，比如进行模型选择。有时候需要提交到服务器，所以我们希望利用命令行就可以完成这一工作。比如在脚本后面添加模型参数，脚本中就可以自动改变模型。

### sys.argv

sys包提供了一个简单的方法将参数返回到脚本内部，返回形式为一个列表。通常`sys.argv[0]`代表文件本身，后面添加的参数依次追加到`sys.argv`列表当中。

```python
import sys
print(sys.argv)

def model_choice():
    
    if sys.argv[1] == 'FCN':
        model = "FCN"
    elif sys.argv[1] == 'Unet':
        model = "Unet"
    else sys.argv[1] == 'DeepLab':
        model = "DeepLab"

    return model

if __name__ == "__main__":
    print(model_choice)

```

```bash
~/Desktop/parser via 🐍 v3.7.3 via C base 
❯ python sysargv.py "Unet"
['sysargv.py', 'Unet']
Unet
```

### [Argparse](https://docs.python.org/zh-cn/3/howto/argparse.html#id1) 

argparse是一个Python模块：命令行选项、参数和子命令解析器。

> 主要有三个步骤：
>
> - 创建 ArgumentParser() 对象
> - 调用 add_argument() 方法添加参数
> - 使用 parse_args() 解析添加的参数

```python
import argparse

def main():
    parser = argparse.ArgumentParser(description="Demo of argparse")
    parser.add_argument("ID",type = int,help = "输入ID") # 位置参数，按照顺序赋值，必须有这个参数
    parser.add_argument('-n','--name', default=' Li ' ,type= str, help= "输入姓氏",choices = ['zhao','qian','sun','Li'])
    parser.add_argument('-y','--year', default='20',type=int, help= "输入年龄")
    args = parser.parse_args()
    print(args)
    name = args.name
    year = args.year
    print('Hello {}  {}'.format(name,year))

if __name__ == '__main__':
    main()
```

```bash
❯ python first.py -h
usage: first.py [-h] [-n {zhao,qian,sun,Li}] [-y YEAR] ID

Demo of argparse

positional arguments:
  ID                    输入ID

optional arguments:
  -h, --help            show this help message and exit
  -n {zhao,qian,sun,Li}, --name {zhao,qian,sun,Li}
                        输入姓氏
  -y YEAR, --year YEAR  输入年龄
  
~/Desktop/parser via 🐍 v3.7.3 via C base 
❯ python first.py 13 -n "sun" -y "25"
Namespace(ID=13, name='sun', year=25)
Hello sun  25

```

更多细节操作，可以查询这篇[博文](https://www.jianshu.com/p/e2f9de45a981)!