#!/usr/bin/env python3
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import  parseaddr,formataddr
import smtplib
def _format_addr(s):
	name,addr=parseaddr(s)
	return formataddr((Header(name,'utf-8').encode(),addr))
from_addr=input('from:')
password=input('password:')
to_addr=input('to')
smtp_server=input('smtp server:')

msg=MIMEText('<html><body><h1>Hello</h1>'+
	  '<p>send by <a href="http://www.python.org">Python</a></p>'+
          '</body></html>','html','utf-8')
msg['from']=_format_addr('Python<%s>'%from_addr)
msg['to']=_format_addr('administrator<%s>'%to_addr)
msg['subject']=Header('come from 163 smtp..','utf-8').encode()

server=smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
