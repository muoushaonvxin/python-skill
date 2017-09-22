    某班学生期末考试成绩，语文，数学，英语分别存储在3个列表中，同时迭代三个列表，计算每个学生的总分
    
    
    from random import randint
    chinese = [randint(60, 100) for _ in xrange(40)]
    math = [randint(60, 100) for _ in xrange(40)]
    english = [randint(60, 100) for _ in xrange(40)]
    
    for i in xrange(len(math)):
        chinese[i] + math[i] + english[i]
    
    zip([1,2,3,4], ('a', 'b', 'c', 'd'))
    [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
    
    zip([1,2,3,4], ('a', 'b', 'c', 'd'), [7.8.9.10])
    [(1, 'a', 7), (2, 'b', 8), (3, 'c', 9), (4, 'd', 10)]

    zip([1,2,3,4], ('a', 'b', 'c', 'd'))
    s[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
    
    for c, m, e in zip(chinese, math, english):
        total.append(c + m + e)
        
        
        
    某年级有4个班，某次考试每班英语成绩分别存储在4个列表中，一次迭代每个列表，统计全学年成绩高于90分的学生？
        并行: 使用内置函数zip，它能将多个可迭代对象合并，每次迭代返回一个元组
        串行: 使用标准库总的itertools.chain 它能将多个可迭代对象链接。
        
        from itertools import chain
        
        e1 = [randint(60, 100) for _ in xrange(40)]
        e2 = [randint(60, 100) for _ in xrange(42)]
        e3 = [randint(60, 100) for _ in xrange(42)]
        e4 = [randint(60, 100) for _ in xrange(39)]
        
        count = 0
        for x in chain(e1, e2, e3, e4):
            if x > 90:
                count += 1


