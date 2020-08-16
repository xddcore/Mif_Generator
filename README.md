# Mif_Generator
A Mif file Generator For Intel FPGA Memory IP Core initial .mif file.[By Python][Have .exe packet]
## 为什么要写这款软件？
2020年8月15日晚，打算直接用片内存储单元 ROM的IP核，结果发现还需要.mif初始化文件。
(这文件贼坑，需要手动定义每个存储单元数据，我有4096个Word存储单元，一个个来得累死人...)
于是我去找了个mif自动生成软件，结果这个软件太老了(2010年所作)，width只支持到16bit，让我32bit的MIPS架构情何以堪。
于是不如自己写一个，开源出去。于是有了Mif Generator2020。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200816114237264.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2MjI5ODc2,size_16,color_FFFFFF,t_70#pic_center)


## 作者信息
作者:xddcore于2020/08/15制作|QQ:1034029664|Github:www.github.com/xddcore
xSoc(一个32位MIPS架构5级流水线Soc软核)开源地址:https://github.com/xddcore/xSoc 
本软件开源地址:https://github.com/xddcore/Mif_Generator

## 使用流程
### 1.双击打开Mif_Generator2020.exe(或者电脑上有python环境的同学，可以执行如下命令运行软件。
```python
python Mif_Generator2020.py
```
### 2.点击“生成.Mif文件”，弹出生成成功对话框后，在软件根目录下即可看到"output.mif"文件
### 3.将使用.mif文件进行FPGA BRAM 相关衍生IP核初始化。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200816114449651.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2MjI5ODc2,size_16,color_FFFFFF,t_70#pic_center)


### 4. 相关IP核创建成功，开始创造吧！
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200816114536798.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2MjI5ODc2,size_16,color_FFFFFF,t_70#pic_center)

