#!/usr/bin/env python3
import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
user='18281573692@163.com'
pwd='huangbiao526114'
pop_server='pop.163.com'

server=poplib.POP3(pop_server)
server.set_debuglevel(1)
print(server.getwelcome().decode('utf-8'))

server.user(user)
server.pass_(pwd)
print('Message:%s. size:%s'%server.stat())

resp,mails,octets=server.list()
index=len(mails)
resp,lines,octets=server.retr(index-1)
msg_content=b'\r\n'.join(lines).decode('utf-8')
#将邮件内容解析为Message对象,
#message 对象本省可能是一个MIMEMutipart对象,
#即包含嵌套其他MIMEBase对象,嵌套可能还不止一层
def guess_charset(msg):
	charset=msg.get_charset()
	if charset is None:
		content_type=msg.get('Content-Type')
		pos=content_type.find('charset=')
		if pos>=0:
			charset=content_type[pos+8:]
	return charset

def decode_str(s):
	value,charset=decode_header(s)[0]
	if charset:
		value=value.decode(charset)
	return value
#递归打印出Message对象的层次结构
def print_info(msg,indent=0):
	if indent==0:
		for header in ['From','To','Subject']:
			value=msg.get(header,'')
			if value:
				if header=='Subject':
					value=decode_str(value)
				else:
					hdr,addr=parseaddr(value)
					name=decode_str(hdr)
					value=u'%s <%s>'%(name,value)
			print('%s%s: %s'%('  '*indent,header,value))
	if (msg.is_multipart()):
			parts=msg.get_payload()
			for n ,part in emnuerate(parts):
				print('%spart %s'%(' '*index,n))
				print('%s--------------------'%(' '*indent))
				print_info(part,indent+1)
	else:
			content_type=msg.get_content_type()
			if content_type=='text/plain' or content_type=='text/html':
				content=msg.get_payload(decode=True)
				charset=guess_charset(msg)
				if charset:
					content=content.decode(charset)
				print('%s Text: %s'%(' '*indent,content+'...'))
			else:
				print('%sAttachment: %s'%(' '*indent,conten_type))


msg=Parser().parsestr(msg_content)
print_info(msg)
server.quit()

