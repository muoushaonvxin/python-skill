
## Tornado 介绍

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


