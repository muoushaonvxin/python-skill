
## Tornado 介绍

<br/>

Tornado全称为 Tornado Web Server, 是一种 Web 服务器软件的开源版本.

### 特点
* 作为Web框架, 类似于另一个 Python web 框架 web.py 其拥有异步非柱塞 io 的处理方式. 
* 作为web服务器, tornado有较为出色的抗负载能力, 官方用nginx反向代理的方式部署tornado和其他python web应用框架进行对比, 结果浏览量超过第二名40%

### 使用场景
* 用户量大, 高并发
* 大量的HTTP持久连接

### C10K

上面的高并发问题, 通常用C10K这一概念来描述. C10K - Concurrently handing ten thousand connections. 即并发10000个连接. 对于单台服务器而言, 根本无法承担, 而采用多台服务器分布式又意味着高昂的成本.

### 性能

tornado在设计之初就考虑到了性能因素, 旨在解决C10K的问题, 这样的问题, 这样设计使得其成为一个拥有非常高性能的解决方案.


#### 安装tornado扩展安装包

```shell
[root@zhangyz ~]# /usr/local/python34/bin/pip3 install tornado
Collecting tornado
  Downloading https://files.pythonhosted.org/packages/e6/78/6e7b5af12c12bdf38ca9bfe863fcaf53dc10430a312d0324e76c1e5ca426/tornado-5.1.1.tar.gz (516kB)
    100% |████████████████████████████████| 522kB 233kB/s 
Collecting backports_abc>=0.4 (from tornado)
  Downloading https://files.pythonhosted.org/packages/7d/56/6f3ac1b816d0cd8994e83d0c4e55bc64567532f7dc543378bd87f81cebc7/backports_abc-0.5-py2.py3-none-any.whl
Installing collected packages: backports-abc, tornado
  Running setup.py install for tornado ... done
Successfully installed backports-abc-0.5 tornado-5.1.1
```

#### tornado小段代码测试 

```python
import tornado.web
import tornado.ioloop

# 一个业务处理类
class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("ok good idea.")

if __name__ == "__main__":
    app = tornado.web.Application(
        [
            (r"/", IndexHandler)
        ]
    )
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
```

tornado用法简介
```shell
import tornado.web # tornado的基础web框架模块
```

让tornado运行web服务
```shell
import tornado.ioloop # tornado的核心IO循环模块, 封装了Linux的epoll和BSD的kqueue, 它是tornado框架高效的基础
```

建立处理业务逻辑的类对象
```shell
import tornado.web
import tornado.ioloop

# 一个业务处理类
class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("ok good idea.")
```

tornado处理业务逻辑的对应url设置
```shell
import tornado.web
import tornado.ioloop

if __name__ == "__main__":
    # Application: 是tornado web框架的核心应用类, 是与服务器对应的接口
    # 里面保存了路由映射表, 有一个listen方法用来创建一个http服务器的实例, 并绑定监听端口
    # 但是, 此时服务器只是设置监听端口, 但是并没有真正监听
    app = tornado.web.Application(
        [
            (r"/", IndexHandler)
        ]
    )
    app.listen(8000)
```

tornado开启端口监听让用户能够访问web服务器
```shell
# IOLoop.current(): 当回当前线程的IOLoop的实例
# IOLoop.start(): 启动IOLoop实例的 I/O 循环
tornado.ioloop.IOLoop.current().start() 
```
