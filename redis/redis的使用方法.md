首先安装redis模块

```shell
[root@zhangyz ~]# pip3 install redis
Collecting redis
  Downloading https://files.pythonhosted.org/packages/3b/f6/7a76333cf0b9251ecf49efff635015171843d9b977e4ffcf59f9c4428052/redis-2.10.6-py2.py3-none-any.whl (64kB)
    100% |████████████████████████████████| 71kB 595kB/s 
Installing collected packages: redis
Successfully installed redis-2.10.6
```

python3连接运用redis模块连接redis缓存服务器可以通过设置键值的方式来设置键名或取值
```python
import redis
r = redis.Redis(host='8.8.8.128')
r.set("Name", "Chunzhangyz", ex=3)
print(r.get("name"))
b'zhangyz'
```

获取所有的keys

```python
import redis
pool = redis.ConnectionPool(host='10.0.0.1', port=6379, db=0)
r = redis.Redis(connection_pool=pool) 
r.keys() # 以列表展示redis当中的所有key
r.set('foo', 'Bar')
print(r.get('foo'))
```

注意事项如果redis存储的是一个列表需要使用 lrange key 0 -1 这样的下标和名字来进行查看
* lpush(name, values)

在name对应的list中添加元素每个新的元素都添加到列表的最左边
```python
import redis
pool = redis.ConnectionPool(host='10.0.0.1', port=6379, db=0)
r = redis.Redis(connection_pool=pool) 
r.lpush('oo', 11, 22, 33)
```
保存顺序为: 33, 22, 11
        
在name对应的list中添加元素每个新的元素都添加到列表的最右边
* rpush(name, values)
    
取一个列表范围的值
```python     
import redis
pool = redis.ConnectionPool(host='10.0.0.1', port=6379, db=0)
r = redis.Redis(connection_pool=pool) 
r.lrange("name_list", 0, -1) # 表示查看该键内的所有元素
['c', 'b', 'a', 'rain', 'lao']

r.rpush("name_list", 'd', 'e')
r.lrange("name_list", 0, -1)
['c', 'b', 'a', 'rain', 'lao', 'd', 'e']
```
            
在Redis中设置值, 默认, 不存在则创建存在则修改参数
* ex: 过期时间 (秒)
* px: 过期时间 (毫秒)
* nx: 如果设置为True, 则只有name不存在时当前set操作才执行
* xx: 如果设置为True, 则只有name存在时当前set操作才执行
        	
## Redis的订阅和发布

订阅者

```python
#!/usr/bin/env python
# -*- coding: utf8 -*-

from monitor.RedisHelper import RedisHelper

obj = RedisHelper()
redis_sub = obj.subscribe() # 真正进行接收

while True:
    msg = redis_sub.parse_response()
    print(msg)
```

发布者

```python
#!/usr/bin/env python
# -*- coding: utf8 -*-

from monitor.RedisHelper import RedisHelper

obj = RedisHelper()
obj.public('hello')
```


```example RedisHelper.py

import redis

class RedisHelper(object):

    def __init__(self):
        self.__conn = redis.Redis(host='10.211.55.123', port=6379, db=0)
        self.chan_sub = 'fm104.5'
        self.chan_pub = 'fm104.5'

    def public(self, msg):
	self.__conn.publish(self.chan_pub, msg)
	return True

    def subscribe(self):
	# 打开一个对应的频道
	pub = self.__conn.pubsub()
	pub.subscribe(self.chan_sub)
	pub.parse_response() # 准备接收
	return pub
```

该代码的作用是可以一直不断的接收消息
