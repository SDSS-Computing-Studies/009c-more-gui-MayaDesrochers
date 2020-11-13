import tkinter as tk
from tkinter import *
from tkinter import ttk
import math 

window =tk.Tk()
window.geometry("500x350")
eoutput=StringVar()

triangle=PhotoImage(file="triangle.png")

def clickFunction():
    a=e1.get()
    b=e2.get()
    c=e3.get()
    d=e4.get()
    #a=hypotenuse
    #b=height
    #c=side
    #d=base
    
    
    
    try:
        b=float(b)  
    except:
        b=0
        
    try:
       a=float(a) 
    except:
        a=0
    try:
        c=float(c)
    except:
        c=0
    try:
        d=float(d)
    except:
        d=0
   

    if b>0:
        answer=(b*d)/2
    
    elif (b==0 and a>0 and c>0 and d>0):
        s=(a+c+d)/2
        answer=math.sqrt(s*(s-a)*(s-c)*(s-d))

    elif (b==0 and (a==0 or c==0 or d==0)):
        answer="Area cannot be calculated"

    entry1.delete(0,END)
    entry1.insert(0,answer)

photo=Label(window, image=triangle)
l1=Label(window, text="Enter in as much information about the\n triangle shown and I will calculate the area")
b1=Button(window, text="Calculate!", command=clickFunction)
e1=Entry(window,width=10)
e2=Entry(window,width=10)
e3=Entry(window,width=10)
e4=Entry(window,width=10)
entry1=Entry(window, textvariable=eoutput,width=25)


#placement
photo.place(x=0, y=0)
e1.place(x=140, y=125)
e2.place(x=300, y=125)
e3.place(x=400, y=125)
e4.place(x=250, y=240)
b1.place(x=250, y=300)
entry1.place(x=340, y=300)
l1.place(x=0, y=300)
window.mainloop()





