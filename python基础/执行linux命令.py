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
        # Popen是subprocess的核心，底层的创建和管理逻辑都是基于它的。使用Popen可以实现一些更复杂的逻辑。
        return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='utf-8').stdout.read()

        #此方法为python3.5版本后的推荐方法，可以获取执行结果、返回内容等一些常用的信息， 满足大部分开发需要。
        # return subprocess.run(cmd, shell=True, capture_output=True, encoding='utf-8').stdout

        # 直接获取命令执行后的输出内容，返回值为str
        # return subprocess.getoutput(cmd)

        '''
        subprocess.call() 为python3.5以前版本使用，与 subprocess.run()用法基本一致，但call()返回的为命令结束码，无法获取更多信息，不推荐使用，现已被run()取代。
        subprocess.check_call() 与call()的区别为，check_call()如果命令失败（即 returncode不为0）会主动抛出subprocess.CalledProcessError异常，使用subprocess.run(check=True)可取代subprocess.check_call()。
        '''

if __name__ == '__main__':
    lc = LinuxCommand()
    print(lc.exec_command_by_system('pwd'))
    print(lc.exec_command_by_popen('pwd'))
    print(lc.exec_command_by_subprocess('pwd'))
