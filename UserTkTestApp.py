import TkControls

from tkinter import *
import tkinter as tk
from tkinter import ttk





def click_me():
	global my_lable
	global scroll_txt
	print("Button Click")
	lable_text:str = 'Hello ' + TkControls.TextBoxText(my_text_var) + TkControls.ComboBoxText(my_combo_var) + TkControls.TextScrollText(scroll_txt)
	TkControls.LableText(my_lable, lable_text, color='red')
	TkControls.CtrlEnable(my_text_box,False)
	return(True)



# Radiobutton Globals
COLOR:[] = ["Blue", "Gold",  "Red"]
# Radiobutton Callback
def radCall():
	global radVar
	global main_window
	radSel = TkControls.RadioValue(radVar)
	if radSel >= 1 and radSel <= 3: main_window.configure(background=COLOR[radSel-1])



def AppMain():
	global main_window
	main_window = TkControls.WindowNew('Tk Test App', resize = True)

	global my_lable
	my_lable = TkControls.LableNew(main_window, "A Label", column=0, row=0)

	global my_text_var
	global my_text_box
	my_text_box, my_text_var = TkControls.TextBoxNew(main_window, column=0, row=1, width=20)
	TkControls.CtrlFocus(my_text_box)

	global my_button
	my_button =	TkControls.ButtonNew(main_window, "Click Me!", clic_func=click_me, column=1, row=1)


	global my_combo_var
	global my_combo_box
	numbers: tuple = (1, 2, 4, 42, 100)
	my_combo_box, my_combo_var = TkControls.ComboBoxNew(main_window, numbers, column=2, row=1, width=12)

	global check1, chVarDis
	check1, chVarDis = TkControls.CheckBoxNew(main_window, 'Disabled', False, True, column=0, row=4)

	global check2, chVarUn
	check2, chVarUn = TkControls.CheckBoxNew(main_window, 'UnChecked', True, False, column=1, row=4)

	global check3, chVarEn
	check3, chVarEn  = TkControls.CheckBoxNew(main_window,'Enabled', True, True, column=2, row=4)

	global radVar
	radVar = None
	radio = [None]*3
	for col in range(3):
		radio[col],radVar  = TkControls.RadioAddNew(main_window, str(COLOR[col]), radVar, col, radCall, column=col, row=5, columnspan=3)

	global scroll_txt
	scroll_txt = TkControls.TextScrollAdd(main_window, 30, 3, column=0, columnspan= 3)


	main_window.mainloop()

if __name__ == '__main__':
	AppMain()