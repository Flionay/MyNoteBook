# Ubuntu cron 定时任务

### 使用场景

下载实时数据，部署实时模型。编写Python下载脚本，让其在指定时间运行。利用凌晨服务器空闲时间，自动训练模型等。

### 基本使用方法

#### 1. crontab服务启动

`Ubuntu16.04`  默认自带  `cron` ,如果没有，则进行安装：

```
sudo apt install cron
```

查看服务是否启动：

```
pgrep cron
```

如果有进程 `PID` ，则表示服务已经启动！

小记：linux常用命令 pgrep ，以名称为依据，从运行进程队列中查找进程，并显示查找到的进程PID。



| 选项 | 描述                             |
| ---- | -------------------------------- |
| -o   | 仅显示找到的最小（起始）进程号； |
| -n   | 仅显示找到的最大（结束）进程号； |
| -l   | 显示进程名称；                   |
| -P   | 指定父进程号；                   |
| -g   | 指定进程组；                     |
| -t   | 指定开启进程的终端；             |
| -u   | 指定进程的有效用户ID。           |



如果没有启动服务，需要重新启动一下， 可能需要管理员：

```
service cron start
```

### crontab 命令

`cron` 的任务计划保存在 `/etc/crontab` 文件中，文件内容如：

```
# /etc/crontab: system-wide crontab     
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user  command
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
#
```

这是root用户的定时任务，可以直接编辑此文件进行任务部署，但如果你不是root用户，不建议这样做。一般使用crontab命令，添加用户的定时任务。

可以通过 `crontab`命令进行任务管理：

```
# 编辑用户username 的计划任务文件
crontab -u username -e
# 显示某个用户的计划任务文件; 默认为当前用户
crontab -l 
crontab -u username -l
# 设置定时任务, 编辑某个用户的计划任务文件；默认为当前用户 
crontab -e 
# 删除某个用户的计划任务文件；默认为当前用户
crontab -r
```

## 3. 添加任务计划

进入 `crontab `编辑模式，进行任务添加。注意编辑模式可能不是 `vim` ，我的就是 `nona` ，百度一下其编辑和保存命令即可。

```
crontab -e
```

也可以直接编辑 `/etc/crontab` 文件，在尾部添加计划任务. `crontab` 任务计划的语法格式：

```
# m h dom mon dow user command
# 分　时　日　月　周 用户名 计划任务命令 
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
# 第1列 - 分钟1～59 每分钟用 * 或者 */1 表示 
# 第2列 - 小时1～23（0表示0点） 
# 第3列 - 日期1～31 
# 第4列 - 月份1～12 
# 第5列 - 星期0～6（0表示星期天） 
# 第6列 - 用户名
# 第7列 - 计划执行的任务命令
```

其中，使用`run-parts` 运行指定目录下的所有脚本.(编辑的脚本必须包含 `#!/bin/bash`). 如：

```
# 每天 23:30 运行 /home/my_scripts/ 目录下的所有脚本
30 23 * * * run-parts /home/my_scripts/
```

更多计划设置，如：

```
# 每晚的 22:30 执行 cd /home/username/
30 22 * * * cd /home/username/
# 每月5，15，25日的 6:30 执行 ls  
30 6 5,15,25 * * ls  
# 每周六、周日的 21:25 执行 cd /opt/
25 21 * * 6,0 cd /opt/       
# 每天3:00 至 6:00 之间每隔 30 分钟 执行 ls
0,30 3-6 * * * ls   
# 每星期六的 23:00 执行 cd /home/username/ 
0 23 * * 6 cd /home/username/ 
# 每一小时 执行一次 ls  
0 */1 * * * ls     
# 23:00 至 7:00，每隔一小时 执行 ls 
0 23-7/1 * * * ls
# 每月 7 号、每周二到周五的 23:00 执行 ls
0 23 4 * tue-fri ls
# 1 月 1 号的 1:00 执行 cd /home/username/
0 1 1 jan * cd /home/username/   
# 每个小时的第 20 分钟执行一次 ls
20   *  *  *  * ls 
# 每天 8:30 执行 cd /home/username/
30  8  *  *  * cd /home/username/ 
# 每隔20分钟执行一次 ls
*/20 *  *  *  * ls
```

注：

```
* 表示所有值
/ 表示“每”
- 表示区间范围
, 表示分割数字
```



> 值得注意的几点：
>
> 自动脚本中尽量使用绝对路径
>
> 如果使用Pyhon虚拟环境，不要使用conda activate，直接用解释器的绝对路径，例如：/home/msdc_2/anaconda3/envs/tf2/bin/python  /home/msdc_2/temp/auto.py