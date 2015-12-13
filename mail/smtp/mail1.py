#!/usr/bin/env python3
#email模块负责构造邮件
#smtplib 负责发送邮件
from email.mime.text import MIMEText
import smtplib
msg=MIMEText('hello,send by python..','plain','utf-8')
from_addr=input('from:')
password=input('password:')
to_addr=input('to:')
smtp_server=input('SMTP server:')

server=smtplib.SMTP(smtp_server,25)
#打印出和smtp服务器交互的所有信息
server.set_debuglevel(1)
#登入smtp服务器
server.login(from_addr,password)
#发送邮件
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()

