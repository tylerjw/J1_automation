'''
Folder Replicator

author: Tyler Weaver
created: 12 July 2013
dependencies:
    Python 2.7.5
    Tkinter: 8.5.2

This program walks throgh a folder tree and builds a copy of that tree.
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
        self.master.title("Folder Replicator v" + version)
        self.master.iconname("Folder Replicator")

        self.indir = StringVar() #tkinter does not work with standard python variables
        self.outdir = StringVar()
        
        description = "This program walks throgh a folder tree and builds a copy of that tree.\n" + \
                      "1. Select input directory (share point or sharedrive root folder)\n" + \
                      "2. Create a new folder and select it as the output\n" + \
                      "     -(create different folders for the sharedrive and share point)\n" + \
                      "3. Zip those folders and email them to me.\n\n"
        
        row1 = Frame(self)
        Label(row1, text="Input Directory:").pack(side=LEFT, pady=10)
        self.dir_ent = Entry(row1, width=80, textvariable=self.indir)
        self.dir_ent.pack(side=LEFT)
        Button(row1, text="Browse", width=10, command=self.browse_in).pack(side=LEFT, padx=5)
        row1.pack(side=TOP, ipadx=15)
        
        row2 = Frame(self)
        Label(row2, text="Output Directory:").pack(side=LEFT, pady=10)
        self.dir_ent = Entry(row2, width=80, textvariable=self.outdir)
        self.dir_ent.pack(side=LEFT)
        Button(row2, text="Browse", width=10, command=self.browse_out).pack(side=LEFT, padx=5)
        row2.pack(side=TOP, ipadx=15)

        row3 = Frame(self)
        btn = Button(row3, text="Run Script", command=self.walk, width=15)
        btn.pack(side=LEFT, padx=5, pady=10)
        row3.pack(side=TOP)

        self.output = ScrolledText(self, height=15, state="normal",
                                   padx=10, pady=10,
                                   wrap='word')
        self.output.insert(END,description)
        self.output.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)


        self.bind('<Key-Return>', self.walk) #bind enter press to walk

    def browse_in(self):
        dirpath = askdirectory(parent=self, title="Select Input Directory")
        self.indir.set(dirpath)

    def browse_out(self):
        dirpath = askdirectory(parent=self, title="Select Output Directory")
        self.outdir.set(dirpath)

    def walk(self):
        roots = []
        os.chdir(self.outdir.get())
        start = len(self.indir.get())
        self.output.insert(END, '\n')
        log = open("log.txt",'w')
        for root, dirs, files in os.walk(self.indir.get()):
            if not dirs:
                roots.append(root[start:])
                self.output.insert(END, root[start:]+'\n')
                log.write(root[start:]+'\n')
        
        
        self.output.insert(END, '\n\nCreating directories: \n')
        log.write('\n\nCreating directories: \n')
        for root in roots:
            self.output.insert(END, self.outdir.get() + root + '\n')
            os.makedirs(self.outdir.get() + root)
            log.write(self.outdir.get() + root + '\n')
        log.close()
            
            

if __name__ == '__main__':
    FileWalkerWindow().mainloop()
