import pymongo


class MongoDBApi():
    def __init__(self, host, db, collection, port=27017):
        self.host = host
        self.port = port
        self.client = pymongo.MongoClient(self.host, self.port)
        self.db = self.client[db]  # 如果该数据库不存在，则自动创建，否则切换到指定数据库。
        self.collection = self.db[collection]

    def insert(self, data):
        # 数据以列表形式传递
        self.collection.insert_many(data)

    def delete(self, condition):
        self.collection.delete_many(condition)

    def update(self, condition, update_rule):
        self.collection.update_many(condition, update_rule)
        # 例如： collection.update_many(condition, {'$inc': {'age': 1}})，指定了查询条件为age等于24，然后更新条件为{'$inc': {'age': 1}} ，也就是age加1。

    def query(self, condition):
        res = []
        for data in self.collection.find(condition):  # 返回结果是Cursor类型,遍历取到所有的结果
            res.append(data)
        return res




# 参考http://www.ay1.cc/article/2491.html