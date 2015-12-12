#!/usr/bin/env python3
import socket

#创建一个socket
#AF_INET 指定为IPv4协议
#AF_INET6 指定为IPv6协议
#SOCK_STREAM 指定使用面向流的TCP协议
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立连接
data=''
try :
	s.connect(('www.sina.com.cn',80))
except:
	s.close()
	print(r"can't connect to server")
	exit()
#发送请求
s.send(b'GET / HTTP/1.1\r\nHost:www.sina.com.cn\r\nConnection:close\r\n\r\n')
buf=[]
while True:
#指定每次最多接收1K字节的数据
	d=s.recv(1024)
	if d:
		buf.append(d)
	else:
		break
	data=b''.join(buf)

#关闭连接
s.close()
header,html=data.split('\r\n\r\n'.encode('utf-8'),1)
print(header.decode('utf-8'))
with open('sina.html','wb') as f:
	f.write(html)
print('OK')
	


