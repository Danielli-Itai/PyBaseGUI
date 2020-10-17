import os
from tkinter import *

sys.path.append(os.path.join(os.getcwd(),'../PyBase'))





# Exit GUI cleanly.
def _quit(win:Tk):
    win.quit()
    win.destroy()
    exit()