# 整理关于安装python3解释器的方法

<br>

<br>

1.首先从官方网站下载python3解释器
```shell
[root@zhangyz tools]# wget https://www.python.org/downloads/release/Python-3.4.1.tgz 
[root@zhangyz tools]# tar -xf Python-3.4.1.tgz
[root@zhangyz tools]# cd Python-3.4.1
```

2.然后就可以进行安装了
```shell
[root@zhangyz tools]# ./configure --prefix=/usr/local/python34
[root@zhangyz tools]# # ......
[root@zhangyz tools]# make && make install
```

3.安装完成之后可以生成一个环境变量这样就可以直接调用python了
```shell
[root@zhangyz tools]# export PATH=$PATH:/usr/local/python34/bin
[root@zhangyz tools]# python3
[GCC 4.4.7 20120313 (Red Hat 4.4.7-18)] on linux
Type "help", "copyright", "credits" or "license" for more information
>>>
```

4.最重要的是安装python第三方的软件包python之所以有特色就是因为这些软件包而变得丰富多彩
```shell
[root@zhangyz tools]# python3
python3            python3.4          python3.4-config   python3.4m         python3.4m-config  python3-config   
[root@zhangyz tools]# pip3
pip3    pip3.4  
```

		# 列出常用的一些软件包,这里是我自己动手装的
		[root@zhangyz tools]# pip3 list
		aiohttp (1.3.5)
		aiohttp-cors (0.5.1)
		ansible (2.3.1.0)
		asn1crypto (0.22.0)
		async-timeout (1.2.1)
		attrs (17.2.0)
		Automat (0.6.0)
		backports-abc (0.5)
		bcrypt (3.1.3)
		bleach (2.0.0)
		certifi (2017.4.17)
		cffi (1.10.0)
		chardet (3.0.4)
		click (6.7)
		configparser (3.5.0)
		constantly (15.1.0)
		cryptography (1.9)
		cssselect (1.0.1)
		decorator (4.0.11)
		Django (1.11.2)
		entrypoints (0.2.3)
		Flask (0.12.2)
		html5lib (0.999999999)
		hyperlink (17.2.1)
		idna (2.5)
		incremental (17.5.0)
		ipaddress (1.0.18)
		ipykernel (4.6.1)
		ipython (5.0.0)
		ipython-genutils (0.2.0)
		ipywidgets (6.0.0)
		itsdangerous (0.24)
		jedi (0.10.2)
		Jinja2 (2.9.6)
		jsonschema (2.6.0)
		jupyter-client (5.1.0)
		jupyter-console (5.1.0)
		jupyter-core (4.3.0)
		lxml (3.8.0)
		MarkupSafe (1.0)
		mistune (0.7.4)
		multidict (3.1.1)
		mysqlclient (1.3.10)
		nbconvert (5.2.1)
		nbformat (4.3.0)
		notebook (5.0.0)
		pandocfilters (1.4.1)
		paramiko (2.2.1)
		parsel (1.2.0)
		pexpect (4.2.1)
		pickleshare (0.7.4)
		pip (9.0.1)
		prompt-toolkit (1.0.14)
		protobuf (3.3.0)
		psutil (5.2.2)
		ptyprocess (0.5.2)
		pyasn1 (0.2.3)
		pyasn1-modules (0.0.9)
		pycparser (2.17)
		pycrypto (2.6.1)
		PyDispatcher (2.0.5)
		Pygments (2.2.0)
		PyMySQL (0.7.11)
		PyNaCl (1.1.2)
		pyOpenSSL (17.0.0)
		python-dateutil (2.6.0)
		python-nmap (0.6.1)
		python-qt (0.50)
		pytz (2017.2)
		PyYAML (3.12)
		pyzmq (16.0.2)
		Qt (0.2.1)
		qtconsole (4.3.0)
		queuelib (1.4.2)
		raven (6.1.0)
		requests (2.18.1)
		scapy-python3 (0.14)
		Scrapy (1.4.0)
		service-identity (17.0.0)
		setuptools (36.0.1)
		simplegeneric (0.8.1)
		six (1.10.0)
		terminado (0.6)``````
		testpath (0.3.1)
		tornado (4.5.1)
		traitlets (4.3.2)
		Twisted (17.5.0)
		typing (3.6.1)
		urllib3 (1.21.1)
		w3lib (1.17.0)
		wcwidth (0.1.7)
		webencodings (0.5.1)
		Werkzeug (0.12.2)
		widgetsnbextension (2.0.0)
		yarl (0.9.8)
		zipstream (1.1.4)
		zope.interface (4.4.2)



----------

 
> **python3 编译安装的话自带了pip 这个软件,该软件是专门安装python第三方包的软件**

		[root@zhangyz tools]# pip3 install django
		[root@zhangyz tools]# pip3 install django
		Requirement already satisfied: django in /usr/local/python34/lib/python3.4/site-packages
		Requirement already satisfied: pytz in /usr/local/python34/lib/python3.4/site-packages (from django)

		# 卸载一些python的第三方包方法		
		[root@zhangyz tools]# pip3 uninstall django -y


***


> **python3 安装mysqldb 和 连接mysql驱动的第三方包安装如下两个包就好**

		[root@zhangyz tools]# pip3 install pymysql
		Downloading/unpacking pymysql
		  Downloading PyMySQL-0.7.11-py2.py3-none-any.whl (78kB): 78kB downloaded
		Installing collected packages: pymysql
		Successfully installed pymysql
		Cleaning up...

		[root@zhangyz tools]# pip3 install mysqlclient
		Downloading/unpacking mysqlclient
		  Downloading mysqlclient-1.3.10.tar.gz (82kB): 82kB downloaded
		  Running setup.py (path:/tmp/pip_build_root/mysqlclient/setup.py) egg_info for package mysqlclient
    
		    warning: no files found matching 'GPL-2.0'
		Installing collected packages: mysqlclient
		  Running setup.py install for mysqlclient
		    building '_mysql' extension
		    gcc -pthread -Werror=declaration-after-statement -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -Dversion_info=(1,3,10,'final',0) -D__version__=1.3.10 -I/usr/include/mysql -I/usr/local/python34/include/python3.4m -c _mysql.c -o build/temp.linux-x86_64-3.4/_mysql.o -g -pipe -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=4 -m64 -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -fno-strict-aliasing -fwrapv -fPIC -DUNIV_LINUX -DUNIV_LINUX
		    In file included from /usr/local/python34/include/python3.4m/Python.h:8,
		                     from _mysql.c:40:
		    /usr/local/python34/include/python3.4m/pyconfig.h:554:1: warning: "HAVE_MBRTOWC" redefined
		    In file included from /usr/include/mysql/my_config.h:14,
		                     from _mysql.c:29:
		    /usr/include/mysql/my_config_x86_64.h:564:1: warning: this is the location of the previous definition
		    gcc -pthread -shared build/temp.linux-x86_64-3.4/_mysql.o -L/usr/lib64/mysql -lmysqlclient_r -lz -lpthread -lcrypt -lnsl -lm -lpthread -lssl -lcrypto -o build/lib.linux-x86_64-3.4/_mysql.cpython-34m.so -rdynamic
		    
		    warning: no files found matching 'GPL-2.0'
		Successfully installed mysqlclient
		Cleaning up...

		如果安装失败 yum -y install mysql-devel mysql



> **python3 安装 scrapy**
		
