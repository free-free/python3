#!/usr/bin/env python3

import time,threading
balance=0
lock=threading.Lock()
def change_it(n):
	global balance
	balance=balance+n
	balance=balance-n
def run_thread(n):
	for i in range(1000000):
		lock.acquire()
		try:
			change_it(n)
		finally:
			lock.release()

if __name__=='__main__':
	t1=threading.Thread(target=run_thread,args=(5,))
	t2=threading.Thread(target=run_thread,args=(10,))
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	print(balance)
