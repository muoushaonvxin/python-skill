    import redis
    
    pool = redis.ConnectionPool(host='10.0.0.1', port=6379, db=0)
    r = redis.Redis(connection_pool=pool)
    
    # 获取所有的keys 
    r.keys()          // 以列表展示redis当中的所有key
    
    r.set('foo', 'Bar')
    print r.get('foo')
    
    ---------------------------------------------------
    
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
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    