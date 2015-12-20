#!/usr/bin/env python
from wsgiref.simple_server import make_server

def application(environ,response):
	response('200 OK',[('Content-Type','text/html')])
	body=b'<h1>Hello, %s</h1>'%(environ['PATH_INFO'][1:] or 'web')
	return [body]

httpd=make_server('',80,application)
print('Server HTTP on  port 80...')
httpd.serve_forever()

