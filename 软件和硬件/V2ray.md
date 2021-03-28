# 使用魔方云VPS搭建V2ray翻墙服务器

### 前言

防火长城，坐落在网络世界的中国与世界的边界，在官方称之为自我审查的标签下，审查了政治的同时，同样也阻碍了技术的发展，主要为难的就是这些没有官方办法出去看世界，但是又想要出去学习的年轻人。

2020年春这次疫情，让中国民众深深的认识到了社会主义的制度优势，感受到中国政府集中力量的能力，作为对比近期美国的状况着实吓人。而这团结，积极的社会心态和国家环境，和网络环境，媒体环境是息息相关的。有很多人吐槽，新闻让我们看到的只是想让我们看到的。这也是国家防火墙存在的意义吧，创造这样一种团结积极的氛围是国家政府为了维护社会安定，国家团结所应该做的。

试想一下，如果开放网络环境呢，有一部分人我相信是有足够的是非辨别能力的，但是舆论的力量恐怕会对社会的安定造成巨大的影响。一个人成长的路上都难免犯错，何况一个国家。如果有人拿着政府的历史污点在网络上大肆造谣会带来什么样的后果？（想象一下的话，可以回想一下近几年明星上网络热搜事件的影响力，如果明星事件变成了政治事件呢？）

很多东西都是双刃剑，防火墙的缺点就是隔绝了国人与外界的联系，社交网络先不说，很多文件数据的下载真的是可以用艰难形容，明明是开源共享，但是因为墙的原因，不能够享受开源共享带来的福利。

但是我想一定有人想到了这一点，就科学技术而言，如果你已经有了外面资源的需求，那么你也一定具备自己开门走出去的能力。

本博文就是为了出去下载数据的一次造门经历。

## 购买VPS

VPS（Virtual Private Server 虚拟专用服务器）技术，将一台[服务器](https://baike.baidu.com/item/服务器/100571)分割成多个虚拟专享服务器的优质服务。实现VPS的技术分为容器技术，和[虚拟化技术](https://baike.baidu.com/item/虚拟化技术/276750) [1] 。在容器或虚拟机中，每个VPS都可选配独立公网IP地址、独立操作系统、实现不同VPS间磁盘空间、内存、CPU资源、进程和系统配置的隔离，为用户和应用程序模拟出“独占”使用计算资源的体验。VPS可以像独立服务器一样，重装操作系统，安装程序，单独重启服务器。

其实就是购买一台境外服务器，然后代理本地网络。提供VPS的服务商有很多，网上也有很多VPS评测，选择一家即可，然后注册并购买相应套餐，付款后会提供Linux远程接口。

## 搭建V2ray服务

V2Ray 是一个类似于 SS 的代理服务器，但 V2Ray 的功能和支持的代理协议要比 SS 多，甚至 V2Ray 还有 SS 的插件，也就是说 V2Ray 也包含 SS 的功能。下面是官方的介绍：

> Project V 是一个工具集合，它可以帮助你打造专属的基础通信网络。Project V 的核心工具称为V2Ray，其主要负责网络协议和功能的实现，与其它 Project V 通信。V2Ray 可以单独运行，也可以和其它工具配合，以提供简便的操作流程。

### 搭建步骤

1. 利用ssh接入远端Linux服务器，以魔方云为例，在控制面板内新建指令控制台，利用提供的ip用户和密码接入远程服务器：

![yJIpMK](https://cdn.jsdelivr.net/gh/Flionay/pic_bed@master/Upic/202005/yJIpMK.png)

2. V2Ray 的服务端是用 Go 语言 写的，软件无需安装，直接打开就能使用，但是配置文件还是比较麻烦的，而且还需要设置后台运行和开机启动，所以这里先用脚本安装。

   这里安装的 V2Ray 传输协议选择的是 TCP，也没有使用混淆之类的，如果要查看使用 WS + TLS 的配置可以访问 [V2Ray 配置 WebSocket + TLS](https://www.misterma.com/archives/856/) 。
   

**这个脚本支持的 Linux 版本包括：Ubuntu 16+、Debian 8+、CentOS 7+。**
我这里安装的系统是Debian 9
下载脚本：
```bash
wget https://git.io/v2ray.sh
```
添加执行权限：
```bash
chmod +x v2ray.sh
```
执行脚本：
```bash
./v2ray.sh
```
执行脚本后会看到如下提示
```bash
........... V2Ray 一键安装脚本 & 管理脚本 by 233v2.com ..........

帮助说明: https://233v2.com/post/1/

搭建教程: https://233v2.com/post/2/

 1. 安装

 2. 卸载

请选择 [1-2]:
```
输入 1 然后 回车，接着是选择传输协议：
```bash
请选择 V2Ray 传输协议 [1-32]

  1. TCP
  2. TCP_HTTP
  3. WebSocket
  4. WebSocket + TLS
  5. HTTP/2
  6. mKCP
  7. mKCP_utp
  8. mKCP_srtp
  9. mKCP_wechat-video
 10. mKCP_dtls
 11. mKCP_wireguard
 12. QUIC
 13. QUIC_utp
 14. QUIC_srtp
 15. QUIC_wechat-video
 16. QUIC_dtls
 17. QUIC_wireguard
 18. TCP_dynamicPort
 19. TCP_HTTP_dynamicPort
 20. WebSocket_dynamicPort
 21. mKCP_dynamicPort
 22. mKCP_utp_dynamicPort
 23. mKCP_srtp_dynamicPort
 24. mKCP_wechat-video_dynamicPort
 25. mKCP_dtls_dynamicPort
 26. mKCP_wireguard_dynamicPort
 27. QUIC_dynamicPort
 28. QUIC_utp_dynamicPort
 29. QUIC_srtp_dynamicPort
 30. QUIC_wechat-video_dynamicPort
 31. QUIC_dtls_dynamicPort
 32. QUIC_wireguard_dynamicPort

备注1: 含有 [dynamicPort] 的即启用动态端口..
备注2: [utp | srtp | wechat-video | dtls | wireguard] 分别伪装成 [BT下载 | 视频通话 | 微信视频通话 | DTLS 1.2 数据包 | WireGuard 数据包]

(默认协议: TCP):
```
这里我选择的 是 TCP ，传输协议以后还可以在配置文件中更改，直接 回车 ，然后是选择端口：
```bash
 V2Ray 传输协议 = TCP
----------------------------------------------------------------

请输入 V2Ray 端口 [1-65535]
(默认端口: 31663):
```
端口可以随便选，只要不和其他软件的端口冲突就行，然后是 广告拦截
```bash
是否开启广告拦截(会影响性能) [Y/N]
(默认 [N]):
```
如果不需要广告拦截的话直接回车，然后是配置 SS：
```bash
是否配置 Shadowsocks [Y/N]
(默认 [N]): 
```
如果要配置 SS 的话还需要输入 SS 的端口和密码，如果不配置的话直接回车，然后查看配置信息：
```bash
 ....准备安装了咯..看看有毛有配置正确了...

---------- 安装信息 -------------

 V2Ray 传输协议 = TCP

 V2Ray 端口 = 9999

 是否配置 Shadowsocks = 未配置

---------- END -------------

按 Enter 回车键 继续....或按 Ctrl + C 取消.
```
确认无误后 回车，安装完成后会显示 连接信息：

 ```bash
 
 ---------- V2Ray 配置信息 -------------

 地址 (Address) = 172.93.47.76

 端口 (Port) = 9999

 用户ID (User ID / UUID) = f5870b6z-d212-4dd8-a177-c3f79m2c7052

 额外ID (Alter Id) = 666

 传输协议 (Network) = tcp

 伪装类型 (header type) = none

---------- END -------------

V2Ray 客户端使用教程: https://233v2.com/post/4/

提示: 输入 v2ray url 可生成 vmess URL 链接 / 输入 v2ray qr 可生成二维码链接
 ```
然后就可以利用v2ray url命令生成链接，之后通过剪切板配置到本地v2ray客户端即可。

## 本地客户端配置

本地客户端会区分系统，不同系统有不同的客户端以及多种版本，具体选择可以在github自行搜索，选择对应版本release版本下载即可，然后右键客户端，从剪切板导入服务器设置，将v2ray url导入就✅

在服务端输入 `v2ray url` 生成 `vmess URL 链接` ，生成的 `vmess URL 链接` 形式如下：

```bash
---------- V2Ray vmess URL / V2RayNG v0.4.1+ / V2RayN v2.1+ / 仅适合部分客户端 -------------

vmess://ewoidiI6ICIymFkZCI6ICIxNzguMTI4LjQ5LjEwIiwKInBvcnQiOiAiMTAwODYiLAoiaWQiOiAiZjU4ODBiNmUtZDIxNy00ZGQ4LWEwNzctYjNmNzlkMmM3MDUyIiwKImFpZCI6ICIyMzMiLAoibmV0IjogInRjcCIsCiJ0eXBlIjogIm5vbmUiLAoiaG9zdCI6ICIiLAoicGF0aCI6ICIiLAoidGxzIjogIiIKfQo=
```
#### 几种客户端下载地址

##### Win

先进入： https://github.com/2dust/v2rayN/releases 下载客户端，下载的时候选择 `v2rayN-Core.zip` 。下载完成后解压，打开 `v2rayN.exe` ，点击任务栏的 v2rayN 托盘图标进入 v2rayN。

##### Android

目前 Android 的 V2Ray 的客户端有 [v2rayNG](https://play.google.com/store/apps/details?id=com.v2ray.ang&hl=zh) 、[Kitsunebi](https://play.google.com/store/apps/details?id=fun.kitsunebi.kitsunebi4android&hl=zh)，两个应用在 [Google Play](https://play.google.com/store?hl=zh) 都可以下载到，如果无法访问 Google Play 的话也可以在 [Github](https://github.com/) 下载， [点击进入 v2rayNG -  Github](https://github.com/2dust/v2rayNG/releases) ，[点击进入 Kitsunebi - Github](https://github.com/eycorsican/kitsunebi-android/releases)。

##### iOS

iOS 的 V2Ray 客户端有 [Shadowrocket](https://apps.apple.com/hk/app/shadowrocket/id932747118) 、[Kitsunebi](https://apps.apple.com/us/app/kitsunebi-proxy-utility/id1446584073) 、[Quantumult](https://apps.apple.com/us/app/quantumult/id1252015438)，不过以上客户端都无法在国区的 Apple Store 下载，需要转区。

##### Mac

Mac 的 V2Ray 客户端有 V2rayU ，V2rayX都可以直接在 [Github](https://github.com/) 搜索下载。

## 更改配置命令

在服务端输入 `v2ray` 会显示 V2Ray 的管理菜单，按照提示输入数字进入相应的管理选项，如下：

 ```ssh
........... V2Ray 管理脚本 v3.09 by 233v2.com ..........

## V2Ray 版本: v4.19.1  /  V2Ray 状态: 正在运行 ##

帮助说明: https://233v2.com/post/1/

反馈问题: https://github.com/233boy/v2ray/issues

TG 群组: https://t.me/blog233

捐赠脚本作者: https://233v2.com/donate/

捐助 V2Ray: https://www.v2ray.com/chapter_00/02_donate.html

  1. 查看 V2Ray 配置

  2. 修改 V2Ray 配置

  3. 下载 V2Ray 配置 / 生成配置信息链接 / 生成二维码链接

  4. 查看 Shadowsocks 配置 / 生成二维码链接

  5. 修改 Shadowsocks 配置

  6. 查看 MTProto 配置 / 修改 MTProto 配置

  7. 查看 Socks5 配置 / 修改 Socks5 配置

  8. 启动 / 停止 / 重启 / 查看日志

  9. 更新 V2Ray / 更新 V2Ray 管理脚本

 10. 卸载 V2Ray

 11. 其他

温馨提示...如果你不想执行选项...按 Ctrl + C 即可退出

请选择菜单 [1-11]:
 ```







