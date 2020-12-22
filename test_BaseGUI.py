#!/usr/bin/env python
"""
import gtk
import webkit
import gobject

gobject.threads_init()
win = gtk.Window()
bro = webkit.WebView()
bro.open("http://www.google.com")
win.add(bro)
win.show_all()
gtk.main()
"""
import urllib.request
from tk_html_widgets import HTMLLabel
import tkinter as tk

import os
import sys

# Set project include path.
sys.path.append(os.path.join(os.getcwd(),'../'))





root = tk.Tk()

#frame = HtmlFrame(root, horizontal_scrollbar="auto")
#frame.grid(sticky=tk.NSEW)
#root.columnconfigure(0, weight=1)
#root.rowconfigure(0, weight=1)

lable = HTMLLabel(root, html="""<html>
<body>
<h1>Hello world!</h1>
<p>First para</p>
<ul>
    <li>first list item</li>
    <li>second list item</li>
</ul>
</body>
</html>""")
lable.grid(column=0, row=0, sticky='W')
lable.pack()

lable.set_html('<h1>Hello world!</h1>')

root.mainloop()