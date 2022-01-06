import smtplib
from email.mime.text import MIMEText
from email.header import Header

'''
首先，调用 email 模块下面的 MIMEText 类，定义发送邮件的正文、格式，以及编码。
然后，调用 email 模块下面的 Header 类，定义邮件的主题和编码类型。
smtplib 模块用于发送邮件。 connect()方法指定连接的邮箱服务； login()方法指定登录
邮箱的账号和密码； sendmail()方法指定发件人、收件人，以及邮件的正文； quit()方法用
于关闭邮件服务器的连接。
'''
# 发送邮件主题
subject = 'Python email test'
# 编写 HTML 类型的邮件正文
msg = MIMEText('<html><h1>你好！ </h1></html>', 'html', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')
# 发送邮件
smtp = smtplib.SMTP()
smtp.connect("smtp.qq.com")
smtp.login("976331609@qq.com", "t.142027.float")
smtp.sendmail("976331609@qq.com", "tangli.1994@163.com", msg.as_string())
