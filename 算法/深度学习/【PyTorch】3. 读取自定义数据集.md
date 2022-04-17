# 创建数据集、读取数据流
Pytorch通常使用Dataset和DataLoader这两个工具类来构建数据管道。
```python
from torch.utils.data import Dataset, DataLoader
```


Dataset定义了数据集的内容，它相当于一个类似列表的数据结构，具有确定的长度，能够用索引获取数据集中的元素。

而DataLoader定义了按batch加载数据集的方法，它是一个实现了`__iter__`方法的可迭代对象，每次迭代输出一个batch的数据。

DataLoader能够控制batch的大小，batch中元素的采样方法，以及将batch结果整理成模型所需输入形式的方法，并且能够使用多进程读取数据。

在绝大部分情况下，用户只需实现Dataset的`__len__`方法和`__getitem__`方法，就可以轻松构建自己的数据集，并用默认数据管道进行加载。

## 1.利用Dataset创建数据集

Dataset创建数据集常用的方法有：

- 使用 torch.utils.data.TensorDataset 根据Tensor创建数据集(numpy的array，Pandas的DataFrame需要先转换成Tensor)。
- 使用 torchvision.datasets.ImageFolder 根据图片目录创建图片数据集。
- 继承 torch.utils.data.Dataset 创建自定义数据集。

此外，还可以通过

- torch.utils.data.random_split 将一个数据集分割成多份，常用于分割训练集，验证集和测试集。
- 调用Dataset的加法运算符(`+`)将多个数据集合并成一个数据集。

## 2. 使用DataLoader加载数据集

DataLoader能够控制batch的大小，batch中元素的采样方法，以及将batch结果整理成模型所需输入形式的方法，并且能够使用多进程读取数据。

DataLoader的函数签名如下。

```
DataLoader(
    dataset,
    batch_size=1,
    shuffle=False,
    sampler=None,
    batch_sampler=None,
    num_workers=0,
    collate_fn=None,
    pin_memory=False,
    drop_last=False,
    timeout=0,
    worker_init_fn=None,
    multiprocessing_context=None,
)
```

一般情况下，我们仅仅会配置 dataset, batch_size, shuffle, num_workers, drop_last这五个参数，其他参数使用默认值即可。

DataLoader除了可以加载我们前面讲的 torch.utils.data.Dataset 外，还能够加载另外一种数据集 torch.utils.data.IterableDataset。

和Dataset数据集相当于一种列表结构不同，IterableDataset相当于一种迭代器结构。 它更加复杂，一般较少使用。

- dataset : 数据集
- batch_size: 批次大小
- shuffle: 是否乱序
- sampler: 样本采样函数，一般无需设置。
- batch_sampler: 批次采样函数，一般无需设置。
- num_workers: 使用多进程读取数据，设置的进程数。
- collate_fn: 整理一个批次数据的函数。
- pin_memory: 是否设置为锁业内存。默认为False，锁业内存不会使用虚拟内存(硬盘)，从锁业内存拷贝到GPU上速度会更快。
- drop_last: 是否丢弃最后一个样本数量不足batch_size批次数据。
- timeout: 加载一个数据批次的最长等待时间，一般无需设置。
- worker_init_fn: 每个worker中dataset的初始化函数，常用于 IterableDataset。一般不使用。

```
#构建输入数据管道
ds = TensorDataset(torch.arange(1,50))
dl = DataLoader(ds,
                batch_size = 10,
                shuffle= True,
                num_workers=2,
                drop_last = True)
#迭代数据
for batch, in dl:
    print(batch)
tensor([43, 44, 21, 36,  9,  5, 28, 16, 20, 14])
tensor([23, 49, 35, 38,  2, 34, 45, 18, 15, 40])
tensor([26,  6, 27, 39,  8,  4, 24, 19, 32, 17])
tensor([ 1, 29, 11, 47, 12, 22, 48, 42, 10,  7])
```

## 3. 调用dataloader 并 分割数据集

```python
import numpy as np 
import torch 
from torch.utils.data import TensorDataset,Dataset,DataLoader,random_split 

# 根据Tensor创建数据集

from sklearn import datasets 
iris = datasets.load_iris()
ds_iris = TensorDataset(torch.tensor(iris.data),torch.tensor(iris.target))

# 分割成训练集和预测集
n_train = int(len(ds_iris)*0.8)
n_valid = len(ds_iris) - n_train
ds_train,ds_valid = random_split(ds_iris,[n_train,n_valid])

print(type(ds_iris))
print(type(ds_train))


# 使用DataLoader加载数据集
dl_train,dl_valid = DataLoader(ds_train,batch_size = 8),DataLoader(ds_valid,batch_size = 8)

for features,labels in dl_train:
    print(features,labels)
    break

# 演示加法运算符（`+`）的合并作用
ds_data = ds_train + ds_valid
```



## 4. 实际案例一 ：加载VOC数据集

### 4.1 Dataset类模板

任何自定义的数据集类都必须继承自PyTorch的数据集类。自定义的类必须实现两个函数：`__len__(self)`,`__getitem__`任何和Dataset类表现类似的自定义类都应和下面的代码类似

```python
class FirstDataset(data.Dataset):#需要继承data.Dataset
    def __init__(self,root_dir,size=(16,16)):
        # TODO
        # 1. 初始化文件路径或文件名列表。
        # 2. 设置一些基本参数
        #也就是在这个模块里，我们所做的工作就是初始化该类的一些基本参数。
        self.files = os.listdir(root_dir)
        self.size = size
    def __getitem__(self, index):
        #1。从文件中读取一个数据（例如，使用numpy.fromfile，PIL.Image.open）。
        #2。预处理数据（例如torchvision.Transform）。
        #3。返回数据对（例如图像和标签）。
        #这里需要注意的是，使用index索引
        img = self.files[index][0]
        label = self.files[index][1]
        return img,label
        
    def __len__(self):
        # 将0更改为数据集的总大小。
        return len(self.files)

```

定义了数据集类之后就可以创建对象并在其上进行迭代，例如：

```python
datasets = FirstDataset('../data/')
for image,label in datasets:
  pass
```

### 4.2 Dataloader 模板


1. Dataloader

   Dataset类一般用于调用单个数据实例，现代的GPU都对批数据的执行进行了性能优化，DataLoader类通过多进程迭代器，为我们提供批量图片。

   ```python
   train_loader = DataLoader(dataset=train_data, batch_size=6, shuffle=True ，num_workers=4)
   test_loader = DataLoader(dataset=test_data, batch_size=6, shuffle=False，num_workers=4)
   ```

   >batch_size：类似将数据打包成小份，设置每一小份的大小
   >
   >shuffle=True：是否对数据进行洗牌操作(shuffling)，是否打乱数据集内数据分布的顺序
   >
   >num_workers=2：可以并行加载数据(利用多核处理器加快载入数据的效率）

2. [torchvision](https://pytorch.org/docs/master/torchvision/index.html)：

  - dataset 一些基本的，常用的数据集
  - models 图像分类，图像分割，图像检测，视频分类的一些常用网络模型都有官方代码
  - transforms 对图片进行基础处理，切割，转换通道，归一化等。详细的'torchvision.transforms'的全部细节操作可以看[这里](https://www.jianshu.com/p/1ae863c1e66d)
  - io/utils/ops 提供一些处理视频或一些特殊操作的接口，用到了在详细查询即可。

###  4.3 梳理基本流程

1. 先将图片分成三个文件夹，分别是训练验证测试
2. 然后将对应文件夹的图片和标签的路径读出来，写入txt，保证读取顺序
3. 读取txt路径，创建DATASET类，用DataLoader读取

这是图片的读取方式，一些小细节要注意，图片的读取方式，一般为RGB，如果不是要转换一下。如果是调用现成的网络结构最好根据网络输入transform里切割或者resize一下，减少调整shape的工作量。

### 4.4 VOC数据集实例

要根据自己的数据格式来具体调整导入数据的方式，如果原始数据不是图片，只需要把数据导入成图片格式的矩阵维度即可，如果是语义分割任务，label也是一张图片，这里要注意一些细节，label的切割，transform会把类别变成小数。

```python
import os
from torch.utils.data import Dataset, DataLoader
import torchvision
import torchvision.transforms as transforms
from torch import nn



class CustomDataset(Dataset):
    def __init__(self,data_root,NUM_CLASSES):
        
        self.train_data = np.load(os.path.join(data_root,'trainAVISO-SSH_2000-2010.npy'))
        self.train_label = np.load(os.path.join(data_root,'trainSegmentation_2000-2010.npy'))
        self.data_transform = transforms.Compose([
                                transforms.ToPILImage(), \
                                transforms.CenterCrop(10), \
                                transforms.ToTensor(), \
                                transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                                     std=[0.229, 0.224, 0.225])
                                ])
        
    def __len__(self):
        return self.train_data.shape[0]

    def __getitem__(self, index):
      
        images = Image.fromarray(self.train_data[index,:,:])
        if images.mode != 'RGB':
            images = images.convert('RGB')
        image = self.data_transform(images)
        
        # ----------label--------------

        labels = Image.fromarray(self.train_label[index,:,:])
        self.train_labels = self.data_transform_label(labels)

        mask_each_classes = torch.zeros(NUM_CLASSES, image.shape[1], image.shape[2])
        for i in range(NUM_CLASSES):
            class_value = np.unique(self.train_labels.cpu().numpy()) # 类别经过归一化不再是 0，1，2
            mask_each_classes[i][self.train_labels[0,:,:] == class_value[i]] = 1

        batch = {'input': image, 'target': mask_each_classes}
        return batch

```

```python
DATA_ROOT = 'data/data_origin/'    
train_dataset = CustomDataset(DATA_ROOT,NUM_CLASSES = 3)
train_dataloader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True, num_workers=0)
```

## 5. 实际案例二：加载大型CSV文件

这里我们下载了kaggle的一个数据集，train.csv文件大小为18G，显然对于一般的计算机是很难一次性读入内存的。

这样就要设定一个读入流，训练的时候迭代加入一个个batch，不一次性读入内存，实现模型的大数据集训练。

```python
import os
from torch.utils.data import Dataset, DataLoader
import torchvision
import torchvision.transforms as transforms
from torch import nn
import torch
import pandas as pd
import numpy as np

class CustomDataset(Dataset):
    '''
        读取一个18G的csv
        并不是一次性读入，实现一个读入流，迭代器
    
    '''
    def __init__(self,csv_file:str,chunksize:int): 
        # 可以用这个chunksize 替代 batch_size
        self.chunksize = chunksize
        
        self.csv_reader = pd.read_csv(csv_file, iterator=True, chunksize=chunksize)
        
    def __len__(self):
        # 因为csv文件太大，只读取一列，获得其长度
        # rows_all = len(pd.read_csv(self.csv_path, usecols=['time_id']))
        
        # 有多少个chunk
        return int(942961/self.chunksize) #rows_all

    def __getitem__(self, index):
        
        chunk_data = self.csv_reader.get_chunk()
        x = chunk_data.iloc[:,4:]
        y = chunk_data.iloc[:,3]
        
        # 转换为tensor
        x_tensor = torch.FloatTensor(np.array(x))
        y_tensor = torch.FloatTensor(np.array(y))
        

        batch = {'input': x_tensor, 'target': y_tensor}
        return batch
```



```python
DATA_ROOT = "/data/Chenjq/kaggle/data/train.csv"
train_dataset = CustomDataset(DATA_ROOT,chunksize=1000)
train_dataloader = DataLoader(train_dataset,shuffle=True, num_workers=0)

for batch in train_dataloader:
    print(batch['input'].shape)
    print(batch['target'].shape)
    break
```

