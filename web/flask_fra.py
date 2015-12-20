#!/usr/bin/env python3
from flask import Flask
from flask import request

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
	return '<h1>Home</h1>'
@app.route('/signin',methods=['GET'])
def signin_get():
	return '''<form action='/signin' method='post'>
		<p><input type="text" name="user_name"></p>
		<p><input type="password" name="password"></p>
		<p><button type="submit">Sign In</button></p>
		</form>'''
@app.route('/signin',methods=['POST'])
def signin_post():
	if request.form['user_name']=='admin' and request.form['password']=='password':
		return '<h1>Hello,Admin!</h1>'
	return '<h1>Bad Username or password.</h1>'
if __name__=='__main__':
	app.run()


