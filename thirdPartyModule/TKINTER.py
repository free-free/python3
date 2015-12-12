#!/usr/bin/env python3
try:
	from tkinter import *
except ImportError:
	from  tkinter import Frame,Button,Label
class Application(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()
	def createWidgets(self):
		self.helloLabel=Label(self,text='hello')
		self.helloLabel.pack()
		self.quitButton=Button(self,text='Cancel',command=self.quit)
		self.quitButton.pack()

app=Application()
app.master.title('worl')
app.mainloop()
