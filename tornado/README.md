
## Tornado 介绍

Tornado全称为 Tornado Web Server, 是一种 Web 服务器软件的开源版本.

### 特点
* 作为Web框架, 类似于另一个 Python web 框架 web.py 其拥有异步非柱塞 io 的处理方式. 
* 作为web服务器, tornado有较为出色的抗负载能力, 官方用nginx反向代理的方式部署tornado和其他python web应用框架进行对比, 结果浏览量超过第二名40%

### 使用场景
* 用户量大, 高并发
* 大量的HTTP持久连接
