# CSS

## 1. 主要内容

1. css是什么

2. css怎么用（快速入门）

3. **CSS选择器（重点+难点）**

4. 美化网页 （文字，阴影，超链接，列表，渐变......）

5. 盒子模型

6. 浮动

7. 定位

8. 网页动画（特效效果）

## 2. 基本入门

**Cascading Stule Sheet 层叠级联样式表**

Css : 表现 美化网页

字体，颜色，边距，高度，宽度，背景图片，网页定位，网页浮动。。。

![6yxUNS](https://cdn.jsdelivr.net/gh/Flionay/pic_bed@master/Upic/202103/6yxUNS.jpg)

## 3. 快速入门

### css style 基本入门

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Title</title>
    <!-- 规范，<style> 可以编写css的代码，每一个声明，都用分号结尾 可以直接写在html文件中
        语法： 
            选择器{
                声明1；
                声明2；
                声明3；
            }
    -->
   
    <style> 
        h1{
            color: red;
        }
    </style>

</head>

<body>
    <h1>这是标题</h1>
</body>

</html>
```

![内容表现分离](https://cdn.jsdelivr.net/gh/Flionay/pic_bed@master/Upic/202103/OzteFw.png)

css 的优势：

1. 内容和表现分离

2. 网页结构表现统一，可以复用 

3. 样式十分的丰富

4. 建议使用独立语html的css文件

5. 利用SEO，容易被搜索引擎收录！

### css的导入方式

```HTML
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="en">
        <title>Title</title>

        <!-- 内部样式 -->
        <style>
            h1{
                color: red;
            }
        </style>

        <!-- 外部样式 -->
        <link rel="stylesheet" href="css/style.css">
    </head>
<body>
    <!-- 优先级 行内样式>内部样式>外部样式 -->
    
    <!-- 优先级 就近原则 -->
    
    <!-- 行内样式，在标签元素内直接编写一个style属性 -->
    <h1 style="color: green;">这是标题</h1>

</body>
</html>
```

## 4. 选择器

> 作用：选择页面上的某一个活着某一类元素

#### 4.1 基本选择器

1. **标签选择器**：选择一类标签 标签{}

2. **类 选择器** ： 选择所有具有class属性的标签，可以复用 .class{}

3. **id选择器**：全局唯一，一对一 #id{}

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>

    <style>
    /*id 选择器*  id必须保证全局唯一！/
    /*#id 名称{}*/
    /*优先级不遵循就近原则*/
    /*ID选择器>类选择器>标签选择器*/

    #first{
        color: #b0146a;
    }
    .second{
        color: aqua;
    }
    h1{
        color: black;
    }
    </style>
</head>
<body>
<h1 id="first">标题1</h1>
<h2 class="second">标题2</h2>
<h3>标题3</h3>


</body>
</html>
```

> 优先级:  *ID选择器>类选择器>标签选择器*

#### 4.2 高级选择器

1. **后代选择器**：在某个元素的后面   

```CSS
/*    后代选择器*/
body p{
    background: #b0146a;
}
```

1. **子选择器**：只有一代

```CSS
/*    子选择器*/
body>p{
    background: black;
}
```

1. **相邻兄弟选择器**

```CSS
/*    相邻兄弟选择器：只有下面这个邻居 */
.active+p{
    background: azure;
}
```

1. **通用选择器**

```CSS
/*  通用兄弟选择器 当前选中元素的乡下的所有元素*/
.active ~ p {
    background: #2424c0;
}
```

#### 4.3 结构伪类选择器

伪类:相当于

```CSS
/*ul的第一个子元素*/

ul li:first-child{
    background: blue;
}
/*ul的最后一个子元素*/
ul li:last-child{
    background: burlywood;
}
/*    定位父元素，选择当前的第一个元素*/
    p:nth-child(1){
        background: aqua;
    }
/*    选中父元素下，下的P元素中的第二个，选择根据类型选择*/
    p:nth-of-type(2){
        background: blueviolet;
    }
```

#### 4.4 属性选择器(常用)

id + class 结合

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .demo a{
            float: left;
            display: block;
            height: 50px;
            width:50px;
            border-radius: 10px;
            background: blue;
            text-align: center;
            margin-right: 5px;
            font: bold 20px/50px Arial;
            color: aliceblue;
            text-decoration: none;
        }

    /*    存在id属性的元素*/
    /*    a[属性名/属性名=属性值（正则）]{ }*/
    /*     = 绝对等于
           *= 包含
            ^= 以这个开头
            $= 以这个结尾


    */
    /*    a[id]{*/
    /*        background: yellow;*/
    /*    }*/
    /*    */
        a[id=first]{
            background: green;
        }

        a[class*=links]{
            background: yellow;}

    /*    选中href中以http开头的元素*/
        a[href^=http]{
            background: #b0146a;
        }

        a[href$=doc]{
            background: blueviolet;
        }
    </style>
</head>
<body>
<p class="demo">
        <a href="http://www.baidu.com" class="links item first" id="first">1</a>
        <a href="http://blog.kuangstudy.com" class="links item active" target="_blank" title="test">2</a>
        <a href="images/123.html" class="links item">3</a>
        <a href="images/123.png" class="links item">4</a>
        <a href="images/123.jpg" class="links item">5</a>
        <a href="abc" class="links item">6</a>
        <a href="/a.pdf" class="links item">7</a>
        <a href="/abc.pdf" class="links item">8</a>
        <a href="abc.doc" class="links item">9</a>
        <a href="abcd.doc" class="links item last">10</a>
</p>

</body>
</html>
```

![RGEwK3](https://cdn.jsdelivr.net/gh/Flionay/pic_bed@master/Upic/202104/RGEwK3.png)

## 5. 美化网页元素

###  为什么要美化网页

1、有效的传递页面信息
2、美化网页，页面漂亮，才能吸引人
3、凸显页面的主题
4、提高用户体验


### span标签：重点要突出的字，使用span标签套起来

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        #title{
            font-size: 50px;
        }
    </style>
</head>
<body>


欢迎学习<span id="title">Java</span>
</body>
</html>
```

### 字体样式

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <!-- 
        font-family: 字体
        font-size : 
        font-weight:
        color:
     -->
    <style>
        body{
            font-family: 'Times New Roman', 楷体;
            font-weight: lighter;
        }

        h1{
            font-size:35px;
        }

        p{
            background-color:honeydew;
            color: hotpink;
        }
    </style>
</head>
<body>
    <h1>LSTM</h1>

    <p>图中空心小圆圈表示矩阵对应元素相乘，又称为Hadamard乘积。这种LSTM结构我们也可以称之为FC-LSTM，因其内部门之间是依赖于类似前馈式神经网络来计算的，而这种FC-LSTM对于时序数据可以很好地处理，但是对于空间数据来说，将会带来冗余性，原因是空间数据具有很强的局部特征，但是FC-LSTM无法刻画此局部特征。本文提出的ConvLSTM尝试解决此问题，做法是将FC-LSTM中input-to-state和state-to-state部分由前馈式计算替换成卷积的形式，</p>
    <p>ConvLSTM的内部结构如下图所示：</p>
    
</body>
</html>
```

### 文本样式

1. 颜色
2. 文本对齐的方式
3. 首行缩进
4. 行高
5. 装饰
6. 文本图片水平对齐

### 超链接伪类

```html
<style>
    a{
        text-decoration: none;
        color: #000000;
    }
    a:hover{
        color:orange;

    }
</style>
```

### 列表

```css
#nav{
    height:500px;
    width:300px;
    
}

.title{
    font-size: 13;
    font-weight: bold;
    text-indent: 1em;
    line-height: 30px;
    color:red;
    background-color: darkgreen;
}
/* ul li */

/* 
list style
none 去掉圆点
circle 空心圆
decimal 数字
*/

ul li {
    height:30px;
    list-style: decimal;
}
a{
    text-decoration: none;
    font-size: 14px;
    color: black;
}

a:hover {
    color: hotpink;
    text-decoration: underline;
}

```

### 背景

```css
<style> 
    div{
        border: 1px solid red;
        width:500px;
        height:500px;
        background-image: url("images/b.png")
    }
    .div1{
        background-repeat: no-repeat;
    }
    .div2{
        background-repeat: repeat-y;
    }
</style>

```

### 背景和渐变

https://uigradients.com/#BackToEarth

### 盒子模型

![6hwHHi](https://cdn.jsdelivr.net/gh/Flionay/pic_bed@master/Upic/202105/6hwHHi.png)
margin : 外边距
padding : 内边距
border : 边框


### 浮动

块级元素：独占一行，

```html
h1-h6 p div li... 
```

行内元素：

```html
span a img strong...
```

## 6. 定位- position属性

`position`属性规定应用于元素的定位方法的类型（static relative fixed absolute或 sticky）。

元素其实是使用top、 bottom、left、right、属性定位的。但是，必须要首先设置position属性，否则上下左右不起作用。因为根据不同的定位方式，上下左右起作用的方式不同。

1. `position: static` 

   是默认的定位方式，**静态**定位方式。该属性不会受到 top、right、bottom 和 left 属性的影响，始终根据页面的正常流进行定位。

2. `positon: relative`

   该属性**相对**于其正常位置进行定位。设置相对定位的元素的 top、right、bottom 和 left 属性将导致其偏离其正常位置进行调整。

3. `position: fixed`

   **固定**定位：这意味着即使滚动页面，他也始终位于同一位置。 top、right、bottom 和 left 属性用于定位此元素。

4. `positon: absolute`

   **绝对定位**：相对于最近的上一级单元进行定位。如果没有上一级，那么使用body进行绝对定位，随页面一起移动。

   但是要注意：绝对定位相对于最近position不为static的父级元素来定位的。

5. `positon: sticky`

   position: sticky; 的元素根据用户的滚动位置进行定位。

   粘性元素根据滚动位置在相对（relative）和固定（fixed）之间切换。起先它会被相对定位，直到在视口中遇到给定的偏移位置为止 - 然后将其“粘贴”在适当的位置（比如 position:fixed）。

