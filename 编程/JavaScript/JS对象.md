# Date

> 标准对象

```js
typeof(123)
"number"
typeof '12'
"string"
typeof NAN
"undefined"
typeof NaN
"number"
typeof {}
"object"
typeof Math.abs
"function"
typeof undefined
"undefined"
```

# Json

json是一种轻量级的数据交换格式。具有简洁和清晰的层次结构。易于机器解析和生成，有效提高网络的传输效率。

在js中一切皆对象，任何js支持的类型都可以用json来表示。

对象都用{}；数组都有[];所有的键值对都用key:value;

```js
let user={
    name:'lll',
    age:24,
    sex:'male'}
//undefined
user.age
//24
var jsonUser = JSON.stringify(user)
//undefined
console.log(jsonUser)
//VM803:1 {"name":"lll","age":24,"sex":"male"}

JSON.parse('{"name":"lll","age":24,"sex":"male"}')
//{name: "lll", age: 24, sex: "male"}age: 24name: "lll"sex: "male"_cg_keys: 
```

# 面向对象

```js
<script>
    var person={
        name:'name',
        age:12,
        run:function (){
            console.log(this.name+"run.....");
        }
    }

    var xiaoming={
        name:"xiaoming"
    }

    xiaoming.__proto__ = person;
    console.log(xiaoming.run())
</script>
```

```js
<script>
    function Student(name){
        this.name = name;
    }

    //给student新增一个方法
    Student.prototype.hello = function(){
        alert('Hello');
    }

    //ES6 之后
    // 定义一个学生类
    class Student{
        constructor(name) {
            this.name = name;
        }

        hello(){
            alert('Hello');
        }
    }
</script>
```





