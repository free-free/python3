#!/usr/bin/env python3
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
import smtplib

def _format_addr(s):
	name,addr=parseaddr(s)
	return formataddr((Header(name,'utf-8').encode(),addr))
from_addr=input('from:')
password=input('password:')
to_addr=input('to:')
smtp_server=input('SMTP server:')

msg=MIMEText('hello,send by Python...','plain','utf-8')
msg['From']=_format_addr('Python Lover<%s>'%from_addr)
msg['To']=_format_addr('administer<%s>'%to_addr)
msg['Subject']=Header('come from smtp..','utf-8').encode()

server=smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()

