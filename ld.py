#!/usr/bin/env python3
#-*- coding:utf-8 -*-
from datetime import datetime
import os 
import sys
dr='.'
if len(sys.argv)>1 and sys.argv[1] !='':
	dr=sys.argv[1]
pwd=os.path.abspath(dr)
print('		Size Last Modified Name')
print('----------------------------------------------------------')
for f in os.listdir(pwd):
		if os.path.isfile(os.path.join(pwd,f)):
			fsize=os.path.getsize(os.path.join(pwd,f))
			mtime=datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
		else:
			fsize=0
			mtime="*"
		flag='/' if os.path.isdir(f) else ''
		print('%10d %s %s%s'%(fsize,mtime,f,flag))

