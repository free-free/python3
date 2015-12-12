#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import subprocess
print('$ nslookup')
p=subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out,err=p.communicate(b'set q=mx\npython.org\nexit\n')
print(out.decode('utf-8'))
print('exit code:',p.returncode)
