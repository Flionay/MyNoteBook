# MyBatis

![img](https://cdn.jsdelivr.net/gh/flionay/pic_bed//PicGo/7896890-d2f3f8fbccb13196.png)

## 什么是 MyBatis？

MyBatis 是一款优秀的**持久层**框架，它支持自定义 SQL、存储过程以及高级映射。MyBatis 免除了几乎所有的 JDBC 代码以及设置参数和获取结果集的工作。MyBatis 可以通过简单的 XML 或注解来配置和映射原始类型、接口和 Java POJO（Plain Old Java Objects，普通老式 Java 对象）为数据库中的记录。

MyBatis 本是apache的一个开源项目iBatis, 2010年这个项目由apache software foundation 迁移到了google code，并且改名为MyBatis，是一个基于Java的持久层框架。

- **持久层：** 可以将业务数据**存储到磁盘，具备长期存储能力**，只要磁盘不损坏，在断电或者其他情况下，重新开启系统仍然可以读取到这些数据。
- **优点：** 可以**使用巨大的磁盘空间**存储相当量的数据，并且很**廉价**
- **缺点：慢**（相对于内存而言）

## 为什么使用 MyBatis

在我们**传统的 JDBC 中**，我们除了需要自己提供 SQL 外，还必须操作 Connection、Statment、ResultSet，不仅如此，为了访问不同的表，不同字段的数据，我们需要些很多雷同模板化的代码，闲的**繁琐又枯燥**。

而我们在使用了 **MyBatis** 之后，**只需要提供 SQL 语句就好了**，其余的诸如：建立连接、操作 Statment、ResultSet，处理 JDBC 相关异常等等都可以交给 MyBatis 去处理，我们的**关注点于是可以就此集中在 SQL 语句上**，关注在增删改查这些操作层面上。

并且 MyBatis 支持使用简单的 XML 或注解来配置和映射原生信息，将接口和 Java 的 POJOs(Plain Old Java Objects,普通的 Java对象)映射成数据库中的记录。

## HelloWorld

1. 构建基本的Maven项目，引入依赖[我这里加入了springboot项目]

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
   	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
   	<modelVersion>4.0.0</modelVersion>
   
   	<parent>
   		<groupId>org.springframework.boot</groupId>
   		<artifactId>spring-boot-starter-parent</artifactId>
   		<version>2.5.3</version>
   		<relativePath/> <!-- lookup parent from repository -->
   	</parent>
   
   
   	<groupId>com.angyi</groupId>
   	<artifactId>springBoot</artifactId>
   	<version>0.0.1-SNAPSHOT</version>
   	<name>springBoot</name>
   	<description>springBoot</description>
   
   
   	<properties>
   		<java.version>1.8</java.version>
   	</properties>
   
   
   	<dependencies>
   		<dependency>
   			<groupId>mysql</groupId>
   			<artifactId>mysql-connector-java</artifactId>
   			<version>8.0.22</version>
   		</dependency>
   		<dependency>
   			<groupId>org.springframework.boot</groupId>
   			<artifactId>spring-boot-starter-web</artifactId>
   		</dependency>
   
   		<dependency>
   			<groupId>org.springframework.boot</groupId>
   			<artifactId>spring-boot-starter-test</artifactId>
   			<scope>test</scope>
   		</dependency>
   
   		<!--MyBatis依赖-->
   		<dependency>
   			<groupId>org.mybatis</groupId>
   			<artifactId>mybatis</artifactId>
   			<version>3.5.1</version>
   		</dependency>
   
   
   
   	</dependencies>
   
   	<build>
   		<plugins>
   			<plugin>
   				<groupId>org.springframework.boot</groupId>
   				<artifactId>spring-boot-maven-plugin</artifactId>
   			</plugin>
   		</plugins>
   
   		<resources>
   			<resource>
   				<directory>src/main/java</directory>
   				<includes>
   					<include>**/*.xml</include>
   				</includes>
   			</resource>
   		</resources>
   	</build>
   
   </project>
   ```

2. 构建数据库表，并成功测试连接IDEA；

      ![image-20210813174023167](/Users/ay/Library/Application Support/typora-user-images/image-20210813174023167.png)

3. 配置总的mybatis配置文件，路径在resources目录下；

   ```xml
   <?xml version="1.0" encoding="UTF-8" ?>
   <!DOCTYPE configuration
           PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
           "http://mybatis.org/dtd/mybatis-3-config.dtd">
   <configuration>
       <!--设置日志-->
       <!--
       <settings>
           <setting name="logImpl" value="STDOUT_LOGGING"/>
       </settings>-->
   
       <environments default="development">
           <environment id="development">
               <!--配置JDBC事务管理-->
               <transactionManager type="JDBC"/>
               <!--配置数据源：创建Connection对象-->
               <dataSource type="POOLED">
                   <!--driver：驱动内容-->
                   <property name="driver" value="com.mysql.jdbc.Driver"/>
                   <!--连接数据库的url-->
                   <property name="url" value="jdbc:mysql://localhost:3306/school?useUnicode=true&amp;characterEncoding=utf-8"/>
                   <!--用户名-->
                   <property name="username" value="root"/>
                   <!--密码-->
                   <property name="password" value="123456"/>
               </dataSource>
           </environment>
       </environments>
   
       <!--指定其他mapper文件的位置
           目的是找到其他mapper文件的sql语句
       -->
       <mappers>
           <!--使用mapper的resource属性指定mapper文件的路径
               这个路径是从target/classes路径开启的
               使用注意：resource="mapper"文件的路径，使用 / 分割路径
                       一个resource指定一个mapper文件
           -->
           <mapper resource="com/bjpowernode/dao/StudentDao.xml"/>
       </mappers>
   </configuration>
   ```

4. 构建实体类，与数据库表结构相关联，增删改查体现在java对象上，万物皆对象；

      ```java
      package com.angyi.springboot.entity;
      
      import java.util.Date;
      
      public class Student {
          private Integer id;
          private String name;
          private String pwd;
          private String sex;
          private Date birthday;
          private String address;
          private String email;
      
          public Integer getId() {
              return id;
          }
      
          public void setId(Integer id) {
              this.id = id;
          }
      
          public String getName() {
              return name;
          }
      
          public void setName(String name) {
              this.name = name;
          }
      
          public String getPwd() {
              return pwd;
          }
      
          public void setPwd(String pwd) {
              this.pwd = pwd;
          }
      
          public String getSex() {
              return sex;
          }
      
          public void setSex(String sex) {
              this.sex = sex;
          }
      
          public Date getBirthday() {
              return birthday;
          }
      
          public void setBirthday(Date birthday) {
              this.birthday = birthday;
          }
      
          public String getAddress() {
              return address;
          }
      
          public void setAddress(String address) {
              this.address = address;
          }
      
          public String getEmail() {
              return email;
          }
      
          public void setEmail(String email) {
              this.email = email;
          }
      
          public Student(Integer id, String name, String pwd, String sex, Date birthday, String address, String email) {
              this.id = id;
              this.name = name;
              this.pwd = pwd;
              this.sex = sex;
              this.birthday = birthday;
              this.address = address;
              this.email = email;
          }
      
          public Student() {
          }
      }
      ```

5. 创建sql语句的mapper，操控数据库；

      ```xml
      <?xml version="1.0" encoding="UTF-8" ?>
      <!DOCTYPE mapper
              PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
              "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
      
      <mapper namespace="com.angyi.springboot.Dao.StudentDao">
          <!--
          <select id="selectBlog" resultType="Blog">
              select * from Blog where id = #{id}
          </select>-->
          <insert id="insertStudent" parameterType="com.angyi.springboot.entity.Student">
                  insert into student(name,pwd,birthday,address,email) values (#{name},#{pwd},#{birthday},#{address},#{email})
          </insert>
      
          <!--查询一个学生Student
              <select>：表示查询操作，里面是select语句
              id：要执行的sql语句的唯一标识，是一个自定义字符串
                  推荐使用Dao接口中的方法名称
              resultType：告诉MyBatis，执行sql语句，把数据赋值给哪个类型的Java对象
                          推荐使用Java对象的全限定名称
              #{studentId}：占位符，表示从Java程序中传入过来的数据
          -->
          <select id="selectStudentById" resultType="com.angyi.springboot.entity.Student">
              select id,name,email,age from student where id=#{studentId}
          </select>
      </mapper>
      
      <!--
          1.约束文件
            http://mybatis.org/dtd/mybatis-3-mapper.dtd
            约束文件作用：定义和限制当前文件中可以使用的标签和属性，以及标签出现的顺序
          2.mapper是根标签
            namespace：命名空间，必须有值（唯一），不能为空。
                       推荐使用Dao接口的全限定名称
            作用：参与识别sql语句的作用
          3.在mapper里面可以写 <insert>,<update>,<delete>,<select>标签
            <insert>里面是 insert 语句，表示执行的是 insert 操作
            <update>里面是 update 语句，表示执行的是 update 操作
            <delete>里面是 delete 语句，表示执行的是 delete 操作
            <select>里面是 select 语句，表示执行的是 select 操作
      -->
      ```

6. 在用测试类调用一下

      ```java
      
      import com.angyi.springboot.entity.Student;
      import org.apache.ibatis.session.*;
      
      import java.io.InputStream;
      
      
      public class BatisTest {
          public static void main(String[] args) {
              InputStream config = BatisTest.class.getClassLoader().getResourceAsStream("mybatis.xml");
              System.out.println(config);
              SqlSessionFactory sqlSessionFactory = new SqlSessionFactoryBuilder().build(config);
              SqlSession sqlSession = sqlSessionFactory.openSession();
              Student student= new Student(1,"王武","rtesws","male", null,"shandong","email.com");
              String sql = "com.angyi.springboot.mapper.StudentDao.insertStudent";
              sqlSession.insert(sql,student);
              sqlSession.commit();
          }
      }
      
      ```

      ​	更新信息成功！

      ## 总结大体的步骤

      >创建 student 表（id，name，email，age）。
      >新建 Maven 项目。
      > 修改 pom.xml 。
      >  1）加入Maven依赖：MyBatis依赖、MySQL驱动、junit
      >
      >  2）在 <build> 中加入资源插件
      >
      >创建实体类 Student，定义属性（属性名和列名保持一致）。
      >创建 Dao 接口，定义操作数据库的方法。
      >创建 StudentDao.xml（mapper文件），写sql语句。
      >1）MyBatis框架推荐是把 Java 代码和 sql 语句分开
      >
      >2）mapper文件：定义在和 Dao接口同一个目录下，一个表一个mapper文件
      >
      >创建 MyBatis.xml 文件，放在 resources 目录下。
      >1）定义创建连接实例的数据源（DataSource）对象
      >
      >2）指定其他 mapper 文件的位置
      >
      >创建测试类
      >
      >1）可以使用 main 方法，测试访问数据库。
      >
      >2）也可以使用 junit 访问数据库。

## 编写Mybatis工具类

从上面的步骤我们可以总结出，就是变Dao层中接口的mapper文件中的sql语句即可，然后再总配置文件中注册。调用的时候根据总配置文件获取sqlsessionFactory，然后opensession，执行语句，执行哪条语句呢，根据总配置文件中注册的mapper，然后去利用命名空间和sqlid定位语句执行。

那么这里的获取sqlsession这部分代码其实是重复的，可以创建一个工具类。

> 工具类

```java
package com.angyi.springboot.utils;

import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

import java.io.InputStream;

public class MyBatisUtil {
    public static SqlSession getSqlSession(){
        SqlSession sqlSession = null;
        try {
            InputStream config = MyBatisUtil.class.getClassLoader().getResourceAsStream("mybatis.xml");
            SqlSessionFactory sqlSessionFactory = new SqlSessionFactoryBuilder().build(config);
            sqlSession = sqlSessionFactory.openSession();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return sqlSession;
    }

}

```

> Junit Test
>
> 这种调用接口的方式也是使用最多的，前面那种被抛弃了。

```java
package com.angyi.springboot.dao;

import com.angyi.springboot.entity.Student;
import com.angyi.springboot.utils.MyBatisUtil;
import org.apache.ibatis.session.SqlSession;
import org.junit.jupiter.api.Test;

import java.util.List;

public class StudentDaoTest {
    @Test
    public void getStudentListTest(){
        // 1. 获取sqlsession
        SqlSession sqlSession = MyBatisUtil.getSqlSession();
        //2. 获取mapper 执行sql
        StudentDao studentdao = sqlSession.getMapper(StudentDao.class); // 这里可以理解与mapper无关，
                                                                        // 就是调用接口对象，然后使用接口中的方法
        List<Student> list = studentdao.getStudentList();

        for (Student stu:list){
            System.out.println(stu.getName());
        }
        sqlSession.close();
    }

}
```

增删改查就是对应xml文件中的几个不同标签；

步骤：==1. 写接口 2. 写xml文件sql 3. 总config中注册xml 4. 调用接口方法（getmapper）==

## 配置解析

![image-20210814144331657](https://cdn.jsdelivr.net/gh/Flionay/pic_bed@master/Upic/202108/image-20210814144331657.png)

```xml
<environments default="development"> <!--选择环境-->
        <environment id="development">
            <!--配置JDBC事务管理-->
            <transactionManager type="JDBC"/>
            <!--配置数据源：创建Connection对象-->
            <dataSource type="POOLED">
                <!--driver：驱动内容-->
                <property name="driver" value="com.mysql.jdbc.Driver"/>
                <!--连接数据库的url-->
                <property name="url" value="jdbc:mysql://localhost:3306/school?useUnicode=true&amp;characterEncoding=utf-8&amp;useSSL=false"/>
                <!--用户名-->
                <property name="username" value="root"/>
                <!--密码-->
                <property name="password" value="123456"/>
            </dataSource>
        </environment>
    </environments>
```

mybatis默认过的事务管理器就是JDBC，连接池是POOLED

可以在mybatis-config.xml中引入外部配置文件；

```xml
<properties resource="db.properties"></properties>

<environments default="development">
  <environment id="development">
    <transactionManager type="JDBC"/>
    <dataSource type="POOLED">
      <!--driver：驱动内容-->
      <property name="driver" value="${driver}"/>
      <!--连接数据库的url-->
      <property name="url" value="${url}"/>
      <!--用户名-->
      <property name="username" value="${user}"/>
      <!--密码-->
      <property name="password" value="${pwd}"/>
    </dataSource>
  </environment>
```

### 别名

类型别名可为 Java 类型设置一个缩写名字。 它仅用于 XML 配置，意在降低冗余的全限定类名书写。

两种方式，一种在xml文件中协定alias，自己起个别名；另一种是制定一个包，java会自动搜索该包下的所有javabean，并将其小写作为别名 可以自己改，方法就是在实体类中增加注解@Alias("author")，这种方法真香；

### 映射器

既然 MyBatis 的行为已经由上述元素配置完了，我们现在就要来定义 SQL 映射语句了。 但首先，我们需要告诉 MyBatis 到哪里去找到这些语句。 在自动查找资源方面，Java 并没有提供一个很好的解决方案，所以最好的办法是直接告诉 MyBatis 到哪里去找映射文件。 你可以使用相对于类路径的资源引用，或完全限定资源定位符（包括 `file:///` 形式的 URL），或类名和包名等。例如：

```
<!-- 使用相对于类路径的资源引用 -->
<mappers>
  <mapper resource="org/mybatis/builder/AuthorMapper.xml"/>
  <mapper resource="org/mybatis/builder/BlogMapper.xml"/>
  <mapper resource="org/mybatis/builder/PostMapper.xml"/>
</mappers>

<!-- 使用完全限定资源定位符（URL） -->
<mappers>
  <mapper url="file:///var/mappers/AuthorMapper.xml"/>
  <mapper url="file:///var/mappers/BlogMapper.xml"/>
  <mapper url="file:///var/mappers/PostMapper.xml"/>
</mappers>

<!-- 使用映射器接口实现类的完全限定类名 -->
<mappers>
  <mapper class="org.mybatis.builder.AuthorMapper"/>
  <mapper class="org.mybatis.builder.BlogMapper"/>
  <mapper class="org.mybatis.builder.PostMapper"/>
</mappers>

<!-- 将包内的映射器接口实现全部注册为映射器 -->
<mappers>
  <package name="org.mybatis.builder"/>
</mappers>
```

这些配置会告诉 MyBatis 去哪里找映射文件；方式一是最推荐的，方式二不推荐，方式三和四必须保证mapper文件和接口类名称同名。

### 作用域（Scope）和生命周期

理解我们之前讨论过的不同作用域和生命周期类别是至关重要的，因为错误的使用会导致非常严重的并发问题。

------

**提示** **对象生命周期和依赖注入框架**

依赖注入框架可以创建线程安全的、基于事务的 SqlSession 和映射器，并将它们直接注入到你的 bean 中，因此可以直接忽略它们的生命周期。 如果对如何通过依赖注入框架使用 MyBatis 感兴趣，可以研究一下 MyBatis-Spring 或 MyBatis-Guice 两个子项目。

------

#### SqlSessionFactoryBuilder

这个类可以被实例化、使用和丢弃，一旦创建了 SqlSessionFactory，就不再需要它了。 因此 SqlSessionFactoryBuilder 实例的最佳作用域是方法作用域（也就是局部方法变量）。 你可以重用 SqlSessionFactoryBuilder 来创建多个 SqlSessionFactory 实例，但最好还是不要一直保留着它，以保证所有的 XML 解析资源可以被释放给更重要的事情。

#### SqlSessionFactory

SqlSessionFactory 一旦被创建就应该在应用的运行期间一直存在，没有任何理由丢弃它或重新创建另一个实例。 使用 SqlSessionFactory 的最佳实践是在应用运行期间不要重复创建多次，多次重建 SqlSessionFactory 被视为一种代码“坏习惯”。因此 SqlSessionFactory 的最佳作用域是应用作用域。 有很多方法可以做到，最简单的就是使用单例模式或者静态单例模式。

#### SqlSession

每个线程都应该有它自己的 SqlSession 实例。SqlSession 的实例不是线程安全的，因此是不能被共享的，所以它的最佳的作用域是请求或方法作用域。 绝对不能将 SqlSession 实例的引用放在一个类的静态域，甚至一个类的实例变量也不行。 也绝不能将 SqlSession 实例的引用放在任何类型的托管作用域中，比如 Servlet 框架中的 HttpSession。 如果你现在正在使用一种 Web 框架，考虑将 SqlSession 放在一个和 HTTP 请求相似的作用域中。 换句话说，每次收到 HTTP 请求，就可以打开一个 SqlSession，返回一个响应后，就关闭它。 这个关闭操作很重要，为了确保每次都能执行关闭操作，你应该把这个关闭操作放到 finally 块中。 下面的示例就是一个确保 SqlSession 关闭的标准模式：

```
try (SqlSession session = sqlSessionFactory.openSession()) {
  // 你的应用逻辑代码
}
```

在所有代码中都遵循这种使用模式，可以保证所有数据库资源都能被正确地关闭。

#### 映射器实例

映射器是一些绑定映射语句的接口。映射器接口的实例是从 SqlSession 中获得的。虽然从技术层面上来讲，任何映射器实例的最大作用域与请求它们的 SqlSession 相同。但方法作用域才是映射器实例的最合适的作用域。 也就是说，映射器实例应该在调用它们的方法中被获取，使用完毕之后即可丢弃。 映射器实例并不需要被显式地关闭。尽管在整个请求作用域保留映射器实例不会有什么问题，但是你很快会发现，在这个作用域上管理太多像 SqlSession 的资源会让你忙不过来。 因此，最好将映射器放在方法作用域内。就像下面的例子一样：

```
try (SqlSession session = sqlSessionFactory.openSession()) {
  BlogMapper mapper = session.getMapper(BlogMapper.class);
  // 你的应用逻辑代码
}
```

## 结果集映射

## 日志

1. 日志工厂

   如果一个数据库操作异常，我们需要查看sql语句排除错误；

   Mybatis 通过使用内置的日志工厂提供日志功能。内置日志工厂将会把日志工作委托给下面的实现之一：

   - SLF4J
   - Apache Commons Logging
   - Log4j 2
   - Log4j
   - JDK logging

   可以通过在 MyBatis 配置文件 mybatis-config.xml 里面添加一项 setting 来选择其它日志实现。

   ```xml
   <configuration>
     <settings>
       ...
       <setting name="logImpl" value="LOG4J"/>
       ...
     </settings>
   </configuration>
         
   ```

- 现在maven中导入包

- 编写log4j.properties 	文件

  ```properties
  #将等级为DEBUG的日志信息输出到console和file这两个目的地，console和file的定义在下面的代码
  log4j.rootLogger=DEBUG,console,file
  
  #控制台输出的相关设置
  log4j.appender.console = org.apache.log4j.ConsoleAppender
  log4j.appender.console.Target = System.out
  log4j.appender.console.Threshold=DEBUG
  log4j.appender.console.layout = org.apache.log4j.PatternLayout
  log4j.appender.console.layout.ConversionPattern=[%c]-%m%n
  
  #文件输出的相关设置
  log4j.appender.file = org.apache.log4j.RollingFileAppender
  log4j.appender.file.File=./log/shun.log
  log4j.appender.file.MaxFileSize=10mb
  log4j.appender.file.Threshold=DEBUG
  log4j.appender.file.layout=org.apache.log4j.PatternLayout
  log4j.appender.file.layout.ConversionPattern=[%p][%d{yy-MM-dd}][%c]%m%n
  
  #日志输出级别
  log4j.logger.org.mybatis=DEBUG
  log4j.logger.java.sql=DEBUG
  log4j.logger.java.sql.Statement=DEBUG
  log4j.logger.java.sql.ResultSet=DEBUG
  log4j.logger.java.sql.PreparedStatement=DEBUG
  ```

```java
Static Logger logger = Logger.getLogger(UserDaoTest.class);
logger.info()
```

## 分页

为什么要分页：

```sql
SELECT * FROM user limit 0,2 #每页显示两个 从第0开始查
SELECT * FROM user limit 2 #[0,n]
```

**分页插件**

## 使用注解

面向接口编程 ==解耦==

还有一种方式可以避免xml配置文件的繁琐，如果只有简单的sql语句，可以将sql语句注解到接口类中的方法上，适用于简单sql场景。

在接口方法中可以@param（）定义参数名，方便后面调用；#{}安全，防止sql注入；

## Lombok

一个插件，简化实体类的构建，只需要在实体类上标明注解即可，免去了get set方法等的繁琐步骤。

```xml
<dependency>
  <groupId>org.projectlombok</groupId>
  <artifactId>lombok</artifactId>
  <version>1.18.20</version>
  <scope>provided</scope>
</dependency>
```

在实体类使用注解

```java
package com.angyi.springboot.entity;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.Date;
@Data
@AllArgsConstructor
@NoArgsConstructor
public class Student {
    private Integer id;
    private String name;
    private String pwd;
    private String sex;
    private Date birthday;
    private String address;
    private String email;

}
```

![image-20210814200753948](https://cdn.jsdelivr.net/gh/Flionay/pic_bed@master/Upic/202108/image-20210814200753948.png)

# 复杂查询环境搭建

**关联**：多对一；一对多；**集合**

多表查询查询到的返回值肯定就不是一个简单的类，需要做resultmap结果映射；

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper
        PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">

<mapper namespace="com.angyi.dao.StudentMapper">
    <select id="getStudentAndTeacher" resultMap="StudentAndTeacher">
        select s.id as sid,s.name as sname,t.name as tname from student s,teacher t where s.tid=t.id;
    </select>
    <resultMap id="StudentAndTeacher" type="com.angyi.pojo.Student">
        <id property="id" column="sid"/>
        <result property="name" column="sname"/>
        <association property="teacher" javaType="com.angyi.pojo.Teacher">
            <result property="name" column="tname"/>
        </association>
    </resultMap>
</mapper>
```

# 动态sql

