import time  #time模块用于提供各种各样与时间有关的函数

import datetime  #datatime模块重新封装了time模块，提供更多接口，用于提供更多与时间有关的函数

import sys  #sys模块提供对解释器使用或维护的一些变量的访问，以及与解释器强烈交互的函数。它始终可用。

print('输入指定日期即可穿越(只能到未来)'"\n"'请输入目标年月日：')
y=int(input('年'))
m=int(input('月'))
d=int(input('日'))
sj=str(y)+' '+str(m)+' '+str(d)  #新定义一个和时间有关的变量sj
d1=datetime.datetime(y,m,d)
print('启动中，还需要')


while True:
   d2=datetime.datetime.now()
   sec=round((d1-d2).total_seconds())
   op=[int(sec/86400),'天',int((sec-int(sec/86400)*86400)/3600),'小时',int((sec-int(sec/3600)*3600)/60),'分',int((sec-int(sec/60)*60)),'秒']
   nn=(''.join('%s' %id for id in op))
   sys.stdout.write("\r%s"%nn)
   sys.stdout.write('即可启动')
   sys.stdout.flush()  #调用sys模块实现对变量的访问
   time.sleep(1)  #时间变量变化的步长设定为一秒
