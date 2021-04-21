![HITeHE](https://cdn.jsdelivr.net/gh/Flionay/pic_bed@master/Upic/202104/HITeHE.png)

**使用需求：**

1. gpu cuda python环境的快速迁移和部署
1. Linux用户增加的话，一方面可以部署容器到其他硬盘，减少/home路径的硬盘占用，另一方面能够避免用户修改cuda驱动导致所有用户都不能使用的局面，减少驱动层的公用带来可能的问题。
## 为什么需要 Nvidia Docker
Docker容器与系统平台无关，也和硬件无关。但是当使用需要内核模块和用户级库才能运行的专用硬件（例如NVIDIA GPU）时，这就出现了一个问题。 结果就导致Docker本身不支持容器内的NVIDIA GPU。

 解决此问题的早期方法之一是在容器中完全安装NVIDIA驱动程序，并在启动时将其映射到与NVIDIA GPU（例如/ dev / nvidia0）相对应的字符设备中。 该解决方案比较脆弱，因为主机驱动程序的版本必须与容器中安装的驱动程序的版本完全匹配。 这项要求极大地降低了这些早期容器的可移植性，从而破坏了Docker更重要的功能之一。

 为了在使用NVIDIA GPU的Docker映像中实现可移植性，英伟达开发了nvidia-docker，这是一个托管在Github上的开源项目，它提供了基于便携式GPU的容器所需的两个关键组件：**与驱动程序无关的 CUDA映像**；  **Docker命令行包装器， 上执行代码。 仅在使用nvidia-docker run执行使用GPU的容器时非常有用。 


## Installing Docker and NVIDIA Docker
### 安装docker
安装步骤跟着官网的教程一步一步做就行，安装完之后可能会遇到权限问题。 

![image.png](https://cdn.jsdelivr.net/gh/Flionay/pic_bed@master/Upic/202104/1618196439943-45f6c3c7-d795-4786-a881-828a87827f39-20210421202952985.png)一个解决方案就是用sudo执行所有的docker命令，当然这样很不方便。
查看没有权限的这个文件，发现该文件属于docker用户组，那么只需要将我们的用户添加到这个组，就可以使用docker命令了：

![image.png](https://cdn.jsdelivr.net/gh/Flionay/pic_bed@master/Upic/202104/1618196682986-bb49d170-9560-4679-b475-b223efa5676f.png)

```bash
$ sudo gpasswd -a username docker #将普通用户username加入到docker组
newgrp docker  #更新docker组
```
### 安装Nvidia Docker
基本跟着官方教程安装就可以，没遇到什么其他问题：
[https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html)


```bash
distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
   && curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add - \
   && curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
   
   sudo apt-get update
   
   sudo apt-get install -y nvidia-docker2
   
   sudo systemctl restart docker
   # 拉取基础的cuda镜像，测试一下nvidia-smi，如果有显卡信息，则安装成功。
   sudo docker run --rm --gpus all nvidia/cuda:11.0-base nvidia-smi
```
## 移动Docker默认存储位置
查看docker的存放位置，一般位于 `Docker Root Dir: /var/lib/docker` 
```bash
sudo docker info | grep "Docker Root Dir"   #查看默认存放位置
```
```bash
#关闭docker 服务
sudo service docker stop

#移动数据到新的目录
mv /var/lib/docker /data/docker

# 修改配置文件
sudo vim /etc/default/docker
# 在配置文件最后一行追加 DOCKER_OPTS="-g /root/data/docker"

#重启docker 服务
service docker start

```
这样做完之后，查看默认路径还是在var，但是下载数据，这个目录已经不会增加占用了，应该是成功了。
## 拉取nvidia/cuda镜像


在dockerhub搜索nvidia/cuda即可，根据你的系统平台可以在tag列表里进一步精确查找。


![image.png](https://cdn.nlark.com/yuque/0/2021/png/2637180/1618209987421-44949a53-0c29-4fa8-a406-be6f6774c828.png?x-oss-process=image%2Fresize%2Cw_1492)


然后复制右边得命令，直接拉取即可。


## 镜像换源
![image.png](https://cdn.jsdelivr.net/gh/Flionay/pic_bed@master/Upic/202104/1618210560307-3c4f2b06-daf1-4413-98f9-42fa20e2e4ac.png)


默认的dockerhub源国内速度都很慢，可以通过换源加速镜像拉取的过程。
登录阿里云账号，在控制台搜索容器镜像服务，能够根据命令配置个人的容器加速服务。


## 启动容器，搭建环境
```bash
# 查看镜像
(base) msdc_2@amax:~$ docker images
REPOSITORY    TAG                             IMAGE ID       CREATED       SIZE
nvidia/cuda   10.2-cudnn7-devel-ubuntu18.04   e37754c25fbb   4 weeks ago   3.85GB

# 从镜像启动容器 并-it 进入
(base) msdc_2@amax:~$ docker run --name=docker_gpu -it e37
root@9497e5432fe5:/home# nvcc -V
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2019 NVIDIA Corporation
Built on Wed_Oct_23_19:24:38_PDT_2019
Cuda compilation tools, release 10.2, V10.2.89

# 然后就可以安装anaconda和tensorflow等环境了

bash Anaconda3-2020.02-Linux-x86_64.sh 
bash ./bashrc
```


## Docker安装SSH
```bash
apt-get update

# 安装ssh-client命令
apt-get install openssh-client

# 安装ssh-server命令
apt-get install openssh-server

# 安装完成后，先启动服务#
/etc/init.d/ssh start

# 查看是否正确启动
ps -e|grep ssh

```
## 端口转发
本来应该是启动的时候docker run命令后面跟端口转发的，但是现在容器已经运行起来了，没有做端口转发。
最简便的方法就是将现在修改过的容器保存成镜像，然后重新启动一次。
```bash
# 将修改保存成镜像
(base) msdc_2@amax:~$ docker commit 9497e5432fe5 chla

# 查看镜像id
(base) msdc_2@amax:~$ docker images
REPOSITORY    TAG                             IMAGE ID       CREATED       SIZE
chla          latest                          eaa1ce6462df   5 hours ago   10GB
nvidia/cuda   10.2-cudnn7-devel-ubuntu18.04   e37754c25fbb   4 weeks ago   3.85GB

# 启动镜像
(base) msdc_2@amax:~$ docker run -it --name=chla -p 2222:22 eaa
(base) root@e9a7211c5aad:/# 

# 修改ssh配置
(base) msdc_2@amax:~$ docker exec -it e9a /bin/bash
(base) root@e9a7211c5aad:/# vim /etc/ssh/sshd_config
PermitRootLogin yes  #允许root用户ssh登录
UsePAM no            ##禁用PAM

# 修改root用户密码
(base) root@e9a7211c5aad:/# passwd
Enter new UNIX password: 
Retype new UNIX password: 
passwd: password updated successfully

```
## 本地ssh连接
```powershell
(base) PS C:\Users\user> ssh root@159.226.158.152 -p 2222
root@159.226.158.152's password:
(base) root@e9a7211c5aad:~# ls
anaconda3
```
























