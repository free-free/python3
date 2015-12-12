#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#with open('./read.txt','r') as f:
#	back='a'
#	while  back != '':
#		back=f.read(1)
#		print(back)
with open('./read.txt','r',encoding='utf-8',errors='ignore') as f:
	back='1'
	while not back =='':
		back=f.readline()
		back=back.strip()#把末尾的'\n'删除
		#f.readlines()
		print(back)
