import os
from tkinter import *

# Set project include path.
sys.path.append(os.path.join(os.getcwd(),'../'))





######################################################################
#                                                                    #
#							Tk Quit 								 #
#                                                                    #
######################################################################

# Exit GUI cleanly.
def _quit(win:Tk):
    win.quit()
    win.destroy()
    exit()