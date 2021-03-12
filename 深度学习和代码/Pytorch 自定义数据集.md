数据下载和预处理一直都是机器学习，深度学习实际项目中最耗时又最重要的任务之一，往往占据了项目的大部分时间。好在Pytorch提供了专门的数据下载，数据处理包，学会使用它们，能极大的提高我们的开发效率和数据质量。

## 概述

1. Dataset类

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

   

2. Dataloader

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

3. [torchvision](https://pytorch.org/docs/master/torchvision/index.html)：
  - dataset 一些基本的，常用的数据集
  - models 图像分类，图像分割，图像检测，视频分类的一些常用网络模型都有官方代码
  - transforms 对图片进行基础处理，切割，转换通道，归一化等。详细的'torchvision.transforms'的全部细节操作可以看[这里](https://www.jianshu.com/p/1ae863c1e66d)
  - io/utils/ops 提供一些处理视频或一些特殊操作的接口，用到了在详细查询即可。

### 基本流程

1. 先将图片分成三个文件夹，分别是训练验证测试
2. 然后将对应文件夹的图片和标签的路径读出来，写入txt，保证读取顺序
3. 读取txt路径，创建DATASET类，用DataLoader读取

这是图片的读取方式，一些小细节要注意，图片的读取方式，一般为RGB，如果不是要转换一下。如果是调用现成的网络结构最好根据网络输入transform里切割或者resize一下，减少调整shape的工作量。

## 实例

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

