#!/usr/bin/env python3
from sqlalchemy import Column,String,create_engine,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base
"""
Base=declarative_base()
#定义User表的ORM
class User(Base):
	__tablename__='user'
	id =Column(String(20),primary_key=True)
	name=Column(String(20))

engine=create_engine('mysql+mysqlconnector://root:526114@localhost:3306/test')
DBSession=sessionmaker(bind=engine)

#插入操作
session=DBSession()
new_user=User(id='1',name='Huangbiao')
session.add(new_user)
session.commit()
session.close()
#查询操作
session=DBSession()
user=session.query(User).filter(User.id=='1').one()
print('type:',type(user))
print('name:',user.name)
session.close()

"""
#一对多的关系,一个user对应多本book
Base=declarative_base()
class User(Base):
	__tablename__='user'
	id=Column(String(20),primary_key=True)
	name=Column(String(20))
	books=relationship("Book")
class Book(Base):
	__tablename__='book'
	id=Column(String(20),primary_key=True)
	name=Column(String(20))
	user_id=Column(String(20),ForeignKey('user.id'))
engine=create_engine('mysql+mysqlconnector://root:526114@localhost:3306/test')
DBSession=sessionmaker(bind=engine)
session=DBSession();
books=session.query(User).filter(User.id=='1');
for data in books:
	print(data.id)
	print(data.name)
	for book in data.books:
		print('book id:',book.id)
		print('book name:',book.name)
session.close()

