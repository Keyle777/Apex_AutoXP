import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.header import Header
from email.utils import formataddr


class DailySentenceEmailSender:
    def __init__(self, content, sender_email, sender_password, receiver_email):
        self.content = content
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.receiver_email = receiver_email
        
    def send_email(self):
        # 发送邮件的配置信息
        config = {
            'host': 'smtp.qq.com',
            'port': 587,
            'user': self.sender_email,
            'password': self.sender_password,
            'sender': self.sender_email,
            'receiver': self.receiver_email
        }

        # 创建邮件体
        message = MIMEMultipart()
        message['From'] = formataddr(['波波', config['sender']])
        message['To'] = formataddr(['波波的Gmail邮箱', config['receiver']])
        message['Subject'] = Header('Apex目前战况', 'utf-8')

        # 添加文本内容
        text = MIMEText(self.content, 'plain', 'utf-8')
        message.attach(text)

        try:
            # 连接到邮件服务器并发送邮件
            smtpObj = smtplib.SMTP(config['host'], config['port'])
            smtpObj.starttls()
            smtpObj.login(config['user'], config['password'])
            smtpObj.sendmail(config['sender'], config['receiver'], message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException as e:
            print("邮件发送失败:", e)