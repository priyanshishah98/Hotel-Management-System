from tkinter import *
import tkinter.messagebox
import sqlite3

def insert():
    n = name1.get()
    e = e_id1.get()
    u=int(user_id1.get())
    pwd=password1.get()
    g=gender.get()

    insertsql="insert into db(name1,e_id1,user_id1,password1,gender) values('%s','%s','%d','%s','%s')"%(n,e,u,pwd,g)
    cursor.execute(insertsql)
    d.commit()

d=sqlite3.connect('signupdb')
cursor=d.cursor()

def agree():
    if len(name1.get()) == 0:
        tkinter.messagebox.showinfo("Warning!", "Enter your Name correctly!")
    elif len(e_id1.get()) == 0:
        tkinter.messagebox.showinfo("Warning!", "Enter correct email id!")
    elif len(user_id1.get()) == 0:
        tkinter.messagebox.showinfo("Warning!", "Enter valid User id!")
    elif len(password1.get()) <6:
        tkinter.messagebox.showinfo("Warning!", "Set a strong password!")
    elif gender.get() < 1:
        tkinter.messagebox.showinfo("Warning!", "Gender Not Defined!")
    else:
        tkinter.messagebox.showinfo("Title", "Signed up Successfully!")
       # insert()
        root.destroy()


root=Tk()	#Create root window
root.title('Sign up form')
root.geometry("500x500")
root.configure(background="black")
z=Frame(root,bg="black",height=500,width=500)
z.propagate(0)
z.pack()
#Label goes here
name=Label(text="Name:",fg="purple", bg="light blue", font=('arial',13))
e_id=Label(text="Email id:", font=('arial',13))
user_id=Label(text="User id:", font=('arial',13))
password=Label(text="Password:", font=('arial',13))
gend=Label(text="Gender:", font=('arial',13))
cityl=Label(text="City:", font=('arial',13))
#Entry Boxes
name1=Entry(z,width=20,fg="purple",bg="light blue",font=('arial',13))
e_id1=Entry(z,width=30,fg="purple",bg="light blue",font=('arial',15))
user_id1=Entry(z,width=20,fg="purple",bg="light blue",font=('italic',15))
password1=Entry(z,width=20,fg="purple",bg="light blue",show="*",font=('italic',13))
gender=IntVar()
gend1=Radiobutton(z,text='Male',variable=gender,value=1)
gend2=Radiobutton(z,text='Female',variable=gender,value=2)
citylist=['Mumbai','Surat','Pune','Ahmedabad','Delhi']
variable = StringVar(root)
variable.set(citylist[0]) # default value
x = OptionMenu(root, variable, *citylist)
x.config(bg = "GREEN")
x.pack()
but=Button(z,text='Submit Details', command=agree)
name.place(x=50,y=30)
name1.place(x=200 ,y=30)
e_id.place(x=50,y=90)
e_id1.place(x=200, y=90)
user_id.place(x=50,y=130)
user_id1.place(x=200,y=130)
password.place(x=50,y=175)
password1.place(x=200,y=175)
gend.place(x=50,y=230)
gend1.place(x=200,y=230)
gend2.place(x=270,y=230)
cityl.place(x=50,y=270)
x.place(x=200,y=270)

but.place(x=350,y=350)

d.close()

root.mainloop()
