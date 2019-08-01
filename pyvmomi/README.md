
### 安装必要模块pyvmomi

<br/>

pyvmomi 该模块是专门用来管理esxi虚拟机的，可以用该模块实现相关自动化操作

```shell
[root@zhangyz ~]# cd /usr/local/src
[root@zhangyz src]# wget https://pypi.python.org/packages/source/p/pyvmomi/pyvmomi-6.0.0.tar.gz
--2019-08-01 15:23:47--  https://pypi.python.org/packages/source/p/pyvmomi/pyvmomi-6.0.0.tar.gz
Resolving pypi.python.org... 151.101.228.223, 2a04:4e42:1a::223
Connecting to pypi.python.org|151.101.228.223|:443... connected.
HTTP request sent, awaiting response... 301 Redirect to Primary Domain
Location: https://pypi.org/packages/source/p/pyvmomi/pyvmomi-6.0.0.tar.gz [following]
--2019-08-01 15:23:48--  https://pypi.org/packages/source/p/pyvmomi/pyvmomi-6.0.0.tar.gz
Resolving pypi.org... 151.101.0.223, 151.101.192.223, 151.101.128.223, ...
Connecting to pypi.org|151.101.0.223|:443... connected.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: https://files.pythonhosted.org/packages/source/p/pyvmomi/pyvmomi-6.0.0.tar.gz [following]
--2019-08-01 15:23:49--  https://files.pythonhosted.org/packages/source/p/pyvmomi/pyvmomi-6.0.0.tar.gz
Resolving files.pythonhosted.org... 151.101.109.63, 2a04:4e42:36::319
Connecting to files.pythonhosted.org|151.101.109.63|:443... connected.
HTTP request sent, awaiting response... 302 Found
Location: 
Reusing existing connection to files.pythonhosted.org:443.
HTTP request sent, awaiting response... 200 OK
Length: 216134 (211K) [application/octet-stream]
Saving to: “pyvmomi-6.0.0.tar.gz”

100%[==================================================================>] 216,134     30.0K/s   in 7.0s    

2019-08-01 15:24:02 (30.0 KB/s) - “pyvmomi-6.0.0.tar.gz” saved [216134/216134]
 
[root@zhangyz src]# tar -xf pyvmomi-6.0.0.tar.gz 
[root@zhangyz src]# cd pyvmomi-6.0.0
[root@zhangyz pyvmomi-6.0.0]# ls
LICENSE.txt  MANIFEST.in  NOTICE.txt  PKG-INFO  pyVim  pyVmomi  pyvmomi.egg-info  README.rst  requirements.txt  sample  setup.cfg  setup.py  test-requirements.txt  tests  tox.ini
[root@zhangyz pyvmomi-6.0.0]# /usr/local/python34/bin/python3 setup.py install  
[root@zhangyz pyvmomi-6.0.0]# /usr/local/python34/bin/ipython
Python 3.4.1 (default, Nov  2 2017, 12:27:39) 
Type 'copyright', 'credits' or 'license' for more information
IPython 6.5.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import pyVmomi
```

看到导入模块没有报错, 说明安装成功了
