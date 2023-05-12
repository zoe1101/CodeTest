'''
判断文件是否存在
文件遍历
文件创建
文件删除
文件复制
文件移动
文件名称修改

更多参考：https://www.cnblogs.com/effortsing/p/10071201.html
'''

import os
import shutil
import stat

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
    # fl = FileHandler()
    # print(fl.is_exist('../../data'))
    # print(fl.get_file_format('../../data/config.ini'))
    # print(fl.traverse_file(dir='../../data', ext='.ini'))
    # fl.create_file('../../data/create_file.txt')
    # fl.copy_file('../../data/create_file.txt', '../../data/压缩解压test')
    # fl.remove_file('../../data/压缩解压test/create_file.txt')
    # fl.move_file('../../data/create_file.txt', '../../data/压缩解压test')
    # fl.remove_file('../../data/压缩解压test/create_file.txt')
    # fl.rename_file('../../data/config.ini', '../../data/confignew.ini')
    # fl.rename_file('../../data/confignew.ini', '../../data/config.ini')
    # fl.rename_file('../../data', '../../datanew')
    # fl.rename_file('../../datanew', '../../data')

    pth = os.getcwd()  # 当前路径
    print(pth)
    print(os.path.dirname(pth))  # 上一级路径
    print(os.path.basename(pth))  # 如果是文件夹，表示当前路径最后一级
    print(os.path.basename('文件路径操作.py'))  # 如果是具体文件，表示获取文件名  文件路径操作.py
    print(os.path.split(pth))  # 拆分路径: 目录+文件,('D:\\CODE\\CodeTest\\python基础', '文件操作')
    print(os.path.splitext('文件路径操作.py')[1])  # 获取文件格式 .py

    # 获取目录或者文件的访问权限
    # Mode:os. F_OK(是否存在)、os.R_OK（可读 ）、os.W_OK（可写）、os.X_OK（可执行）
    print(os.access(pth, os.R_OK))
    # 修改查询文件权限
    os.chmod(pth, stat.S_IROTH) # R代表读,W代表写，X代表执行权限。USR代表用户，GRP代表组，OTH代表其它

    print(os.stat('文件路径操作.py')) # 获取文件属性