#!/usr/bin/env python3
import mysql.connector

conn=mysql.connector.connect(user='root',password='526114',database='test')
cursor=conn.cursor()
cursor.execute('create table user(id varchar(20) primary key,name varchar(2))')
cursor.execute('insert user (id,name) values(%s,%s)',['1','huangbiao'])
print(cursor.rowcount)
conn.commit()
cursor.close()
cursor=conn.cursor()
cursor.execute('select * from user where id=%s',['1'])
values=cursor.fetchall()
print(values)
cursor.close()
conn.close()
