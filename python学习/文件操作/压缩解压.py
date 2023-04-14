# coding: utf-8
'''
python可以解压缩五种文件：.gz,.tar,.tgz,.zip,.rar
rar：Windows 环境下用的比较多的压缩，比较著名的GUI工具是winrar
tar: Linux系统下的打包工具，只打包，不压缩
gz：即gzip，通常只能压缩一个文件。与tar结合起来就可以实现先打包，再压缩。
tgz：即gz。先用tar打包，然后再用gz压缩得到的文件
zip：不同于gzip，虽然使用相似的算法，可以打包压缩多个文件，不过分别压缩文件，压缩率低于tar
7z：7zip压缩软件支持的格式，压缩效率较高。
'''
import os
import tarfile
import time
import zipfile
import gzip
import rarfile
import py7zr

class FileCompressHaddler():
    def decompress(self, ori_path, target_path, ):
        file_type = os.path.splitext(ori_path)[-1]

        if file_type in ['.tgz','tar', 'gz']:
            with tarfile.open(ori_path) as f:
                f.extractall(target_path)

        elif file_type == '.zip':
            if zipfile.is_zipfile(ori_path):
                with zipfile.ZipFile(ori_path,'r') as f:
                    f.extractall(target_path)
            else:
                print('文件不是正确的zip压缩文件')

        elif file_type == '.rar':
            with rarfile.RarFile(ori_path,'r') as f:
                f.extractall(target_path)

        elif file_type == '.7z':
            with py7zr.SevenZipFile(ori_path, 'r') as f:
                f.extractall(target_path)

    def compress(self, ori_path, target_path):
        file_type = os.path.splitext(target_path)[-1]
        if file_type  == '.gz':
            tar = tarfile.open(target_path, 'w:gz')
            for root, dir, files in os.walk(ori_path):  # 逐个添加文件打包，未打包空子目录。可过滤文件。
                for file in files:
                    fullpath = os.path.join(root, file)  # 拼接路径
                    tar.add(fullpath)  # 添加压缩文件
        elif file_type == '.zip':
            f = zipfile.ZipFile(target_path, "w", zipfile.ZIP_DEFLATED)  # 写模式下，重新写入压缩文件，会将打开之前的压缩文件覆盖掉。
            pre_len = len(os.path.dirname(ori_path))  # 源路径占用长度
            for dirpath, dirs, files in os.walk(ori_path):
                for file in files:
                    if file == target_path:
                        continue
                    filename = os.path.join(dirpath, file)
                    arcname = filename[pre_len:].strip(os.path.sep)  # 相对路径
                    f.write(filename, arcname)
            f.close()
        elif file_type == '.rar':
            rar_path = r'F:\"Program Files (x86)"\WinRAR\WinRAR.exe'
            cmd_command = r'%s a %s %s' % (rar_path, target_path, ori_path)
            print(cmd_command)
            os.system(cmd_command)
        elif file_type == '.7z':
            with py7zr.SevenZipFile(target_path, 'w') as f:
                f.writeall(ori_path)



if __name__ == '__main__':
    fc = FileCompressHaddler()

# tar.gz
    # fc.compress(ori_path='../../data/压缩解压test/', target_path='../../data/test.tar.gz')
    # fc.decompress(ori_path='../../data/test.tar.gz', target_path='../../data/testgz/')

# zip
    # fc.compress(ori_path='../../data/压缩解压test/', target_path='../../data/test.zip')
    # fc.decompress(ori_path='../../data/test.zip', target_path='../../data/testzip/')

#rar
    # fc.compress(ori_path='../../data/压缩解压test/', target_path='../../data/test.rar')
    # fc.decompress(ori_path='../../data/test.rar', target_path='../../data/testrar/')


# 7z
#     fc.compress(ori_path='../../data/压缩解压test/', target_path='../../data/test.7z')
    fc.decompress(ori_path='../../data/test.7z', target_path='../../data/test7z/')
