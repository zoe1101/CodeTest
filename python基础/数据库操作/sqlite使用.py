import sqlite3


class SqliteApi:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()

    def execute_sql(self, sql):
        res = self.cursor.execute(sql)
        self.conn.commit()
        return res

    def close(self):
        self.conn.close()


if __name__ == '__main__':
    sa = SqliteApi('../../data/test.db')
    # 建表
    # sa.execute_sql('''CREATE TABLE IF NOT EXISTS COMPANY
    #    (ID INT PRIMARY KEY     NOT NULL,
    #    NAME           TEXT    NOT NULL,
    #    AGE            INT     NOT NULL,
    #    ADDRESS        CHAR(50),
    #    SALARY         REAL);''')
    # 插入
    sa.execute_sql("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'ABC', 23, 'ABC', 200.00 )")
    # 查询
    res = sa.execute_sql("SELECT * FROM COMPANY")
    for row in res:
        print(row)
    print(res)

    # 更新
    sa.execute_sql("UPDATE COMPANY set SALARY = 200.00 where ID=2")

    # 查询
    res = sa.execute_sql("SELECT * FROM COMPANY")
    for row in res:
        print(row)
    print(res)

    # 删除
    sa.execute_sql("DELETE from COMPANY where ID=2;")

    sa.close()
