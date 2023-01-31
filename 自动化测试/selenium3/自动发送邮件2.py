import yagmail
# 连接邮箱服务器
yag = yagmail.SMTP(user="sender@126.com", password="a123456",
host='smtp.126.com')
# 邮件正文
contents = ['This is the body, and here is just text http://somedomain/image.png',
'You can find an audio file attached.']
# 发送邮件
yag.send('receiver@126.com', 'subject', contents)
yag.send(['aa@126.com','bb@qq.com','cc@gmail.com'], 'subject', contents) #给多个用户发邮件
yag.send('aa@126.com', 'subject', contents, ["d://logs.txt","d://baidu_img.jpg"]) #发送带附件的邮件。还可以通过 list 指定多个附件