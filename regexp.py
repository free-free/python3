#!/usr/bin/env python3
import re,sys
s=r'^\d{3}\-\d{3,8}'
if re.match(s,'010-2311'):
	print('matched')
else:
	print('not matched')

print(re.split(r'\s+','ab c d   e'))
m=re.match(r'^(\d{3})-(\d{3,8})$','010-12345')
print(m.group(0))
print(m.group(1))
print(m.group(2))
#贪婪匹配
print(re.match(r'^(\d+)(0*)$','102300').groups())
x=re.compile(s)
x.match('010-2311')
