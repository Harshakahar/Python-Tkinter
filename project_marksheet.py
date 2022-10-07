from tkinter import *
import pandas as pd
import tkinter.messagebox as msg
df=pd.read_csv('marksheet.csv')
def key(event):
    global i
    i=int(e1.get())
def show():
    global i
    m=i-1
    if (i > 5):
        msg.showinfo("ERROR", "Enter number between 1-5")
    elif i==0:
      msg.showinfo("Invalid","Enter Valid Number")
    else:
        f=Frame(bg="LightCyan2")
        Label(f, text="ROLL NO:" + str(i), font="lucida 20 bold",bg="LightCyan2").grid(row=2, column=2, padx=20, pady=20)
        Label(f,text="NAME: " + str(df.Name[m]),font="lucida 20 italic",bg="LightCyan2").grid(row=3,column=2,padx=20,pady=20)
        Label(f, text="Maths: " + str(df.Maths[m]),font="lucida 20 italic",bg="LightCyan2").grid(row=4,column=2,padx=20,pady=20)
        Label(f, text="Physics: " + str(df.Physics[m]),font="lucida 20 italic",bg="LightCyan2").grid(row=5,column=2,padx=20,pady=20)
        Label(f, text="Chemistry: " + str(df.Chemistry[m]),font="lucida 20 italic",bg="LightCyan2").grid(row=6,column=2,padx=20,pady=20)
        Label(f,text="Percentage: "+str(float(((df.Maths[m]) + (df.Physics[m]) + (df.Chemistry[m])) / 3))+"%",font="lucida 20 italic",bg="LightCyan2").grid(row=8,column=2,padx=20,pady=20)
        f.grid(row=3,column=0,pady=25)

tk=Tk()
tk.geometry("600x550")
tk.title("Marksheet")
tk.configure(bg="pink")
l=Label(tk,text="Enter Your Roll No: ",font="miriamlibre 20 italic bold",width=20).grid(row=0,column=0,padx=25)
e1=Entry(tk)
tk.bind("<Key>",key)
e1.grid(row=0,column=1,ipadx=20,ipady=5,padx=5)
e1.focus_set()
Button(tk,text="SHOW RESULT",relief=SUNKEN,fg="#FFFAF0",bg="#4b7A8C",activeforeground='white',width=15,height=2,command=show).grid(row=1,column=1)
Button(tk,text="EXIT",relief=SUNKEN,fg="yellow",bg="#4a7abc",activeforeground='white',width=10,height=2,command=quit).grid(row=1,column=2,padx=10)

tk.mainloop()

