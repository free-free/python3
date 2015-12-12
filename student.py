#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
import types
from collections import Iterable
from collections import Iterator
from types import MethodType
from functools import reduce
from functools import wraps
from enum import Enum,unique

@unique
class Weekday(Enum):
	Sun=0
	Mon=1
	Tue=2
	Wed=3
	Thu=4
	Fri=5
	Sat=6
class Student(object):
	__slots__=('_name','_age')	
	item={}
	def __init__(self,name,age):
		self._name=name
		self._age=age
	@property
	def name(self):
		return self._name
	@name.setter
	def name(self,value):
		if not isinstance(value,str):
			raise ValueError('name must be string')
		self._name=value
	@property
	def age(self):
		return self._age
	def __str__(self):
		return "the student class!"	
	__repr__=__str__
	def __iter__(self):
		return self
	def __next__(self):
		self.a,self.b=self.b,self.a+self.b
		if self.a>10000:
			raise StopIteration()
		return self.a
	def __getitem__(self,n):
		if isinstance(n,int):
			a,b=1,1
			for x in range(n):
				a,b=b,b+a
			return a
		if isinstance(n,slice):
			start=n.start
			stop=n.stop	
			if start is None:
				start=0
			a,b=1,1
			L=[]
			for x in range(stop):
				if x>=start:
					L.append(a)
				a,b=b,a+b
			return L
	def __getattr__(self,attr):
		if attr!='gender':
			if attr in self.item:
				return self.item[attr]
			return 'none'
		if attr=='gender':
			return lambda:'male'
	def __call__(self):
		print('My name is %s.'%self._name)
	def __setattr__(self,name,value):
		self.item[name]=value
	
if __name__=='__main__':
	Month=Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
	for name,member in Month.__members__.items():
		print(name,'==>',member,',',member.value)
	for name,member in Weekday.__members__.items():
		print(name,':',member,',',member.value)


		
		
		
