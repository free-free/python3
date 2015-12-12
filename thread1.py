#!/usr/bin/env python3

import time,threading
def loop():
	print('Thread %s is running...'%threading.current_thread().name)
	n=0
	while n<5:
		n=n+1
		print('thread %s >>>%s'%(threading.current_thread().name,n))
		time.sleep(1)
	print('thread %s end'%threading.current_thread().name)


if __name__=='__main__':
	print('thread %s is running...'%threading.current_thread().name)
	t=threading.Thread(target=loop,name='LoopThread')
	t.start()
	n=0
	while n<10:
		n=n+1
		print('main thread print')
		time.sleep(1)
	t.join()
	print('thrad %s end'%threading.current_thread().name)

