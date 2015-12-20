#!/usr/bin/env python3
import threading
import asyncio

@asyncio.coroutine
def hello():
	print('Hello (%s)'%threading.current_thread().name)
	yield from asyncio.sleep(1)
	print('hello again %s'%threading.current_thread().name)
loop=asyncio.get_event_loop()
tasks=[hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

