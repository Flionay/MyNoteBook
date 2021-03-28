

![](https://raw.githubusercontent.com/Flionay/myhugo/master/hugoblog/static/images/java_s.jpg)


## Java的 `Hello world`

```java
/**
可以用来自动创建文档的注释
*/

public class hello{
    public static void main(String[] args){
        //向屏幕输出文本
        System.out.println("hello world !")
            /* 多行注释开始
            注释content
            注释结束
            */
            
    }
}// class 定义结束
```

## 程序基本结构和程序规范

> 类名要求： 大写字母开头
>
> `public`是访问修饰符，表示该`class`公开的，不写的话，外部不能使用
>
> 这里的方法是`main`  返回值是`void` 表示没有任何返回值
>
> 方法也需要修饰词，而关键字`static`是另一种修饰符，表示静态方法
>
> java程序入口规定的方法必须是静态方法，方法名为`main`,括号内的参数必须是`String`数组
>
> 方法名的命名是首字母小写

**在方法内部，语句才是真正的执行代码。Java的每一行语句必须以分号结束：**

## 注释

```java
// 单行注释
/*
多行注释
*/

/** 
* 用来生成注释文档
*标题
*第一章
*
*/
```

## 变量和数据类型

```java
//int x = 1;
// 定义并打印变量
public class Main{
    public static void innt(String[] args){
        int x = 100;
        System.out.println(x)
    }
}

```

```java
public class Main {
    public static void main(String[] args) {
        int n = 100; // 定义变量n，同时赋值为100
        System.out.println("n = " + n); // 打印n的值

        n = 200; // 变量n赋值为200
        System.out.println("n = " + n); // 打印n的值

        int x = n; // 变量x赋值为n（n的值为200，因此赋值后x的值也是200）
        System.out.println("x = " + x); // 打印x的值

        x = x + 100; // 变量x赋值为x+100（x的值为200，因此赋值后x的值是200+100=300）
        System.out.println("x = " + x); // 打印x的值
        System.out.println("n = " + n); // 再次打印n的值，n应该是200还是300？
   }
}
/**
*int x =100 之后，第二次不需要int 因为x 已经存在 只要x = 200
*/

```

### 基本数据类型

基本数据类型是CPU可以直接进行运算的类型。Java定义了以下几种基本数据类型：

- 整数类型：byte，short，int，long
- 浮点数类型：float，double
- 字符类型：char
- 布尔类型：boolean

Java定义的这些基本数据类型有什么区别呢？要了解这些区别，我们就必须简单了解一下计算机内存的基本结构。

计算机内存的最小存储单元是字节（byte），一个字节就是一个8位二进制数，即8个bit。它的二进制表示范围从`00000000`~`11111111`，换算成十进制是0~255，换算成十六进制是`00`~`ff`。

内存单元从0开始编号，称为内存地址。每个内存单元可以看作一间房间，内存地址就是门牌号。

```ascii
  0   1   2   3   4   5   6  ...
┌───┬───┬───┬───┬───┬───┬───┐
│   │   │   │   │   │   │   │...
└───┴───┴───┴───┴───┴───┴───┘
```

一个字节是1byte，1024字节是1K，1024K是1M，1024M是1G，1024G是1T。一个拥有4T内存的计算机的字节数量就是：

```
4T = 4 x 1024G
   = 4 x 1024 x 1024M
   = 4 x 1024 x 1024 x 1024K
   = 4 x 1024 x 1024 x 1024 x 1024
   = 4398046511104
```

不同的数据类型占用的字节数不一样。我们看一下Java基本数据类型占用的字节数：

```ascii
       ┌───┐
  byte │   │
       └───┘
       ┌───┬───┐
 short │   │   │
       └───┴───┘
       ┌───┬───┬───┬───┐
   int │   │   │   │   │
       └───┴───┴───┴───┘
       ┌───┬───┬───┬───┬───┬───┬───┬───┐
  long │   │   │   │   │   │   │   │   │
       └───┴───┴───┴───┴───┴───┴───┴───┘
       ┌───┬───┬───┬───┐
 float │   │   │   │   │
       └───┴───┴───┴───┘
       ┌───┬───┬───┬───┬───┬───┬───┬───┐
double │   │   │   │   │   │   │   │   │
       └───┴───┴───┴───┴───┴───┴───┴───┘
       ┌───┬───┐
  char │   │   │
       └───┴───┘
```

`byte`恰好就是一个字节，而`long`和`double`需要8个字节。

#### 整型

对于整型类型，Java只定义了带符号的整型，因此，最高位的bit表示符号位（0表示正数，1表示负数）。各种整型能表示的最大范围如下：

- byte：-128 ~ 127
- short: -32768 ~ 32767
- int: -2147483648 ~ 2147483647
- long: -9223372036854775808 ~ 9223372036854775807

我们来看定义整型的例子：

```java
public class Main {
    public static void main(String[] args) {
        int i = 2147483647;
        int i2 = -2147483648;
        int i3 = 2_000_000_000; // 加下划线更容易识别
        int i4 = 0xff0000; // 十六进制表示的16711680
        int i5 = 0b1000000000; // 二进制表示的512
        long l = 9000000000000000000L; // long型的结尾需要加L
    }
}
```

**特别注意**：同一个数的不同进制的表示是完全相同的，例如`15`=`0xf`＝`0b1111`。

#### 浮点型

```java
float f1 = 3.14f;  //float 类型需要加f后缀
float f2 = 3.14e38f;
double d=1.79e308;
double d1 = -1.79e308;
double d2 = 4.9e-324;
```

#### 布尔类型

```java
boolean b1 = true;
boolean b2 =false;
boolean isGreater = 5>3;
int age =12;
boolean isAdult = age >18;

```

#### 字符类型

```java
public class Main {
    public static void main(String[] argfs) {
        char a = 'A';
        char zh = '中';
        System.out.println(a);
        System.out.println(zh);
    }
}

```

> **单引号**，表示`'char'`
>
> **双引号**，表示`"string"`

#### 常量

定义变量的时候，如果加上`final`修饰符，这个变量就变成了常量：

```java
final double PI = 3.14; // PI是一个常量
double r = 5.0;
double area = PI * r * r;
PI = 300; // compile error!
```

常量在定义时进行初始化后就不可再次赋值，再次赋值会导致编译错误。

常量的作用是用有意义的变量名来避免魔术数字（Magic number），例如，不要在代码中到处写`3.14`，而是定义一个常量。如果将来需要提高计算精度，我们只需要在常量的定义处修改，例如，改成`3.1416`，而不必在所有地方替换`3.14`。

根据习惯，**常量名通常全部大写**。

#### Var 关键字

### 

有些时候，类型的名字太长，写起来比较麻烦。例如：

```
StringBuilder sb = new StringBuilder();
```

这个时候，如果想省略变量类型，可以使用`var`关键字：

```
var sb = new StringBuilder();
```

编译器会根据赋值语句自动推断出变量`sb`的类型是`StringBuilder`。对编译器来说，语句：

```
var sb = new StringBuilder();
```

实际上会自动变成：

```
StringBuilder sb = new StringBuilder();
```

因此，使用`var`定义变量，仅仅是少写了变量类型而已。

> 万物皆对象，变量也是有类型的



> java 中的{} 是用来控制程序模块的  相当于Python的缩进
>
> 同时 {} 也控制着变量的作用域

### 整数运算

### 布尔运算

```java
boolean isGreater = 5>3; //true
int age =12;
boolean isZero = age ==0; //false
boolean isNonzero = !isZero; 
boolean isAdult = age >= 18;
boolean isTeenager =age >6 && age<18;
```

运算符的优先级从高到低依次是：

- `!`
- `>`，`>=`，`<`，`<=`
- `==`，`!=`
- `&&`
- `||`

布尔运算的一个重要特点是短路运算，

### 数组类型



### 流程控制
#### 输入和输出
```java
public class Main{
    public static void main(String[],args){
        System.out.print("A,");
        System.out.print("B,");
        System.out.println("换行输出")
    }
}



```

**格式化输出**
```java
public class Main{
    public static void main(String[] args){
        doubole d = 1290000;
        System.out.println(d); //1.29E6
        System.out.printf("%.2f\n",d)
        System.out.printf("%.4f\n",d)
    }
}
```
Java的格式化功能提供了多种占位符，可以把各种数据类型“格式化”成指定的字符串：

占位符	说明
%d	格式化输出整数
%x	格式化输出十六进制整数
%f	格式化输出浮点数
%e	格式化输出科学计数法表示的浮点数
%s	格式化字符串
注意，由于%表示占位符，因此，连续两个%%表示一个%字符本身。