import os
from tkinter import *
import tkinter as tk
from tkinter import ttk

sys.path.append(os.path.join(os.getcwd(),'../PyBase'))





#Open application main window blocking.
def WindowNew(title:str, resize:bool)->Tk:
	win = Tk()
	win.title(title)
	win.resizable(resize, resize)
	return(win)

#Set focus to control
def CtrlFocus(control:Widget)->bool:
	control.focus()
	return(True)

#Enamble/Disable  control
def CtrlEnable(control:Widget, state:bool)->bool:
	if(state):
		control.configure(state='enable')
	else:
		control.configure(state='disable')
	return(True)


# Add new lable to GUI container.
def LableNew(win:Tk, text:str, column:int, row:int)->ttk.Label:
	lable = ttk.Label(win, text=text)
	lable.grid(column=column, row=row, sticky='W')
	return(lable)

#Set lable text.
def LableText(lable:ttk.Label, text:str, color='black')->bool:
	lable.configure(text=text, foreground = color)
	return(True)


# Add new button to GUI container.
def ButtonNew(win:Tk, lable:str, clic_func, column:int, row:int)->ttk.Button:
	# Adding a Button
	button = ttk.Button(win, text=lable, command=clic_func)
	button.grid(column=column, row=row)
	return(button)

#Set button text and color:'red'.
def ButtonText(button:ttk.Button, text:str, color:str)->bool:
	button.configure(text=text)
	button.configure(foreground=color)

#Add new text-box to container.
def TextBoxNew(win:Tk, text:str, column:int, row:int, columnspan = 0)->(ttk.Entry, tk.StringVar):
	# Adding a Text box Entry widget
	text_box:tk.Text = tk.Text(win)
	if(columnspan):
		text_box.grid(column=column, row=row, columnspan=columnspan)
	else:
		text_box.grid(column=column, row=row, sticky=N+S+W+E)
		text_box.insert('1.0', text)
	return(text_box)

#Add new text-box to container.
def TextEntryNew(win:Tk, column:int, row:int, width, columnspan= 1)->(ttk.Entry, tk.StringVar):
	# Adding a Text box Entry widget
	text_var:tk.StringVar =  tk.StringVar()
	text_box:ttk.Entry = ttk.Entry(win, textvariable=text_var, width = width)
	if(columnspan):	text_box.grid(column=column, row=row, columnspan=columnspan)
	else:   text_box.grid(column=column, row=row, sticky=N+S+W+E)
	return(text_box, text_var)

#Set txt-box text.
def TextBoxText(text_var:tk.StringVar)->str:
	return(text_var.get())

#Add new combo-box to container.
def ComboBoxNew(win:Tk, numbers:tuple ,column:int, row:int, width:int)->(ttk.Combobox,tk.StringVar):
	text_var: tk.StringVar	=  tk.StringVar()
	combo_box = ttk.Combobox(win, width=width, textvariable=text_var)
	combo_box['values'] = numbers
	combo_box.grid(column=column, row=row)
	combo_box.current(0)
	return(combo_box, text_var)

#se combo-box text.
def ComboBoxText(text_var: tk.StringVar) -> str:
	return (text_var.get())

# Add new check-box (stand alone).
def CheckBoxNew(win:Tk, text:str, state:bool, selected:bool ,column:int, row:int)->(tk.Checkbutton, tk.IntVar):
	chVar = tk.IntVar()

	if(not state):	check = tk.Checkbutton(win, text=text, variable=chVar, state='disabled')
	else:	check = tk.Checkbutton(win, text=text, variable=chVar, state='normal')

	if(selected):	check.select()
	else: check.deselect()
	check.grid(column=column, row=row, sticky=tk.W)
	return(check, chVar)

#Add or create new radion button, group of buttons share the same radVar.
def RadioAddNew(win:Tk, text:str, radVar:tk.IntVar, value:int, clic_func, column:int, row:int, columnspan:int)->(tk.Radiobutton,tk.IntVar):
	if(not radVar): radVar = tk.IntVar()
	radio_button:tk.Radiobutton = tk.Radiobutton(win, text=text, variable=radVar, value=value, command=clic_func)
	radio_button.grid(column=column, row=row, sticky=tk.W, columnspan=columnspan)
	return(radio_button, radVar)

#Get radio-button value.
def RadioValue(radio_var: tk.StringVar) -> int:
	return (radio_var.get())


# Add new scrolled Text control to container.
from tkinter import scrolledtext
def TextScrollAdd(win:Tk, scrol_h:int, column:int, row:int, columnspan:int=1)->scrolledtext:
	scroll = scrolledtext.ScrolledText(win, height=scrol_h, wrap=tk.WORD)
	if(columnspan):
		scroll.grid(column=column, row=row, columnspan=columnspan)
	else:
		scroll.grid(column=column, row=row, sticky=E+W)
	return(scroll)

#Get text from Scroll text.
def TextScrollText(text_scroll:scrolledtext)->str:
	return(text_scroll.get('1.0', END+'-1c'))


