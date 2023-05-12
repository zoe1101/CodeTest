'''


'''
import yaml
from yaml.loader import SafeLoader


class YamlHandler(object):
    def read(self, file):
        with open(file, 'r', encoding='utf-8') as f:
            data = yaml.load(f, Loader=SafeLoader)
            return data

    def write(self, data, file):
        with open(file, 'w', encoding='utf-8') as f:
            yaml.dump(data, f)


if __name__ == '__main__':
    yml = YamlHandler()
    yamldata = yml.read('../../data/test.yaml')
    print(yamldata)

    yml.write(yamldata, '../../data/testyamlwrite.yaml')
