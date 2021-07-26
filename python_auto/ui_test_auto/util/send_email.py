# -*- coding:utf-8 -*-
# @Author:chenjing
"""
    邮件类
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.header import Header


class SendEmail:

    def __init__(self):
        self.mail_host = 'smtp@qq.com'
        self.mail_user = '448788583@qq.com'
        self.mail_password = ''
        self.sender = '448788583@qq.com'
        self.receiver = '448788583@qq.com'

    # send
    def send_email(self):
        """
        发送
        :return:
        """
        try:
            self.con = smtplib.SMTP_SSL(self.mail_host, 465)
            self.con.login(self.mail_user, self.mail_password)
            message = MIMEMultipart()
            file = MIMEText('c', 'html', 'utf-8')
            file['Content-Disposition'] = 'attachment;filename="a.html"'
            img = open('../report/img', 'rb').read()
            img1 = MIMEImage(img)
            img1['Content-Disposition'] = 'attachment;filename="a.png"'
            message.attach(img1)
            message.attach(file)
            message['From'] = Header('448788583@qq.com')
            message['To'] = Header('444444@qq.com')
            message['Subject'] = Header('邮件')
            self.con.sendmail(self.sender, self.receiver, message.as_string())


        except Exception as e:
            print('error%s' % e)


if __name__ == '__main__':
    send = SendEmail()
    send.send_email()
