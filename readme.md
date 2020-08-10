# 基于python的“时光机”代码介绍

## 完成代码所需的模块

### 模块简介
完成“时光机”代码的编写需要使用到三个模块，分别是“time”、“datetime”和“sys”
#### time模块 
time模块用于提供各种与时间有关的函数
#### datetime模块
datatime模块重新封装了time模块，提供更多接口，用于提供更多与时间有关的函数
#### sys模块
sys模块提供对解释器使用或维护的一些变量的访问，以及与解释器强烈交互的函数。它始终可用。


### 调用模块使用的代码
```python
import time

import datetime

import sys

```





## 完整代码
```python
import time
import datetime
import sys

print('输入指定日期即可穿越(只能到未来)'"\n"'请输入目标年月日：')
y=int(input('年'))
m=int(input('月'))
d=int(input('日'))
sj=str(y)+' '+str(m)+' '+str(d)
d1=datetime.datetime(y,m,d)
print('启动中，还需要')


while True:
   d2=datetime.datetime.now()
   sec=round((d1-d2).total_seconds())
   op=[int(sec/86400),'天',int((sec-int(sec/86400)*86400)/3600),'小时',int((sec-int(sec/3600)*3600)/60),'分',int((sec-int(sec/60)*60)),'秒']
   nn=(''.join('%s' %id for id in op))
   sys.stdout.write("\r%s"%nn)
   sys.stdout.write('即可启动')
   sys.stdout.flush()
   time.sleep(1)


```

