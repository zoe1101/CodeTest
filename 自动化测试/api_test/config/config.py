import yaml


def read_config():
    with open('config.yaml', "r", encoding="utf-8") as f:
        conf = yaml.load(f.read(), Loader=yaml.FullLoader)
        print('正在加载环境变量')
        return conf
