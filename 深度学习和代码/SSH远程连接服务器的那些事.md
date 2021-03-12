# SSH远程连接服务器搭建Python环境全套解析

![OQq8RW](https://cdn.jsdelivr.net/gh/Flionay/pic_bed@master/Upic/202102/OQq8RW.png)

##  ssh

SSH（Secure Shell）是一套协议标准，可以用来实现两台机器之间的安全登录以及安全的数据传送，其保证数据安全的原理是**非对称加密**。

传统的**对称加密**使用的是一套秘钥，数据的加密以及解密用的都是这一套秘钥，可想而知所有的客户端以及服务端都需要保存这套秘钥，泄露的风险很高，而一旦秘钥便泄露便保证不了数据安全。

**非对称加密**解决的就是这个问题，它包含两套秘钥 - 公钥以及 私钥，其中公钥用来加密，私钥用来解密，并且通过公钥计算不出私钥，因此私钥谨慎保存在服务端，而公钥可以随便传递，即使泄露也无风险。

保证SSH安全性的方法，简单来说就是客户端和服务端各自生成一套私钥和公钥，并且互相交换公钥，这样每一条发出的数据都可以用对方的公钥来加密，对方收到后再用自己的私钥来解密。

> 总结：公钥和私钥是通过一种算法得到的一个密钥对(即一个公钥和一个私钥)，将其中的一个向外界公开，称为公钥；另一个自己保留，称为私钥。通过这种算法得到的密钥对能保证在世界范围内是唯一的。
>
> 当然这其中还有更加复杂的密码学算法，涉及到数字签名 哈希算法等，这里我们不仔细研究。
>
> 总结操作流程来说就是**公钥加密，私钥解密。私钥数字签名，公钥验证。**

## 通常我们有两种**连接服务器**的方式

1. 利用密码登录

   需要有服务器ip，端口，用户名，密码

   ![密码登录原理图解](http://5b0988e595225.cdn.sohucs.com/images/20180927/4ae74ee9e7ee4b9c905e60c95dd1aa02.jpeg)

   1. 服务端收到登录请求后，首先互换公钥，详细步骤如上一节所述。
   2. 客户端用服务端的公钥加密账号密码并发送
   3. 服务端用自己的秘钥解密后得到账号密码，然后进行验证
   4. 服务端用客户端的公钥加密验证结果并返回
   5. 服务端用自己的秘钥解密后得到验证结果

通常我们可以用一些ssh客户端，比如用终端/putty/final shell /Xshell等工具登陆服务器命令行：

![终端连接服务器](https://cdn.jsdelivr.net/gh/Flionay/pic_bed@master/Upic/202005/截屏2020-05-12%20下午6.46.13.png)

输入ssh命令，用户名@ip，然后输入密码即可登录到服务器终端。到了这一步我们就打通了与服务器的连接，通过命令行我们可以对服务器进行一些配置操作，来响应本地用户的要求。

2. 密码登录方式在每次登录时都需要输入密码，而利用公，

   ![公钥登录原理图解](http://5b0988e595225.cdn.sohucs.com/images/20180927/6eac3973857947a68da9d0d28abdd446.jpeg)

   1. 客户端用户必须手动地将自己的公钥添加到服务器一个名叫authorized_keys的文件里，顾名思义，这个文件保存了所有可以远程登录的机器的公钥。
   2. 客户端发起登录请求，并且发送一个自己公钥的指纹（具有唯一性，但不是公钥）
   3. 服务端根据指纹检测此公钥是否保存在authorized_keys中
   4. 若存在，服务端便生成一段随机字符串，然后利用客户端公钥加密并返回
   5. 客户端收到后用自己的私钥解密，再利用服务端公钥加密后发回
   6. 服务端收到后用自己的私钥解密，如果为同一字符串，则验证通过

   ==使用这一行命令即可将个人公钥添加到服务器，之后登陆就可以免密码输入这一步骤了==

   ```bash
   ssh-copy-id -i ~/.ssh/id_rsa.pub user@server
   ```

   

## 安装Anaconda

后面这些配置项目只针对于利用GPU服务器进行深度学习或者Python相关工作人员：

### 下载安装包

1. 利用wget下载官网链接，这种方式可能比较慢，需要确定版本的包名称。

```bash
wget https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh
```

2. 直接在本地去官网或者清华镜像下载Anaconda对应安装包，然后利用Filezilla等Ftp传输工具，将安装包传输到服务器。

### 安装

```bash
cd 安装包所在路径
bash Anaconda安装包.sh
```



然后一路回车，直到安装完成。中间会有好几次输入yes操作，一般选择安装到默认位置，添加环境变量，所以都输入yes，如果忘记操作，没有添加到环境变量，可以用下面的命令添加到环境变量

### 添加到环境变量

```bash
sudo gedit ~/.bashrc
export PATH="/home/用户名/anaconda3/bin:$PATH"
source ~/.bashrc
```

> 这里曾经遇到过一个小烦恼，如果服务器默认命令行不是bash，而是sh之类的，可能你添加了环境变量也会无法运行conda，会提示not found，这是只需要exec bash将命令行转为bash即可。

## 单配置jupyter

1. 生成Jupyter的配置文件，使用命令自动生成配置文件
```bash    
jupyter notebook --generate-config
```
2. 生成jupyter密钥，找个Ipython命令行，然后输入以下代码：
```python
from notebook.auth import passwd
passwd()
#就会提示输入两次密码:  # 输入你自己的自定义密码两次
`sha1:67c9e60bb8b6:9ffede0825894254b2e042ea597d771089e11aed'`
```
复制输出的sha1密钥，打开配置文件的路径中的配置文件`.jupyter/jupyter_notebook_config.py`,修改下面的设置

```vim
    c.NotebookApp.password = u'sha1:67c9e60bb8b6:9ffede0825894254b2e042ea597d771089e11aed'
    c.NotebookApp.ip = '*'
    c.NotebookApp.open_browser = False
    c.NotebookApp.port = 9999
```

随后就可以在服务器命令行输入`jupyter notebook`,然后在本地浏览器输入`ip：8888`，就会出现login界面，输入自定义密码即可打开jupyter。

## 配置VsCode

天地大同，万物合一编辑器Vscode逐渐成为了我的最爱，用Vscode直接连接服务器进行代码工作也是非常方便。 

在扩展栏搜索ssh，添加微软官方Remote SSH扩展插件，添加成功之后在左边栏出现的图标

![VsCode ssh插件](https://cdn.jsdelivr.net/gh/Flionay/pic_bed@master/Upic/202005/image-20200518154333814.png)

点击边栏图标，点击加号，输入ssh命令行语句然后选择ssh配置文件即可连接，Vscode现在支持原生jupyter，一切都是这么流畅。

> 注意类似VsCode python等插件，服务器与本地也是分开的，所以需要重新安装一下。

## Python 虚拟环境

服务器的环境往往不是一个人在使用，或者你个人目录下有多个项目，需要建立不同的Python环境，或者项目最后需要一起打包依赖，那么在这些场景下，我都建议你使用Python的虚拟环境,因为她们彼此独立，。

利用conda创建虚拟环境：

```bash
conda create -n environment_name python=X.X
```

然后就可以利用VsCode的解释器选择窗口选择虚拟环境，新建终端，会发现命令行会自动激活所选环境，一切如丝绸般顺滑！

![VsCode激活虚拟环境](https://cdn.jsdelivr.net/gh/Flionay/pic_bed@master/Upic/202005/WI46Ym.png)

