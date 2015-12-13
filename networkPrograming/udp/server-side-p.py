#!/usr/bin/env python3
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',9999))
print('listening on 127.0.0.1')
while True:
	data,addr=s.recvfrom(1024)
	print('receive msg from %s:%s'%addr)
	s.sendto(b'hello %s'%data,addr)

	
