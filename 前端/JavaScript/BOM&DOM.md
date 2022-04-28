# BOM

# BOM

浏览器对象模型(browser object model)
BOM可以使我们通过JS来操作浏览器
在BOM中为我们提供了一组对象，用来完成对浏览器的操作
BOM对象
Window
 代表的是整个浏览器的窗口，同时window也是网页中的全局对象
Navigator
 代表的当前浏览器的信息，通过该对象可以来识别不同的浏览器
Location
 代表当前浏览器的地址栏信息，通过Location可以获取地址栏信息，或者操作浏览器跳转页面
History
 代表浏览器的历史记录，可以通过该对象来操作浏览器的历史记录
	由于隐私原因，该对象不能获取到具体的历史记录，只能操作浏览器向前或向后翻页
	而且该操作只在当次访问时有效
Screen
 代表用户的屏幕的信息，通过该对象可以获取到用户的显示器的相关的信息

这些BOM对象在浏览器中都是作为window对象的属性保存的，
可以通过window对象来使用，也可以直接使用

## Navigator

 代表的当前浏览器的信息，通过该对象可以来识别不同的浏览器
 由于历史原因，Navigator对象中的大部分属性都已经不能帮助我们识别浏览器了
 一般我们只会使用userAgent来判断浏览器的信息，
	userAgent是一个字符串，这个字符串中包含有用来描述浏览器信息的内容，
	不同的浏览器会有不同的userAgent

火狐的userAgent
Mozilla5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko20100101 Firefox50.0

Chrome的userAgent
Mozilla5.0 (Windows NT 6.1; Win64; x64) AppleWebKit537.36 (KHTML, like Gecko) Chrome52.0.2743.82 Safari537.36

IE8
Mozilla4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)

IE9
Mozilla5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)

IE10
Mozilla5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)

IE11
Mozilla5.0 (Windows NT 6.1; WOW64; Trident7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; rv:11.0) like Gecko
 在IE11中已经将微软和IE相关的标识都已经去除了，所以我们基本已经不能通过UserAgent来识别一个浏览器是否是IE了

```javascript
alert(navigator.appName);

var ua = navigator.userAgent;

console.log(ua);

if(firefoxi.test(ua)){
alert("你是火狐！！！");
}else if(chromei.test(ua)){
alert("你是Chrome");
}else if(msiei.test(ua)){
alert("你是IE浏览器~~~");
}else if("ActiveXObject" in window){
alert("你是IE11，枪毙了你~~~");
}
```

## History

 对象可以用来操作浏览器向前或向后翻页	
length
 属性，可以获取到当成访问的链接数量
back()
 可以用来回退到上一个页面，作用和浏览器的回退按钮一样	
forward()
 可以跳转下一个页面，作用和浏览器的前进按钮一样	
go()
 可以用来跳转到指定的页面
 它需要一个整数作为参数
	1:表示向前跳转一个页面 相当于forward()
	2:表示向前跳转两个页面
	-1:表示向后跳转一个页面
	-2:表示向后跳转两个页面

## Location

 该对象中封装了浏览器的地址栏的信息	
如果直接打印location，则可以获取到地址栏的信息（当前页面的完整路径）
alert(location);
如果直接将location属性修改为一个完整的路径，或相对路径
则我们页面会自动跳转到该路径，并且会生成相应的历史记录
location = "http:www.baidu.com";
location = "01.BOM.html";
assign()
 用来跳转到其他的页面，作用和直接修改location一样	
reload()
 用于重新加载当前页面，作用和刷新按钮一样
 如果在方法中传递一个true，作为参数，则会强制清空缓存刷新页面
location.reload(true);	
replace()
 可以使用一个新的页面替换当前页面，调用完毕也会跳转页面
	不会生成历史记录，不能使用回退按钮回退

## window

###定时器

**setInterval()**
 定时调用
 可以将一个函数，每隔一段时间执行一次
 参数：
	1.回调函数，该函数会每隔一段时间被调用一次
	2.每次调用间隔的时间，单位是毫秒

 返回值：
	返回一个Number类型的数据
	这个数字用来作为定时器的唯一标识
**clearInterval()可以用来关闭一个定时器**
方法中需要一个定时器的标识作为参数，这样将关闭标识对应的定时器 

clearInterval()可以接收任意参数，
	如果参数是一个有效的定时器的标识，则停止对应的定时器
	如果参数不是一个有效的标识，则什么也不做

```javascript
var num = 1;
var timer = setInterval(function() {
	count.innerHTML = num++;
	if(num == 11) {
		//关闭定时器
		clearInterval(timer);
	}
}, 1000);
```

### 延时调用

**setTimeout**

延时调用一个函数不马上执行，而是隔一段时间以后在执行，而且只会执行一次
延时调用和定时调用的区别，定时调用会执行多次，而延时调用只会执行一次
延时调用和定时调用实际上是可以互相代替的，在开发中可以根据自己需要去选择

var timer = setTimeout(function(){
console.log(num++);
},3000);

使用clearTimeout()来关闭一个延时调用
clearTimeout(timer);

#类的操作

**直接修改元素的类css：**

通过style属性来修改元素的样式，每修改一个样式，浏览器就需要重新渲染一次页面。 这样的执行的性能是比较差的，而且这种形式当我们要修改多个样式时，也不太方便 我希望一行代码，可以同时修改多个样式

我们可以通过修改元素的class属性来间接的修改样式.这样一来，我们只需要修改一次，即可同时修改多个样式，浏览器只需要重新渲染页面一次，性能比较好，
并且这种方式，可以使表现和行为进一步的分离

```javascript
box.className += " b2";	//注意有空格，添加class属性
```

```javascript
//定义一个函数，用来向一个元素中添加指定的class属性值
/*
 * 参数:
 * 	obj 要添加class属性的元素
 *cn 要添加的class值
 * 	
 */
function addClass(obj, cn) {
	if (!hasClass(obj, cn)) {
		obj.className += " " + cn;
	}
}
/*
 * 判断一个元素中是否含有指定的class属性值
 * 	如果有该class，则返回true，没有则返回false
 * 	
 */
function hasClass(obj, cn) {
	var reg = new RegExp("\\b" + cn + "\\b");
	return reg.test(obj.className);
}
/*
 * 删除一个元素中的指定的class属性
 */
function removeClass(obj, cn) {
	//创建一个正则表达式
	var reg = new RegExp("\\b" + cn + "\\b");
	//删除class
	obj.className = obj.className.replace(reg, "");
}
/*
 * toggleClass可以用来切换一个类
 * 	如果元素中具有该类，则删除
 * 	如果元素中没有该类，则添加
 */
function toggleClass(obj , cn){	
	//判断obj中是否含有cn
	if(hasClass(obj , cn)){
		//有，则删除
		removeClass(obj , cn);
	}else{
		//没有，则添加
		addClass(obj , cn);
	}
}
```

## 

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



# DOM

Document Object Model
文档对象模型，通过DOM可以来任意来修改网页中各个内容
文档
 文档指的是网页，一个网页就是一个文档
对象
 对象指将网页中的每一个节点都转换为对象
	转换完对象以后，就可以以一种纯面向对象的形式来操作网页了
模型
 模型用来表示节点和节点之间的关系，方便操作页面
节点（Node）
 节点是构成网页的最基本的单元，网页中的每一个部分都可以称为是一个节点
 虽然都是节点，但是节点的类型却是不同的
 常用的节点
	 文档节点 （Document），代表整个网页
	 元素节点（Element），代表网页中的标签
	 属性节点（Attribute），代表标签中的属性
	 文本节点（Text），代表网页中的文本内容
	

## DOM操作

 DOM查询
 在网页中浏览器已经为我们提供了**document对象**，
	**它代表的是整个网页，它是window对象的属性，可以在页面中直接使用。**
 document查询方法：
	 根据元素的id属性查询一个元素节点对象：
		 document.getElementById("id属性值");
	 根据元素的name属性值查询一组元素节点对象:
		 document.getElementsByName("name属性值");
	 根据标签名来查询一组元素节点对象：
		 document.getElementsByTagName("标签名");
		
 元素的属性：
	 **读取元素的属性：**
		语法：元素.属性名
		例子：ele.name
			ele.id
			ele.value 
			ele.className
			注意：class属性不能采用这种方式，
			**读取class属性时需要使用 元素.classNam**e	 

修改元素的属性：
	语法：元素.属性名 = 属性值
	
 innerHTML
	 使用该属性可以获取或设置元素内部的HTML代码

## 事件（Event）

 事件指的是用户和浏览器之间的交互行为。比如：点击按钮、关闭窗口、鼠标移动。。。
 我们可以为事件来绑定回调函数来响应事件。
 绑定事件的方式：
	1.可以在标签的事件属性中设置相应的JS代码
		例子：

```javascript
<button onclick="js代码。。。">按钮</button>
```

2.可以通过为对象的指定事件属性设置回调函数的形式来处理事件
	例子：

```javascript
<button id="btn">按钮</button>
<script>
var btn = document.getElementById("btn");
btn.onclick = function(){

};
</script>
```

文档的加载
 浏览器在加载一个页面时，是按照自上向下的顺序加载的，加载一行执行一行。
 如果将js代码编写到页面的上边，当代码执行时，页面中的DOM对象还没有加载，
	此时将会无法正常获取到DOM对象，导致DOM操作失败。
 解决方式一：
	 可以将js代码编写到body的下边
	

```javascript
<body>
		<button id="btn">按钮</button>

		<script>
			var btn = document.getElementById("btn");
			btn.onclick = function(){
		
			};
	</script>
</body>
```

 解决方式二：
	 将js代码编写到window.onload = function(){}中
	 window.onload 对应的回调函数会在整个页面加载完毕以后才执行，
		所以可以确保代码执行时，DOM对象已经加载完毕了		

```javascript
<script>
window.onload = function(){
var btn = document.getElementById("btn");
btn.onclick = function(){
};
};
</script>	
```

## DOM查询

通过具体的元素节点来查询
元素.getElementsByTagName()
通过标签名查询当前元素的指定后代元素

**子节点包括便签元素中的文本，子元素自包含标签元素**

元素.childNodes
 获取当前元素的**所有子节点**
 **会获取到空白的文本子节点**

childNodes属性会获取包括文本节点在呢的所有节点
根据DOM标签标签间空白也会当成文本节点
注意：在IE8及以下的浏览器中，不会将空白文本当成子节点，
	所以该属性在IE8中会返回4个子元素而其他浏览器是9个

元素.children
 获取当前元素的**所有子元素**

元素.firstChild
 获取当前元素的**第一个子节点**，会获取到空白的文本子节点

元素.lastChild
 获取当前元素的**最后一个子节点**

元素.parentNode
 获取当前元素的父元素

元素.previousSibling
 获取当前元素的前一个兄弟节点

previousElementSibling获取前一个兄弟元素，IE8及以下不支持

元素.nextSibling
 获取当前元素的后一个兄弟节点

firstElementChild获取当前元素的第一个子元素
 firstElementChild不支持IE8及以下的浏览器，
	如果需要兼容他们尽量不要使用

innerHTML和innerText
这两个属性并没有在DOM标准定义，但是大部分浏览器都支持这两个属性
两个属性作用类似，都可以获取到标签内部的内容，
**不同是innerHTML会获取到html标签，而innerText会自动去除标签**
如果使用这两个属性来设置标签内部的内容时，没有任何区别的	

**读取标签内部的文本内容**

</h1>h1中的文本内容</h1>

元素.firstChild.nodeValue

## document对象的其他的属性和方法

document.all
 **获取页面中的所有元素**，相当于document.getElementsByTagName("*");

document.documentElement
 **获取页面中html根元素**

document.body
 获取页面中的body元素

document.getElementsByClassName()
 **根据元素的class属性值查询一组元素节点对象**
 这个方法不支持IE8及以下的浏览器

document.querySelector()
 **根据CSS选择器去页面中查询一个元素**
 如果匹配到的元素有多个，则它会返回查询到的第一个元素	

document.querySelectorAll()	
 根据CSS选择器去页面中查询一组元素
 会将匹配到所有元素封装到一个数组中返回，即使只匹配到一个

##DOM修改

document.createElement("TagName")
	可以用于创建一个元素节点对象，
	它需要一个标签名作为参数，将会根据该标签名创建元素节点对象，
	并将创建好的对象作为返回值返回
document.createTextNode("textContent")
可以根据文本内容创建一个文本节点对象

**父节点.appendChild(子节点)**
向父节点中添加指定的子节点
**父节点.insertBefore(新节点,旧节点)**
 将一个新的节点插入到旧节点的前边
父节点.replaceChild(新节点,旧节点)
 使用一个新的节点去替换旧节点

**父节点.removeChild(子节点)**
 删除指定的子节点
推荐方式：**子节点.parentNode.removeChild(子节点)**

**以上方法，实际就是改变了相应元素（标签）的innerHTML的值。**

```javascript
myClick("btn07",function(){
//向city中添加广州
var city = document.getElementById("city");

/*
	* 使用innerHTML也可以完成DOM的增删改的相关操作
	* 一般我们会两种方式结合使用
	*/
//city.innerHTML += "<li>广州</li>";

//创建一个li
var li = document.createElement("li");
//向li中设置文本
li.innerHTML = "广州";
//将li添加到city中
city.appendChild(li);

});
```

## DOM对CSS的操作

### 读取和修改内联样式

使用style属性来操作元素的内联样式
	读取内联样式：
	语法：元素.style.样式名
例子：
	元素.style.width
	元素.style.height
	注意：**如果样式名中带有-，则需要将样式名修改为驼峰命名法将-去掉，然后后的字母改大写**
	比如：backgroundcolor > backgroundColor
	borderwidth > borderWidth
修改内联样式：
语法：元素.style.样式名 = 样式值
 **通过style修改和读取的样式都是内联样式**，由于内联样式的优先级比较高，
	所以我们通过JS来修改的样式，往往会立即生效，
	**但是如果样式中设置了!important，则内联样式将不会生效。**
	

### 读取元素的当前样式

正常浏览器
 **使用getComputedStyle()**
 这个方法是window对象的方法，可以返回一个对象，这个对象中保存着当前元素生效样式
 参数：
	1.要获取样式的元素
	2.可以传递一个伪元素，一般传null
 例子：
	获取元素的宽度
		getComputedStyle(box , null)["width"];
 通过该方法读取到样式都是只读的不能修改

IE8
 **使用currentStyle**
 语法：
	元素.currentStyle.样式名
 例子：
	box.currentStyle["width"]
 通过这个属性读取到的样式是只读的不能修改

**实现兼容性**

//对象.属性不存在，不会报错，如果直接寻找对象，（当前作用域到全局作用域）找不到会报错

```javascript
/*
* 定义一个函数，用来获取指定元素的当前的样式
* 参数：
* 		obj 要获取样式的元素
* 		name 要获取的样式名
*/
function getStyle(obj , name){
//对象.属性不存在，不会报错，如果直接寻找对象，（当前作用域到全局作用域）找不到会报错
if(window.getComputedStyle){
//正常浏览器的方式，具有getComputedStyle()方法
return getComputedStyle(obj , null)[name];
}else{
//IE8的方式，没有getComputedStyle()方法
return obj.currentStyle[name];
}
//return window.getComputedStyle?getComputedStyle(obj , null)[name]:obj.currentStyle[name];			
}
```

### 其他的样式相关的属性

注意：以下样式都是只读的,未指明偏移量都是相对于当前窗口左上角

clientHeight
 元素的可见高度，包括元素的内容区和内边距的高度
clientWidth
 元素的可见宽度，包括元素的内容区和内边距的宽度
offsetHeight
 整个元素的高度，包括内容区、内边距、边框
offfsetWidth
 整个元素的宽度，包括内容区、内边距、边框
offsetParent
 当前元素的定位父元素
 离他最近的开启了定位的祖先元素，如果所有的元素都没有开启定位，则返回body
offsetLeft
offsetTop
 当前元素和定位父元素之间的偏移量
 offsetLeft水平偏移量offsetTop垂直偏移量

scrollHeight
scrollWidth
 获取元素滚动区域的高度和宽度

scrollTop
scrollLeft
 获取元素垂直和水平滚动条滚动的距离

判断滚动条是否滚动到底
 垂直滚动条
	scrollHeight -scrollTop = clientHeight
	
 水平滚动	
	scrollWidth -scrollLeft = clientWidth	



# 
