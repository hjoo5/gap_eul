from tkinter import *
from tkinter.scrolledtext import *
import tkinter.filedialog as filedialog
import tkinter.messagebox as tkMessageBox
import time
import os

root = tkinter.Tk(className="Simple Text Editor")
textPad = ScrolledText(root, width=100, height=80, highlightcolor = "white")

def open_command():
    file = filedialog.askopenfile(parent=root,mode='rb',title='Select a file')
    if file != None:
        contents = file.read()
        textPad.delete('1.0', END);
        textPad.insert('1.0',contents)
        file.close()

def save_command():
    file = filedialog.asksaveasfile(defaultextension='.txt',
                                 filetypes=(('Text files', '*.txt'),
                                            ('Python files', '*.py *.pyw'),
                                            ('All files', '*.*')))
    if file != None:
        data = textPad.get('1.0', END+'-1c')
        file.write(data)
        file.close()

def exit_command():
    if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()

def about_command():
    label = tkMessageBox.showinfo("About", "Simple Text Editor \n Copyright " +
                                  "\n No rights left to reserve")

def new_command():
    textPad.delete('1.0', END);

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=new_command, accelerator = "Ctrl+N")
filemenu.add_command(label="Open...", command=open_command, accelerator = "Ctrl+O")
filemenu.add_command(label="Save", command=save_command, accelerator = "Ctrl+S")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_command)
settingmenu = Menu(menu)
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=about_command)

#
textPad.pack()
root.mainloop()
