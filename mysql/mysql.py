import pymysql


class DB(object):

    def __init__(self, host, username, password, port, database):
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.database = database
        self.getConnection = self.dbconnection()
        self.connection = self.getConnection[0]
        self.cursor = self.getConnection[1]

    def dbconnection(self):
        connection = pymysql.connect(self.host, self.username, self.password, self.database)
        cursor = connection.cursor(cursor=pymysql.cursors.DictCursor)
        return [connection, cursor]

    def add(self, table, data, sqlPrint=False):
        if table == None:
            print('insert table is null')
            return False

        if data == None:
            print('no data insert into')
            return False

        k1 = []
        v1 = []
        for k, v in data.items():
            k1.append('`' + k + '`')
            v1.append(v)

        key_str = ", ".join(k1)

        value_str = ''
        for i in v1:
            if i == 'null' or i == None or i == 'NULL':
                value_str = value_str + "NULL" + ","
            else:
                value_str = value_str + '"' + str(i) + '"' + ","
        value_str = value_str.rstrip(',')
        sql = "insert into " + table + " (" + key_str + ") values (" + value_str + ");"

        try:
            if sqlPrint == True:
                print(sql)
            self.cursor.execute(sql)
            self.connection.commit()

            # 获取最新的那一条数据的ID
            last_id = self.cursor.lastrowid
            print("最后一条数据的ID是:", last_id)
            return last_id
        except pymysql.MySQLError as e:
            print('insert failed!!' + e)
            self.connection.rollback()
            return False

    def query(self, table, where, sqlPrint=False):
        if table == None:
            print('select table is null')
            return False

        if where == None:
            print('no data found for query')
            return False

        v1 = []
        for k, v in where.items():
            query_colume = k + " = " + "'" + str(v) + "'"
            v1.append(query_colume)

        query_str = " and ".join(v1)
        sql = "select * from " + table + " where " + query_str + ";"

        try:
            if sqlPrint == True:
                print(sql)
            self.cursor.execute(sql)
            query_data = self.cursor.fetchall()
            self.connection.commit()
            return query_data
        except pymysql.MySQLError as e:
            print('query data failed!!' + e)
            self.connection.rollback()
            return False

    def find(self, table, where, sqlPrint=False):
        if table == None:
            print('select table is null')
            return False

        if where == None:
            print('no data found for query')
            return False

        v1 = []
        for k, v in where.items():
            query_colume = k + " = " + "'" + str(v) + "'"
            v1.append(query_colume)

        query_str = " and ".join(v1)
        sql = "select * from " + table + " where " + query_str + ";"

        try:
            if sqlPrint == True:
                print(sql)
            self.cursor.execute(sql)
            query_data = self.cursor.fetchall()
            self.connection.commit()
            if len(query_data) > 0:
                return query_data[0]
            return False
        except pymysql.MySQLError as e:
            print('query data failed!!' + e)
            self.connection.rollback()
            return False

    def update(self, table, where, data, sqlPrint=False):
        if table == None:
            print('update table is null')
            return False

        if where == None:
            print('no where data found for query')

        if data == None:
            print('no data found for update')

        v1 = []
        for k, v in where.items():
            query_colume = k + " = " + "'" + str(v) + "'"
            v1.append(query_colume)

        v2 = []
        for k, v in data.items():
            set_colume = k + " = " + "'" + str(v) + "'"
            v2.append(set_colume)

        query_str = " and ".join(v1)
        set_str = ", ".join(v2)
        sql = "update " + table + " set " + set_str + " where " + query_str + ";"

        try:
            if sqlPrint == True:
                print(sql)
            res = self.cursor.execute(sql)
            self.connection.commit()
            return res
        except pymysql.MySQLError as e:
            print('update data failed!!' + e)
            self.connection.rollback()
            return False

    def all(self, table, order_by=None, limit=None, sqlPrint=False):
        if table == None:
            print('query table is null!')
            return False

        if limit == None and order_by == None:
            sql = "select * from " + table + ";"
        elif limit == None and order_by != None:
            sql = "select * from " + table + " " + order_by + ";"
        elif limit != None and order_by == None:
            sql = "select * from " + table + " order by id desc " + limit + ";"
        elif limit != None and order_by != None:
            sql = "select * from " + table + " " + order_by + " " + limit + ";"

        try:
            if sqlPrint == True:
                print(sql)
            self.cursor.execute(sql)
            query_data = self.cursor.fetchall()
            self.connection.commit()
            return query_data
        except pymysql.MySQLError as e:
            print('query data failed!!' + e)
            return False

    def delete(self, table, where, sqlPrint=False):
        if table == None:
            print('delete table is null!')
            return False

        if where == None:
            print('no where data found for query')
            return False

        v1 = []
        for k, v in where.items():
            query_colume = k + " = " + "'" + str(v) + "'"
            v1.append(query_colume)

        query_str = " and ".join(v1)
        sql = "delete from " + table + " where " + query_str + ";"

        try:
            if sqlPrint == True:
                print(sql)
            res = self.cursor.execute(sql)
            self.connection.commit()
            return res
        except pymysql.MySQLError as e:
            print('delete data failed!!' + e)
            return False

    # 运行原生的查询sql语句
    def run_select_sql(self, sql):
        if sql == None:
            print('select sql can not null!!!')

        try:
            self.cursor.execute(sql)
            query_data = self.cursor.fetchall()
            self.connection.commit()
            return query_data
        except pymysql.MySQLError as e:
            print('sql run failed!!' + e)
            return False
