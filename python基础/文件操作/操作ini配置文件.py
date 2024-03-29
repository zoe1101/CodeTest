'''
后缀名.ini 用于存储项目全局配置变量
比如：接口地址 项目地址....输出文件路径

ini文件编写格式
[节点]
选项=选项值
注释前面加;


注意：节点不可以重复
'''
import configparser


class INIHelper(object):
    def __init__(self):
        self.config = configparser.ConfigParser()

    def get_sections(self):  # 获取ini文件中所有的节点
        return self.config.sections()

    def get_options(self, section):  # 获取ini文件中某个节点下所有选项
        return self.config.options(section)

    def get_value(self, section, option):  # 获取某个节点下某个选项的选项值
        return self.config.get(section=section, option=option)

    def get_items(self, section):  # 获取某个节点下的所有选项及选项值  ---》元组列表
        return self.config.items(section=section)

    def add_node(self, section, option, value):  # 添加节点
        if section not in self.get_sections():
            self.config.add_section(section)
            self.config.set(section, option, value)

    def remove_node(self, section):  # 删除节点
        if section not in self.get_sections():
            self.config.remove_section(section)

    def remove_option(self, section, option):  # 删除选项及选项值
        self.config.remove_option(section, option)

    @staticmethod
    def read_from_ini(path, section=None, option=None, encoding=None):
        """
        读取ini文件，变成python格式并返回。
        :param path: 文件路径
        :param section: 段名，可不传，不传返回所有段 ，传入时返回指定段
        :param option: 选项名，可不传，传入时，需要和段名配合使用。
        :param encoding: 编码，默认为utf8
        :return: 当同时传入段名以及选项名时，返回字符串，其他情况返回字典。
        """
        config = configparser.ConfigParser()
        config.read(path, encoding=encoding)
        res = dict()

        if not section:
            sections = config.sections()
            for temp_section in sections:
                section_values = config.items(temp_section)
                res[temp_section] = section_values
            return res
        else:
            if not config.has_section(section):
                return None
            if not option:
                res[section] = config.items(section)
                return res
            else:
                if not config.has_option(section, option):
                    return None
                return config.get(section, option)

    @classmethod
    def write_to_ini(cls, path, data: dict, mode='a', encoding='utf8'):
        """
        将配置写入ini
        :param path: 文件路径
        :param data: 多层dict,形如下方:
        {"user1": [('name','wangwu'),('age','18')]}
        或者
        {"user2":{"name":"zhaoliu","age":"19"}}
        :param mode:写入模式，a为追加，w 为覆盖
        :param encoding: 编码，默认utf8
        :return: 返回值
        """
        try:
            config = configparser.ConfigParser()
            for section in data:
                if not config.has_section(section):
                    config.add_section(section)
                    if isinstance(data[section], tuple) or isinstance(data[section], list):
                        for key, value in data[section]:
                            config.set(section, key, str(value))
                    if isinstance(data[section], dict):
                        for key, value in data[section].items():
                            config.set(section, key, str(value))
            config.write(open(path, mode, encoding=encoding))

            return True
        except:
            return False


if __name__ == '__main__':
    file_path = '../../data/config.ini'  # 相对路径
    print(INIHelper.read_from_ini(file_path))
    # {'user_info': [('name', 'zhangsan'), ('age', '18'), ('gender', '男'), ('is_admin', 'true')],
    # 'connect': [('host', '127.0.0.1'), ('user', 'db'), ('password', '123456'), ('port', '1521'), ('db', 'zet')]}

    print(INIHelper.read_from_ini(file_path, 'user_info'))
    # {'user_info': [('name', 'zhangsan'), ('age', '18'), ('gender', '男'), ('is_admin', 'true')]}

    print(INIHelper.read_from_ini(file_path, 'connect', 'host'))
    # 127.0.0.1

    print(INIHelper.read_from_ini(file_path, 'connect', 'host1'))  # 获取不存在的数据项
    # None

    save_path = '../../data/config_w.ini'
    # data = INIHelper.read_from_ini(file_path)
    # data['user1'] = [('name', 'www'), ('age', '18')]
    data = dict()
    data['user1'] = {'name': 'zhangsan', 'age': 18}
    res = INIHelper.write_to_ini(save_path, data)
    print(res)
