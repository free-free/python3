#!/usr/bin/env python3
import socket
#socket.SOCK_DGRAM 指定这个socket的类型为UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('121.42.169.254',9999))
print("Bing UDP on 9999....")
while True:
	data,addr=s.recvfrom(1024)
	print("Received from %s:%s."%addr)
	s.sendto(b'hello,%s'%data,addr)

