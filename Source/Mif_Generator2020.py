import wx
import os
import random
import math
from pygame import mixer # Load the required library

#############mif文件生成地址################
mif_file_path = "./output.mif"
#############参数定义################
min_width = 4 #存储单元位宽最小选项
max_width = 32 #存储单元位宽最大选项

min_depth = 4 #存储单元深度最小选项
max_depth = 32 #存储单元深度最大选项

mem_width_type = 32 #存储单元宽度
mem_depth_type = 4096 #存储单元深度 默认4096Word(4096*4bytes=16kb)
mem_data_type = 1 #存储单元数据表示格式 Hex:1 Decimal:2
mem_addr_type = 1 #存储单元地址表示格式 Hex:1 Decimal:2

PI = 3.141592
#############变量################
MEM_WIDTH_LIST = [] #存储单元位宽选项
MEM_DEPTH_LIST = [] #存储单元深度选项
SHOW_TYPE_LIST = ["HEX","DEC"] #数据表示进制


#生成存储单元宽度选项
def gen_MEM_WIDTH_LIST(min_width,max_width):
    i = 0
    MEM_WIDTH_LIST = []
    for i in range(min_width,max_width+1):
        MEM_WIDTH_LIST.append(str(i))
    return MEM_WIDTH_LIST

#生成存储单元深度选项
def gen_MEM_DEPTH_LIST(min_width,max_width):
    i = 0
    MEM_DEPTH_LIST = []
    for i in range(min_width,max_width+1):
        MEM_DEPTH_LIST.append(str(pow(2,i)))
    return MEM_DEPTH_LIST

MEM_WIDTH_LIST = gen_MEM_WIDTH_LIST(min_width,max_width)
MEM_DEPTH_LIST = gen_MEM_DEPTH_LIST(min_width,max_width)

def mem_width_event(event):#存储单元宽度选择框
    global mem_width_type
    print("存储单元宽度选择{0}".format(event.GetString()))
    mem_width_type = int(event.GetString())

def mem_depth_event(event):#存储单元深度选择框
    global mem_depth_type
    print("存储单元宽度选择{0}".format(event.GetString()))
    mem_depth_type = int(event.GetString())

def addr_type_event(event):#存储单元地址选择框
    global mem_addr_type
    print("存储单元宽度选择{0}".format(event.GetString()))
    if(event.GetString() == SHOW_TYPE_LIST[0]):#Hex
        mem_addr_type = 1
    elif(event.GetString() == SHOW_TYPE_LIST[1]):#Decimal
        mem_addr_type = 2

def data_type_event(event):#存储单元地址选择框
    global mem_data_type
    print("存储单元宽度选择{0}".format(event.GetString()))
    if(event.GetString() == SHOW_TYPE_LIST[0]):#Hex
        mem_data_type = 1
    elif(event.GetString() == SHOW_TYPE_LIST[1]):#Decimal
        mem_data_type = 2

def gen_mif_file(event):#存储单元地址选择框
    i = 0
    s = 0
    print("开始生成.mif文件")
    try:
        with open(mif_file_path,"w") as file:#每次覆盖
            file.write("DEPTH = "+str(mem_depth_type)+";\n")
            file.write("WIDTH = "+str(mem_width_type)+";\n")
            file.write("ADDRESS_RADIX = "+SHOW_TYPE_LIST[mem_addr_type-1]+";\n")
            file.write("DATA_RADIX = "+SHOW_TYPE_LIST[mem_data_type-1]+";\n")
            file.write("CONTENT\n")
            file.write("BEGIN\n")
            #生成数据
            for i in range(0,mem_depth_type):#存储单元深度/个数
                s = math.sin(PI*i/64);   
                #temp = (int)((s+1)*255/2);#0-255 8bit正弦
                temp = (int)((s+1)*(pow(2,mem_width_type)-1)/2);#生成对应宽度的正弦
                #file.write("{0:x}\t:\t{0:x};\n".format(i,temp));
                if(mem_addr_type == 2):
                    file.write("{}\t:".format(i));
                else:
                    file.write("{0:x}\t:".format(i));
                if(mem_addr_type == 2):
                    file.write("\t{};\n".format(temp));
                else:
                    file.write("\t{0:x};\n".format(temp));
                i = i + 1
            file.write("END;\n")
            wx.MessageBox('.mif文件生成成功,位于软件根目录下','信息', wx.OK | wx.ICON_INFORMATION)
    except Exception as e:
        print(e)
        wx.MessageBox('.mif文件生成失败:'+e,'错误', wx.OK | wx.ICON_INFORMATION)



#创建APP
app = wx.App()
#创建窗体
frame = wx.Frame(None,title = "Mif_Generator 作者:xddcore QQ:1034029664",pos = (1000,200),size = (500,400))
panel = wx.Panel(frame)

mem_width_text = wx.StaticText(panel,label='存储单元宽度(bits):')
mem_width_combobox = wx.ComboBox(panel,-1,value='32',choices=MEM_WIDTH_LIST,style=wx.TE_READONLY)
mem_width_combobox.Bind(wx.EVT_COMBOBOX,mem_width_event)

mem_depth_text = wx.StaticText(panel,label='存储单元深度(32bits Word):')
mem_depth_combobox = wx.ComboBox(panel,-1,value='4096',choices=MEM_DEPTH_LIST,style=wx.TE_READONLY)
mem_depth_combobox.Bind(wx.EVT_COMBOBOX,mem_depth_event)

addr_type_text = wx.StaticText(panel,label='地址总线表示进制:')
addr_type_combobox = wx.ComboBox(panel,-1,value='Hex',choices=SHOW_TYPE_LIST,style=wx.TE_READONLY)
addr_type_combobox.Bind(wx.EVT_COMBOBOX,addr_type_event)

data_type_text = wx.StaticText(panel,label='数据总线表示进制:')
data_type_combobox = wx.ComboBox(panel,-1,value='Hex',choices=SHOW_TYPE_LIST,style=wx.TE_READONLY)
data_type_combobox.Bind(wx.EVT_COMBOBOX,data_type_event)

decoder_button = wx.Button(panel,label = "生成.Mif文件")
decoder_button.Bind(wx.EVT_BUTTON,gen_mif_file)# 绑定事件

log_text = wx.TextCtrl(panel,style = wx.TE_MULTILINE|wx.TE_READONLY)#剩余打开时间

box1 = wx.BoxSizer() # 不带参数表示默认实例化一个水平尺寸器
box1.Add(mem_width_text,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 5) # 添加组件
box1.Add(mem_width_combobox,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 5) # 添加组件

box2 = wx.BoxSizer() # 不带参数表示默认实例化一个水平尺寸器
box2.Add(mem_depth_text,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 5) # 添加组件
box2.Add(mem_depth_combobox,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 5) # 添加组件

box3 = wx.BoxSizer() # 不带参数表示默认实例化一个水平尺寸器
box3.Add(addr_type_text,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 5) # 添加组件
box3.Add(addr_type_combobox,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 5) # 添加组件

box4 = wx.BoxSizer() # 不带参数表示默认实例化一个水平尺寸器
box4.Add(data_type_text,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 5) # 添加组件
box4.Add(data_type_combobox,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 5) # 添加组件

box5 = wx.BoxSizer() # 不带参数表示默认实例化一个水平尺寸器
box5.Add(decoder_button,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 5) # 添加组件

box6 = wx.BoxSizer() # 不带参数表示默认实例化一个水平尺寸器
box6.Add(log_text,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 5) # 添加组件

v_box = wx.BoxSizer(wx.VERTICAL) # wx.VERTICAL参数表示实例化一个垂直尺寸器
v_box.Add(box1,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 3) # 添加组件
v_box.Add(box2,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 3) # 添加组件
v_box.Add(box3,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 3) # 添加组件
v_box.Add(box4,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 3) # 添加组件
v_box.Add(box5,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 3) # 添加组件
v_box.Add(box6,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 3) # 添加组件

log_text.SetValue("欢迎使用Mif_Generator\n" 
                  +"本软件用于为Intel FPGA片内存储单元IP核生成.mif初始化文件。\n"
                  +"作者:xddcore于2020/08/15制作|QQ:1034029664|Github:www.github.com/xddcore\n"
                  +"xSoc(一个32位MIPS架构5级流水线Soc软核)开源地址:https://github.com/xddcore/xSoc \n"
                  +"本软件开源地址:https://github.com/xddcore/Mif_Generator")

panel.SetSizer(v_box) # 设置主尺寸器
frame.Show()
app.MainLoop()

