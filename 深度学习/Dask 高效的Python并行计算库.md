# Dask 高效的Python并行计算库



![CxdPvE](https://cdn.jsdelivr.net/gh/Flionay/pic_bed@master/Upic/202101/CxdPvE.jpg)


> 官网【[https://dask.org/](https://dask.org/)】

> 官方文档 【[https://docs.dask.org/](https://docs.dask.org/en/latest/)】

> 没有学的很精通，也无法从小到大，由浅到深的讲解，所以记录一些使用场景吧，这种记录方式也挺实用的。



### 场景1. 读取较大的数据集
Dask有着丰富的读取数据的接口，而且接口与常用的   `pandas`   `numpy` 数据接口基本相同，非常容易上手。
由于专业关系，我最常用的数据格式为 `netCDF` ,通常需要借助 `xarray` 库进行读取保存等操作。但非常好的消息是 `xarray` 与 `Dask` 建立了十分友好的互帮互助，共同进步关系， `xarray` 有着非常方便的参数接口，不需要太多额外配置就能够直接使用 `Dask` .
```python
# hycom 在线数据，TB级别，传入chunks分块参数，直接使用Dask能够秒级别导入
data_global = xr.open_dataset('http://tds.hycom.org/thredds/dodsC/GLBy0.08/expt_93.0',decode_times=False,chunks={"time":100})

# 如果是多个小文件，使用mfdataset，传入parallel并行参数，秒级别打开多个数据，并且能够按照某个维度整合
dataall = xr.open_mfdataset(url_exist,parallel = True,decode_times=False,combine='nested',concat_dim="time")

# 注意该函数对本地文件夹循环也非常好用
dataall = xr.open_mfdataset('data_all/*.nc',parallel=True)

```
### 场景2. 保存和下载数据
使用 `save_mfdataset(filelist,paths)` 并行保存数据。注意前提是数据为 `dask` 类型，否则相当于循环调用 `to_netcdf()` 。
```python
import xarray as xr

data_global = xr.open_dataset('http://tds.hycom.org/thredds/dodsC/GLBy0.08/expt_93.0',decode_times=False,chunks={"time":100})

data_latest = data_global.sel(lat = slice(2,42),lon = slice(104,132),depth=slice(0,1001))

from datetime import datetime,timedelta
import pandas as pd
import numpy as np
def return_latest_time():
    date_start = '2000-01-01 00:00:00'
    date_list = []
    for i in data_latest.time.data:
        date_list.append(pd.to_datetime(date_start)+timedelta(hours = i))
    return date_list
date_list = return_latest_time()

data_latest['time'] = pd.to_datetime(date_list) # 重新更新文件时间

date_time = pd.to_datetime(date_list)

data_latest_now =[]
data_latest_path= []
for date in date_time:
    if (date.hour == 0 or date.hour == 12) and date.year>2019:
        data_latest_now.append(data_latest.sel(time = date))
        data_latest_path.append("/data/hycom_2020_latest/{}.nc".format(str(date)))
        print(date,"已完成！！！")         

xr.save_mfdataset(data_latest_now,data_latest) # 并行保存

#### 下载  一天两次 普通保存

# for date in date_time:
#     if date.hour == 0 or date.hour == 12 :
#         data_latest_now = data_latest.sel(time = date)
#         data_latest_now.to_netcdf("/data/hycom_2018_latest/{}.nc".format(str(date)))
#         print(date,"已完成！！！")       
```
### 场景3. Delay
`delay` 是先将运算搁置，等到 `compute` 的时候再进行计算，非常方便调试大数据程序。
### 场景3. Persist
`persist` 作用是将dask先进行一次运算，结果任然保持dask格式，后面的运算仍支持dask并行计算。
