import Tkinter as tk
import ttk
import MySQLdb
con=MySQLdb.connect('localhost','root','1234','dbms')
cur=con.cursor()

def fun():
	w=tk.Tk()
	w.geometry('480x430')
	w.title("DETAILS")
	w.resizable(False,False)
	#
	ttk.Label(w,text="DETAILS  :",font=('italic',30) ).grid(row=0,column=0)

	ttk.Label(w,text="").grid(row=1,column=0)
	ttk.Label(w,text=" ").grid(row=2,column=0)
	#
	# name related information


	#
	impo_name=tk.StringVar(w)
	name=ttk.Label(w,text="Name :")
	name.grid(row=3,column=0,sticky=tk.W)

	name1=ttk.Entry(w,width=25,textvariable=impo_name)

	name1.grid(row=3,column=2)
	name1.focus()
	#
	ttk.Label(w,text=" ").grid(row=4,column=0)
	#


	# rollno related information

	impo_rollno=tk.StringVar(w)
	rollno=ttk.Label(w,text="Roll No. :")
	rollno.grid(row=5,column=0,sticky=tk.W)

	rollno1=ttk.Entry(w,width=25,textvariable=impo_rollno)
	rollno1.grid(row=5,column=2)
	#

	#
	ttk.Label(w,text=" ").grid(row=6,column=0)
	#
	#


	#branch information
	impo_branch=tk.StringVar(w)
	branch=ttk.Label(w,text="Branch :")
	branch.grid(row=7,column=0,sticky=tk.W)

	branch1=ttk.Entry(w,width=25,textvariable=impo_branch)
	branch1.grid(row=7,column=2)

	#
	#
	ttk.Label(w,text=" ").grid(row=8,column=0)

	#
	#age related information 
	#
	impo_age=tk.StringVar(w)
	age=ttk.Label(w,text="Age :")
	age.grid(row=9,column=0,sticky=tk.W)

	age1=ttk.Entry(w,width=25,textvariable=impo_age)
	age1.grid(row=9,column=2)
	#
	#

	ttk.Label(w,text=" ").grid(row=10,column=0)

	#gmail information

	impo_gmail=tk.StringVar(w)
	gmail=ttk.Label(w,text="Gmail :")
	gmail.grid(row=11,column=0,sticky=tk.W)

	gmail1=ttk.Entry(w,width=25,textvariable=impo_gmail)
	gmail1.grid(row=11,column=2)

	#
	ttk.Label(w,text=" ").grid(row=12,column=0)

	#
	#Field information


	impo_field=tk.StringVar(w)
	field=ttk.Label(w,text="Occupation:")
	field.grid(row=13,column=0,sticky=tk.W)

	field1=ttk.Entry(w,width=25,textvariable=impo_field)
	field1.grid(row=13,column=2)

	#
	ttk.Label(w,text=" ").grid(row=14,column=0)
	#


	#degree
	#
	impo_degree=tk.StringVar(w)
	degree=ttk.Label(w,text="Degree :")
	degree.grid(row=15,column=0,sticky=tk.W)

	degree1=ttk.Entry(w,width=25,textvariable=impo_degree)
	degree1.grid(row=15,column=2)
	 
	#
	ttk.Label(w,text=" ").grid(row=16,column=0)


	#address
	#
	impo_address=tk.StringVar(w)
	address=ttk.Label(w,text="Address:")
	address.grid(row=17,column=0,sticky=tk.W)

	address1=ttk.Entry(w,width=25,textvariable=impo_address)
	address1.grid(row=17,column=2)
	 
	#
	ttk.Label(w,text=" ").grid(row=18,column=0)
	#
	#

	#passout
	#

	impo_passout=tk.StringVar(w)
	passout=ttk.Label(w,text="Passout Year:")
	passout.grid(row=19,column=0,sticky=tk.W)

	passout1=ttk.Entry(w,width=25,textvariable=impo_passout)
	passout1.grid(row=19,column=2)
	#
	ttk.Label(w,text=" ").grid(row=20,column=0)
	#
	# gender information


	gender=tk.StringVar(w)
	radio1=tk.Radiobutton(w,text='Male',value='Male',variable=gender)
	radio1.grid(row=24,column=1)
	radio2=tk.Radiobutton(w,text='Female',value='Female',variable=gender)
	radio2.grid(row=24,column=2)

	# coding for submit button
	def action():
		user_name=impo_name.get()
		user_gmail=impo_gmail.get()
		user_age=impo_age.get()
		user_gender=gender.get()
		user_roll_no=impo_rollno.get()
		user_Branch=impo_branch.get()
		user_field=impo_field.get()
		user_degree=impo_degree.get()
		user_address=impo_address.get()
	
		try:
			cur.execute("INSERT INTO Table1 (name,gmail,age,gender,roll_no,branch,field,degree,address) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(user_name,user_gmail,user_age,user_gender,user_roll_no,user_Branch,user_field,user_degree,user_address))
			cur.fetchall()
			con.commit()
			con.close()
			w.destroy()
		except Exception:
			x=tk.Tk()
			x.title("DETAILS")
			x.geometry("400x50")
			#
			ttk.Label(x,text="Duplicate Key:").pack()

			ttk.Label(x,text="").grid(row=1,column=0)
			ttk.Label(x,text=" ").grid(row=1,column=0)		
	#submit button
	
	submit=ttk.Button(w,text='Submit',command=action)
	submit.grid(row=25,column=10,sticky=tk.N)
	w.mainloop()
