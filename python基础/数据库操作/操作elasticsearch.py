import time
import functools
from datetime import datetime, timedelta
from elasticsearch import Elasticsearch, helpers


class ElasticsearchApi(object):
    def __init__(self, host='127.0.0.1', port=9200):
        self.es = Elasticsearch(hosts=[{'host': host, 'port': port}])

    def handle_index(self, handler, index):
        """
        index操作
        :param handler: create\delete\clone\refresh\exists
        :param index:
        :return:
        """
        res = getattr(self.es.indices, handler)(index=index)
        print(res)  # {'acknowledged': True}
        return res

    def delete_doc(self, index, idi):
        self.es.delete(index=index, id=idi)

    def update_doc(self, index, idi, body):
        self.es.update(index=index, id=idi, body=body)

    def get_doc(self, index, idi):
        """
        指定索引,文档类型, id 查询出单条数据
        :param index:
        :param idi:
        :return: dict
        """
        res = self.es.get(index=index, id=idi)
        return res.get('_source')

    def search_doc(self, index):
        """
        查询满足条件的所有文档, 没有id属性, 且index, doc_type和body均可为None
        :param index:
        :return: list
        """
        res = self.es.search(index=index)
        return res.get('hits').get('hits')

    def query_doc(self, index, query):
        """
        模糊查询
        :param index:
        :param query: 一个query查询对象(查询条件：Query DSL，match为查询方案，用于分词模糊查询)
        :return:
        """
        return self.es.search(index=index, body=query)

    def create_doc(self, index, body, idi=None):
        """
        插入一条对应索引，文档类型的数据
        :param index:
        :param body: such as {'name': '印度', 'region': '亚洲'}
        :param idi: id可以指定也可以由其自动生成
        :return:
        """
        return self.es.index(index=index, id=idi, body=body)

    def time_decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            start = time.time()
            res = func(self, *args, **kwargs)
            print('共耗时约 {:.2f} 秒'.format(time.time() - start))
            return res

        return wrapper

    @time_decorator
    def bach_gen_doc(self, index, fields, data, action=None):
        if not action:
            action = ({
                "_index": index,
                # "_type": "country",
                "_source": {
                    fields[0]: item[0],
                    fields[1]: item[1],
                    fields[2]: item[2],
                    # ...
                    # es是伦敦时间 kibana是北京时间
                    "create_time": (datetime.utcnow() - timedelta(hours=i)).isoformat(timespec='milliseconds') + 'Z'
                }
            } for i, item in enumerate(data))  # 1000000条,共耗时约 146.50 秒
        return helpers.bulk(self.es, action, stats_only=True)


if __name__ == '__main__':
    ea = ElasticsearchApi()
    # from utils.country import COUNTRY

    # ea.handle_index('delete',index='world')
    # print(ea.bach_gen_doc(index='new_world', fields=['name', 'x_pos', 'y_pos'], data=COUNTRY))
    query = {
        'query': {
            'match': {
                'name': '索'
                # 'name': '中国'
            }
        }
    }
    print(ea.query_doc(index='new_world', query=query))
