#!/usr/bin/env python3
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for d in [b'hello',b'john',b'hzou']:
	s.sendto(d,("127.0.0.1",9999))
	data=s.recv(1024)
	print(data.decode('utf-8'))
s.close()
