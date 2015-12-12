#!/usr/bin/env python3
#-*- coding:utf-8 -*-

#metaclass是类的模板,所以必须从'type'类型派生
class ListMetaclass(type):
	"""
		cls 是当前准备创建的类的对象
		name 要创建的类的名字
		bases 类继承的父类的集合
		attrs 类的方法集合
	"""
	def __new__(cls,name,bases,attrs):
		attrs['add']=lambda self,value:self.append(value)
		return type.__new__(cls,name,bases,attrs)
class MyList(list,metaclass=ListMetaclass):
	pass

if __name__=='__main__':
	l=MyList()
	l.add(1)
	print(l)
