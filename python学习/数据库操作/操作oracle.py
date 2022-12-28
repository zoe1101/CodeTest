import cx_Oracle


class OracleApi(object):
    def __init__(self, user, password, dsn, charset='UTF-8'):
        self.user = user
        self.password = password
        self.dsn = dsn
        self.charset = charset
        self.conn = cx_Oracle.connect(user=self.user, password=self.password, dsn=self.dsn, encoding=self.charset)
        self.cursor = self.conn.cursor()

    def query(self, sql):
        res = ()
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
        except Exception as err:
            print(err)
        finally:
            self.cursor.close()
            return res

    def insert(self, sql):
        return self.__edit(sql)

    def delete(self, sql):
        return self.__edit(sql)

    def update(self, sql):
        return self.__edit(sql)

    def __edit(self, sql):
        res = None
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as err:
            print(err)
        finally:
            self.cursor.close()
            return res

    def close(self):
        self.cursor.close()
        self.conn.close()
