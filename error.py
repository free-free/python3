#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import logging

"""
	level :
		logging.INFO	
		logging.WARNING
		logging.ERROR
		logging.DEBUG
"""
logging.basicConfig(level=logging.DEBUG)
if __name__=='__main__':
	try:
		print('try....')
		r=10/int('1')
		print('result:',r)
		logging.debug('r=%d'%r)
#	except Exception  as e:
#		print('exception')
#		logging.exception(e)
	except ValueError as e:
		print('ValueError:',e)
		logging.exception(e)
		raise
	except ZeroDivisionError as e:
		print('ZeroDivisionError:',e)
		logging.exception(e)
		raise ValueError('value exception!')
	else:
		print('no error!')
	finally:
		print('finally')
	print('ENG')

