
### 安装必要模块pyvmomi

<br/>

pyvmomi 该模块是专门用来管理esxi虚拟机的，可以用该模块实现相关自动化操作

```shell
[root@zhangyz ~]# /usr/local/python34/bin/pip3 install -i https://pypi.douban.com/simple pyVmomi
DEPRECATION: Python 3.4 support has been deprecated. pip 19.1 will be the last one supporting it. Please upgrade your Python as Python 3.4 won't be maintained after March 2019 (cf PEP 429).
Looking in indexes: https://pypi.douban.com/simple
Collecting pyVmomi
  Downloading https://pypi.doubanio.com/packages/71/24/0bb1257b3bc89f7b2facdbad91cc56902d116d649a263c242ef32f73110e/pyvmomi-6.7.1.2018.12.zip (632kB)
     |████████████████████████████████| 634kB 1.3MB/s 
Requirement already satisfied: requests>=2.3.0 in /usr/local/python34/lib/python3.4/site-packages (from pyVmomi) (2.18.4)
Requirement already satisfied: six>=1.7.3 in /usr/local/python34/lib/python3.4/site-packages (from pyVmomi) (1.11.0)
Requirement already satisfied: certifi>=2017.4.17 in /usr/local/python34/lib/python3.4/site-packages (from requests>=2.3.0->pyVmomi) (2017.7.27.1)
Requirement already satisfied: urllib3<1.23,>=1.21.1 in /usr/local/python34/lib/python3.4/site-packages (from requests>=2.3.0->pyVmomi) (1.22)
Requirement already satisfied: chardet<3.1.0,>=3.0.2 in /usr/local/python34/lib/python3.4/site-packages (from requests>=2.3.0->pyVmomi) (3.0.4)
Requirement already satisfied: idna<2.7,>=2.5 in /usr/local/python34/lib/python3.4/site-packages (from requests>=2.3.0->pyVmomi) (2.6)
Installing collected packages: pyVmomi
  Running setup.py install for pyVmomi ... done
Successfully installed pyVmomi-6.7.1.2018.12
WARNING: You are using pip version 19.1.1, however version 19.2.1 is available.
```

看到导入模块没有报错, 说明安装成功了
