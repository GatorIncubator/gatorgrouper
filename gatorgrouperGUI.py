import sys
import os
from tkinter import *
from tkinter.ttk import *
from functools import partial

class GatorGrouperGUI:
    def __init__(self, master):
        self.master = master
        master.title("Gator Grouper")

        self.randType = StringVar()
        self.tr_radio = Radiobutton(master, text="True Random", value='--random', variable=self.randType)
        self.rr_radio = Radiobutton(master, text="Round Robin", value='--round-robin', variable=self.randType)
        self.tr_radio.invoke()
        self.tr_radio.grid(row=0, padx=125, pady=5)
        self.rr_radio.grid(row=1, padx=125, pady=5)

        self.greet_button = Button(master, text="Run", command= lambda: self.runGG(self.randType.get()))
        self.greet_button.grid(row=0, column=1, rowspan=2, padx=5)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=0, column=2, rowspan=2, padx=5)

    def runGG(self, flag):
        print('python3 gatorgrouper.py ' + flag)
        os.system('python3 $HOME/gatorgrouper/gatorgrouper.py ' + flag)

root = Tk()
root.geometry("666x420")
root.style = Style()
root.style.theme_use("clam")
gg_gui = GatorGrouperGUI(root)
root.mainloop()
