#!/usr/bin/env python3
#-*- coding:utf-8 -*-
"""
编写单元测试时,测试类必须从unittest.TestCase继承
以test开头的方法就是测试方法,不以test开头的方法不被认为是测试方法
测试的时候不会被执行


"""
import unittest

class Dict(dict):
		def __init__(self,**kw):
			super().__init__(**kw)
		def __getattr__(self,key):
			try:
				return self[key]
			except KeyError:
				raise AttributeError(r"'Dic' objct has not attribute '%s'"%key)
		def __setattr__(self,key,value):
			self[key]=value

class TestDict(unittest.TestCase):
		def test_init(self):
			d=Dict(a=1,b='test')
			self.assertEqual(d.a,1)
			self.assertEqual(d.b,'test')
			self.assertTrue(isinstance(d,dict))

		def test_key(self):
			d=Dict()
			d['key']='value'
			self.assertEqual(d.key,'value')
		def test_attr(self):
			d=Dict()
			d.key='value'
			self.assertTrue('key' in d)
			self.assertEqual(d['key'],'value')
		def test_keyerror(self):
			d=Dict()
			with self.assertRaises(KeyError):
				value=d['empty']
		def test_attrerror(self):
			d=Dict()
			with self.assertRaises(AttributeError):
				value=d.empty
		def setUp(self):
			"""
			setUp()和tearDown()方法。这两个方法会
			分别在每调用一个测试方法的前后分别被执行
			"""
			print('setUp....')
		def tearDown(self):
			print('tearDown....')
if __name__=='__main__':
	unittest.main()#or python3 -m unittest unit_test

