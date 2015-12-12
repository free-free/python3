#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from io import StringIO
f=StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())
g=StringIO('hello!\nHi!\nGoodbye!')
while True:
	s=g.readline()
	if s=='':
		break
	print(s.strip())

