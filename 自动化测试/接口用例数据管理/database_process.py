# https://mp.weixin.qq.com/s/9gNUZrhRy1ssNis2u3nxNw

import pymysql
import re
import pymongo
import time

from common.Common.log import logs

logger =logs()

#连接mysql数据库
class Connect_Mysql():
    class Connect_Mysql():
        host = "127.0.01"
        port = 3306
        dbname = "api_test_case"  # 实例名
        table = 'api_case'  # 表名
        user = "root"
        pwssword = "123456"

        def __init__(self):
            self.db_connect = pymysql.connect(host=self.host, user=self.user, password=self.pwssword, port=self.port,
                                              db=self.dbname, charset="utf8")
            self.db_cursor = self.db_connect.cursor()  # 游标

        def now_to_date(self):
            str_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            return str_time

        def create_dbname(self):  # 创建实例名
            self.db_cursor.execute('SELECT VERSION()')
            data = self.db_cursor.fetchone()
            print('Database version:', data)
            self.db_cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
            self.db_connect.close()

        def create_table(self):  # 创建数据表
            sql = 'CREATE TABLE IF NOT EXISTS api_case(case_id int(10) unsigned NOT NULL AUTO_INCREMENT,case_nick varchar(100) NOT NULL,case_name varchar(100) NOT NULL,req_url varchar(200) NOT NULL,req_data varchar(3000) DEFAULT NULL,' \
                  'req_headers varchar(100) NOT NULL,req_assert varchar(100) NOT NULL,create_time timestamp NULL DEFAULT CURRENT_TIMESTAMP,modify_time timestamp NULL DEFAULT CURRENT_TIMESTAMP,PRIMARY KEY (case_id),UNIQUE KEY test1 (case_nick) USING BTREE) ENGINE=InnoDB AUTO_INCREMENT=39803 DEFAULT CHARSET=utf8mb4'
            self.db_cursor.execute(sql)
            self.db_connect.close()

        def select_test_case(self, values):  # 查询数据
            sql = 'SELECT count(*) from api_case where case_nick={values}'.format(values=repr(values))
            try:
                self.db_cursor.execute(sql)
                row = self.db_cursor.fetchall()  # 返回有多少记录数
                return row[0][0]
            except:
                logger.error('连接异常')

        def insert_best(self, data):
            list_name = []
            keys = ', '.join(data.keys())
            for dd in data.values():
                list_name.append(dd)
            values = ','.join(['%s'] * len(data))
            sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=self.table, keys=keys, values=values)
            try:
                if self.select_test_case(list_name[0]) > 0:  # 数据库存在则更新修改时间
                    sql2 = 'UPDATE api_case SET modify_time={now_time} where case_nick={values}'.format(
                        now_time=repr(self.now_to_date()), values=repr(list_name[0]))
                    self.db_cursor.execute(sql2)
                    self.db_connect.commit()
                else:  # 数据库不存在则新增
                    self.db_cursor.execute(sql, tuple(data.values()))
                    self.db_connect.commit()
            except Exception as e:
                logger.info('************数据写入数据库失败***************' + str(e))
                self.db_connect.rollback()
            self.db_connect.close()

        def delete_data(self, data):  # 删除数据
            keys = ', '.join(data.keys())
            values = ','.join(['%s'] * len(data))
            sql = 'DELETE from {table} where ({keys})=({values})'.format(table=self.table, keys=keys, values=values)
            try:
                self.db_cursor.execute(sql)
                self.db_connect.commit()
            except:
                logger.error('连接异常')

        def update_data(self, data):  # 更新数据
            keys = ', '.join(data.keys())
            values = ','.join(['%s'] * len(data))
            sql = 'UPDATE {table} SET modify_time={now_time} where case_nick={values}'.format(
                now_time=repr(table=self.table, now_time=self.now_to_date()), values=repr(values))
            try:
                self.db_cursor.execute(sql)
                self.db_connect.commit()
            except:
                logger.error('连接异常')