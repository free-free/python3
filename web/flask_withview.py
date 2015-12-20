#!/usr/bin/env python3
from flask import Flask
from flask import request
from flask import render_template

app=Flask(__name__)
@app.route('/',methods=['POST','GET'])
def home():
	return render_template('home.html')
@app.route('/signin',methods=['GET'])
def signin_get():
	return render_template('form.html')
@app.route('/signin',methods=['POST'])
def signin_post():
	username=request.form['user_name']
	password=request.form['password']
	if username.upper()=='ADMIN' and password=='admin':
		return render_template('signin-ok.html',username=username)
	return render_template('form.html',message='Wrong user name or password',username=username)

if __name__=='__main__':
	app.run()

