#!/usr/bin/env python3
def consume():
	r=''
	while True:
		n=yield r
		if not n:
			return 
		print('[CONSUMER] Consuming %s..'%n)
		r='200 OK'
def produce(c):
	c.send(None)
	n=0
	while n<=10000:
		n=n+1
		print('[PRODUCER] producing %s ...'%n)
		r=c.send(n)
		print('[PRODUCER] Consuming %s...'%r)
	c.close()

if __name__=='__main__':
	c=consume()
	produce(c)

		
