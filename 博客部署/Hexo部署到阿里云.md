## 1. 购买云服务器

登录官网，购买一台ECS即可，如果你是学生并且是第一次购买在阿里云可以领20优惠券，而且有学生专用云套餐，推荐！

之前将博客部署在github，gitee等免费提供的Page服务上，但是由于这些IP都在墙外，另外购买CDN加速需要绑定备案域名，域名倒是好说，这个备案，它又必须有服务器实例。

所以折腾来折腾去，还是选择买一台云服务器，一是为了博客，而是学习云服务器使用，投资自己嘛。
### 预备姿势
买了阿里云服务器之后，先熟悉一下控制台，别急着上手。这里有几项必备技能，如果你不熟悉，建议提前搜索学习一下。
> 1. SSH 远程连接服务器，公钥配置等，建议去看我上一篇文章来理解SSH
> 2. 开放实例端口，进入ECS具体实例，点击本实例安全组，点击配置规则，添加规则，然后开放必要的端口。
> 3. vim基本操作，键入i进入插入模式，可以编辑文本，保存并退出按 Esc然后输入 :wq
> 4. 宝塔界面第一次进入应该不会有问题，但是如果关闭之后第二天你可能会忘记宝塔地址，密码之类的，只需要在命令行输入bt，按照对应信息即可查询相关地址，或者更改密码等操作。

![宝塔](https://i.loli.net/2020/05/21/qf8zljQnYo3ikUH.png)

## 2. 配置云服务器环境

![博客访问流程，Hexo博客架构](http://img.skyheng.com/picture/hexo/hexo_articlex.png)

先搞明白Hexo博客从搭建到自动发布的架构，才能更好的理解我们每一步进行的操作。不然只跟着步骤过了一遍，却不知道为什么这么做。



### 1. 安装Git

   ```bash
   yum install git
   
   ```
### 2. 创建git用户
  ```
  adduser git
  chmod 740 /etc/sudoers
  vim /etc/sudoers
  ```

找到以下内容

  ```
  ## Allow root to run any commands anywhere
  root    ALL=(ALL)     ALL
  ```

  在下面添加一行

  ```
  git     ALL=(ALL)       ALL
  ```

保存退出后改回权限：`chmod 400 /etc/sudoers`

- 然后给新加的用户git设置权限，编辑/etc/passwd将：`git:x:1003:1003:,,,:/home/git:/bin/bash` 改成：`git:x:1003:1003:,,,:/home/git:/usr/bin/git-shell` 这样git就只能使用git-shell而不能使用bash。
- **git服务器打开RSA认证**
  vim /etc/ssh/sshd_config
  在sshd_config中开启以下几项：

```
RSAAuthentication yes
PubkeyAuthentication yes
AuthorizedKeysFile  .ssh/authorized_keys
```

- 随后设置Git用户的密码

```
#需要root权限
sudo passwd git
```

### 3. 配置ssh

切换到git目录下，创建 ~/.ssh 文件夹和 ~/.ssh/authorized_keys 文件，并赋予相应的权限

```
cd ~/home/git
mkdir ~/.ssh
vim ~/.ssh/authorized_keys
#然后将电脑中执行 cat ~/.ssh/id_rsa.pub | pbcopy ,将公钥复制粘贴到authorized_keys
chmod 600 ~/.ssh/authorzied_keys
chmod 700 ~/.ssh
```

- 然后就可以执行ssh 命令测试是否可以免密登录`ssh -v git@SERVER` 至此，Git用户添加完成。



### 4. 创建仓库

执行命令：`sudo git init --bare hexo.git`

> 使用–bare 参数，Git 就会创建一个裸仓库，裸仓库没有工作区，我们不会在裸仓库上进行操作，它只为共享而存在。

改变 hexo.git 目录的拥有者为git用户：`sudo chown -R git:git hexo.git`

### 5. 自动化部署

创建一个新的 Git 钩子，用于自动部署在 /git/hexo.git 下，有一个自动生成的 hooks 文件夹。我们需要在里边新建一个新的钩子文件 post-receive。

```
vim /git/hexo.git/hooks/post-receive
```



按 i 键进入文件的编辑模式，在该文件中添加两行代码（将下边的代码粘贴进去)，指定 Git 的工作树（源代码）和 Git 目录（配置文件等）

```
#!/bin/bash
git --work-tree=/www/wwwroot/hexo --git-dir=/git/hexo.git checkout -f
```

然后，按 Esc 键退出编辑模式，输入”:wq” 保存退出。

修改文件权限，使得其可执行

```
chown -R git:git git/hexo.git/hooks/post-receive
chmod +x git/hexo.git/hooks/post-receive
```
到这里，我们的 Git 仓库算是完全搭建好了。下面进行 Nginx 的配置。
### 6. 安装nginx

为了适合小白安装部署和后期网站服务器的扩展性，选用宝塔面板来一键部署Nginx
Linux面板6.0安装命令(暂时仅兼容Centos7.x，其它系统版本请安装5.9稳定版)：

```
yum install -y wget && wget -O install.sh http://download.bt.cn/install/install_6.0.sh && bash install.sh
```

Linux面板6.0升级专业版

```
curl http://download.bt.cn/install/update6.sh|bash
```

安装完成后会显示面板后台地址·账号·密码。打开面板后台地址登陆面板（可能需要开放某一端口例如8888），选择Nginx安装，静静等待部署。

部署完成，点击网站-添加站点-输入域名(没有域名的输入自己的IP地址)-底部的PHP版本选择”纯静态”(其他不改或者根据自己的习惯来改)-提交。

![建立网站](https://cdn.jsdelivr.net/gh/Flionay/pic_bed@master/Upic/202005/I6vZyG.png)

网站创建完成后点击设置-配置nginx,开放80端口；

![Nginx配置](https://cdn.jsdelivr.net/gh/Flionay/pic_bed@master/Upic/202005/ewtdzB.png)

## 本地配置

hexo 根目录下的 _config.yml 文件，找到 deploy。

```

deploy:
  type: git
  repo: 
    #github: https://github.com/xxxx/xxx.github.io.git
    #coding: https://git.coding.net/xxx/xxx.git
    server: git@100.1.1.100:/home/git/repo/blog.git
  branch: master
```

然后我们就可以执行`hexo cl && hexo g && hexo d`来部署到云服务器上的git空目录里，然后`hook`会自动部署到我们设置的网站根目录，这样我们就可以通过IP:80来访问到我们的网站，如果域名备案成功，可以绑定域名，解析道我们云服务器的IP即可。

