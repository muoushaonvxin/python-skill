    import csv
    
    csv.read()
    
    csv.writer()
    
    http://table.finance.yahoo.com/table.csv?s=000001.sz, 我们可以通过雅虎网站获取了中国股市（深市）数据集，它以csv数据格式存储。
    
        Date, Open, High, Low, Close, Volume, AdjClose
        2016-06-30, 8.69, 8.74, 8.66, 8.70, 36220400, 8.70
        2016-06-30, 8.69, 8.74, 8.66, 8.70, 36220400, 8.70
        2016-06-30, 8.69, 8.74, 8.66, 8.70, 36220400, 8.70
        2016-06-30, 8.69, 8.74, 8.66, 8.70, 36220400, 8.70
        ......
        
    请将平安银行这支股票，在2016年中成交量超过50000000 的记录存储到另一个csv文件中。
    
    解决发难：  使用标准库中的csv模块，可以使用其中reader和writer 完成csv文件读写。
    
    from urllib import urlretrieve
    
    urlretrieve('http://table.finance.yahoo.com/table.csv?s=000001.sz', 'pinan.csv')
    
    cat pinan.csv | less
    
    ---------------------------------------------------------------------------------------------
    
    import csv
    
    rf = open('pinan.csv', 'rb')   # 打开csv文件
    reader = csv.reader(rf)
    reader.next()
    
    通常来说还有另外一种方法：
    for row in  reader: print(row)
    
    
    # 有关写文件
    import csv
    
    wf = open('pinan_copy.csv', 'wb')
    writer = csv.writer(wf)
    writer.writerow(['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close'])
    writer.writerow(reader.next())
    writer.writerow(reader.next())
    wf.flush()
    
    
    一个小脚本案例：
    import csv
    
    with open('pinan.csv', 'rb') as rf:
        reader = csv.reader(rf)
        with open('pinan2.csv', 'wb') as wf:
            writer = csv.writer(wf)
            headers = reader.next()
            writer.writerow(headers)
            for row in reader:
                if row[0] < '2016-01-01':
                    break
                if int(row[5]) >= 50000000:
                    writer.writerow(row)
                    
    print('the end')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    