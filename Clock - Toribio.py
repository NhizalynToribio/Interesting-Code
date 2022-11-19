# PROGRAMMER: NHIZALYN P. TORIBIO
# YEAR & SECTION: BSCOE 2 - 2
# LABORATORY EXERCISE NO 4

# This is the tkinter of the Clock
from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")


# This is the structure of the Clock
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)


label = Label (root, font=("ds=digital", 80), background="blue", foreground = "cyan")
label.pack(anchor="center")

# This is the output of the clock
time()
mainloop()

# Use reference is : https://www.youtube.com/watch?v=at7rpdT8FeI
