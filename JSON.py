#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import json
flag='notest'
if flag=='test':
	d=dict(name='huangbiao',age=21,score=99)
	json_str='{"name":"HUANGBIAO","age":21}'
	print(json.dumps(d))
	print(json.loads(json_str))

	f=open('js.txt','w')
	json.dump(d,f)
	f.close()
	f=open("js.txt",'r')
	print(json.load(f))
	f.close()
class Student(object):
	def __init__(self,name,age,score):
		self.name=name
		self.age=age
		self.score=score
	#通常class实例都有一个__dict__属性,用来储存实例变量
def student2dict(std):#指定将对象json序列化的方法
	return {
		'name':std.name,
		'age':std.age,
		'score':std.score
	}
def dict2student(d):
	return Student(d['name'],d['age'],d['score'])
json_obj_str='{"age":20,"score":88,"name":"bob"}'
s=Student('Bo',20,88)
print(json.dumps(s,default=student2dict))
print(json.dumps(s,default=lambda obj:obj.__dict__))
print(json.loads(json_obj_str,object_hook=dict2student))
