#!/usr/bin/env python3

#SQLite是一种嵌入式数据库,它的数据库就是一个文件,由于SQLite本身是c写的,而且
#体积很小,所以经常被集成到各种应用程序中
#Python内置了SQLite3,不需要安装任何东西直接使用
import sqlite3,os

db_file=os.path.join(os.path.dirname(__file__),'test.db')
if os.path.isfile(db_file):
	os.remove(db_file)
#连接数据库,如果数据库不存在,自动在当前目录创建
conn=sqlite3.connect('test.db')
#create a cursor
cursor=conn.cursor()
cursor.execute('create table user (id varchar(10) primary key,name varchar(20))')
cursor.execute('insert into user (id,name) values(\'1\',\'huangbiao\')')
print('insert %s row'%cursor.rowcount)
cursor.execute('select * from user where id=?','1')
values=cursor.fetchall()
print(values)
cursor.close()
#提交事务
conn.commit()
#关闭连接
conn.close()

