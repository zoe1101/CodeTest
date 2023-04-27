import pymysql


class MysqlApi(object):
    def __init__(self, host, username, password, db, charset='utf8', port=3306):
        self.host = host
        self.username = username
        self.password = password
        self.db = db
        self.charset = charset
        self.port = port
        self.connect()

    def connect(self):
        try:
            self.conn = pymysql.connect(host=self.host, port=self.port, user=self.username, password=self.password,
                                        db=self.db,
                                        charset=self.charset)
            self.cursor = self.conn.cursor()
        except Exception as err:
            print(err)

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


if __name__ == '__main__':
    pass


# 参考https://www.cnblogs.com/xkdn/p/14227287.html