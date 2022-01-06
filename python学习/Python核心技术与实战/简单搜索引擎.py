class SearchEngineBase(object):
    def __init__(self):
        pass

    def add_corpus(self, file_path):
        '''
        负责读取文件内容，将文件路径作为 ID，连同内容一起送到process_corpus 中。
        :param file_path:
        :return:
        '''
        with open(file_path, 'r') as fin:
            text = fin.read()
        self.process_corpus(file_path, text)

    def process_corpus(self, id, txt):
        '''
        需要对内容进行处理，然后文件路径为 ID ，将处理后的内容存下来。处理后的内容，就叫做索引（index）
        :param id:
        :param txt:
        :return:
        '''
        raise Exception('process_corpus not implemented.')

    def search(self, query):
        '''
        给定一个询问，处理询问，再通过索引检索，然后返回
        :param query:
        :return:
        '''
        raise Exception('search not implemented.')


class SimpleEngine(SearchEngineBase):
    def __init__(self):
        super(SimpleEngine, self).__init__()
        self.__id_to_texts = {}

    def process_corpus(self, id, text):
        self.__id_to_texts[id] = text

    def search(self, query):
        results = []
        for id, text in self.__id_to_texts.items():
            if query in text:
                results.append(id)
        return results


search_engine = SimpleEngine()


def main(search_engine):
    '''
    提供搜索器和用户接口
    :param search_engine:
    :return:
    '''
    for file_path in ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']:
        search_engine.add_corpus(file_path)
    while True:
        query = input('请输入你的问题：')
        results = search_engine.search(query)
        print('found {} result(s):'.format(len(results)))
        for result in results:
            print(result)


main(search_engine)
