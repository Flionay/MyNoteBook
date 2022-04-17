## 1. 构建模型可以用的“砖块”

### 1.2 自带“砖块”

深度学习模型一般由各种模型层组合而成。

torch.nn中内置了非常丰富的各种模型层。它们都属于nn.Module的子类，具备参数管理功能。

### 1.2.1 基础砖块

| 接口      | 名称 | 简介 |
| :--------- |:---- | :---- |
| nn.Linear | 全连接 |      |
| nn.Flatten | 展平 |      |
| nn.BatchNorm1d/2d/3d | 批标准化 | 通过线性变换将输入批次缩放平移到稳定的均值和标准差。 |
| nn.Dropout/2d/3d | 随机失活 | |
| nn.Threshold | 限幅层 | 当输入大于或小于阈值范围时，截断。 |
| nn.ConstantPad2d | 二维常数填充层 | 对二维张量样本填充常数扩展长度 |
| nn.ReplicationPad1d | 一维复制填充层 | 对一维张量样本通过复制边缘值填充扩展长度。 |
| nn.ZeroPad2d | 二维零值填充层 | 对二维张量样本在边缘填充0值. |
| nn.GroupNorm | 组归一化 | FAIR何恺明等人提出组归一化：替代批归一化，不受批量大小限制 |
| nn.LayerNorm | 层归一哈化 | 较少使用 |
| nn.InstanceNorm2d | 样本归一化 | 较少使用 |

### 1.2.2 卷积相关“砖块”

| 接口                   | 名称               | 简介                                                         |
| :--------------------- | :----------------- | :----------------------------------------------------------- |
| nn.Cov1d/2d/3d         | 卷积               | 一维常用于文本，二维常用于图像，三维常用于视频               |
| nn.MaxPool1d/2d/3d     | 最大池化           |                                                              |
| nn.AdaptiveMaxPool2d   | 二维自适应最大池化 | 无论输入图像如何变化，输出一定。                             |
| nn.FractionalMaxPool2d | 二维分数最大池化   | 二维分数最大池化。普通最大池化通常输入尺寸是输出的整数倍。而分数最大池化则可以不必是整数。分数最大池化使用了一些随机采样策略，有一定的正则效果，可以用它来代替普通最大池化和Dropout层 |
| nn.AvgPool2d           | 二维平均池化       |                                                              |
| nn.AdaptiveAvgPool2d   | 二维自适应平均池化 |                                                              |
| nn.ConvTranspose2d     | 二维卷积转置层     | 俗称反卷积层。并非卷积的逆操作，但在卷积核相同的情况下，当其输入尺寸是卷积操作输出尺寸的情况下，卷积转置的输出尺寸恰好是卷积操作的输入尺寸。在语义分割中可用于上采样。 |
| nn.Upsample            | 上采样层           | 操作效果和池化相反。可以通过mode参数控制上采样策略为"nearest"最邻近策略或"linear"线性插值策略。 |
| nn.Unfold              | 滑动窗口提取层     | 实际上，卷积操作可以等价于nn.Unfold和nn.Linear以及nn.Fold的一个组合 |
| nn.Fold                | 逆滑动窗口提取层   |                                                              |

### 1.2.3 循环神经网络 "砖块"

- nn.Embedding：嵌入层。一种比Onehot更加有效的对离散特征进行编码的方法。一般用于将输入中的单词映射为稠密向量。嵌入层的参数需要学习。
- nn.LSTM：长短记忆循环网络层【支持多层】。最普遍使用的循环网络层。具有携带轨道，遗忘门，更新门，输出门。可以较为有效地缓解梯度消失问题，从而能够适用长期依赖问题。设置bidirectional = True时可以得到双向LSTM。需要注意的时，默认的输入和输出形状是(seq,batch,feature),  如果需要将batch维度放在第0维，则要设置batch_first参数设置为True。
- nn.GRU：门控循环网络层【支持多层】。LSTM的低配版，不具有携带轨道，参数数量少于LSTM，训练速度更快。
- nn.RNN：简单循环网络层【支持多层】。容易存在梯度消失，不能够适用长期依赖问题。一般较少使用。
- nn.LSTMCell：长短记忆循环网络单元。和nn.LSTM在整个序列上迭代相比，它仅在序列上迭代一步。一般较少使用。
- nn.GRUCell：门控循环网络单元。和nn.GRU在整个序列上迭代相比，它仅在序列上迭代一步。一般较少使用。
- nn.RNNCell：简单循环网络单元。和nn.RNN在整个序列上迭代相比，它仅在序列上迭代一步。一般较少使用。

### 1.2.3 **Transformer相关层**

- nn.Transformer：Transformer网络结构。Transformer网络结构是替代循环网络的一种结构，解决了循环网络难以并行，难以捕捉长期依赖的缺陷。它是目前NLP任务的主流模型的主要构成部分。Transformer网络结构由TransformerEncoder编码器和TransformerDecoder解码器组成。编码器和解码器的核心是MultiheadAttention多头注意力层。
- nn.TransformerEncoder：Transformer编码器结构。由多个 nn.TransformerEncoderLayer编码器层组成。
- nn.TransformerDecoder：Transformer解码器结构。由多个 nn.TransformerDecoderLayer解码器层组成。
- nn.TransformerEncoderLayer：Transformer的编码器层。
- nn.TransformerDecoderLayer：Transformer的解码器层。
- nn.MultiheadAttention：多头注意力层。

### 1.3 自定义“砖块”

如果这些内置模型层不能够满足需求，我们也可以通过继承nn.Module基类构建自定义的模型层。

因此，我们只要继承nn.Module基类并实现forward方法即可自定义模型层。

```python
import torch
from torch import nn
import torch.nn.functional as F


class Linear(nn.Module):
    __constants__ = ['in_features', 'out_features']

    def __init__(self, in_features, out_features, bias=True):
        super(Linear, self).__init__()
        self.in_features = in_features
        self.out_features = out_features
        self.weight = nn.Parameter(torch.Tensor(out_features, in_features))
        if bias:
            self.bias = nn.Parameter(torch.Tensor(out_features))
        else:
            self.register_parameter('bias', None)
        self.reset_parameters()

    def reset_parameters(self):
        nn.init.kaiming_uniform_(self.weight, a=math.sqrt(5))
        if self.bias is not None:
            fan_in, _ = nn.init._calculate_fan_in_and_fan_out(self.weight)
            bound = 1 / math.sqrt(fan_in)
            nn.init.uniform_(self.bias, -bound, bound)

    def forward(self, input):
        return F.linear(input, self.weight, self.bias)

    def extra_repr(self):
        return 'in_features={}, out_features={}, bias={}'.format(
            self.in_features, self.out_features, self.bias is not None
        )
```



## 2. 构建模型的3种方法

```python
import torch 
from torch import nn
from torchsummary import summary
```



### 2.1 继承nn.module类自定义模型

这种方式最为常见，用来做一些中等大小模型。

以下是继承nn.Module基类构建自定义模型的一个范例。模型中的用到的层一般在`__init__`函数中定义，然后在`forward`方法中定义模型的正向传播逻辑。

```python
class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3,out_channels=32,kernel_size = 3)
        self.pool1 = nn.MaxPool2d(kernel_size = 2,stride = 2)
        self.conv2 = nn.Conv2d(in_channels=32,out_channels=64,kernel_size = 5)
        self.pool2 = nn.MaxPool2d(kernel_size = 2,stride = 2)
        self.dropout = nn.Dropout2d(p = 0.1)
        self.adaptive_pool = nn.AdaptiveMaxPool2d((1,1))
        self.flatten = nn.Flatten()
        self.linear1 = nn.Linear(64,32)
        self.relu = nn.ReLU()
        self.linear2 = nn.Linear(32,1)
        self.sigmoid = nn.Sigmoid()

    def forward(self,x):
        x = self.conv1(x)
        x = self.pool1(x)
        x = self.conv2(x)
        x = self.pool2(x)
        x = self.dropout(x)
        x = self.adaptive_pool(x)
        x = self.flatten(x)
        x = self.linear1(x)
        x = self.relu(x)
        x = self.linear2(x)
        y = self.sigmoid(x)
        return y
```
```python
net = Net()
print(net)
```
```txt
Net(
  (conv1): Conv2d(3, 32, kernel_size=(3, 3), stride=(1, 1))
  (pool1): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
  (conv2): Conv2d(32, 64, kernel_size=(5, 5), stride=(1, 1))
  (pool2): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
  (dropout): Dropout2d(p=0.1, inplace=False)
  (adaptive_pool): AdaptiveMaxPool2d(output_size=(1, 1))
  (flatten): Flatten()
  (linear1): Linear(in_features=64, out_features=32, bias=True)
  (relu): ReLU()
  (linear2): Linear(in_features=32, out_features=1, bias=True)
  (sigmoid): Sigmoid()
)
```



### 2.2 使用nn.Sequential按层顺序构建模型

使用nn.Sequential按层顺序构建模型无需定义forward方法。仅仅适合于简单的模型。

```python
net = nn.Sequential()
net.add_module("conv1",nn.Conv2d(in_channels=3,out_channels=32,kernel_size = 3))
net.add_module("pool1",nn.MaxPool2d(kernel_size = 2,stride = 2))
net.add_module("conv2",nn.Conv2d(in_channels=32,out_channels=64,kernel_size = 5))
net.add_module("pool2",nn.MaxPool2d(kernel_size = 2,stride = 2))
net.add_module("dropout",nn.Dropout2d(p = 0.1))
net.add_module("adaptive_pool",nn.AdaptiveMaxPool2d((1,1)))
net.add_module("flatten",nn.Flatten())
net.add_module("linear1",nn.Linear(64,32))
net.add_module("relu",nn.ReLU())
net.add_module("linear2",nn.Linear(32,1))
net.add_module("sigmoid",nn.Sigmoid())

print(net)
```

```python
net = nn.Sequential(
    nn.Conv2d(in_channels=3,out_channels=32,kernel_size = 3),
    nn.MaxPool2d(kernel_size = 2,stride = 2),
    nn.Conv2d(in_channels=32,out_channels=64,kernel_size = 5),
    nn.MaxPool2d(kernel_size = 2,stride = 2),
    nn.Dropout2d(p = 0.1),
    nn.AdaptiveMaxPool2d((1,1)),
    nn.Flatten(),
    nn.Linear(64,32),
    nn.ReLU(),
    nn.Linear(32,1),
    nn.Sigmoid()
)

print(net)
```

```python
from collections import OrderedDict

net = nn.Sequential(OrderedDict(
          [("conv1",nn.Conv2d(in_channels=3,out_channels=32,kernel_size = 3)),
            ("pool1",nn.MaxPool2d(kernel_size = 2,stride = 2)),
            ("conv2",nn.Conv2d(in_channels=32,out_channels=64,kernel_size = 5)),
            ("pool2",nn.MaxPool2d(kernel_size = 2,stride = 2)),
            ("dropout",nn.Dropout2d(p = 0.1)),
            ("adaptive_pool",nn.AdaptiveMaxPool2d((1,1))),
            ("flatten",nn.Flatten()),
            ("linear1",nn.Linear(64,32)),
            ("relu",nn.ReLU()),
            ("linear2",nn.Linear(32,1)),
            ("sigmoid",nn.Sigmoid())
          ])
        )
print(net)
```

```python
summary(net,input_shape= (3,32,32))
```

```txt
----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
================================================================
            Conv2d-1           [-1, 32, 30, 30]             896
         MaxPool2d-2           [-1, 32, 15, 15]               0
            Conv2d-3           [-1, 64, 11, 11]          51,264
         MaxPool2d-4             [-1, 64, 5, 5]               0
         Dropout2d-5             [-1, 64, 5, 5]               0
 AdaptiveMaxPool2d-6             [-1, 64, 1, 1]               0
           Flatten-7                   [-1, 64]               0
            Linear-8                   [-1, 32]           2,080
              ReLU-9                   [-1, 32]               0
           Linear-10                    [-1, 1]              33
          Sigmoid-11                    [-1, 1]               0
================================================================
Total params: 54,273
Trainable params: 54,273
Non-trainable params: 0
----------------------------------------------------------------
Input size (MB): 0.011719
Forward/backward pass size (MB): 0.359634
Params size (MB): 0.207035
Estimated Total Size (MB): 0.578388
----------------------------------------------------------------
```



### 2.3 大模型继承nn.Module基类，里面封装子模型

当模型的结构比较复杂时，我们可以应用模型容器(nn.Sequential,nn.ModuleList,nn.ModuleDict)对模型的部分结构进行封装。

这样做会让模型整体更加有层次感，有时候也能减少代码量。

注意，在下面的范例中我们每次仅仅使用一种模型容器，但实际上这些模型容器的使用是非常灵活的，可以在一个模型中任意组合任意嵌套使用。

### 2.3.1 使用nn.Sequential作为模型容器

这种我个人使用最多，易于理解。

```python
class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(in_channels=3,out_channels=32,kernel_size = 3),
            nn.MaxPool2d(kernel_size = 2,stride = 2),
            nn.Conv2d(in_channels=32,out_channels=64,kernel_size = 5),
            nn.MaxPool2d(kernel_size = 2,stride = 2),
            nn.Dropout2d(p = 0.1),
            nn.AdaptiveMaxPool2d((1,1))
        )
        self.dense = nn.Sequential(
            nn.Flatten(),
            nn.Linear(64,32),
            nn.ReLU(),
            nn.Linear(32,1),
            nn.Sigmoid()
        )
    def forward(self,x):
        x = self.conv(x)
        y = self.dense(x)
        return y 

net = Net()
```



### 2.3.2 使用nn.ModelList作为容器

```python
class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.layers = nn.ModuleList([
            nn.Conv2d(in_channels=3,out_channels=32,kernel_size = 3),
            nn.MaxPool2d(kernel_size = 2,stride = 2),
            nn.Conv2d(in_channels=32,out_channels=64,kernel_size = 5),
            nn.MaxPool2d(kernel_size = 2,stride = 2),
            nn.Dropout2d(p = 0.1),
            nn.AdaptiveMaxPool2d((1,1)),
            nn.Flatten(),
            nn.Linear(64,32),
            nn.ReLU(),
            nn.Linear(32,1),
            nn.Sigmoid()]
        )
    def forward(self,x):
        for layer in self.layers:
            x = layer(x)
        return x
net = Net()
print(net)

```

### 2.3.3 使用nn.ModuleDict作为模型容器

```python
class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.layers_dict = nn.ModuleDict({"conv1":nn.Conv2d(in_channels=3,out_channels=32,kernel_size = 3),
               "pool": nn.MaxPool2d(kernel_size = 2,stride = 2),
               "conv2":nn.Conv2d(in_channels=32,out_channels=64,kernel_size = 5),
               "dropout": nn.Dropout2d(p = 0.1),
               "adaptive":nn.AdaptiveMaxPool2d((1,1)),
               "flatten": nn.Flatten(),
               "linear1": nn.Linear(64,32),
               "relu":nn.ReLU(),
               "linear2": nn.Linear(32,1),
               "sigmoid": nn.Sigmoid()
              })
    def forward(self,x):
        layers = ["conv1","pool","conv2","pool","dropout","adaptive",
                  "flatten","linear1","relu","linear2","sigmoid"]
        for layer in layers:
            x = self.layers_dict[layer](x)
        return x
net = Net()
print(net)

```

