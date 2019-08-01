
### 安装必要模块pyvmomi

pyvmomi 该模块是专门用来管理esxi虚拟机的，可以用该模块实现相关自动化操作

```shell
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
[root@bdn pyvmomi-6.0.0]# clear
[root@bdn pyvmomi-6.0.0]# /usr/local/python34/bin/python3 setup.py install 
running install
running bdist_egg
running egg_info
writing pyvmomi.egg-info/PKG-INFO
writing dependency_links to pyvmomi.egg-info/dependency_links.txt
writing top-level names to pyvmomi.egg-info/top_level.txt
writing requirements to pyvmomi.egg-info/requires.txt
reading manifest file 'pyvmomi.egg-info/SOURCES.txt'
reading manifest template 'MANIFEST.in'
writing manifest file 'pyvmomi.egg-info/SOURCES.txt'
installing library code to build/bdist.linux-x86_64/egg
running install_lib
running build_py
creating build
creating build/lib
creating build/lib/pyVmomi
copying pyVmomi/Differ.py -> build/lib/pyVmomi
copying pyVmomi/StubAdapterAccessorImpl.py -> build/lib/pyVmomi
copying pyVmomi/DynamicTypeManagerHelper.py -> build/lib/pyVmomi
copying pyVmomi/ServerObjects.py -> build/lib/pyVmomi
copying pyVmomi/Iso8601.py -> build/lib/pyVmomi
copying pyVmomi/pyVmomiSettings.py -> build/lib/pyVmomi
copying pyVmomi/QueryTypes.py -> build/lib/pyVmomi
copying pyVmomi/CoreTypes.py -> build/lib/pyVmomi
copying pyVmomi/Version.py -> build/lib/pyVmomi
copying pyVmomi/__init__.py -> build/lib/pyVmomi
copying pyVmomi/ManagedMethodExecutorHelper.py -> build/lib/pyVmomi
copying pyVmomi/VmomiSupport.py -> build/lib/pyVmomi
copying pyVmomi/SoapAdapter.py -> build/lib/pyVmomi
copying pyVmomi/Cache.py -> build/lib/pyVmomi
creating build/lib/pyVim
copying pyVim/connect.py -> build/lib/pyVim
copying pyVim/__init__.py -> build/lib/pyVim
creating build/bdist.linux-x86_64
creating build/bdist.linux-x86_64/egg
creating build/bdist.linux-x86_64/egg/pyVim
copying build/lib/pyVim/connect.py -> build/bdist.linux-x86_64/egg/pyVim
copying build/lib/pyVim/__init__.py -> build/bdist.linux-x86_64/egg/pyVim
creating build/bdist.linux-x86_64/egg/pyVmomi
copying build/lib/pyVmomi/Differ.py -> build/bdist.linux-x86_64/egg/pyVmomi
copying build/lib/pyVmomi/StubAdapterAccessorImpl.py -> build/bdist.linux-x86_64/egg/pyVmomi
copying build/lib/pyVmomi/DynamicTypeManagerHelper.py -> build/bdist.linux-x86_64/egg/pyVmomi
copying build/lib/pyVmomi/ServerObjects.py -> build/bdist.linux-x86_64/egg/pyVmomi
copying build/lib/pyVmomi/Iso8601.py -> build/bdist.linux-x86_64/egg/pyVmomi
copying build/lib/pyVmomi/pyVmomiSettings.py -> build/bdist.linux-x86_64/egg/pyVmomi
copying build/lib/pyVmomi/QueryTypes.py -> build/bdist.linux-x86_64/egg/pyVmomi
copying build/lib/pyVmomi/CoreTypes.py -> build/bdist.linux-x86_64/egg/pyVmomi
copying build/lib/pyVmomi/Version.py -> build/bdist.linux-x86_64/egg/pyVmomi
copying build/lib/pyVmomi/__init__.py -> build/bdist.linux-x86_64/egg/pyVmomi
copying build/lib/pyVmomi/ManagedMethodExecutorHelper.py -> build/bdist.linux-x86_64/egg/pyVmomi
copying build/lib/pyVmomi/VmomiSupport.py -> build/bdist.linux-x86_64/egg/pyVmomi
copying build/lib/pyVmomi/SoapAdapter.py -> build/bdist.linux-x86_64/egg/pyVmomi
copying build/lib/pyVmomi/Cache.py -> build/bdist.linux-x86_64/egg/pyVmomi
byte-compiling build/bdist.linux-x86_64/egg/pyVim/connect.py to connect.cpython-34.pyc
byte-compiling build/bdist.linux-x86_64/egg/pyVim/__init__.py to __init__.cpython-34.pyc
byte-compiling build/bdist.linux-x86_64/egg/pyVmomi/Differ.py to Differ.cpython-34.pyc
byte-compiling build/bdist.linux-x86_64/egg/pyVmomi/StubAdapterAccessorImpl.py to StubAdapterAccessorImpl.cpython-34.pyc
byte-compiling build/bdist.linux-x86_64/egg/pyVmomi/DynamicTypeManagerHelper.py to DynamicTypeManagerHelper.cpython-34.pyc
byte-compiling build/bdist.linux-x86_64/egg/pyVmomi/ServerObjects.py to ServerObjects.cpython-34.pyc
byte-compiling build/bdist.linux-x86_64/egg/pyVmomi/Iso8601.py to Iso8601.cpython-34.pyc
byte-compiling build/bdist.linux-x86_64/egg/pyVmomi/pyVmomiSettings.py to pyVmomiSettings.cpython-34.pyc
byte-compiling build/bdist.linux-x86_64/egg/pyVmomi/QueryTypes.py to QueryTypes.cpython-34.pyc
byte-compiling build/bdist.linux-x86_64/egg/pyVmomi/CoreTypes.py to CoreTypes.cpython-34.pyc
byte-compiling build/bdist.linux-x86_64/egg/pyVmomi/Version.py to Version.cpython-34.pyc
byte-compiling build/bdist.linux-x86_64/egg/pyVmomi/__init__.py to __init__.cpython-34.pyc
byte-compiling build/bdist.linux-x86_64/egg/pyVmomi/ManagedMethodExecutorHelper.py to ManagedMethodExecutorHelper.cpython-34.pyc
byte-compiling build/bdist.linux-x86_64/egg/pyVmomi/VmomiSupport.py to VmomiSupport.cpython-34.pyc
byte-compiling build/bdist.linux-x86_64/egg/pyVmomi/SoapAdapter.py to SoapAdapter.cpython-34.pyc
byte-compiling build/bdist.linux-x86_64/egg/pyVmomi/Cache.py to Cache.cpython-34.pyc
creating build/bdist.linux-x86_64/egg/EGG-INFO
copying pyvmomi.egg-info/PKG-INFO -> build/bdist.linux-x86_64/egg/EGG-INFO
copying pyvmomi.egg-info/SOURCES.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying pyvmomi.egg-info/dependency_links.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying pyvmomi.egg-info/requires.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying pyvmomi.egg-info/top_level.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying pyvmomi.egg-info/zip-safe -> build/bdist.linux-x86_64/egg/EGG-INFO
creating dist
creating 'dist/pyvmomi-6.0.0-py3.4.egg' and adding 'build/bdist.linux-x86_64/egg' to it
removing 'build/bdist.linux-x86_64/egg' (and everything under it)
Processing pyvmomi-6.0.0-py3.4.egg
Copying pyvmomi-6.0.0-py3.4.egg to /usr/local/python34/lib/python3.4/site-packages
Adding pyvmomi 6.0.0 to easy-install.pth file

Installed /usr/local/python34/lib/python3.4/site-packages/pyvmomi-6.0.0-py3.4.egg
Processing dependencies for pyvmomi==6.0.0
Searching for six==1.11.0
Best match: six 1.11.0
Adding six 1.11.0 to easy-install.pth file

Using /usr/local/python34/lib/python3.4/site-packages
Searching for requests==2.18.4
Best match: requests 2.18.4
Adding requests 2.18.4 to easy-install.pth file

Using /usr/local/python34/lib/python3.4/site-packages
Searching for urllib3==1.22
Best match: urllib3 1.22
Adding urllib3 1.22 to easy-install.pth file

Using /usr/local/python34/lib/python3.4/site-packages
Searching for idna==2.6
Best match: idna 2.6
Adding idna 2.6 to easy-install.pth file

Using /usr/local/python34/lib/python3.4/site-packages
Searching for certifi==2017.7.27.1
Best match: certifi 2017.7.27.1
Adding certifi 2017.7.27.1 to easy-install.pth file

Using /usr/local/python34/lib/python3.4/site-packages
Searching for chardet==3.0.4
Best match: chardet 3.0.4
Adding chardet 3.0.4 to easy-install.pth file
Installing chardetect script to /usr/local/python34/bin

Using /usr/local/python34/lib/python3.4/site-packages
Finished processing dependencies for pyvmomi==6.0.0
[root@bdn pyvmomi-6.0.0]# make
make: *** No targets specified and no makefile found.  Stop.
[root@bdn pyvmomi-6.0.0]# make install 
make: *** No rule to make target `install'.  Stop.
[root@bdn pyvmomi-6.0.0]# 
[root@bdn pyvmomi-6.0.0]# 
[root@bdn pyvmomi-6.0.0]# /usr/local/python34/bin/ipython
Python 3.4.1 (default, Nov  2 2017, 12:27:39) 
Type 'copyright', 'credits' or 'license' for more information
IPython 6.5.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import pyVimoni
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)
<ipython-input-1-e81ab6d60b3f> in <module>()
----> 1 import pyVimoni

ImportError: No module named 'pyVimoni'

In [2]: import pyVmomi

In [3]: 

In [3]: 
```
