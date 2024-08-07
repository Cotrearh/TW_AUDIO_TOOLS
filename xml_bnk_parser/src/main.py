#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 8.0
#  in conjunction with Tcl version 8.6
#    Jun 26, 2024 07:19:28 PM +03  platform: Windows NT

import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
from tkinter import filedialog


import gui
import xml_bnk_parser

_debug = True # False to eliminate debug printing from callback functions.

def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1, _filename, _out_dir, _out_file
    _top1 = root
    _w1 = gui.Toplevel1(_top1)  
    _filename = ""
    _out_dir = ""
    _out_file = ""
    root.mainloop()

def browse(*args):
    _filename = filedialog.askopenfilename(title="Выберите исходный файл")
    _w1.Entry1.delete(0, END)
    _w1.Entry1.insert(0, _filename)
    
    _out_dir = filedialog.askdirectory(title="Выберите папку для сохранения")
    _out_file = os.path.join(_out_dir, "parsed_bnk.tsv")
    _w1.Entry2.delete(0, END)
    _w1.Entry2.insert(0, _out_file)
        
    append(f"source file: {_filename}")
    append(f"out file: {_out_file}")

def parse(*args):
    xml_bnk_parser.parse(_w1.Entry1.get(), _w1.Entry2.get())
    append("complete!")

def append(text):
    _w1.Text1.insert(END, f"{text}\n")

if __name__ == '__main__':
    gui.start_up()




