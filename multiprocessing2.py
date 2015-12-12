#!/usr/bin/env python3
#-*_ coding:utf-8 -*-
import os
from multiprocessing import Process

#子进程要执行的代码
def run_proc(name):
	print("run child process %s (%s)..."%(name,os.getpid()))

if __name__=='__main__':
	print('Parent process %s.'%os.getpid())
	p=Process(target=run_proc,args=('test',))
	print('child process will start')
	p.start()
	p.join()
	print('Child process end.')

