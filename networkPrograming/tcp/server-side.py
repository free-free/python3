#!/usr/bin/env python3
import socket,threading,time
try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except Exception:
	print('bad connection')
	s.close()
	exit()
s.bind(('121.42.169.254',9999))
#参数为等待连接的最大数量
s.listen(5)
print('waiting for connecting')

def tcplink(sock,addr):
	print('Accept new connection from %s:%s...'%addr)
	sock.send(b'welcome!')
	while True:
		data=sock.recv(1024)
		time.sleep(1)
		if not data or data.decode('utf-8')=='exit':
			break
		sock.send(('Hello,%s'%data).encode('utf-8'))
	sock.close()
	print('connection from %s:%s closed'%addr)

while True:
	sock,addr=s.accept()
	t=threading.Thread(target=tcplink,args=(sock,addr))
	t.start()

