# Calculator using tkinter

from tkinter import *

c=Tk()

exp=""
eqn=StringVar()
def press(n):
    global exp
    exp=exp+str(n)
    if exp[0]=='+':
       backspace()
    if exp[0]=='-':
       backspace()
    if exp[0]=='*':
       backspace()
    if exp[0]=='/':
       backspace()
    else:
        eqn.set(exp)

def backspace():
    global exp
    exp=exp[0:len(exp)-1]
    eqn.set(exp)

def clear():
    global exp
    exp=""
    eqn.set(exp)
def equal():
    global exp
    exp=eval(exp)
    eqn.set(exp)
    exp=""

e=Entry(c,width=26,textvariable=eqn).grid(row=0,column=0,columnspan=4)
b9=Button(c,text="9",height=2,width=4,command= lambda: press(9)).grid(row=1,column=0)
b8=Button(c,text="8",height=2,width=4,command= lambda: press(8)).grid(row=1,column=1)
b7=Button(c,text="7",height=2,width=4,command= lambda: press(7)).grid(row=1,column=2)
b=Button(c,text="C",height=2,width=4,command=backspace).grid(row=1,column=3)
b6=Button(c,text="6",height=2,width=4,command= lambda: press(6)).grid(row=2,column=0)
b5=Button(c,text="5",height=2,width=4,command= lambda: press(5)).grid(row=2,column=1)
b4=Button(c,text="4",height=2,width=4,command= lambda: press(4)).grid(row=2,column=2)
pl=Button(c,text="+",height=2,width=4,command= lambda: press('+')).grid(row=2,column=3)
b3=Button(c,text="3",height=2,width=4,command= lambda: press(3)).grid(row=3,column=0)
b2=Button(c,text="2",height=2,width=4,command= lambda: press(2)).grid(row=3,column=1)
b1=Button(c,text="1",height=2,width=4,command= lambda: press(1)).grid(row=3,column=2)
mi=Button(c,text="-",height=2,width=4,command= lambda: press('-')).grid(row=3,column=3)
de=Button(c,text=".",height=2,width=4,command= lambda: press('.')).grid(row=4,column=0)
b0=Button(c,text="0",height=2,width=4,command= lambda: press(0)).grid(row=4,column=1)
di=Button(c,text="/",height=2,width=4,command= lambda: press('/')).grid(row=4,column=2)
mu=Button(c,text="*",height=2,width=4,command= lambda: press('*')).grid(row=4,column=3)
cl=Button(c,text="Clear",bg="red",height=2,width=12,command=clear).grid(row=5,column=0,columnspan=3)
eq=Button(c,text="=",height=2,width=4,command= equal).grid(row=5,column=3)

c.mainloop()