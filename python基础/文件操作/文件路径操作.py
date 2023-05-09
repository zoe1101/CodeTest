'''
判断文件是否存在
文件遍历
文件创建
文件删除
文件复制
文件移动
文件名称修改
'''

import os
import shutil


class FileHandler:
    def is_exist(self, filepath):
        return os.path.exists(filepath)

    def traverse_file(self, dir, ext=None):
        '''
        文件遍历
        :param dir:
        :param ext:
        :return:
        '''
        file_list = []
        if os.path.isdir(dir):
            for home, dirs, files in os.walk(dir):
                for file in files:
                    if not format:
                        file_list.append(os.path.join(home, file))
                    else:
                        file_list.extend([os.path.join(home, file)] if self.get_file_format(file) == ext else [])
        elif os.path.isfile(dir):
            file_list.append(dir)

        return file_list

    def create_file(self, file):
        if not self.is_exist(file):
            if not self.get_file_format(file):  # 文件夹
                os.mkdir(file)
            else:  # 文件
                open(file, 'w')

    def copy_file(self, file, target_dir):
        shutil.copy(file, target_dir)

    def move_file(self, file, target_dir):
        shutil.move(file, target_dir)

    def remove_file(self, file, ext=None):
        file_list = self.traverse_file(file, ext)
        for f in file_list:
            os.remove(f)

    def rename_file(self, filename, target_filename):
        os.rename(filename, target_filename)

    def get_file_format(self, file):
        return os.path.splitext(file)[-1]


if __name__ == '__main__':
    fl = FileHandler()
    print(fl.is_exist('../../data'))
    print(fl.get_file_format('../../data/config.ini'))
    print(fl.traverse_file(dir='../../data', ext='.ini'))
    fl.create_file('../../data/create_file.txt')
    fl.copy_file('../../data/create_file.txt', '../../data/压缩解压test')
    fl.remove_file('../../data/压缩解压test/create_file.txt')
    fl.move_file('../../data/create_file.txt', '../../data/压缩解压test')
    fl.remove_file('../../data/压缩解压test/create_file.txt')
    fl.rename_file('../../data/config.ini', '../../data/confignew.ini')
    fl.rename_file('../../data/confignew.ini', '../../data/config.ini')
    fl.rename_file('../../data', '../../datanew')
    fl.rename_file('../../datanew', '../../data')
