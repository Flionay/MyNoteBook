# 🛅 管理MySQL

为了更加便捷可移动，方便管理和安装，建议使用Docker。
## 利用Docker管理MySQL
### 安装，启动
```shell
docker pull mysql:latest  #拉取最新版本镜像
# 启动mysql容器
docker run -itd --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 -d mysql:latest
#配置好这一步即可用navicat或者数据库连接工具连接本地数据库
docker ps -a 								# 查看运行的容器进程
docker exec -it mysql bash  # 进入shell
mysql -uroot -p							# 登录mysql
```

---

顺便记录一下docker的启动容器命令
```shell
docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
```
OPTIONS说明：

- **-a stdin:** 指定标准输入输出内容类型，可选 STDIN/STDOUT/STDERR 三项；

- **-d:** 后台运行容器，并返回容器ID；

- **-i:** 以交互模式运行容器，通常与 -t 同时使用；

- **-P:** 随机端口映射，容器内部端口**随机**映射到主机的端口

- **-p:** 指定端口映射，格式为：**主机(宿主)端口:容器端口**

- **-t:** 为容器重新分配一个伪输入终端，通常与 -i 同时使用；

- **--name="nginx-lb":** 为容器指定一个名称；

- **--dns 8.8.8.8:** 指定容器使用的DNS服务器，默认和宿主一致；

- **--dns-search example.com:** 指定容器DNS搜索域名，默认和宿主一致；

- **-h "mars":** 指定容器的hostname；

- **-e username="ritchie":** 设置环境变量；

- **--env-file=[]:** 从指定文件读入环境变量；

- **--cpuset="0-2" or --cpuset="0,1,2":** 绑定容器到指定CPU运行；

- **-m :**设置容器使用内存最大值；

- **--net="bridge":** 指定容器的网络连接类型，支持 bridge/host/none/container: 四种类型；

- **--link=[]:** 添加链接到另一个容器；

- **--expose=[]:** 开放一个端口或一组端口；

- **--volume , -v: **绑定一个卷

---

### 开始，停止，删除
```shell
docker start mysql
docker stop mysql
docker rm mysql
```
## 一些常用的sql管理命令
当进入sql之后，命令行会变成sql状态
![image.png](https://cdn.nlark.com/yuque/0/2020/png/2637180/1608790481333-24e2e5b9-8041-4f9f-af00-fd9ce216a4a7.png#align=left&display=inline&height=227&margin=%5Bobject%20Object%5D&name=image.png&originHeight=454&originWidth=1776&size=61474&status=done&style=none&width=888)

1. 列出所有数据库
```bash
mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| shici              |
| sys                |
| test               |
| school             |
+--------------------+
```
其中，`information_schema`、`mysql`、`performance_schema`和`sys`是系统库，不要去改动它们。其他的是用户创建的数据库。

2. 要创建一个新数据库，使用命令：
```
mysql> CREATE DATABASE test;
Query OK, 1 row affected (0.01 sec)
```

3. 要删除一个数据库，使用命令：
```
mysql> DROP DATABASE test;
Query OK, 0 rows affected (0.01 sec)
```

4. 对一个数据库进行操作时，要首先将其切换为当前数据库：
```
mysql> USE test;
Database changed
```
### 表
列出当前数据库的所有表，使用命令：
```
mysql> SHOW TABLES;
+---------------------+
| Tables_in_test      |
+---------------------+
| classes             |
| statistics          |
| students            |
| students_of_class1  |
+---------------------+
```
要查看一个表的结构，使用命令：
```
mysql> DESC students;
+----------+--------------+------+-----+---------+----------------+
| Field    | Type         | Null | Key | Default | Extra          |
+----------+--------------+------+-----+---------+----------------+
| id       | bigint(20)   | NO   | PRI | NULL    | auto_increment |
| class_id | bigint(20)   | NO   |     | NULL    |                |
| name     | varchar(100) | NO   |     | NULL    |                |
| gender   | varchar(1)   | NO   |     | NULL    |                |
| score    | int(11)      | NO   |     | NULL    |                |
+----------+--------------+------+-----+---------+----------------+
5 rows in set (0.00 sec)
```
还可以使用以下命令查看创建表的SQL语句：
```
mysql> SHOW CREATE TABLE students;
+----------+-------------------------------------------------------+
| students | CREATE TABLE `students` (                             |
|          |   `id` bigint(20) NOT NULL AUTO_INCREMENT,            |
|          |   `class_id` bigint(20) NOT NULL,                     |
|          |   `name` varchar(100) NOT NULL,                       |
|          |   `gender` varchar(1) NOT NULL,                       |
|          |   `score` int(11) NOT NULL,                           |
|          |   PRIMARY KEY (`id`)                                  |
|          | ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 |
+----------+-------------------------------------------------------+
1 row in set (0.00 sec)
```
创建表使用`CREATE TABLE`语句，而删除表使用`DROP TABLE`语句：
```
mysql> DROP TABLE students;
Query OK, 0 rows affected (0.01 sec)
```
修改表就比较复杂。如果要给`students`表新增一列`birth`，使用：
```
ALTER TABLE students ADD COLUMN birth VARCHAR(10) NOT NULL;
```
要修改`birth`列，例如把列名改为`birthday`，类型改为`VARCHAR(20)`：
```
ALTER TABLE students CHANGE COLUMN birth birthday VARCHAR(20) NOT NULL;
```
要删除列，使用：
```
ALTER TABLE students DROP COLUMN birthday;
```
### 退出MySQL
使用`EXIT`命令退出MySQL：
```
mysql> EXIT
Bye
```


