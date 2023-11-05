from tkinter import *
import time

window = Tk()
window.title("Digital clock")
window.geometry("8000x7000")
def myTime():
    hour = time.strftime("%I")
    minut = time.strftime("%M")
    second = time.strftime("%S")
    am_pm = time.strftime("%p")
    day = time.strftime('%A')
    year= time.strftime("%Y")
    zone = time.strftime("%Z")
    my_txt= hour + ":" + minut + ":" + second + " " + am_pm
    my_lable.config(text = my_txt)
    my_text2 = day+","+ " " + year + " "+ zone+" "+":)"
    my_lable2.config(text=my_text2)
    my_lable.after(1000,myTime)
my_lable = Label(window,text="",font=("Arial","60"),fg="red",bg="purple")
my_lable.pack()
my_lable2 = Label(window,text = "",font=("Aria","24"),fg = "blue",bg = "Yellow")
my_lable2.pack()


myTime()
window.mainloop()




   