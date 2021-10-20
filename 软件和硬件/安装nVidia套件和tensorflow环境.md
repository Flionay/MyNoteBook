

# 安装Nvidia套件和Tensorflow环境

> 有些事情，重复过多次才能懂！

安装过无数次，每次都是查网页，一些破CSDN误导人无数次，真服了，感觉现在最扰乱网络环境的就是这些CSDN上的破博客。去Google吧，信息是有效，但是英文难免会降低干活的效率。

痛定思痛，一定要自己写个笔记，以防每次都去翻翻翻！

以下流程环境为Ubuntu 20.04 和 NVidia 显卡

一下流程大部分来源于此同学https://www.mlzhilu.com/archives/ubuntu2004%E5%AE%89%E8%A3%85nvidia%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8，感谢有这些写详细博客的好同志！

## 安装Nvidia显卡驱动

### 1. 查看自己的系统和显卡型号

```shell
uname -a #查看以下自己系统的版本，心里有个谱！
lspci | grep -i nvidia # 查看你的显卡型号，一会要对应去找该型号的驱动！
```

![image-20210826161906863](https://cdn.jsdelivr.net/gh/flionay/pic_bed//PicGo/image-20210826161906863.png)

### 2. 查找对应的nVidia显卡驱动

从NVIDIA官网下载相应驱动 https://www.nvidia.com/Download/index.aspx?lang=en-us，根据显卡型号下载！

![image-20210826162115368](https://cdn.jsdelivr.net/gh/flionay/pic_bed//PicGo/image-20210826162115368.png)

点击search，然后download，使用ftp工具上传到linux服务器上。

### 3. 禁用ubuntu自带驱动

在安装此驱动之前，还需要将ubuntu自带的驱动给禁用掉，这是很重要的一步！

卸载Ubuntu自带的驱动程序

```shell
sudo apt purge nvidia*
```

禁用自带的nouveau nvidia驱动

```shell
sodo vi /etc/modprobe.d/blacklist.conf
# vim在文件最后添加以下内容
# blacklist nouveau  
# options nouveau modeset=0 
```

然后保存退出。
更新

```
sudo update-initramfs -u 
```

重启

```shell
sudo reboot 
```

重启后查看是否已经将自带的驱动屏蔽了，输入以下代码

```shell
lsmod | grep nouveau 
```

没有结果输出，则表示屏蔽成功

### 4. 安装官方驱动

先查看系统有没有装gcc

```shell
gcc -version
```

![image-20210826162625948](https://cdn.jsdelivr.net/gh/flionay/pic_bed//PicGo/image-20210826162625948.png)

没有版本信息就安装一下gcc，make同理，如果make也没有装，用如下命令装一下这两个东东：

```shell
sudo apt install gcc 
sudo apt install make
# 或者直接执行
sudo apt install gcc & make # 同时安装gcc和make
```

装完之后，cd到你放置下载的官方驱动的目录，执行：

```shell
sudo chmod a+x NVIDIA-Linux-x86_64-450.142.00.run # 给权限
sudo ./NVIDIA-Linux-x86_64-450.142.00.run -no-x-check -no-nouveau-check -no-opengl-files
# -no-x-check:安装时关闭X服务
# -no-nouveau-check: 安装时禁用nouveau
# -no-opengl-files:只安装驱动文件，不安装OpenGL文件
```

会弹出安装进度，

![image-20210826163047567](https://cdn.jsdelivr.net/gh/flionay/pic_bed//PicGo/image-20210826163047567.png)

![image-20210826163026094](https://cdn.jsdelivr.net/gh/flionay/pic_bed//PicGo/image-20210826163026094.png)

以上这两条如图示选择，其他选择默认即可！

安装完成后执行`nvidia-smi` 查看是否安装成功！

![image-20210911190539956](https://cdn.jsdelivr.net/gh/Flionay/pic_bed@master/Upic/202109/image-20210911190539956.png)

出现类似信息，表明驱动安装成功！

## 安装CUDA

从上面的图中可以看到我的显卡最高可以支持cuda11.0(绿色框内)
下载cuda https://developer.nvidia.com/cuda-toolkit-archive，点进网址，选择cuda11，然后选择linux，即可进入如下界面，选择系统对应信息，会弹出安装命令，复制到终端执行即可！

![image-20210826163639035](https://cdn.jsdelivr.net/gh/flionay/pic_bed//PicGo/image-20210826163639035.png)

```shell
wget http://developer.download.nvidia.com/compute/cuda/11.0.2/local_installers/cuda_11.0.2_450.51.05_linux.run
sudo sh cuda_11.0.2_450.51.05_linux.run
```

安装的时候会让写一个接受协议类似的东西，写入accept即可，在第二个界面移动到Driver前面，按下回车，取消Driver前面的X，其他默认，移动到最后的install安装。

完成之后，添加环境变量

```shell
vim ~/.bashrc

# 将下面的11.0替换为你的cuda版本，其他不变，如果不知道自己安装的是哪个版本，就去/usr/local/文件夹下找一下
export PATH=/usr/local/cuda-11.0/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-11.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}

```

:wd保存之后，执行`source ~/.bashrc`,更新环境变量

最后终端输入`nvcc -V`,如果出现下图，说明安装成功！

![image-20210826164146790](https://cdn.jsdelivr.net/gh/flionay/pic_bed//PicGo/image-20210826164146790.png)

## 安装cudnn

13、下载cudnn https://developer.nvidia.com/rdp/cudnn-download
下载cudnn需要登录账户，可以用QQ或者微信注册一个用户然后登录找到对应cuda版本的cudnn点开找到第一个library点击下载就可以了。
![image.png](https://cdn.jsdelivr.net/gh/Flionay/pic_bed@master/Upic/202109/image-7a7f26ac6fc644969f006c30df578094.png)
解压下载好的cudnn压缩包，然后执行

```
# 将文件复制到cuda对应的文件夹下
sudo cp cuda/include/cudnn.h /usr/local/cuda/include/
sudo cp cuda/lib64/libcudnn* /usr/local/cuda/lib64/
# 赋予文件执行权限
sudo chmod a+r /usr/local/cuda/include/cudnn.h
sudo chmod a+r /usr/local/cuda/lib64/libcudnn*
```

## cuda测试

显卡驱动+cuda+cudnn都安装完成了，当然要试一下能不能用了，接下来我们对其进行测试。

如果安装时安装了sample，那就可以在终端cd到NVIDIA_CUDA-11.0_Samples所在目录，一般默认在/home/你的用户名/NVIDIA_CUDA-11.0_Samples,然后执行make
如果出现如下错误，表示没有安装g++，那么就执行sudo apt install g++，然后再make
![image.png](http://www.mlzhilu.com/upload/2020/11/image-ef026f294e064b9483a5c430df3b32c4.png)
如果不出意外，等一会儿会编译通过
![image.png](http://www.mlzhilu.com/upload/2020/11/image-527a76578c234169be9857f6c60d99a6.png)
然后我们cd到NVIDIA_CUDA-11.0_Samples/1_Utilities/deviceQuery下，执行

```
./deviceQuery 
```

如果result=PASS表示通过
![image.png](https://cdn.jsdelivr.net/gh/Flionay/pic_bed@master/Upic/202109/image-833df671beeb4c18a0f3f1bce2bd5dc5.png)
然后cd到NVIDIA_CUDA-11.0_Samples/1_Utilities/bandwidthTest下，执行：

```
./bandwidthTest
```

如果result=PASS表示通过
![image.png](https://cdn.jsdelivr.net/gh/Flionay/pic_bed@master/Upic/202109/image-3bd9492be6314f9d82481b87fe04f444.png)

至此，全部配置完成，如有错误欢迎留言指出。

# Tensorflow 环境安装

安装某些包或者环境，第一选择一定是官网！！ 

忍不住又要吐槽那些乱七八糟的csdn，深受其害！

进入tensorflow官网，官网推荐pip安装，但是我习惯了用canda，所以根据官方的指引，去这个链接，查看conda官方给的tensorflow安装教程:

就一行命令！简直了，再也不要理百度出来的那些牛马神蛇了！

![image-20210826164927459](https://cdn.jsdelivr.net/gh/flionay/pic_bed//PicGo/image-20210826164927459.png)

![image-20210826164957827](https://cdn.jsdelivr.net/gh/flionay/pic_bed//PicGo/image-20210826164957827.png)

在创建虚拟环境的后面加一个tensorflow-gpu即可，官方已经给你准备好了！！

```shell
conda create -n tf-gpu tensorflow-gpu
conda activate tf-gpu
```

下载之后就可以使用了！不会出现什么调不起来GPU，不会出现各种动态库的问题！

不过要注意，conda install 其他包的时候注意点，别随意升级里面的cudatoolkit cudnn等！
