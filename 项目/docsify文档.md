# 利用docsify生成文档网站

> 点击**博客右上角[文档阅读](https://doc.angyi.online/#/)**即可体验

![image-20211103164538056](https://pic-1300286858.cos.ap-nanjing.myqcloud.com/uPic/2021-11/image-20211103164538056.png)

> 下面的简介摘抄自docsify的官网 [https://docsify.js.org](https://docsify.js.org/) 中的简介

**docsify**是一个神奇的文档网站生成器。他可以快速帮你生成文档网站。不同于`GitBook`、`Hexo`的地方是它不会生成静态的`.html`文件，所有转换工作都是在运行时。如果你想要开始使用他，只需要创建一个`index.html`就可以开始编写文档并直接部署在`GitHub Pages`（码云`Pages`、阿某云`OSS`或者鹅云`COS`等等）。它的主要特性如下：

- 无需构建，写完文档直接发布（运行时`markdown`文档转换）
- 容易使用并且轻量（压缩后 ~21kB，当然这里不包括`markdown`文档的大小）
- 智能的全文搜索
- 丰富的`API`
- 支持`Emoji`，可以在文中添加表情
- 兼容`IE11`
- 支持服务端渲染`SSR`

**docsify**的最大优势是可以让使用者感受到**用写博客的姿势去编写文档，反过来说也行：用写文档的姿势去写博客**。`docsify`的学习成本很低，部署简单，官方文档十分完善，原则上只需要理解`markdown`的语法和`Node.js`的安装即可，对于非`IT`技术从业者也十分友好。知名的技术公众号号主**JavaGuide**的站点就是采用`docsify`构建的。

## 安装 初始化

根据官网教程来即可，比较简单。需要`node` 和`npm` 环境.

https://docsify.js.org/#/?id=docsify
```bash
# 安装
npm i docsify-cli -g    

# 初始化项目
cd YourDocDir
docsify init ./docs # 初始化里面的docs目录，放文章

```

初始化成功后，可以看到 `./docs` 目录下创建的几个文件

- `index.html` 入口文件
- `README.md` 会做为主页内容渲染
- `.nojekyll` 用于阻止 GitHub Pages 忽略掉下划线开头的文件

直接编辑 `docs/README.md` 就能更新文档内容，当然也可以[添加更多页面](https://docsify.js.org/#/zh-cn/more-pages)。

```bash
docsify serve docs # 本地启动服务 预览
```

## 配置侧边栏目录

为了获得侧边栏，您需要创建自己的_sidebar.md，你也可以自定义加载的文件名。默认情况下侧边栏会通过 Markdown 文件自动生成，效果如当前的文档的侧边栏。首先配置 `loadSidebar` 选项，具体配置规则见[配置项#loadSidebar](https://docsify.js.org/#/zh-cn/configuration?id=loadsidebar)。

```html
<!-- index.html -->

<script>
  window.$docsify = {
    loadSidebar: true
  }
</script>
<script src="//cdn.jsdelivr.net/npm/docsify/lib/docsify.min.js"></script>
```

接着创建 `_sidebar.md` 文件，内容如下

```markdown
<!-- docs/_sidebar.md -->

* [首页](zh-cn/)
* [指南](zh-cn/guide)
```

需要在 `./docs` 目录创建 `.nojekyll` 命名的空文件，阻止 GitHub Pages 忽略命名是下划线开头的文件。

复制我们的markdown文件到docs里面，利用generate命令生成sidebar.md 

```bash
docsify generate path # 会在path目录下生成 _sidebar.md 	文件
```



如果将所有的目录都这样配置到最外层的`_sidebar.md` ，会很乱，像这样：

<img src="/Users/angyi/Library/Application Support/typora-user-images/image-20220401143302383.png" alt="image-20220401143302383" style="zoom:50%;" />

我们希望浏览一个目录时，只显示这个目录自己的侧边栏，这可以通过每个文件夹中都添加一个`_sidebar.md` 文件来实现

## 部署

推荐github page，giteepage，腾讯云静态网站托管。

如果你有备案好的域名，一定要利用好二级域名，可以构建多个网址哦！

利用github自动部署到腾讯静态托管，可参考：

https://cloud.tencent.com/document/product/1210/52636





![image-20211103172354047](https://pic-1300286858.cos.ap-nanjing.myqcloud.com/uPic/2021-11/image-20211103172354047.png)
