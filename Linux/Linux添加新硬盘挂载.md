# Linux添加新硬盘挂载

## 一. 查看磁盘信息

首先使用 `df -l` 列出文件系统的整体磁盘空间使用情况，可以用来查看磁盘已被使用多少空间和还剩余多少空间。

```
(base) root@qustx-X299-WU8:/# df -h
文件系统        容量  已用  可用 已用% 挂载点
udev             47G     0   47G    0% /dev
tmpfs           9.5G  2.8M  9.5G    1% /run
/dev/nvme0n1p1  458G  431G  4.2G  100% /
tmpfs            48G  8.0K   48G    1% /dev/shm
tmpfs           5.0M  4.0K  5.0M    1% /run/lock
tmpfs            48G     0   48G    0% /sys/fs/cgroup
....
```

然后使用 `fdisk -l` 查看我们新装的硬盘，确保其安装成功，以及代号：

```
(base) root@qustx-X299-WU8:/# fdisk -l

Disk /dev/nvme0n1：465.78 GiB，500107862016 字节，976773168 个扇区
Disk model: Samsung SSD 970 EVO Plus 500GB          
单元：扇区 / 1 * 512 = 512 字节
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节
磁盘标签类型：dos
磁盘标识符：0xfe4436e1

设备           启动  起点      末尾      扇区   大小 Id 类型
/dev/nvme0n1p1 *     2048 976771071 976769024 465.8G 83 Linux


Disk /dev/sda：3.65 TiB，4000787030016 字节，7814037168 个扇区
Disk model: ST4000NM000A-2HZ
单元：扇区 / 1 * 512 = 512 字节
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节


Disk /dev/sdb：3.65 TiB，4000787030016 字节，7814037168 个扇区
Disk model: ST4000NM000A-2HZ
单元：扇区 / 1 * 512 = 512 字节
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节

....
```

然后使用 `lsblk` 查看磁盘信息：

```
(base) root@qustx-X299-WU8:/# lsblk
NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
loop0         7:0    0  99.2M  1 loop /snap/core/10908
loop1         7:1    0   972K  1 loop /snap/tmux/11
loop2         7:2    0   2.5M  1 loop /snap/gnome-calculator/884
loop3         7:3    0 161.4M  1 loop /snap/gnome-3-28-1804/128
....
sda           8:0    0   3.7T  0 disk /diska
sdb           8:16   0   3.7T  0 disk 
nvme0n1     259:0    0 465.8G  0 disk 
└─nvme0n1p1 259:1    0 465.8G  0 part /
```

看到新安装的 `sdb` 没有被挂载。

## 二、将硬盘分区。

1、当硬盘小于等于2T时，可以用 `fdisk` 

```
fdisk /dev/sdb
1、查看帮助。
输入：m
2、新建分区。
输入：n
3、创建逻辑分区
输入：p
4、输入分区号以及指定分区大小
依照提示，回车表示默认。
5、检查分区情况（此时还未执行分区操作）
Command（m for help）：p 
6、保存退出
Command（m for help）：w
```

2、当硬盘大于2T时，用parted命令。

```
parted /dev/sdb   (用part命令对3T硬盘进行分区处理）
mklabel gpt       (用gpt格式可以将3TB弄在一个分区里)
unit TB           (设置单位为TB)
mkpart primary 0 3 (设置为一个主分区,大小为3TB，开始是0，结束是3）
print              (显示设置的分区大小）
quit               (退出parted程序)
```

## 三、格式化分区。

```
mkfs.ext4 /dev/sdb1
```

## 四、将硬盘挂载到文件夹下。

1、手动挂载。

新建一个文件夹：mkdir /diskb

挂载：mount /dev/sdb /diskb

2、开机自动挂载。

输入：vi /etc/fstab

在最后加入：

```
/dev/sdb    /diska    ext4    defaults    1    1
```

> 最后要注意更改磁盘的读取写入权限。

## 五、通知大家

修改SSH登陆之后显示的基本信息，通知大家硬盘位置

```bash

cd /etc/update-motd.d

vim 10-help-text

```

![2uAVUx](https://cdn.jsdelivr.net/gh/Flionay/pic_bed@master/Upic/202104/2uAVUx.png)