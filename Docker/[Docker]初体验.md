## 基础概念

1. 镜像（Image）：

   好比是一个模版，可以通过这个模版来创建容器服务，tomcat镜像===》run====〉tomcat01容器，功过这个镜像可以创建多个容器（最终服务和项目就是在容器中的）。

2. 容器（container）：

   Docker利用容器技术，独立运行一个或者一个组应用，通过镜像创建的。

   启动，停止，删除，基本命令

   可以把容器理解为一个简易的Linux系统。

3. 仓库（respository）

   仓库就是存放镜像的地方。仓库分为公有仓库和私有仓库。

   Docker Hub 阿里云等都有容器服务器。（配置镜像加速！）

## 安装Docker

## Docker 常用命令

### **帮助命令**

```shell
docker version  #显示docker的版本信息
docker info 		#显示docker的系统信息，包括
docker  命令 --help  #帮助命令
```

帮助命令地址：https://docs.docker.com/engine/reference/commandline/

### **镜像命令**

**docker images** 查看所有本地主机的镜像

**docker search** 搜索镜像

```shell
~ via C base took 2s 
❯ docker search mysql --filter=STARS=3000
NAME      DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
mysql     MySQL is a widely used, open-source relation…   10281     [OK]       
mariadb   MariaDB is a community-developed fork of MyS…   3801      [OK]   
# --filter 过滤
```

**docker pull** 下载镜像

```shell
~ via C base 
❯ docker pull mysql:8.0.18 
# 如果不写tag 默认就是最新的
# 下载是分层下载的
~ via C base 
❯ docker pull mysql                      
Using default tag: latest
latest: Pulling from library/mysql
6ec7b7d162b2: Pull complete 
fedd960d3481: Pull complete 
7ab947313861: Pull complete 
64f92f19e638: Pull complete 
3e80b17bff96: Pull complete 
014e976799f9: Pull complete 
59ae84fee1b3: Pull complete 
ffe10de703ea: Pull complete 
657af6d90c83: Pull complete 
98bfb480322c: Pull complete 
9f2c4202ac29: Pull complete 
a369b92bfc99: Pull complete 
Digest: sha256:365e891b22abd3336d65baefc475b4a9a1e29a01a7b6b5be04367fcc9f373bb7
Status: Downloaded newer image for mysql:latest
docker.io/library/mysql:latest

```

分层是Docker很重要的下载利器，将文件分开下载，遇到不同版本只需要更新有变化的层即可。

**docker rmi** 删除镜像





### 容器命令