'''
后缀名：.yaml .yml
'''
import yaml
from yaml.loader import SafeLoader


class YamlHandler(object):
    def read(self, file):
        #反序列化：从文件转换为Python对象
        with open(file, 'r', encoding='utf-8') as f:
            data = yaml.load(f, Loader=SafeLoader)
            return data

    def write(self, data, file):
        #纯量、对象、数组(Python对象) -----》yaml文件 序列化（持久化）
        with open(file, 'w', encoding='utf-8') as f:
            yaml.dump(data, f)


if __name__ == '__main__':
    yml = YamlHandler()
    yamldata = yml.read('../../data/test.yaml')
    print(yamldata)

    yml.write(yamldata, '../../data/testyamlwrite.yaml')
