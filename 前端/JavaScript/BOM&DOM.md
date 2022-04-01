# BOM

B/S browser object module

操作浏览器对象

**常用对象**

1. window对象

   代表浏览器窗口

   ```js
   window.alert()
   window.innerHeight
   window.outerHeight
   ```

2. navigator

   封装了浏览器的信息

   ```javas	
   navigator.appName
   navigator.appVersion
   navigator.userAgent
   ```

3. screen

   屏幕属性

   ```javas	
   screen.width
   screem.height
   ```

4. location

   location代表当前页面的url信息

   ```js
   Location {ancestorOrigins: DOMStringList, href: 'https://www.bilibili.com/video/BV1JJ41177di?p=19', origin: 'https://www.bilibili.com', protocol: 'https:', host: 'www.bilibili.com', …}ancestorOrigins: DOMStringList {length: 0}assign: ƒ assign()hash: ""host: "www.bilibili.com"hostname: "www.bilibili.com"href: "https://www.bilibili.com/video/BV1JJ41177di?p=19"origin: "https://www.bilibili.com"pathname: "/video/BV1JJ41177di"port: ""protocol: "https:"reload: ƒ reload()replace: ƒ replace()search: "?p=19"toString: ƒ toString()valueOf: ƒ valueOf()Symbol(Symbol.toPrimitive): undefined[[Prototype]]: Location
   ```

5. document

   document代表当前的页面，html Dom树

   能够获取具体的dom节点，从而进行动态修改，将js与html结合起来。

   ```
   document.cookie
   ```

6. history

   记录浏览器历史记录，可以实现前进后退



## 操作DOM

由于HTML文档被浏览器解析后就是一棵DOM树，要改变HTML的结构，就需要通过JavaScript来操作DOM。

始终记住DOM是一个树形结构。操作一个DOM节点实际上就是这么几个操作：

- 更新：更新该DOM节点的内容，相当于更新了该DOM节点表示的HTML的内容；
- 遍历：遍历该DOM节点下的子节点，以便进行进一步操作；
- 添加：在该DOM节点下新增一个子节点，相当于动态增加了一个HTML节点；
- 删除：将该节点从HTML中删除，相当于删掉了该DOM节点的内容以及它包含的所有子节点。

在操作一个DOM节点前，我们需要通过各种方式先拿到这个DOM节点。最常用的方法是`document.getElementById()`和`document.getElementsByTagName()`，以及CSS选择器`document.getElementsByClassName()`。

由于ID在HTML文档中是唯一的，所以`document.getElementById()`可以直接定位唯一的一个DOM节点。`document.getElementsByTagName()`和`document.getElementsByClassName()`总是返回一组DOM节点。要精确地选择DOM，可以先定位父节点，再从父节点开始选择，以缩小范围。

### 更新DOM

获取到标签对象后，可以利用某些方法直接对标签进行更新。
