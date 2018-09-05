## 安装连接中间件的模块pika

```shell
[root@zhangyz ~]# /usr/local/python34/bin/pip3 install pika
Requirement already satisfied: pika in /usr/local/python34/lib/python3.4/site-packages (0.10.0)
```

查看pika模块是否安装完成 (没有报错说明模块安装成功)
```shell
[root@zhangyz newdanye]# /usr/local/python34/bin/python3
Python 3.4.1 (default, Jul 15 2017, 02:05:27) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-18)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import pika
>>> 
```

以下是使用pika模块和rabbitmq中间件进行连接的代码
```python
import pika

credentials = pika.PlainCredentials("guest", "guest")
connection = pika.BlockingConnection(pika.ConnectionParameters("192.168.1.1", 5672, '/', credentials))
channel = connection.channel()
```
