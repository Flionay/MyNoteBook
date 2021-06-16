## 安装

1. 安装[node.js](https://nodejs.org/en/)
2. 安装hexo

```shell
node -v
npm -v
sudo su
npm install -g cnpm --registry=https://registry.npm.taobao.org
cnpm install -g hexo-cli
hexo -v
```

3.使用

创建空文件夹例如`myhexo`

```shell
sh-3.2# cd myhexo
sh-3.2# sudo hexo init
INFO  Cloning hexo-starter https://github.com/hexojs/hexo-starter.git
Cloning into '/Users/ay/Desktop/myhexo'...
remote: Enumerating objects: 30, done.
remote: Counting objects: 100% (30/30), done.
remote: Compressing objects: 100% (24/24), done.
remote: Total 161 (delta 12), reused 12 (delta 4), pack-reused 131
Receiving objects: 100% (161/161), 31.79 KiB | 23.00 KiB/s, done.
Resolving deltas: 100% (74/74), done.
Submodule 'themes/landscape' (https://github.com/hexojs/hexo-theme-landscape.git) registered for path 'themes/landscape'
Cloning into '/Users/ay/Desktop/myhexo/themes/landscape'...
remote: Enumerating objects: 4, done.        
remote: Counting objects: 100% (4/4), done.        
remote: Compressing objects: 100% (4/4), done.        
Receiving objects:  59% (635/1067), 2.96 MiB | 6.00 KiB/s 

```

如果遇到这个问题

`WARN Failed to install dependencies. Please run 'npm install' manually!`

重新运行`cnpm install`

知道最后clone完成，有如下信息，则表示初始化博客成功！

```shell
INFO  Start blogging with Hexo!
```

# 本地运行

```shell
hexo s
INFO  Start processing
INFO  Hexo is running at http://localhost:4000 . Press Ctrl+C to stop.
```

## Themes

去Hexo官网[主题列表](https://hexo.io/themes/)寻找喜欢的主题，clone到themes文件夹下

```shell
cd themes
git clone https://github.com/ppoffice/hexo-theme-icarus.git themes/icarus
```

