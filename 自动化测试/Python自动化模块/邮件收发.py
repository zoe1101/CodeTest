# coding=utf-8
'''
一封电子邮件的旅程就是：
    发件人 -> MUA -> MTA -> MTA -> 若干个MTA -> MDA <- MUA <- 收件人

编写程序来发送和接收邮件，本质上就是：
    编写MUA把邮件发到MTA；
    编写MUA从MDA上收邮件。

Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。
Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。
发送邮件的基本步骤：代码发送邮件的步骤，和人工发送邮件步骤基本一致：登录邮箱 -> 准备邮件内容 -> 发送邮件。
'''
import poplib
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.parser import Parser
from email.header import decode_header, Header
from email.utils import parseaddr, formataddr


def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


class EmailOP:
    def __init__(self):
        self.smtp_server = 'smtp.126.com'
        self.pop3_server = 'pop.126.com'
        self.smtp_port = 25
        self.from_email = 'testyy1101@126.com'
        self.from_password = 'BBLBUZDWHOLEHSCL'  # 授权码
        self.to_email = ['testyy1101@126.com']

    def send(self):
        # 连接到SMTP服务器:
        server = smtplib.SMTP(self.smtp_server, self.smtp_port)  # SMTP协议默认端口是25
        # 打开或关闭调试信息:
        server.set_debuglevel(1)
        server.login(self.from_email, self.from_password)

        msg = MIMEMultipart()  # 创建邮件对象
        msg['Subject'] = Header('测试邮件发送', 'utf-8').encode()  # 主题
        msg['From'] = _format_addr('Python爱好者 <%s>' % self.from_email)  # 发件人
        msg['To'] = _format_addr('管理员 <%s>' % self.to_email[0])  # 收件人
        msg.attach(MIMEText("""
                            <h2>我是正⽂中的标题</h2>
                            <p>邮件正文描述性文字1</p>
                            <p>邮件正⽂描述性文字2</p>
                            <img src='https://www.baidu.com/img/bd_logo1.png'> <center>百度图片</center>
                            <a href='https://www.baidu.com'>百度⼀下</a>
                            """,
                            'html', 'utf-8'))   # 邮件正文
        # 添加附件
        file1 = MIMEText(open('../../data/test.png', 'rb').read(), 'base64', 'utf-8')
        file1["Content-Disposition"] = 'attachment; filename="test.png"'
        msg.attach(file1)

        # 发送邮件
        server.sendmail(self.from_email, self.to_email, msg.as_string())
        print('邮件发送成功！')
        server.quit()

    def receive(self):
        # 连接到POP3服务器:
        server = poplib.POP3(self.pop3_server)
        # 打开或关闭调试信息:
        server.set_debuglevel(1)
        # 可选:打印POP3服务器的欢迎文字:
        print(server.getwelcome().decode('utf-8'))

        # 身份认证:
        server.user(self.from_email)
        server.pass_(self.from_password)

        # stat()返回邮件数量和占用空间:
        total, totalnum = server.stat()  # 邮件的数量和邮件总的字节数
        print(total, totalnum)  # 打印显示统计信息

        # list()返回所有邮件的编号:
        resp, mails, octets = server.list()
        # 查看返回的列表类似[b'1 82923', b'2 2184', ...]
        print(mails)

        # 获取最新一封邮件, 注意索引号从1开始:
        index = len(mails)
        resp, lines, octets = server.retr(index)

        # 获得整个邮件的原始文本,lines存储了邮件的原始文本的每一行:
        msg_content = b'\r\n'.join(lines).decode('utf-8')
        print('邮件内容：', msg_content)


        # 解析出邮件,Message对象本身可能是一个MIMEMultipart对象，即包含嵌套的其他MIMEBase对象，嵌套可能还不止一层。
        # msg = Parser().parsestr(msg_content)
        # print_info(msg)  # 邮件层级解析
        # 根据邮件索引号直接从服务器删除邮件:
        # server.dele(index)
        # 关闭连接:
        server.quit()


# indent用于缩进显示:
def print_info(msg, indent=0):
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % ('  ' * indent, header, value))
    if msg.is_multipart():
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))
            print('%s--------------------' % ('  ' * indent))
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('  ' * indent, content + '...'))
        else:
            print('%sAttachment: %s' % ('  ' * indent, content_type))


e = EmailOP()
e.send()
e.receive()
