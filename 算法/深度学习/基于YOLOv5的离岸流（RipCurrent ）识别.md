![RipCurrent](https://cdn.jsdelivr.net/gh/Flionay/pic_bed@master/Upic/202105/rnqBHm.png)

**项目来源：**

https://arxiv.org/abs/2102.02902

**需求：**

1. 实现基本的海岸图片离岸流识别 。
2. 在图片识别的基础上，做到海岸视频的检测识别。
3. 识别速度一定要快，后期可能会应用到监控摄像头，做到实时识别。 
## 模型
论文使用模型为FasterRCNN，基于前期船舶识别和人流检测项目的知识积累，FasterRCNN这种两段式的模型肯定无法在速度上达到需求。第一步生成候选框就要耗费非常长的时间。


所以这项工作，直接选择YOLO模型构建。


## 数据

这篇论文提供了图片，但是他的标注格式不能够被YOLO模型识别，所以人工对其重新打了标签（大约1800张）。
![Labelimg](https://cdn.jsdelivr.net/gh/Flionay/pic_bed@master/Upic/202105/1621325568316-c679ad13-4726-4281-bef8-7e73a6b0f63d.png)
打好标签的数据集缩略图：
![数据集](https://cdn.jsdelivr.net/gh/Flionay/pic_bed@master/Upic/202105/1621326421283-ef1f50e2-4eb3-41ab-a8cc-5c9ab9495564.jpeg)

## 训练
使用Pytorch构建YOLOv5模型，对数据集进行训练，考虑到数据集的好坏情况，观察到1100张往后的数据图片场景比较杂乱，这里只用了1100张图片进行训练和测试。
![训练状态](https://cdn.nlark.com/yuque/0/2021/png/2637180/1621325113571-340d8034-35aa-4d40-9bf0-69b6f6948530.png?x-oss-process=image%2Fresize%2Cw_1492)
从TensorBoard来看，训练了将近800次，P和R已接近平稳，R有下降的趋势，所以停止训练。但是从纵坐标来看P并不高，最高可能也就70%左右。


奇怪的是论文并没有这些目标检测常用指标的验证，这样就没有直接对比了。


不过按经验来说,FasterRCNN的精准度要高于YOLO，但是其速度实在太慢了，不利于工业应用。


## 结果
**检测结果：**

**图片结果**，图中数字代表置信度。
![image.png](https://cdn.nlark.com/yuque/0/2021/png/2637180/1621326892103-d2ac7ca5-d0a4-463c-9de2-439356a3fde1.png)

**视频结果：**

<video id="video" controls="" preload="none" poster="http://img.blog.fandong.me/2017-08-26-Markdown-Advance-Video.jpg">       <source id="mp4" src="https://cloud.video.taobao.com/play/u/2637180/p/1/d/hd/e/6/t/1/310219713710.mp4?auth_key=YXBwX2tleT04MDAwMDAwMTImYXV0aF9pbmZvPXsidGltZXN0YW1wRW5jcnlwdGVkIjoiNDgwNGNkYjEwOTc2ZDVjYjNkYzlhYzM3ZGVmYzE1MzgifSZkdXJhdGlvbj0mdGltZXN0YW1wPTE2MjE3NzM0MDg=" type="video/mp4">       </video>

视频检测非常快，每帧检测时间在0.009s-0.01s之间。

## web应用

最后构建出了供用户直接访问的浏览器接口，能够实现上传图片实时监测。

![](https://cdn.jsdelivr.net/gh/flionay/pic_bed//PicGo/20210520110320.png#id=yLi7y&originHeight=1695&originWidth=2332&originalType=binary&status=done&style=none)
上传图片，在五秒内基本能出结果。主要时间都耗费在了加载模型，调起GPU设备的过程中，真正检测的时间很短很短。

