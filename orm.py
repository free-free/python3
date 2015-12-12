#!/usr/bin/env python3
#-*- coding:utf-8 -*-
class Field(object):
	def __init__(self,name,columns_type):
		self.name=name
		self.columns_type=columns_type


class StringField(Field):
	def __init__(self,name):
		super(StringField,self).__init__(name,'varchar(20)')


class IntField(Field):
	def __init__(self,name):
		super(IntField,self).__init__(name,'int unsigned')


class ModelMetaclass(type):
	def __new__(cls,name,bases,attrs):
		if name=='Model':
			return type.__new__(cls,name,bases,attrs)
		print ('Found model %s'%name)
		mappings=dict()
		for k,v in attrs.items():
			if isinstance(v,Field):
				print('Found mapping:%s==>%s'%(k,v))
				mappings[k]=v
		for k in mappings.keys():
			attrs.pop(k)
		attrs['__mappings__']=mappings
		attrs['__table__']=name
		return type.__new__(cls,name,bases,attrs)


class Model(dict,metaclass=ModelMetaclass):
	def __init__(self,**kw):
		super(Model,self).__init__(**kw)
	def __getattr__(self,name):
		try:
			return self[name]
		except KeyError:
			raise AttributeError(r"'Model' object has not attribute %s"%name)
	def __setattr__(self,name,value):
		self[name]=value
	def save(self):
		fields=[]
		params=[]
		args=[]
		for k ,v in self.__mappings__.items():
			fields.append(v.name)
			params.append(str(getattr(self,k)))
			args.append(getattr(self,k,None))
		sql='insert into %s (%s) values(%s)'%(self.__table__,','.join(fields),','.join(params))
		print("SQL %s"%sql)
		print("ARGS %s"%str(args))


class User(Model):
	id=IntField('id')
	name=StringField('user_name')
	email=StringField('user_email')
	password=StringField('password')

if __name__=='__main__':
	u=User(id=1,name='huangbiao',email='1994122hb@gmail.com',password="huangbiao526114")		
	u.save()
