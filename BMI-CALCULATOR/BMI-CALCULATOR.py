from tkinter import *

window= Tk()
window.title("BMI CALCULATOR")
window.minsize(width=300,height=200)

weight_label=Label(text="ENTER YOUR WEIGHT(KG)",font=44)
weight_label.pack()

weight_entry=Entry(width=30)
weight_entry.pack()

height_label=Label(text="ENTER YOUR HEIGHT(CM)",font=44)
height_label.pack()

height_entry=Entry(width=30)
height_entry.pack()
calculate_label=Label(text="____________________",font=44)
calculate_label.pack()
def button_clicked():
    body_mass=""
    try:
        we=int(weight_entry.get())
        he=int(height_entry.get())
        he=(he/100)**2
        calculate=we/he
    except:
        calculate_label.config(text="Please text a number.",font=44)
        calculate_label.pack()
        return
    if calculate<18.5:
        body_mass="underweight"
    elif 18.5<=calculate<25:
        body_mass="normal"
    elif 25<=calculate<30:
        body_mass="overweight"
    elif 30<=calculate<40:
        body_mass="obese"
    elif 40<=calculate:
        body_mass="morbidly obese"
    calculate_label.config(text="Your BMI ={} You are {}".format(calculate,body_mass),font=44)
    calculate_label.pack()
button=Button(text="CALCULATE",command=button_clicked,font=44)
button.pack()

window.mainloop()