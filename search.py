from Tkinter import * 
import Tkinter as tk
import ttk
import MySQLdb;
con=MySQLdb.connect("localhost","root","1234","dbms");
cur=con.cursor()



def full():
	win=Tk()
	win.geometry("1200x1000")

	
	label1=Label(win,text=' ')
	label1.pack()
	label1=Label(win,text=' ')
	label1.pack()


	label1=Label(win,text='SEARCH BY ROLL NO : ')
	label1.pack()
	

		
	impo=tk.StringVar(win)
	name1=ttk.Entry(win,width=25,textvariable=impo)
	name1.pack()
	name1.focus()
	
	label1=Label(win,text='  ')
	label1.pack()	

	label1=Label(win,text='OR ')
	label1.pack()


	label1=Label(win,text='  ')
	label1.pack()	

	label1=Label(win,text='SEARCH BY NAME (CAPITAL) : ')
	label1.pack()
	
	impo2=tk.StringVar(win)
	name1=ttk.Entry(win,width=25,textvariable=impo2)
	name1.pack()
	name1.focus()
	
	label1=Label(win,text='')
	label1.pack()
	def action():
		
		label1=Label(win,text='')
		label1.pack()
		label1=Label(win,text='')
		label1.pack()

		q=impo.get()
		l=impo2.get()

		if len(q)!= 0:
			cur.execute("select * from Table1 where roll_no = '%s'"% q)
		else :			
			cur.execute("select * from Table1 where name = '%s'"% l)
		row=cur.fetchall()
		tree=ttk.Treeview(win,height=20,columns=('name','gmail','age','gender','roll_no','branch','field','degree'))
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
		tree.tag_configure('T',font='Arial 20')		
		if(row):
			for i in row:
				tree.insert('','end',text=i[0], values=(i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]))
		else:
			label1=Label(win,text='DATA DOES NOT FOUND')
			label1.pack()
		
	submit=ttk.Button(win,text='Search',command=action)
	submit.pack()
	mainloop()

