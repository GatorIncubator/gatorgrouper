import sys
import os
from tkinter import *
from tkinter.ttk import Style
from tkinter.ttk import Button
from tkinter.ttk import Radiobutton
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

        self.num_stu = IntVar()
        self.num_stu_checked = IntVar()
        self.num_stu_label = Label(master, text="Number of students in group: ")
        self.num_stu_slide = Scale(master, from_=1, to=20, variable=self.num_stu, orient=HORIZONTAL)
        self.num_stu_check = Checkbutton(master, variable=self.num_stu_checked, command=self.checkStudents)
        self.num_stu_check.invoke()
        self.num_stu_slide.set(1)
        self.num_stu_label.grid(row=2, padx=5)
        self.num_stu_slide.grid(row=2, column=1)
        self.num_stu_check.grid(row=2, column=2)

        self.num_group = IntVar()
        self.num_group_checked = IntVar()
        self.num_group_label = Label(master, text="Number of groups: ")
        self.num_group_slide = Scale(master, from_=1, to=10, variable=self.num_group, orient=HORIZONTAL)
        self.num_group_check = Checkbutton(master, variable=self.num_group_checked, command=self.checkGroups)
        self.num_group_slide.set(1)
        self.num_group_label.grid(row=3, padx=5)
        self.num_group_slide.grid(row=3, column=1)
        self.num_group_check.grid(row=3, column=2)

        self.greet_button = Button(master, text="Run", command= lambda: self.runGG(self.randType.get(), ('--group-size ' + str(self.num_stu.get())), ('--num-groups ' + str(self.num_group.get()))))
        self.greet_button.grid(row=0, column=1, rowspan=2, padx=5)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=0, column=2, rowspan=2, padx=5)

    def runGG(self, flag_r, flag_s, flag_g):
        flags = flag_r
        if self.num_stu_checked.get() == 1 and self.num_group_checked.get() == 0:
            flags = flags + ' ' + flag_s
        if self.num_group_checked.get() == 1 and self.num_stu_checked.get() == 0:
            flags = flags + ' ' + flag_g
        os.system('python3 $HOME/gatorgrouper/gatorgrouper.py ' + flags)

    def checkStudents(self):
        if self.num_stu_checked.get() == 0:
            self.num_stu_slide.config(state=DISABLED)
        else:
            self.num_stu_slide.config(state=NORMAL)
            self.num_group_check.deselect()

    def checkGroups(self):
        if self.num_group_checked.get() == 0:
            self.num_group_slide.config(state=DISABLED)
        else:
            self.num_group_slide.config(state=NORMAL)
            self.num_stu_check.deselect()

root = Tk()
root.geometry("666x420")
root.style = Style()
root.style.theme_use("clam")
gg_gui = GatorGrouperGUI(root)
root.mainloop()
