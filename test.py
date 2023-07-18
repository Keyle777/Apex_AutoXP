from send import *
import configparser
import datetime

config = configparser.ConfigParser()
config.read('emailInfo.ini')
sender_email = config.get('email', 'sender_email')
sender_password = config.get('email', 'sender_password')
receiver_email = config.get('email', 'receiver_email')
count = 0

now = datetime.datetime.now()
formatted_time = now.strftime("%Y年%m月%d日%H时%M分%S秒")
sendEmail =  DailySentenceEmailSender(f"游戏于{formatted_time}发生错误，正在重新加入游戏中",sender_email,sender_password,receiver_email)
sendEmail.send_email()