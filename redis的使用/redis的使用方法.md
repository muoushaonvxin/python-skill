    import redis
        
    r = redis.Redis(host='8.8.8.128')
    print(r.get("name"))
    b'zhangyz'
    
    r.set("Name", "Chunzhangyz", ex=3)
    print(r.get("Name"))        
    b'Chunzhangyz'
    
    --------------------------------------------------------------------------------------------------------------------
    
    import redis
    
    pool = redis.ConnectionPool(host='10.0.0.1', port=6379, db=0)
    r = redis.Redis(connection_pool=pool)
    
    # 获取所有的keys 
    r.keys()          // 以列表展示redis当中的所有key
    
    r.set('foo', 'Bar')
    print r.get('foo')
    
    --------------------------------------------------------------------------------------------------------------------
    
    lpush(name, values)
    # 在name对应的list中添加元素，每个新的元素都添加到列表的最左边
    # 如:
        # r.lpush('oo', 11, 22, 33)
        # 保存顺序为:  33. 22. 11
        
    # 扩展
        # rpush(name, values)  表示从右向左操作
        
    去一个列表范围的值
        r.lrange("name_list", 0, -1)
        ['c', 'b', 'a', 'rain', 'lao']
        
        r.rpush("name_list", 'd', 'e')
        r.lrange("name_list", 0, -1)
        ['c', 'b', 'a', 'rain', 'lao', 'd', 'e']
        
        
    在Redis中设置值，默认，不存在则创建，存在则修改
    参数：
        ex, 过期时间（秒）
        px, 过期时间（毫秒）
        nx, 如果设置为True，则只有name不存在时，当前set操作才执行
        xx, 如果设置为True，则只有name存在时，当前set操作才执行
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    