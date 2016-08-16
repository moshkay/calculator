#a program to design a calculator app
from tkinter import *
import dbm

app=Tk()
app.title("CASIO")
app.config(bg="purple")
app.resizable(False,False)

texts="CASIO Becoming a great acountant@DaVinci"
label1=Label(app,text=texts,font="Bahaus93 10 bold",fg="pink",bg="purple",cursor="crosshair")
label1.grid(row=0,column=0,columnspan=4)
screen=StringVar()
e1=Entry(app,bg="gray",fg="black",font="Verdana 15 bold",bd=4,justify=RIGHT,textvariable=screen)
e1.grid(row=1,column=0,columnspan="4",padx=4,pady=4)
e1.index(0)
#the commands for the keys    
def ac():
    e1.delete(0,"end")
    e1.insert(25,"0")
def equal():
  try:
    ans=eval(e1.get())
    e1.delete(0,"end")
    e1.insert(25,ans)
  except(SyntaxError,AttributeError,NameError):
    e1.delete(0,"end")
    e1.insert(0,"Syntax error\t ")
  except(ArithmeticError,ZeroDivisionError):
    e1.delete(0,"end")
    e1.insert(0,"Math error\t ")


def off():
    e1.delete(0,"end")
def mr():
      db=dbm.open("values","c")
      
      db["mem"]=e1.get()
      e1.delete(0,"end")
      e1.insert(25,db["mem"])
      db.close()
def on():
    e1.delete(0,"end")
    e1.insert(25,"0")

keys=["AC","MR","ON","OFF"]
num=["123+","456-","789/",".0=*"]
r,c=2,0
b="blue"
fun1=[ac,mr,on,off]

#design of the keys
for i in keys:
    but=Button(app,bg=b,fg="gray",text=i,font="Verdana 10 bold",height=2,width=6,
               bd=3,padx=2,command=fun1[c])
    but.grid(row=r,column=c,padx=2,pady=2)
    c+=1
    if c==3:
        b="red"
    else:
        b="blue"
R=3
C=0
j=0
for i in num:
    for key in i:
        but=Button(app,bg=b,fg="gray",text=key,height=2,width=6,bd=3,font="Verdana 10 bold",padx=2,
                   command=lambda b=screen,s="%s"%key: b.set(b.get()+s))
        if key=="=":
            but.config(command=equal)
        but.grid(row=R,column=C,padx=2,pady=2)
        C+=1
        j+=1
        if C==3:
            b="red"
        else:
            b="blue"
    C=0
    R+=1


app.mainloop()
