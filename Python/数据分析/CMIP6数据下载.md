# CMIP6 海气耦合模型数据下载

## 下载工具说明

官方下载路线走不通，采用搜到的CMIP6数据获取方式，是一个python包。

https://github.com/TaufiqHassan/acccmip6

在官网找到需要下载的文件名称，并且罗列如下：

```text
CMIP6.CMIP.NCAR.CESM2-FV2.historical.r1i1p1f1.Oday.tos.gn 是原始格点的
tauu_Eday_CESM2-FV2_historical_r1i1p1f1_gn_20000101-20091231.nc
tauu_Eday_CESM2-FV2_historical_r1i1p1f1_gn_20100101-20150101.nc

tauv_Eday_CESM2-FV2_historical_r1i1p1f1_gn_20000101-20091231.nc
tauv_Eday_CESM2-FV2_historical_r1i1p1f1_gn_20100101-20150101.nc

tos_Oday_CESM2-FV2_historical_r1i1p1f1_gn_20000102-20150101.nc
tos_Oday_CESM2-FV2_historical_r1i1p1f1_gr_20000102-20150101.nc

CAS
vas_day_FGOALS-f3-L_historical_r1i1p1f1_gr_20000101-20091231.nc
vas_day_FGOALS-f3-L_historical_r1i1p1f1_gr_20100101-20141231.nc

uas_day_FGOALS-f3-L_historical_r1i1p1f1_gr_20000101-20091231.nc
uas_day_FGOALS-f3-L_historical_r1i1p1f1_gr_20100101-20141231.nc

tos_Omon_FGOALS-f3-L_historical_r1i1p1f1_gn_185001-201412.nc
```



CMIP6数据文件的名字构成是有意义的，以CMIP6.CMIP.NCAR.CESM2-FV2.historical.r1i1p1f1.Oday.tos.gn为例子，解析开每部分分别是以下这些意思：



```text
Cmip6 第几次计划
Cmip 那个子计划
Ncar 那个机构
CESM2-FV2 那个模式
historical 哪个实验
r1i1p1f1 那些运行模式的控制指标
Oday 数据类型的时间频率
Tos 变量名缩写
Grid label 输出数据的网格类型
```



而acccmip6包的下载逻辑也是这样的。



```terminal
(base) msdc_2@amax:/data/Chenjq/CMIP6_makai$ acccmip6 --help
usage: acccmip6 [-h] [-dir DIR] -o OUTPUT_OPTIONS [-m M] [-e E] [-v V] [-f F]
                [-r R] [-rlzn RLZN] [-cr] [-yr YR] [-c C] [-desc DESC]
                [-time TIME] [-skip SKIP]

optional arguments:
  -h, --help            show this help message and exit
  -dir DIR              Download directory.
  -o OUTPUT_OPTIONS, --output-options OUTPUT_OPTIONS
                        S for 'Searching' or D for 'Downloading'. Use M to
                        initiate the CMIP6DB module.
  -m M                  Model names
  -e E                  Experiment names
  -v V                  Variable names
  -f F                  Output frequency
  -r R                  Output realm
  -rlzn RLZN            Select realization
  -cr                   Select common realizations
  -yr YR                Select year
  -c C                  Checker: yes to check inputs
  -desc DESC            Description: yes to print out experiment description
  -time TIME            Description: yes to print out avalable time periods
  -skip SKIP            Skip any item in your do
```



先进性搜索，看看能不能找到想要下载的数据文件。



```bash
# S 是搜索
acccmip6 -o S -m CESM2-FV2 -e historical -v tauu -f day
# -time 会显示可下载时间段
acccmip6 -o S -m CESM2-FV2 -e historical -v tauu -f day -time yes
# -yr 进行时间的切割 
acccmip6 -o S -m CESM2-FV2 -e historical -v tauu -f day -time yes -yr -15
```

![img](https://pic-1300286858.cos.ap-nanjing.myqcloud.com/uPic/2021-11/1635491627359-0b946a9e-7b91-414c-88ce-708edf2e06d2.png)

```plain
# D 是下载
acccmip6 -o D -m CESM2-FV2 -e historical -v tauu -f day -time yes -yr -15 -dir ./tauu

acccmip6 -o D -m CESM2-FV2 -e historical -v ['tos','tauv'] -f day -rlzn 1 -time yes -yr -15
```

## ![img](https://pic-1300286858.cos.ap-nanjing.myqcloud.com/uPic/2021-11/1635491656460-d04f5f06-8f53-40be-8449-fd732da38e5c.png)

## 参考：

https://acccmip6.readthedocs.io/en/latest/

https://cloud.tencent.com/developer/article/1744928