#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 8.0
#  in conjunction with Tcl version 8.6
#    Jul 02, 2024 03:03:46 PM +03  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_location = os.path.dirname(__file__)

import main

_bgcolor = '#d9d9d9'
_fgcolor = '#000000'
_tabfg1 = 'black' 
_tabfg2 = 'white' 
_bgmode = 'light' 
_tabbg1 = '#d9d9d9' 
_tabbg2 = 'gray40' 

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("509x250+394+156")
        top.minsize(120, 1)
        top.maxsize(1284, 701)
        top.resizable(1,  1)
        top.title("recognizer")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")

        self.top = top

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.177, rely=0.088, height=23, width=43)
        self.Label1.configure(activebackground="#d9d9d9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 9")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="#000000")
        self.Label1.configure(text='''source:''')

        self.Entry2 = tk.Entry(self.top)
        self.Entry2.place(relx=0.273, rely=0.216, height=20, relwidth=0.676)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="-family {Courier New} -size 10")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="#000000")
        self.Entry2.configure(insertbackground="#000000")
        self.Entry2.configure(selectbackground="#d9d9d9")
        self.Entry2.configure(selectforeground="black")

        self.Text1 = tk.Text(self.top)
        self.Text1.place(relx=0.059, rely=0.508, relheight=0.416, relwidth=0.888)

        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="#000000")
        self.Text1.configure(insertbackground="#000000")
        self.Text1.configure(selectbackground="#d9d9d9")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(wrap="word")

        self.Entry1 = tk.Entry(self.top)
        self.Entry1.place(relx=0.273, rely=0.088, height=20, relwidth=0.676)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="-family {Courier New} -size 10")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="#000000")
        self.Entry1.configure(insertbackground="#000000")
        self.Entry1.configure(selectbackground="#d9d9d9")
        self.Entry1.configure(selectforeground="black")

        self.browseBtn = tk.Button(self.top)
        self.browseBtn.place(relx=0.059, rely=0.104, height=46, width=47)
        self.browseBtn.configure(activebackground="#d9d9d9")
        self.browseBtn.configure(activeforeground="black")
        self.browseBtn.configure(background="#d9d9d9")
        self.browseBtn.configure(command=main.browse)
        self.browseBtn.configure(disabledforeground="#a3a3a3")
        self.browseBtn.configure(font="-family {Segoe UI} -size 9")
        self.browseBtn.configure(foreground="#000000")
        self.browseBtn.configure(highlightbackground="#d9d9d9")
        self.browseBtn.configure(highlightcolor="#000000")
        self.browseBtn.configure(text='''Open''')

        self.parseBtn = tk.Button(self.top)
        self.parseBtn.place(relx=0.059, rely=0.348, height=26, width=47)
        self.parseBtn.configure(activebackground="#d9d9d9")
        self.parseBtn.configure(activeforeground="black")
        self.parseBtn.configure(background="#d9d9d9")
        self.parseBtn.configure(command=main.parse)
        self.parseBtn.configure(disabledforeground="#a3a3a3")
        self.parseBtn.configure(font="-family {Segoe UI} -size 9")
        self.parseBtn.configure(foreground="#000000")
        self.parseBtn.configure(highlightbackground="#d9d9d9")
        self.parseBtn.configure(highlightcolor="#000000")
        self.parseBtn.configure(text='''Parse''')

        self.Label2 = tk.Label(self.top)
        self.Label2.place(relx=0.177, rely=0.216, height=23, width=43)
        self.Label2.configure(activebackground="#d9d9d9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 9")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="#000000")
        self.Label2.configure(text='''output:''')

        self.Label3 = tk.Label(self.top)
        self.Label3.place(relx=0.177, rely=0.36, height=21, width=54)
        self.Label3.configure(activebackground="#d9d9d9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(compound='left')
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Segoe UI} -size 9")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="#000000")
        self.Label3.configure(text='''files list''')

        self.Entry3 = tk.Entry(self.top)
        self.Entry3.place(relx=0.275, rely=0.36, height=20, relwidth=0.676)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="-family {Courier New} -size 10")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(highlightbackground="#d9d9d9")
        self.Entry3.configure(highlightcolor="#000000")
        self.Entry3.configure(insertbackground="#000000")
        self.Entry3.configure(selectbackground="#d9d9d9")
        self.Entry3.configure(selectforeground="black")

def start_up():
    main.main()

if __name__ == '__main__':
    main.main()
