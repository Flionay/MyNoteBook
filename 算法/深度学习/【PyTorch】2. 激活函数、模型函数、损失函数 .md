## 1. torch.nn.function

PyTorch 和神经网络相关的功能组件基本都封装在`torch.nn`中，而这些功能组件基本上都有函数和类两种形式实现。

函数实现方法：`nn.functional(F)`的基本功能组件罗列如下：

| 激活函数  | 模型层       | 损失函数               |
| :-------- | :----------- | :--------------------- |
| F.relu    | F.linear     | F.binary_cross_entropy |
| F.sigmoid | F.cov2d      | F.mse_loss             |
| F.tanh    | F.max_pool2d | F.cross_entropy        |
| F.softmax | F.dropout2d  |                        |
|           | F.embedding  |                        |

类实现：`torch.nn.class`， `from torch import nn`

| 激活函数   | 模型层       | 损失函数            |
| :---------- | :------------ | :------------------- |
| nn.ReLu    | nn.Linear    | nn.BCELoss          |
| nn.Sigmoid | nn.Cov2d     | nn.MSELoss          |
| nn.Tanh    | nn.MaxPool2d | nn.CrossEntropyLoss |
| nn.Softmax | nn.DropOut2d |                     |
|            | nn.Embedding |                     |

## 2. torch.nn.Module

在Pytorch中，模型的参数是需要被优化器训练的，因此，通常要设置参数为 requires_grad = True 的张量。

同时，在一个模型中，往往有许多的参数，要手动管理这些参数并不是一件容易的事情。

### nn.Module 管理参数

Pytorch一般将参数用nn.Parameter来表示，并且用nn.Module来管理其结构下的所有参数。

```python
# nn.ParameterList 可以将多个nn.Parameter组成一个列表
params_list = nn.ParameterList([nn.Parameter(torch.rand(8,i)) for i in range(1,3)])
print(params_list)
print(params_list[0].requires_grad)
```

```text
ParameterList(
    (0): Parameter containing: [torch.FloatTensor of size 8x1]
    (1): Parameter containing: [torch.FloatTensor of size 8x2]
)
True
```



```python
# nn.ParameterDict 可以将多个nn.Parameter组成一个字典

params_dict = nn.ParameterDict({"a":nn.Parameter(torch.rand(2,2)),
                               "b":nn.Parameter(torch.zeros(2))})
print(params_dict)
print(params_dict["a"].requires_grad)

```

```text
ParameterDict(
    (a): Parameter containing: [torch.FloatTensor of size 2x2]
    (b): Parameter containing: [torch.FloatTensor of size 2]
)
True
```

### nn.Module管理模型子模块

一般情况下，我们都很少直接使用 nn.Parameter来定义参数构建模型，而是通过一些拼装一些常用的模型层来构造模型。

这些模型层也是继承自nn.Module的对象,本身也包括参数，属于我们要定义的模块的子模块。

如果模型是分功能模块的，那么可以通过下面这种方式，定义子模块。

```python
class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        
				## 第一个子模块
        self.embedding = nn.Embedding(num_embeddings = 10000,embedding_dim = 3,padding_idx = 1)
        
        ## 第二个子模块
        self.conv = nn.Sequential()
        self.conv.add_module("conv_1",nn.Conv1d(in_channels = 3,out_channels = 16,kernel_size = 5))
        self.conv.add_module("pool_1",nn.MaxPool1d(kernel_size = 2))
        self.conv.add_module("relu_1",nn.ReLU())
        self.conv.add_module("conv_2",nn.Conv1d(in_channels = 16,out_channels = 128,kernel_size = 2))
        self.conv.add_module("pool_2",nn.MaxPool1d(kernel_size = 2))
        self.conv.add_module("relu_2",nn.ReLU())
        
				## 第三个子模块
        self.dense = nn.Sequential()
        self.dense.add_module("flatten",nn.Flatten())
        self.dense.add_module("linear",nn.Linear(6144,1))
        self.dense.add_module("sigmoid",nn.Sigmoid())

    def forward(self,x):
        x = self.embedding(x).transpose(1,2)
        x = self.conv(x)
        y = self.dense(x)
        return y

net = Net()
```



遍历子模块

```python
i = 0
for name,child in net.named_children():
    i+=1
    print(name,":",child,"\n")
print("child number",i)
```



### 冻结某一个模块

```python
children_dict = {name:module for name,module in net.named_children()}

print(children_dict)
embedding = children_dict["embedding"]
embedding.requires_grad_(False) #冻结其参数
```



