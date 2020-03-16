import ttk
from Tkinter import *
import MySQLdb
con=MySQLdb.connect('localhost','root','1234','dbms')
cur=con.cursor()
import Tkinter as tk
import Tkinter


import search
import result
import insert


root = Tk()
root.geometry("700x700")


root.configure(background="white")
label3=Label(root)
label3.configure(background="white")
label3.pack()



label1=Label(root,text="STUDENT ALUMNI",font='Arial 90',)
label1.configure(background="white",foreground="DarkOrchid3")
label1.pack()
label2=Label(root,text="Database  Management  System",font='Arial 40')
label2.configure(background="white",foreground="DarkOrchid3")
label2.pack()

label3=Label(root)
label3.pack()
label3.configure(background="white")

photo=Tkinter.PhotoImage(file="rj.png")
label=Label(root,image=photo)
label.configure(background="white")
label.pack()

button1=Button(root,text='details',command=insert.fun)
button1.pack()

label3=Label(root)
label3.pack()
label3.configure(background="white")

button3=Button(root,text='search',command=search.full)
button3.pack()

label3=Label(root)
label3.pack()
label3.configure(background="white")
button2=ttk.Button(root,text='database',command=result.result)
button2.pack()

root.mainloop()
