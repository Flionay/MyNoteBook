

# Hugo博客迁移Hexo

## 记录Hugo博客2.0

Hugo的优点就是基于Go语言开发，生成静态文件速度很快。随着用户量的增加，主题也逐渐多样，也就造成了参差不齐的主题水平，一个集合所有功能，而且美观的主题一直没有找到。图片主题是基于Allinone的，自己也进行了很多优化，添加了一些功能，如果想要用Hugo的朋友可以去借鉴我的Hugo标签文章，记录了优化过程。

![首页](https://cdn.jsdelivr.net/gh/Flionay/pic_bed@master/Upic/202005/首页.png)

![内容](https://cdn.jsdelivr.net/gh/Flionay/pic_bed@master/Upic/202005/内容.png)



![底部](https://cdn.jsdelivr.net/gh/Flionay/pic_bed@master/Upic/202005/底部.png)



![归档](https://cdn.jsdelivr.net/gh/Flionay/pic_bed@master/Upic/202005/归档.png)

![书籍系列](https://cdn.jsdelivr.net/gh/Flionay/pic_bed@master/Upic/202005/书籍系列.png)

## Hexo

本着折腾的精神，又迁移到了Hexo,不同于Hugo，Hexo活跃时间更长，社区用户量基数大，所以有各种各样的主题，功能全优化好。

至于Hexo的搭建，我就不重复造轮子了，百度一搜很多教程，配置也比较简单。

至于主题，本博客主题是matery，想要使用本主题或者对matery进行相关优化可以参考这些链接。

1. [主题作者 闪烁之狐](https://blinkfox.github.io/2018/09/28/qian-duan/hexo-bo-ke-zhu-ti-zhi-hexo-theme-matery-de-jie-shao/)

2. [主题优化 Hongxing](https://sunhwee.com/)
3. [搭建和优化步骤全解析](https://yafine-blog.cn/)

参考他们的博客搭建步骤以及优化博文，就可以搭建完美个人博客了。
### busuanzi插件不显示问题
跟着他们的配置优化过程都挺流畅，但是有一点他们都没有写到，就是busuanzi可能会显示不出来的问题，我找到了如下解决方案，记录一下。

首先是将不蒜子的js插件保存到本地，我的主题中位于`\themes\hexo-theme-matery\source\libs\others\busuanzi.pure.mini.js`。

```js
var bszCaller,bszTag;!function(){var c,d,e,a=!1,b=[];ready=function(c){return a||"interactive"===document.readyState||"complete"===document.readyState?c.call(document):b.push(function(){return c.call(this)}),this},d=function(){for(var a=0,c=b.length;c>a;a++)b[a].apply(document);b=[]},e=function(){a||(a=!0,d.call(window),document.removeEventListener?document.removeEventListener("DOMContentLoaded",e,!1):document.attachEvent&&(document.detachEvent("onreadystatechange",e),window==window.top&&(clearInterval(c),c=null)))},document.addEventListener?document.addEventListener("DOMContentLoaded",e,!1):document.attachEvent&&(document.attachEvent("onreadystatechange",function(){/loaded|complete/.test(document.readyState)&&e()}),window==window.top&&(c=setInterval(function(){try{a||document.documentElement.doScroll("left")}catch(b){return}e()},5)))}(),bszCaller={fetch:function(a,b){var c="BusuanziCallback_"+Math.floor(1099511627776*Math.random());window[c]=this.evalCall(b),a=a.replace("=BusuanziCallback","="+c),scriptTag=document.createElement("SCRIPT"),scriptTag.type="text/javascript",scriptTag.defer=!0,scriptTag.src=a,document.getElementsByTagName("HEAD")[0].appendChild(scriptTag)},evalCall:function(a){return function(b){ready(function(){try{a(b),scriptTag.parentElement.removeChild(scriptTag)}catch(c){bszTag.hides()}})}}},bszCaller.fetch("//busuanzi.ibruce.info/busuanzi?jsonpCallback=BusuanziCallback",function(a){bszTag.texts(a),bszTag.shows()}),bszTag={bszs:["site_pv","page_pv","site_uv"],texts:function(a){this.bszs.map(function(b){var c=document.getElementById("busuanzi_value_"+b);c&&(c.innerHTML=a[b])})},hides:function(){this.bszs.map(function(a){var b=document.getElementById("busuanzi_container_"+a);b&&(b.style.display="")})},shows:function(){this.bszs.map(function(a){var b=document.getElementById("busuanzi_container_"+a);b&&(b.style.display="inline")})}
```



操作其实就是把其中的b.style.display="none"中none去掉。
