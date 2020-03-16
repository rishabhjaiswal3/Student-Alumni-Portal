from Tkinter import * 
import ttk

import MySQLdb;
con=MySQLdb.connect("localhost","root","1234","dbms");
cur=con.cursor()


def result():
	master =Tk()
	master.geometry("1200x450");


	w= Scrollbar(master)
	w.pack(side=RIGHT,fill =Y)
	w.pack()

	con.commit()
	cur.execute("select * from Table1")
	row=cur.fetchall()


	tree=ttk.Treeview(master,height=20,columns=('name','gmail','age','gender','roll_no','branch','field','degree'))
	tree.pack()

	tree.heading("#0",text="Name")
	tree.column("#0",width=120)
	tree.heading("#1",text="Gmail")
	tree.heading("#2",text="Age")
	tree.column("#2",width=80)
	tree.heading("#3",text="Gender")
	tree.column("#3",width=100)
	tree.heading("#4",text="Roll No.")
	tree.column("#4",width=100)
	tree.heading("#5",text="Branch")
	tree.column("#5",width=100)
	tree.heading("#6",text="Occupation")
	tree.column("#6",width=100)
	tree.heading("#7",text="Degree")
	tree.column("#7",width=100)
	tree.heading("#8",text="Address")


	for i in row:
		tree.insert('','end',text=i[0], values=(i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]))
	tree.tag_configure('T',font='Arial 20')
	con.commit()
	mainloop()

