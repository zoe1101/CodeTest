import paramiko
# python自动化第三方库之paramiko库：连接远程服务器并通过ssh协议远程执行命令

class SSHApi:
    def __init__(self, host='', username='liauto', port=22, password=''):
        self.ip = host
        self.port = port
        self.username = username
        self.password = password
        self.connection = None
        self.connect()

    def connect(self):
        self.connection = paramiko.SSHClient()
        self.connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            if self.password != '':
                self.connection.connect(self.ip, self.port, self.username, (str(self.password)), timeout=5.0)
            else:
                try:
                    self.connection.connect(self.ip, self.port, self.username, look_for_keys=False,
                                            allow_agent=False, timeout=5.0)
                except paramiko.ssh_exception.SSHException:
                    self.connection.get_transport().auth_none(self.username)
                    self.connection.exec_command('uname -a')
                self.connection.sftp = paramiko.SFTPClient.from_transport(self.connection.get_transport())
        except Exception as e:
            try:
                print(str(e.args))
                self.connection = None
            finally:
                e = None
                del e

    def exec_command(self, command):
        # 执行命令并获取命令结果
        stdin, stdout, stderr = self.connection.exec_command(command)
        # stdin为输入的命令
        # stdout为命令返回的结果
        # stderr为命令错误时返回的结果
        return stdin, stdout, stderr


if __name__ == '__main__':
    test = SSHApi()
    stdin, stdout, stderr = test.exec_command('uname -a')
    print(stdout.read())