import os


class LinuxCommand:
    def exec_command_by_system(self, cmd):
        '''
        os.system方法:
            在子终端运行系统命令，可以获取命令执行后的返回信息以及执行返回的状态
            执行后返回两行结果，第一行是结果， 第二行是执行状态信息
        '''
        # cmd = f'LANG="zh_CN.UTF-8";'+cmd
        # print(cmd)
        return os.system(cmd)

    def exec_command_by_popen(self, cmd):
        '''
        os.popen方法:
            不仅执行命令而且返回执行后的信息对象(常用于需要获取执行命令后的返回信息)，是通过一个管道文件将结果返回
        '''
        po = os.popen(cmd)
        return po.buffer.read().decode('utf-8')

    def exec_command_by_subprocess(self, cmd):
        '''
        subprocess模块:
            运用对线程的控制和监控，将返回的结果赋于一变量，便于程序的处理。有丰富的参数可以进行配置，可供我们自定义的选项多，灵活性高。之前我使用os.system的时候遇到文件描述符被子进程继承的问题，后来通过close_fds = False 这个参数来解决的。
        '''
        import subprocess
        return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read().decode(
            'utf-8')


if __name__ == '__main__':
    lc = LinuxCommand()
    print(lc.exec_command_by_system('pwd'))
    print(lc.exec_command_by_popen('pwd'))
    print(lc.exec_command_by_subprocess('pwd'))
