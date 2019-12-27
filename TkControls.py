from tkinter import *
import tkinter as tk
from tkinter import ttk





#Open application main window blocking.
def WindowNew(title:str, resize:bool)->Tk:
	win = Tk()
	win.title("Welcome to LikeGeeks app")
	win.resizable(resize, resize)
	return(win)

#Set focus to control
def CtrlFocus(control:Widget)->bool:
	control.focus()
	return(True)

#Set focus to control
def CtrlEnable(control:Widget, state:bool)->bool:
	if(state):
		control.configure(state='enable')
	else:
		control.configure(state='disable')
	return(True)


# Adding a Label.
def LableNew(win:Tk, text:str, column:int, row:int)->ttk.Label:
	lable = ttk.Label(win, text=text)
	lable.grid(column=column, row=row)
	return(lable)

def LableText(lable:ttk.Label, text:str, color='black')->bool:
	lable.configure(text=text, foreground = color)
	return(True)


# Adding a button.
def ButtonNew(win:Tk, lable:str, clic_func, column:int, row:int)->ttk.Button:
	# Adding a Button
	button = ttk.Button(win, text=lable, command=clic_func)
	button.grid(column=column, row=row)
	return(button)

def ButtonText(button:ttk.Button)->bool:
	button.configure(text="** I have been Clicked! **")
	button.configure(foreground='red')


def TextBoxNew(win:Tk, column:int, row:int, width:int)->(ttk.Entry, tk.StringVar):
	# Adding a Text box Entry widget
	text_var:tk.StringVar =  tk.StringVar()
	text_box:ttk.Entry = ttk.Entry(win, width=width, textvariable=text_var)
	text_box.grid(column=column, row=row)
	return(text_box, text_var)

def TextBoxText(text_var:tk.StringVar)->str:
	return(text_var.get())


def ComboBoxNew(win:Tk, numbers:tuple ,column:int, row:int, width:int)->(ttk.Combobox,tk.StringVar):
	text_var: tk.StringVar	=  tk.StringVar()
	combo_box = ttk.Combobox(win, width=width, textvariable=text_var)
	combo_box['values'] = numbers
	combo_box.grid(column=column, row=row)
	combo_box.current(0)
	return(combo_box, text_var)

def ComboBoxText(text_var: tk.StringVar) -> str:
	return (text_var.get())

# Create a new stand alone checkbox.
def CheckBoxNew(win:Tk, text:str, state:bool, selected:bool ,column:int, row:int)->(tk.Checkbutton, tk.IntVar):
	chVar = tk.IntVar()

	if(not state):	check = tk.Checkbutton(win, text=text, variable=chVar, state='disabled')
	else:	check = tk.Checkbutton(win, text=text, variable=chVar, state='normal')

	if(selected):	check.select()
	else: check.deselect()
	check.grid(column=column, row=row, sticky=tk.W)
	return(check, chVar)

#Add or create new radion button.
def RadioAddNew(win:Tk, text:str, radVar:tk.IntVar, value:int, clic_func, column:int, row:int, columnspan:int)->(tk.Radiobutton,tk.IntVar):
	if(not radVar): radVar = tk.IntVar()
	radio_button:tk.Radiobutton = tk.Radiobutton(win, text=text, variable=radVar, value=value, command=clic_func)
	radio_button.grid(column=column, row=row, sticky=tk.W, columnspan=columnspan)
	return(radio_button, radVar)

def RadioValue(radio_var: tk.StringVar) -> int:
	return (radio_var.get())


# Using a scrolled Text control
from tkinter import scrolledtext
def TextScrollAdd(win:Tk, scrol_w:int, scrol_h:int, column:int, columnspan:int)->scrolledtext:
	scroll = scrolledtext.ScrolledText(win, width=scrol_w, height=scrol_h, wrap=tk.WORD)
	scroll.grid(column=column, columnspan=columnspan)
	return(scroll)

def TextScrollText(text_scroll:scrolledtext)->str:
	return(text_scroll.get('1.0', END+'-1c'))