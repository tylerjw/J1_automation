'''
File Walker

author: Tyler Weaver
created: 25 June 2013
dependencies:
    Python 2.7.5
    Tkinter: 8.5.2

This program demonstrates walking through directories looking for files.
'''

version = '0.1'

import os
from Tkinter import BOTH,LEFT,TOP,END,StringVar
from ttk import Frame, Entry, Button, Label
from ScrolledText import ScrolledText
from tkFileDialog import askdirectory

class FileWalkerWindow(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=True, fill=BOTH)
        self.master.title("File Walker v" + version)
        self.master.iconname("File Walker")

        self.dir = StringVar() #tkinter does not work with standard python variables
        self.dir.set(os.getcwd()) # set to current working directory
        
        description = "This program walks directories looking " \
        + "for files.  A directory path is outputed each time a file is " \
        + "found.  These directory paths can be coppied into explorer to " \
        + "view files."
        
        row1 = Frame(self)
        Label(row1, text="Root Directory:").pack(side=LEFT, pady=10)
        self.dir_ent = Entry(row1, width=80, textvariable=self.dir)
        self.dir_ent.pack(side=LEFT)
        Button(row1, text="Browse", width=10, command=self.browse).pack(side=LEFT, padx=5)
        row1.pack(side=TOP, ipadx=15)

        row2 = Frame(self)
        btn = Button(row2, text="Find Files", command=self.walk, width=15)
        btn.pack(side=LEFT, padx=5, pady=10)
        row2.pack(side=TOP)

        self.output = ScrolledText(self, height=15, state="normal",
                                   padx=10, pady=10,
                                   wrap='word')
        self.output.insert(END,description)
        self.output.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)


        self.bind('<Key-Return>', self.walk) #bind enter press to walk

    def browse(self):
        dirpath = askdirectory(parent=self, title="Select Root Directory")
        self.dir.set(dirpath)

    def walk(self):
        self.output.delete(1.0, END)
        for root, dirs, files in os.walk(self.dir.get()):
            if files:
                self.output.insert(END, root+'\n')


if __name__ == '__main__':
    FileWalkerWindow().mainloop()
