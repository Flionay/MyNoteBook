## 1. 简介

**JavaScript**（简称“JS”） 是一种具有[函数](https://baike.baidu.com/item/函数/301912)优先的[轻量级](https://baike.baidu.com/item/轻量级/22359343)，解释型或即时编译型的**高级**[**编程语言**](https://baike.baidu.com/item/编程语言/9845131)。虽然它是作为开发Web页面的[脚本语言](https://baike.baidu.com/item/脚本语言/1379708)而出名的，但是它也被用到了很多非浏览器环境中，JavaScript 基于原型[编程](https://baike.baidu.com/item/编程/139828)、多范式的动态脚本语言，并且支持[面向对象](https://baike.baidu.com/item/面向对象/2262089)、命令式和声明式（如[函数式编程](https://baike.baidu.com/item/函数式编程/4035031)）风格。

JavaScript在1995年由[Netscape](https://baike.baidu.com/item/Netscape)公司的[Brendan Eich](https://baike.baidu.com/item/Brendan Eich)，在[网景导航者](https://baike.baidu.com/item/网景导航者/10404300)浏览器上首次设计实现而成。因为Netscape与[Sun](https://baike.baidu.com/item/Sun/69463)合作，Netscape管理层希望它外观看起来像[Java](https://baike.baidu.com/item/Java/85979)，因此取名为JavaScript。但实际上它的语法风格与[Self](https://baike.baidu.com/item/Self/4959923)及[Scheme](https://baike.baidu.com/item/Scheme)较为接近。

​       布兰登·艾奇（Brendan Eich，1961年～），[JavaScript](https://baike.baidu.com/item/JavaScript)的发明人，2005年至2014年期间，在[Mozilla](https://baike.baidu.com/item/Mozilla)公司担任首席技术长（Chief Technology Officer）。出任Mozilla的CEO十天就被迫辞职。

在本地运行的浏览器脚本语言。Node.js 服务端开发，应用很广。![img](https://cdn.nlark.com/yuque/0/2020/png/2637180/1602157418615-b4e07461-e828-4435-bd68-c9be161c3f7f.png)

#### 浏览器怎么执行JS？

浏览器中有渲染引擎和Js引擎，JavaScript需要js引擎来编译执行，chrome中的V8就是JS引擎。

#### JS的组成

![img](https://cdn.jsdelivr.net/gh/Flionay/pic_bed@master/Upic/202106/1616546772193-1401197d-128e-42dc-a325-016ef21be7ea.jpeg)



JavaScript是世界上最流行的脚本语言。

==一个合格的后端人员必须精通JavaScript==

最新版本已经到es6版本，但是大部分浏览器只停留在支持es5代码上！

开发环境 -- 线上环境，版本不一致。

## 2. 快速入门

### 2.1 引入js

1. 内部标签

```javascript
<script>
 //....
</script>
```

2. 外部引入

```js
<script src='example.js'></script>
```

> 有外部js文件引入的时候，内嵌的js代码将不会被执行。
>
> 如果js有比较耗时的复杂操作，建议将其放到body标签的最下面。

### 2.2 基本语法

浏览器调试：

![image](https://cdn.jsdelivr.net/gh/Flionay/pic_bed@master/Upic/202107/image-20210701163418251.png)

### 2.3 数据类型

数值，文本，图形，音频，视频

1. 变量声明

   JS中的变量是若类型，可以保存所有类型的数据，即变量没有类型而值有类型。变量名以字母、$、_ 开始，后跟字母、数字、_。

==var==

```js
var web = 1
console.log(typeof web) //number
web = 'js'
console.log(typeof web) // string
web = {'code':"js"}
console.log(typeof web) // object
```

==numbe==

​	`js`不区分小数和整数，Number

```js
123
123.1
1.23e3
-99
NaN
Infinity 
```

==字符串==

​	`abc` "abc"

```js
<script>
    // 字符串
    let web = "昂一"
  console.log(web)

  // 多行字符串        
  web = `Hello
  world
  !`
  console.log(web)

  // 模版字符串
  web = "Angyi"
  let h = `Hello ${web}`
  console.log(h)

  // 字符串属性
  console.log(web.length) //5
  console.log(web[0]) //A

  // 字符串不可变
  web[0]="1"
  console.log(web) //Angyi

  // 字符串方法 
  console.log(web.toLowerCase())
  console.log(web.toUpperCase())
  console.log(web.indexOf("g"))  // 2
  console.log(web.substring(0,3)) // Ang

</script>
```

==布尔值==

true , false

==逻辑运算==

```js
&& 
||
!
```

==比较运算符==

```
=
== 等于 （类型不一样，值一样，也会判断为true）
=== 绝对等于（类型一样，值一样，才会为true）
```

坚持不要使用`==`进行比较

NaN不能用等号进行判断，只能用isNull()判断。

尽量避免使用浮点数进行运算，存在精度问题。

==null  undifined==

==数组==

可以允许数组中不相同的对象存在一个数组中，不会数组越界，超过索引会索引到undefined。

```js
    <script>
        var arr = [1,2,3,4,5,6]

        console.log(arr[1])     // 2
        console.log(arr.length) // 6
        console.log(arr.indexOf(3)) // 2
        console.log(arr.indexOf("3")) // -1

        // slice 截取一部分
        console.log(arr.slice(3,5))   // [4,5]

        // push() , pop()  尾部增加和删除
        console.log(arr.push('a','b'))
        console.log(arr.pop('b'))
        console.log(arr)  //[1, 2, 3, 4, 5, 6, "a"]

        // unshitf() shift() 头部增加和删除
        console.log(arr.shift(1))
        console.log(arr)  //[2, 3, 4, 5, 6, "a"]

        // sort() reverse()
        console.log(arr.sort())
        console.log(arr.reverse())

        // concat()   
        console.log(arr.concat(['d','x'])) //返回一个新数组 ["a", 6, 5, 4, 3, 2, "d", "x"]

        // join 拼接符
        // 多维数组
        
    </script>
```

==对象==

每个属性之间使用逗号隔开，最后一个不需要，类似于python的字典。

```javascript
<script>
  var person ={
  name:"angyi",
  age:3,
  email:"angyi_jq@163.com"
  } // 键都是字符串

  console.log(person.age);

  person.age = 18;
  console.log(person.age); //18

  // 随意删减对象属性
  delete person.email;
  person.sex = "male";
  console.log(person.sex);

  // 判断对象是否有某个属性
  console.log("age" in person) //true

</script>
```

==map set== 

ES6的新特性

```js
<script>
  let book = new Map([["two","java编程思想"],["three","javascript"]]);
  book.set("one","平凡的世界")
  //获取
  console.log(book.get("two"));

  // 循环读取
  for (let [key,value] of book){
    h=`${key}=${value}`;
    console.log(h);
  }
</script>
```

```JS
<script>
  let mySet = new Set();
  mySet.add("one");
  mySet.add(1)

  let o = {q:1,b:2};
  mySet.add(o)

  for(let item of mySet){
    console.log(item);
  }

</script>
```



### 2.4 严格检查模式

Idea - languages&frameworks - JavaScript - ECMAScript 6

## 3. 函数

### 3.1 函数定义和调用

函数局部变量，内部可以访问外部，外部不能访问内部变量。

```js
var y = 2;
function qj(){
    var x=1;
    console.log(x+y);

}
qj()
// console.log(x)
```



```js
<script>
    function abs(x){
        if(x>0){
            return x;
        }else{
            return -x;
        }
    }
    console.log(abs(-10))

    function app_add(x,y,z){
        return x+y;
    }
    
    console.log(app_add(1,2)) //参数不全同样可以调用
</script>
```

> `JavaScript` 函数很灵活，调用参数多和少都可以调用成功。

`arguments`是`js`指向当前函数的参数的一个关键字；利用这个关键字可以拿到调用函数所用的参数，即使函数没有定义任何形式参数。

```js
function foo(x) {
  	console.log(arguments.length) 
    console.log('x = ' + x); 
    for (var i=0; i<arguments.length; i++) {
        console.log('arg ' + i + ' = ' + arguments[i]); 
    }
}
foo(10, 20, 30);

// 3
// x=10
// 10, 20, 30
```

ES6引入了新特性，`rest`关键字用来获取除了定义的参数以外的其他所有参数；

### 3.2 变量作用域

**变量提升**: 

js使用`var`声明变量会提前解析，并将变量声明提前，而赋值语句还是停留在原位。由于JavaScript的这一怪异的“特性”，我们在函数内部定义变量时，请严格遵守“在函数内部首先申明所有变量”这一规则。

ES6标准引入了新的关键字`const`来定义常量，`const`与`let`都具有块级作用域。

==全局变量==会绑定到window上，js实际上只有这一个全局作用域，任何变量都会在函数局部作用域进行查找，然后去window全局作用域查找，找不到就会报错。

不同函数有同名的内部变量，不受影响；函数内外都有同名变量，优先内部变量，屏蔽外部变量；函数内部可以访问外部，外部不能访问内部。

```js
var x='xxx';
console.log(x);
console.log(window.x)
```

> 规范：由于所有的全局变量都会绑定到window上。如果不同的js文件，使用了相同的全局变量，会产生冲突。

可以利用对象来解决这个问题，将需要的变量定义在一个对象中。把自己的代码用到的变量放到自定义唯一的空间名字中，解决变量冲突的问题。

```js
<script>
    var myapp = {};
    myapp.name = 'xxx';
    myapp.add = function(a,b){
        return a+b
    }
</script>
```

==局部变量==

使用`let`声明，必须先声明后使用，这是正常逻辑。为了解决块级作用域，ES6引入了新的关键字`let`，用`let`替代`var`可以申明一个块级作用域的变量。

```js
function app(){
    for(let i=0;i<100;i++){
        console.log(i);
    }
   // console.log(i+1); //报错
}
app();
```

==常量==

```js
const pi = 3.14 //readonly
```

### 3.3 方法

方法就是把函数放在对象里面

```js
var app={
    name:"qq",
    birth:2005,
    age:function(){
        var now = new Date().getFullYear();
        return now-this.birth;
    }
}

console.log(app.birth);
console.log(app.age());

```

