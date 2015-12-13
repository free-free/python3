#!/usr/bin/env python3
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr,formataddr
import smtplib




def _format_addr(s):
	name,addr=parseaddr(s)
	return formataddr((Header(name,'utf-8').encode(),addr))
from_addr='18281573692@163.com'
password='huangbiao526114'
to_addr='1462086237@qq.com'
smtp_server='smtp.163.com'

msg=MIMEMultipart()
msg['from']=_format_addr('Python Lover<%s>'%from_addr)
msg['to']=_format_addr('administrator<%s>'%to_addr)
msg['subject']=Header('come from 163','utf-8').encode()
msg.attach(MIMEText('Send with File...','plain','utf-8'))

with open('./Picture1.png','rb') as f:
	mime=MIMEBase('image','png',filename='hello.png')
	mime.add_header('Content-Disposition','attachment',filename='hello.png')
	mime.add_header('Content-ID','<0>')
	mime.add_header('X-AttachMent-Id','0')
	mime.set_payload(f.read())
	encoders.encode_base64(mime)
	msg.attach(mime)

server=smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()


