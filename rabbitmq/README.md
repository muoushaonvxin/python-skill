## 安装连接中间件的模块pika

<br/>

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
import collections
import json

credentials = pika.PlainCredentials("guest", "guest")
connection = pika.BlockingConnection(pika.ConnectionParameters("192.168.1.1", 5672, '/', credentials))
channel = connection.channel()
```

连上了rabbitmq之后需要对当中的队列进行相关操作, 所以需要调用pika当中的api方法去对这些数据做操作
```python
message = collections.OrderedDict()
message['data'] = 'hello world'
channel.exchange_declare(exchange='250test', exchange_type='direct', durable=True)
channel.basic_publish(exchange='250test', routing_key="info", body=json.dumps(message))
```

发送完成之后使用 close() 方法就可以和rabbitmq断开连接
```python
connection.close()
```

-----------------------------------------------------------------------------

rabbitmq可以存放消息, 也可以将消息送给相关的消费程序
```python
import pika
import json

credentials = pika.PlainCredentials("guest", "guest")
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.1', 5672, '/', credentials))
channel = connection.channel()
```

和rabbitmq当中的交换机和队列做绑定
```python
channel.exchange_declare(exchange='250test', exchange_type='direct', durable=True)
channel.queue_declare(exclusive=True)
channel.queue_bind(exchange='250test', queue='test', routing_key='info')
```

编写接收payload(消息体)的函数, 关联channel开始消费队列当中的消息
```python
def callback(ch, method, properties, body):
    var01 = json.loads(body.decode())
    print(var01)
    
channel.basic_consume(callback, queue='250test', no_ack=True)
channel.start_consuming()
```
