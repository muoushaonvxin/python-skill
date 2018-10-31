
使用python连接mysql需要先安装一个模块来进行

```shell
[root@zhangyz ~]# /usr/local/python34/bin/pip install pymysql 
Requirement already satisfied: pymysql in /usr/local/python34/lib/python3.4/site-packages (0.9.2)
Requirement already satisfied: cryptography in /usr/local/python34/lib/python3.4/site-packages (from pymysql) (2.3.1)
Requirement already satisfied: asn1crypto>=0.21.0 in /usr/local/python34/lib/python3.4/site-packages (from cryptography->pymysql) (0.24.0)
Requirement already satisfied: six>=1.4.1 in /usr/local/python34/lib/python3.4/site-packages (from cryptography->pymysql) (1.11.0)
Requirement already satisfied: idna>=2.1 in /usr/local/python34/lib/python3.4/site-packages (from cryptography->pymysql) (2.6)
Requirement already satisfied: cffi!=1.11.3,>=1.7 in /usr/local/python34/lib/python3.4/site-packages (from cryptography->pymysql) (1.11.5)
Requirement already satisfied: pycparser in /usr/local/python34/lib/python3.4/site-packages (from cffi!=1.11.3,>=1.7->cryptography->pymysql) (2.19)
```
