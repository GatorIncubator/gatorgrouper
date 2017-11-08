import sys
import os
import tkinter
#import tkMessageBox
top=tkinter.Tk()

def runProgram():
    os.system('python gatorgrouper.py')

button=tkinter.Button(top,text="Run GatorGrouper",command=runProgram)
button.pack()
top.mainloop()
