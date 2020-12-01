import os
import sys

from PyBaseGUI import TkBase
from PyBaseGUI import TkControls
from PyBaseGUI import TkLayouts

# Set project include path.
sys.path.append(os.path.join(os.getcwd(),'../'))





######################################################################
#                                                                    #
#							Tk GUI Test								 #
#                                                                    #
######################################################################

def button_click():
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
def radio_click():
	global radVar
	global main_window
	radSel = TkControls.RadioValue(radVar)
	if radSel >= 0 and radSel <= 2: main_window.configure(background=COLOR[radSel])


def menu_click():
	print("MenuClicked")
	return

def quite_click():
	global main_window
	TkBase._quit(main_window)
	return









def AppMain():
	global main_window
	main_window = TkControls.WindowNew('Tk Test App', resize = True)
	main_frame = TkLayouts.FrameNew(main_window, 'Main Frame', column=0, row= 0, padding= 20)

	#Add read only lable to a frame.
	global my_lable
	my_lable = TkControls.LableNew(main_frame, "A Label", column=0, row=0)

	# Add editable text box to a frame.
	global my_text_var
	global my_text_box
	my_text_box, my_text_var = TkControls.TextBoxNew(main_frame, column=0, row=1, width=20)
	TkControls.CtrlFocus(my_text_box)

	global my_button
	my_button =	TkControls.ButtonNew(main_frame, "Click Me!", clic_func=button_click, column=1, row=1)


	global my_combo_var
	global my_combo_box
	numbers: tuple = (1, 2, 4, 42, 100)
	my_combo_box, my_combo_var = TkControls.ComboBoxNew(main_frame, numbers, column=2, row=1, width=12)

	global check1, chVarDis
	check1, chVarDis = TkControls.CheckBoxNew(main_frame, 'Disabled', False, True, column=0, row=4)
	global check2, chVarUn
	check2, chVarUn = TkControls.CheckBoxNew(main_frame, 'UnChecked', True, False, column=1, row=4)
	global check3, chVarEn
	check3, chVarEn  = TkControls.CheckBoxNew(main_frame, 'Enabled', True, True, column=2, row=4)

	global radVar
	radVar = None
	radio = [None]*3
	for col in range(3):
		radio[col],radVar  = TkControls.RadioAddNew(main_frame, str(COLOR[col]), radVar, col, radio_click, column=col, row=5, columnspan=3)

	global scroll_txt
	scroll_txt = TkControls.TextScrollAdd(main_frame, 30, 3, column=0, columnspan= 3)

	frame_lables= TkLayouts.FrameNew(main_frame, 'Lables Frame', column=1, row=7, padding=20)
	frame_lable1 = TkControls.LableNew(frame_lables, "Frame  Label", column=0, row=0)
	frame_lable2 = TkControls.LableNew(frame_lables, "Frame  Labe2", column=1, row=1)

	main_menu = TkLayouts.MenuBarNew(main_window)
	file_menu = TkLayouts.MenuSubNew(main_menu, "Command1", True, menu_click)
	TkLayouts.MenuSubAdd(file_menu, 'Quite', False, quite_click)
	TkLayouts.MenuBarAdd(main_menu, 'Menu1', file_menu)


	tab_frame = TkLayouts.FrameNew(main_window, 'Tab Frame', column=0, row= 1, padding= 20)
	tabControl = TkLayouts.TabControlNew(tab_frame)
	tab1 = TkLayouts.TabControlAdd(tabControl,'Tab1')
	tab2 = TkLayouts.TabControlAdd(tabControl,'Tab1')
	mighty = TkLayouts.FrameNew(tab1, text=' Mighty Python ', column=0, row=0, padding=8)
	a_label = TkControls.LableNew(mighty, text="Enter a name:", column=0, row=0)

	main_frame.mainloop()

if __name__ == '__main__':
	AppMain()