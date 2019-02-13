#Python Calculator GUI
from tkinter import *

calculator = Tk()

calculator.title("Python Calculator")

calculator.geometry("250x300")

#global vars--------------------------------------------------------------------------------

display = []

entryText = StringVar()

#functions------------------------------------------------------------------------------------

#def equals():
	#global display
	#count = 0
	#count_ = 0
	#vector = []
	#for e in display:
		#count_ = count_ + 1
		#vector.append(e)
		#if e == '+' or e == '-' or e == '*' or e == '/':
			#count = count + 1
			#if count == 2:



def click7():
	display.append('7')
	entryText.set(display)

def click8():
	display.append('8')
	entryText.set(display)

def click9():
	display.append('9')
	entryText.set(display)

def click4():
	display.append('4')
	entryText.set(display)

def click5():
	display.append('5')
	entryText.set(display)

def click6():
	display.append('6')
	entryText.set(display)

def click1():
	display.append('1')
	entryText.set(display)

def click2():
	display.append('2')
	entryText.set(display)

def click3():
	display.append('3')
	entryText.set(display)

def click0():
	display.append('0')
	entryText.set(display)

def clickSum():
	display.append('+')
	entryText.set(display)

def clickSubs():
	display.append('-')
	entryText.set(display)

def clickMult():
	display.append('*')
	entryText.set(display)

def clickDiv():
	display.append('/')
	entryText.set(display)

def clickCE():
	entryText.set(' ')
	del display[:]


#widgets-------------------------------------------------------------------------------------

button7 = Button(calculator, text = "7", fg = "blue", command = click7).place(x = 20, y = 50, width = 40)

button8 = Button(calculator, text = "8", fg = "blue", command = click8).place(x = 70, y = 50, width = 40)

button9 = Button(calculator, text = "9", fg = "blue", command = click9).place(x = 120, y = 50, width = 40)

button4 = Button(calculator, text = "4", fg = "blue", command = click4).place(x = 20, y = 80, width = 40)

button5 = Button(calculator, text = "5", fg = "blue", command = click5).place(x = 70, y = 80, width = 40)

button6 = Button(calculator, text = "6", fg = "blue", command = click6).place(x = 120, y = 80, width = 40)

button1 = Button(calculator, text = "1", fg = "blue", command = click1).place(x = 20, y = 110, width = 40)

button2 = Button(calculator, text = "2", fg = "blue", command = click2).place(x = 70, y = 110, width = 40)

button3 = Button(calculator, text = "3", fg = "blue", command = click3).place(x = 120, y = 110, width = 40)

button0 = Button(calculator, text = "0", fg = "blue", command = click0).place(x = 70, y = 140, width = 40)

buttonSum = Button(calculator, text = "+", fg = "red", command = clickSum).place(x = 170, y = 50, width = 40)

buttonSubs = Button(calculator, text = "-", fg = "red", command = clickSubs).place(x = 170, y = 80, width = 40)

buttonMult = Button(calculator, text = "*", fg = "red", command = clickMult).place(x = 170, y = 110, width = 40)

buttonDiv = Button(calculator, text = "/", fg = "red", command = clickDiv).place(x = 170, y = 140, width = 40)

buttonClose = Button(calculator, text = "CE", fg = "red", command = clickCE).place(x = 120, y = 140, width = 40)

buttonBack = Button(calculator, text = "<-", fg = "red").place(x = 20, y = 140, width = 40)

labelDisplay = Entry(calculator, textvariable = entryText).place(x = 100 , y = 10 )

calculator.mainloop()
