from tkinter import *

window= Tk()
window.title("BMİ CALCULATOR")
window.minsize(width=300,height=200)

weight_label=Label(text="ENTER YOUR WEIGHT(KG)",font=44)
weight_label.pack()

weight_entry=Entry(width=30)
weight_entry.pack()

height_label=Label(text="ENTER YOUR HEIGHT(CM)",font=44)
height_label.pack()

height_entry=Entry(width=30)
height_entry.pack()

def button_clicked():
    print("CALCULATED")

button=Button(text="CALCULATE",command=button_clicked)
button.pack()

window.mainloop()