from tkinter import *
from time import strftime , sleep

root = Tk()
root.title("Clock")

root.geometry("800x400")  

root.wm_title("Clock")
root.adderrorinfo("wait")

def clock():
    time = strftime('%H:%M:%S %p')
    if time != '':
        time_label.config(text=time,font="calibri 40 bold")
    root.after(100,clock)
time_label = Label(root,justify='center')

time_label.pack(expand=True) 
clock()
root.mainloop()
