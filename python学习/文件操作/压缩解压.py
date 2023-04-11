# coding: utf-8
# python可以解压缩五种文件：.gz,.tar,.tgz,.zip,.rar
import os
import tarfile
import time
import zipfile
import gzip
import rarfile

class FileCompressHaddler():
    def decompress(self, ori_path, target_path, ):
        file_type = os.path.splitext(ori_path)[-1]

        if file_type in ['.tgz','tar', 'gz']:
            f = tarfile.open(ori_path)
            f.extractall(target_path)
            f.close()
        elif file_type == '.zip':
            if zipfile.is_zipfile(ori_path):
                f = zipfile.ZipFile(ori_path, 'r')
                f.extractall(target_path)
                f.close()
            else:
                print('文件不是正确的zip压缩文件')
        elif file_type == '.rar':
            f = rarfile.RarFile(ori_path,'r')
            f.extractall(target_path)
            f.close()

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
            rar_path = r'F:\Program Files (x86)\WinRAR\WinRAR.exe'
            cmd_command = r'%s a %s %s' % (rar_path, target_path, ori_path)
            print(cmd_command)
            os.system(cmd_command)


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
    fc.decompress(ori_path='../../data/test.rar', target_path='../../data/testrar/')