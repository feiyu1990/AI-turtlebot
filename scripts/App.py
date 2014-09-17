from Tkinter import *
import tkSimpleDialog
from PIL import Image, ImageTk
import numpy as np
import os

class App:
	def __init__(self, master):
		#n is number of results
		self.n = 1
		self.currclass = ''
		self.quit = False
		self.ready = False
		self.checkAll = True

		self.addData = False
		self.trainData = False
		self.saveData = False
		self.whatclass = -1
		self.istakepic = False
		self.issavedata =False

		#master.aspect(4,2,4,2)
		bgcolor = "#333"
		fgcolor = "#EEE"
		self.master = master
		self.master.geometry('1200x600')
		self.master.title("Recognizer")
		self.master.config(bg=bgcolor)
		self.master.resizable()
		completeframe = Frame(master, bg=bgcolor)
		completeframe.pack(fill=BOTH)

		#Padding
		padframe = Frame(completeframe, height=30, bg=bgcolor)
		padframe.pack(side=TOP, fill=X)
		padframe = Frame(completeframe, width=50, bg=bgcolor)
		padframe.pack(side=LEFT, fill=BOTH)
		padframe = Frame(completeframe, width=50, bg=bgcolor)
		padframe.pack(side=RIGHT, fill=BOTH)
		padframe = Frame(completeframe, height=50, bg=bgcolor)
		padframe.pack(side=BOTTOM, fill=X)

		title = Label(completeframe, text="Object Recognizer", fg=fgcolor, bg=bgcolor, font=("Arial", 26))
		title.pack()

		padframe = Frame(completeframe, height=40, bg=bgcolor)
		padframe.pack(fill=X)

		pictureframe = Frame(completeframe, bg=bgcolor)
		pictureframe.pack(side=LEFT)
		#photoImage = ImageTk.PhotoImage(Image.open("Screen.png"))
		self.picture = Label(pictureframe)
		#self.picture.image = photoImage
		self.picture.pack()

		padframe = Frame(completeframe, width=50, bg=bgcolor)
		padframe.pack(side=LEFT, fill=Y)

		resultsframe = Frame(completeframe)
		resultsframe.pack(side=LEFT)

		#w = Label(resultsframe, text="Top Results", fg=fgcolor, font=("Arial", 20), bg=bgcolor)
		#w.pack(fill=X)

		padframe = Frame(resultsframe, height=10, bg=bgcolor)
		padframe.pack(fill=X)

		self.stringVars = []
		for i in range(self.n):
			self.stringVars.append(StringVar())
			#if i == 0:
			w = Label(resultsframe, textvariable=self.stringVars[-1], fg="#333", bg="#EEC", font=("Arial", 20), highlightbackground="grey", highlightthickness=1, pady=15, padx=10, width=30)
			#else:
			#	w = Label(resultsframe, textvariable=self.stringVars[-1], fg="#666", font=("Arial", 16), highlightbackground="grey", highlightthickness=1, pady=10, padx=10, width=50)
			w.pack()
			padframe = Frame(resultsframe, height=10, bg=bgcolor)
			padframe.pack(fill=X)


		padframe = Frame(resultsframe, height=10, bg=bgcolor)
		padframe.pack(fill=X)

		commandsframe = Frame(resultsframe, bg=bgcolor)
		commandsframe.pack(side=BOTTOM, fill=X)
		buttonframe = Frame(commandsframe, bg=bgcolor)
		buttonframe.pack()
		runbutton = Button(buttonframe, text="Run", fg="red", command=self.runProgram, bg=bgcolor, highlightbackground=bgcolor)
		toggleControlbutton = Button(buttonframe, text="Toggle Auto", fg="red", command=self.toggleCheckAll, bg=bgcolor, highlightbackground=bgcolor)
		takepicbutton = Button(buttonframe, text="take picture", fg="red", command=self.takepic, bg=bgcolor, highlightbackground=bgcolor).pack()
		savedatabutton = Button(buttonframe, text="savedata", fg="red", command=self.savedata, bg=bgcolor, highlightbackground=bgcolor).pack()
		closebutton = Button(buttonframe, text="Quit", fg="red", command=quit, bg=bgcolor, highlightbackground=bgcolor)
		self.statustext = StringVar()
		self.statustext.set("press Run to start program")
		status=Label(commandsframe, textvariable=self.statustext, fg=fgcolor, bg=bgcolor)
		runbutton.pack(side=LEFT)
		toggleControlbutton.pack()
		closebutton.pack(side=RIGHT)
		padframe = Frame(commandsframe, height=10, bg=bgcolor)
		padframe.pack(fill=X)
		status.pack(side=BOTTOM)
		#master.mainloop()
	def takepic(self):
		self.istakepic = True

	def runProgram(self):
		self.ready = True
		if not self.checkAll:
			self.statustext.set("Running...on its own!")
		else:
			self.statustext.set("Running...with checks")
	def toggleCheckAll(self):
		self.checkAll = not self.checkAll
		if not self.checkAll:
			self.statustext.set("Running...on its own!")
		else:
			self.statustext.set("Running...with checks")
	def quit():
		self.quit = True
		self.master.quit()
	def savedata(self):
		self.issavedata = True
	def isquit(self):
		return self.quit
	
	def updatePhoto(self, inputimg):
		#convertedimg = Image.fromarray(inputimg)
		#convertedimg.show()
		img = ImageTk.PhotoImage(inputimg) 
		self.picture.configure(image = img)
		self.picture.image = img

	def promptUser(self, title, msg):
		print "hey"
		return tkSimpleDialog.askstring(title, msg)
	def addData(self):
		self.addData = True
	def trainData(self):
		self.trainData = True
	def saveData(self):
		self.saveData = True
	def updateResults(self, results, inputimg):
		noun, likelihood = results
		img = ImageTk.PhotoImage(inputimg)
		self.stringVars[0].set(str(noun)+" -> "+str("%.3f" % likelihood)) 
		self.picture.configure(image = img)
		self.picture.image = img
		
		'''if self.currclass != noun:
			os.system("echo \""+noun+"\" | festival --tts")
			self.currclass = noun
		'''		
		'''else:
			self.stringVars[0].set("")
			self.currclass = ""
		'''
		'''noun, likelyhood = results
		self.stringVars[0].set(str(noun)+": "+str("%.3f" % likelyhood))
		'''

if __name__ == "__main__":
	root = Tk()
	app = App(root)
	root.mainloop()
