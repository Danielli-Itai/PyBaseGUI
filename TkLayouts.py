#This module provides an interface to GUI containers.
import os
from tkinter import *
from tkinter import ttk
from tkinter import Menu

# Set project include path.
sys.path.append(os.path.join(os.getcwd(),'../'))





######################################################################
#                                                                    #
#							Tk GUI Layouts 							 #
#                                                                    #
######################################################################

##################################
#        Window menu-bar
# Create new window menu-bar.
def MenuBarNew(win:Tk)->Menu:
	menu_bar = Menu(win)
	win.config(menu=menu_bar)
	return(menu_bar)

# Add sub-menu to existing menu-bar.
def MenuBarAdd(menu_bar:Menu, text:str, menu_sub:Menu):
	menu_bar.add_cascade(label="File", menu=menu_sub)
	return

# Create new sub-menu and add command..
def MenuSubNew(menu_bar:Menu, text:str, sep:bool, command):
	sub_menu = Menu(menu_bar, tearoff=0)
	if(text and command):sub_menu.add_command(label=text, command=command)
	if(sep):sub_menu.add_separator()
	return(sub_menu)

# Add new command to a sub-menu.
def MenuSubAdd(sub_menu:Menu, text:str, sep:bool, command):
	if(text and command):sub_menu.add_command(label=text, command=command)
	if(sep):sub_menu.add_separator()
	return(sub_menu)




###################################
#        Controls frame
# Create new frame and add it to container.
def FrameNew(container:ttk.Widget, text:str, column:int, row:int, padding:int)->ttk.LabelFrame:
	# Create a container to hold labels
	frame = ttk.LabelFrame(container, text=text)
	frame.grid(column=column, padx=padding  , row=row, pady=padding, sticky=N+S+W+E)
	return(frame)




###################################
#        Tabbed frames
# Create Tab Control.
def TabControlNew(container:ttk.Widget):
	tabControl = ttk.Notebook(container)
	return(tabControl)

# Add new tab frame.
def TabControlAdd(tabControl:ttk.Notebook, text:str):
	tab_frame = ttk.Frame(tabControl)  # Create a tab
	tabControl.add(tab_frame, text=text)  # Add the tab
	tabControl.pack(expand=1, fill="both")  # Pack to make visible
	return(tab_frame)