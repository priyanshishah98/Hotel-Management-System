import sqlite3
import tkinter as tk

def insert():
    u=uid.get()
    f=firstname.get()
    l=lastname.get()
    a=age.get()
    g=gender.get()
    p=phn.get()
    e=email.get()
    insertsql="insert into person(uid,fname,lname,age,gender,phn,email) values('%d','%s','%s','%d','%s','%d','%s')"%(u,f,l,a,g,p,e)
    cursor.execute(insertsql)
    db.commit()

db=sqlite3.connect('wanderlust')
cursor=db.cursor()
db.close()

def singapore():
    window=tk.Toplevel(root)
    window.title('Singapore')
    window.geometry('1350x740')
    string1='Singapore is known as a bustling metropolis that also happens to be one of the cleanest and safest cities of its size in the world.' + '\n' + '(Just make sure you heed the local laws—something like spitting in the street might merely be considered rude in your hometown, but here, it carries a severe penalty.)' + '\n' + "You'll find historic sites like the Thian Hock Keng temple, superlative shopping (including gargantuan malls) and numerous beaches." + '\n'
    lbl=tk.Label(window,text=string1,font=('Comic Sans MS',10))
    lbl.place(x=30,y=10,height=500,width=500)
    lbl.pack()
    #window.after(30000, lambda: window.destroy())


def malaysia():
    window=tk.Toplevel(root)
    window.title('Malaysia')
    window.geometry('1350x740')
    string2='Singapore is known as a bustling metropolis that also happens to be one of the cleanest and safest cities of its size in the world.' + '\n' + '(Just make sure you heed the local laws—something like spitting in the street might merely be considered rude in your hometown, but here, it carries a severe penalty.)' + '\n' + "You'll find historic sites like the Thian Hock Keng temple, superlative shopping (including gargantuan malls) and numerous beaches." + '\n'
    lbl=tk.Label(window,text=string2,font=('Comic Sans MS',10))
    lbl.place(x=30,y=10,height=500,width=500)
    lbl.pack()
    
    
def paris():
    window=tk.Toplevel(root)
    window.title('paris')
    window.geometry('1350x740')
    string3='Singapore is known as a bustling metropolis that also happens to be one of the cleanest and safest cities of its size in the world.' + '\n' + '(Just make sure you heed the local laws—something like spitting in the street might merely be considered rude in your hometown, but here, it carries a severe penalty.)' + '\n' + "You'll find historic sites like the Thian Hock Keng temple, superlative shopping (including gargantuan malls) and numerous beaches." + '\n'
    lbl=tk.Label(window,text=string3,font=('Comic Sans MS',10))
    lbl.place(x=30,y=10,height=500,width=500)
    lbl.pack()
    

def spain():
    window=tk.Toplevel(root)
    window.title('spain')
    window.geometry('1350x740')
    string4='Singapore is known as a bustling metropolis that also happens to be one of the cleanest and safest cities of its size in the world.' + '\n' + '(Just make sure you heed the local laws—something like spitting in the street might merely be considered rude in your hometown, but here, it carries a severe penalty.)' + '\n' + "You'll find historic sites like the Thian Hock Keng temple, superlative shopping (including gargantuan malls) and numerous beaches." + '\n'
    lbl=tk.Label(window,text=string4,font=('Comic Sans MS',10))
    lbl.place(x=30,y=10,height=500,width=500)
    lbl.pack()


def dubai():
    window=tk.Toplevel(root)
    window.title('dubai')
    window.geometry('1350x740')
    string5='Singapore is known as a bustling metropolis that also happens to be one of the cleanest and safest cities of its size in the world.' + '\n' + '(Just make sure you heed the local laws—something like spitting in the street might merely be considered rude in your hometown, but here, it carries a severe penalty.)' + '\n' + "You'll find historic sites like the Thian Hock Keng temple, superlative shopping (including gargantuan malls) and numerous beaches." + '\n'
    lbl=tk.Label(window,text=string5,font=('Comic Sans MS',10))
    lbl.place(x=30,y=10,height=500,width=500)
    lbl.pack()


def amsterdam():
    window=tk.Toplevel(root)
    window.title('amsterdam')
    window.geometry('1350x740')
    string6='Singapore is known as a bustling metropolis that also happens to be one of the cleanest and safest cities of its size in the world.' + '\n' + '(Just make sure you heed the local laws—something like spitting in the street might merely be considered rude in your hometown, but here, it carries a severe penalty.)' + '\n' + "You'll find historic sites like the Thian Hock Keng temple, superlative shopping (including gargantuan malls) and numerous beaches." + '\n'
    lbl=tk.Label(window,text=string6,font=('Comic Sans MS',10))
    lbl.place(x=30,y=10,height=500,width=500)
    lbl.pack()


def switzerland():
    window=tk.Toplevel(root)
    window.title('switzerland')
    window.geometry('1350x740')
    string7='Singapore is known as a bustling metropolis that also happens to be one of the cleanest and safest cities of its size in the world.' + '\n' + '(Just make sure you heed the local laws—something like spitting in the street might merely be considered rude in your hometown, but here, it carries a severe penalty.)' + '\n' + "You'll find historic sites like the Thian Hock Keng temple, superlative shopping (including gargantuan malls) and numerous beaches." + '\n'
    lbl=tk.Label(window,text=string7,font=('Comic Sans MS',10))
    lbl.place(x=30,y=10,height=500,width=500)
    lbl.pack()


def india():
    window=tk.Toplevel(root)
    window.title('india')
    window.geometry('1350x740')
    string8='Singapore is known as a bustling metropolis that also happens to be one of the cleanest and safest cities of its size in the world.' + '\n' + '(Just make sure you heed the local laws—something like spitting in the street might merely be considered rude in your hometown, but here, it carries a severe penalty.)' + '\n' + "You'll find historic sites like the Thian Hock Keng temple, superlative shopping (including gargantuan malls) and numerous beaches." + '\n'
    lbl=tk.Label(window,text=string8,font=('Comic Sans MS',10))
    lbl.place(x=30,y=10,height=500,width=500)
    lbl.pack()


def usa():
    window=tk.Toplevel(root)
    window.title('usa')
    window.geometry('1350x740')
    string9='Singapore is known as a bustling metropolis that also happens to be one of the cleanest and safest cities of its size in the world.' + '\n' + '(Just make sure you heed the local laws—something like spitting in the street might merely be considered rude in your hometown, but here, it carries a severe penalty.)' + '\n' + "You'll find historic sites like the Thian Hock Keng temple, superlative shopping (including gargantuan malls) and numerous beaches." + '\n'
    lbl=tk.Label(window,text=string9,font=('Comic Sans MS',10))
    lbl.place(x=30,y=10,height=500,width=500)
    lbl.pack()


def mexico():
    window=tk.Toplevel(root)
    window.title('mexico')
    window.geometry('1350x740')
    string10='Singapore is known as a bustling metropolis that also happens to be one of the cleanest and safest cities of its size in the world.' + '\n' + '(Just make sure you heed the local laws—something like spitting in the street might merely be considered rude in your hometown, but here, it carries a severe penalty.)' + '\n' + "You'll find historic sites like the Thian Hock Keng temple, superlative shopping (including gargantuan malls) and numerous beaches." + '\n'
    lbl=tk.Label(window,text=string10,font=('Comic Sans MS',10))
    lbl.place(x=30,y=10,height=500,width=500)
    lbl.pack()

def start():
    root=tk.Tk()
    root.geometry('1350x740')
    root.title('Wanderlust Vibes')
    b1=tk.Button(root,text='Singapore',command=singapore)
    b1.place(x=30,y=10,height=40,width=100)
    b2=tk.Button(root,text='Malaysia',command=malaysia)
    b2.place(x=30,y=60,height=40,width=100)
    b3=tk.Button(root,text='Paris',command=paris)
    b3.place(x=30,y=110,height=40,width=100)
    b4=tk.Button(root,text='Spain',command=spain)
    b4.place(x=30,y=160,height=40,width=100)
    b5=tk.Button(root,text='Dubai',command=dubai)
    b5.place(x=30,y=210,height=40,width=100)
    b6=tk.Button(root,text='Amsterdam',command=amsterdam)
    b6.place(x=30,y=260,height=40,width=100)
    b7=tk.Button(root,text='Switzerland',command=switzerland)
    b7.place(x=30,y=310,height=40,width=100)
    b8=tk.Button(root,text='India',command=india)
    b8.place(x=30,y=360,height=40,width=100)
    b9=tk.Button(root,text='USA',command=usa)
    b9.place(x=30,y=410,height=40,width=100)
    b10=tk.Button(root,text='Mexico',command=mexico)
    b10.place(x=30,y=460,height=40,width=100)


    root.mainloop()