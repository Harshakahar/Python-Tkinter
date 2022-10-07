from tkinter import *
from datetime import date
root=Tk()
root.geometry("333x444")
root.title("AGE CALCI")
root.configure(bg="light pink")
def cal():
    t=date.today()
    bdate=date(int(yvalue.get()),int(mvalue.get()),int(dvalue.get()))
    age=t.year -bdate.year-((t.month,t.day)<(bdate.month,bdate.day))
    Label(root,text=f"{nvalue.get()} your age is {age}",font="lucida 25 bold underline",bg="white",fg="red").place(x=500,y=500)

Label(root,text="AGE CALCULATOR",bg="LightCyan2",fg="green",font="lucida 30 underline bold",width=30).pack(side="top",pady=50)
Label(root,text="Name ",font="lucida 20 bold").place(x=500,y=200)
Label(root,text="YEAR ",font="lucida 20 bold").place(x=500,y=250)
Label(root,text="Month ",font="lucida 20 bold").place(x=500,y=300)
Label(root,text="Day ",font="lucida 20 bold").place(x=500,y=350)

nvalue=StringVar()
yvalue=StringVar()
mvalue=StringVar()
dvalue=StringVar()

name=Entry(root,textvariable=nvalue,font=20,width=20,borderwidth=8).place(x=600,y=200)
year=Entry(root,textvariable=yvalue,font=20,width=20,borderwidth=8).place(x=600,y=250)
month=Entry(root,textvariable=mvalue,font=20,width=20,borderwidth=8).place(x=600,y=300)
day=Entry(root,textvariable=dvalue,font=20,width=20,borderwidth=8).place(x=600,y=350)
Button(root,text="CALCULATE",font=30,width=20,height=2,command=cal,bg="#4a7abc",fg="yellow").place(x=600,y=400)

root.mainloop()