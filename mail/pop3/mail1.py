#!/usr/bin/env python3
import poplib
from email.parser import Parser
'''
	get mail from pop server by pop3 protocol
'''

email="18281573692@163.com"
password="huangbiao526114"
pop3_server="pop.163.com"

server=poplib.POP3(pop3_server)
server.set_debuglevel(1)
print(server.getwelcome().decode('utf-8'))

#authenticattion
server.user(email)
server.pass_(password)
#stat()返回邮件数量和占用空间
print('Message:%s. size:%s'%server.stat())
#list()返回所有邮件编号
resp,mails,octets=server.list()
print(mails)
index=len(mails)
#获取最新一封邮件,邮件索引从1开始
resp,lines,octets=server.retr(index-1)
#lines储存了邮件的原始文本的没一行
#可以获得整个邮件的院士文本
msg_content=b'\r\n'.join(lines).decode('utf-8')
#解析出邮件
msg=Parser().parsestr(msg_content)
#可以根据邮件索引号直接从服务器上删除邮件
#server.dele(index)
#关闭链接
print(msg)
with open('msg.txt','w') as f:
	f.write(msg_content)
server.quit()
