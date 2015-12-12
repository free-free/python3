#!/usr/bin/env python3

import threading,multiprocessing

def loop():
	x=0
	while True:
		x=x^1
cpu_num=multiprocessing.cpu_count()
print("cput number %s"%cpu_num)
for i in range(cpu_num):
	t=threading.Thread(target=loop)
	t.start()

	

