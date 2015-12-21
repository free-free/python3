#!/usr/bin/env python3
import os,re
class Status(object):
	def __init__(self,commands):
		self.cmd=commands
	def get_release(self):
		result=os.popen('lsb_release -a').readlines()
		res=[]
		for x in result:
			line=re.match(r'^Description:\t(.*)',x)
			if line:
				res.append(line.group(1))
		if len(res)>=1:
			return res[0].strip()
		return ''
	def get_kernel(self):
		result=os.popen('uname -r').readlines()
		if result:
			return result[0].strip()
		return ''
	def get_datetime(self):
		result=os.popen("date +'%Y/%m/%d %H:%M:%S'").readlines()
		if result:
			return result[0].strip()
		return ''
	def get_status(self):
		status='Release : '+self.get_release()+'\r\n'
		status=status+'Kernel : '+self.get_kernel()+'\r\n'
		status=status+'Datetime : '+self.get_datetime()
		return status
	def __str__(self):
		return self.get_status()
	__repr__=__str__
	
if __name__=='__main__':
	print(Status('dede'))
	
