from create_db import *

from tkinter import ttk ,messagebox
class Studentclass:


    #=======================================main cours=============
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Mangament System")
        self.root.geometry("1200x480+70+170")
        self.root.config(bg="white")
        self.root.focus_force()
         #====title===
        title = Label(self.root, text="Manage Students Details",font=("goudy old style", 20, "bold"), bg="#033054",
                     fg="white").place(x=10, y=15, width=1180, height=35)
        #====variables====
        self.var_rollno=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_address=StringVar()
        self.var_contact=StringVar()
        self.var_a_date=StringVar()
        self.var_state=StringVar()
        self.var_city=StringVar()
        self.var_pin=StringVar()
        self.var_course=StringVar()
        self.var_cid=IntVar()

        #=== widgets ====
        #==========columns===================
        lbl_rollno=Label(self.root,text="Roll NO",font=("goudy old style ",15,'bold'),bg="white").place(x=10,y=60)
        lbl_name =Label(self.root,text="Name",font=("goudy old style ",15,"bold"),bg="white").place(x=10,y=100)
        lbl_email = Label(self.root, text="Email", font=("goudy old style ", 15, "bold"), bg="white").place(x=10,y=140)
        lbl_gender = Label(self.root, text="Gender", font=("goudy old style ", 15, "bold"), bg="white").place(x=10,y=180)
        lbl_state = Label(self.root, text="State", font=("goudy old style ", 15, "bold"), bg="white").place(x=10,y=220)
        lbl_address = Label(self.root, text="Address", font=("goudy old style ", 15, "bold"), bg="white").place(x=10,y=260)
        #==================column2=========================
        lbl_dob = Label(self.root, text="D.O.B", font=("goudy old style ", 15, 'bold'), bg="white").place(x=360,y=60)
        lbl_contact = Label(self.root, text="Contact", font=("goudy old style ", 15, "bold"), bg="white").place(x=360, y=100)
        lbl_admission= Label(self.root, text="Admission", font=("goudy old style ", 15, "bold"), bg="white").place(x=360, y=140)
        lbl_course = Label(self.root, text="Course", font=("goudy old style ", 15, "bold"), bg="white").place(x=360,y=180)
        lbl_city = Label(self.root, text="City", font=("goudy old style ", 15, "bold"), bg="white").place(x=310,y=220)
        lbl_pin = Label(self.root, text="Pin Code", font=("goudy old style ", 15, "bold"), bg="white").place(x=470,y=220)
        #===entryfield===
        #=============================column1========================================
        self.txt_rollno = Entry(self.root,state=NORMAL,textvariable=self.var_rollno, font=("goudy old style ", 15, 'bold'), bg="lightyellow")
        self.txt_rollno.place(x=150, y=60,width=200)
        self.txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style ", 15,"bold"), bg="lightyellow")
        self.txt_name.place(x=150,y=100,width=200)
        self.txt_email =  Entry(self.root,textvariable=self.var_email,  font=("goudy old style ", 15,"bold"), bg="lightyellow")
        self.txt_email.place(x=150,y=140,width=200)
        self.txt_state = Entry(self.root, textvariable=self.var_state, font=("goudy old style ", 15, "bold"),
                               bg="lightyellow")
        self.txt_state.place(x=150, y=220, width=150)
        self.txt_gender = ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Others"),  font=("goudy old style ", 15,"bold"),justify="center",state="readonly")
        self.txt_gender.place(x=150,y=180,width=200)
        self.txt_gender.current(0)
       #===========================column2===========================================================
        self.course_list=['Select',]
        self.fetch_course()
        #============================function call=================

        self.txt_dob = Entry(self.root, textvariable=self.var_dob, font=("goudy old style ", 15, 'bold'),
                                bg="lightyellow")
        self.txt_dob.place(x=480, y=60, width=200)
        self.txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style ", 15, "bold"),
                              bg="lightyellow")
        self.txt_contact.place(x=480, y=100, width=200)
        self.txt_admission = Entry(self.root, textvariable=self.var_a_date, font=("goudy old style ", 15, "bold"),
                               bg="lightyellow")
        self.txt_admission.place(x=480, y=140, width=200)
        self.txt_course = ttk.Combobox(self.root, textvariable=self.var_course,values=self.course_list,
                                       font=("goudy old style ", 15, "bold"), justify="center", state="readonly")
        self.txt_course.place(x=480, y=180, width=200)
        self.txt_course.current(0)
        self.txt_city = Entry(self.root, textvariable=self.var_city, font=("goudy old style ", 15, 'bold'),
                             bg="lightyellow")
        self.txt_city.place(x=360, y=220, width=100)
        self.txt_pin = Entry(self.root, textvariable=self.var_pin, font=("goudy old style ", 15, 'bold'),
                             bg="lightyellow")
        self.txt_pin.place(x=560, y=220, width=120)
        #self.txt_email =  Entry(self.root,textvariable=self.var_charges,  font=("goudy old style ", 15,"bold"), bg="lightyellow")
        #self.txt_email.place(x=150,y=140,width=200)
        #self.txt_email =  Entry(self.root,textvariable=self.var_charges,  font=("goudy old style ", 15,"bold"), bg="lightyellow")
        #self.txt_email.place(x=150,y=140,width=200)
        #self.txt_email =  Entry(self.root,textvariable=self.var_charges,  font=("goudy old style ", 15,"bold"), bg="lightyellow")
        #self.txt_email.place(x=150,y=140,width=200)




        #=================Text Address=================================================
        self.txt_address=Entry(self.root,textvariable=self.var_address,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_address.place(x=150,y=260,height=100,width=540)
        #self.txt_subject2 = Entry(self.root, textvariable=self.var_dob, font=("goudy old style", 15,"bold"),
         #                         bg="lightyellow")
        #self.txt_subject2.place(x=150, y=220, width=200)
        #self.txt_subject3 = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15,"bold"),
         #                         bg="lightyellow")
        #self.txt_subject3.place(x=150, y=260, width=200)
        #self.txt_descrition =Text(self.root,font=("goudy old style ", 15, "bold"), bg="lightyellow")
        #self.txt_descrition.place(x=150, y=180,width=500,height=130)

        #===button======
        self.btn_add=Button(self.root,text="Save",font=("goudy old style ",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=150,y=400,width=110,height=40)
        self.btn_update = Button(self.root, text="Update", font=("goudy old style ", 15, "bold"), bg="#4caf50", fg="white",cursor="hand2",command=self.update)
        self.btn_update.place(x=270, y=400, width=110, height=40)
        self.btn_delete = Button(self.root, text="Delete", font=("goudy old style ", 15, "bold"), bg="#f44336",fg="white",cursor="hand2",command=self.dele)
        self.btn_delete.place(x=390, y=400, width=110, height=40)
        self.btn_clear= Button(self.root, text="Clear", font=("goudy old style ", 15, "bold"), bg="#607d8b", fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510, y=400, width=110, height=40)

        #===search panel====
        self.var_search=StringVar()
        lbl_search = Label(self.root, text="Roll No.", font=("goudy old style ", 15, 'bold'), bg="white").place(
            x=720, y=60)
        txt_search = Entry(self.root, textvariable=self.var_search, font=("goudy old style ", 15, 'bold'),
                                    bg="lightyellow").place(x=870, y=60, width=180)
        btn_search = Button(self.root, text="Search", font=("goudy old style ", 15, "bold"), bg="#03a9f4", fg="white",
                              cursor="hand2",command=self.search).place(x=1070, y=60, width=120, height=28)
        #====content list ====
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720,y=100,width=470,height=340)

        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("roll","name","email","gender","dob","contact","admission","course","state","city","pin","address"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)
        self.CourseTable.heading("roll",text="Roll No")
        self.CourseTable.heading("name", text="Name")
        self.CourseTable.heading("email", text="Email")
        self.CourseTable.heading("gender", text="Gender")
        self.CourseTable.heading("dob", text="D.O.B")
        self.CourseTable.heading("contact", text="Contact")
        self.CourseTable.heading("admission", text="Admission")
        self.CourseTable.heading("course", text="Course")
        self.CourseTable.heading("state", text="State")
        self.CourseTable.heading("city", text="City")
        self.CourseTable.heading("pin", text="PIN")
        self.CourseTable.heading("address", text="Address")


        self.CourseTable["show"]="headings"
        self.CourseTable.column("roll",width=100 )
        self.CourseTable.column("name",width=100 )
        self.CourseTable.column("email", width=100)
        self.CourseTable.column("dob",width=100 )
        self.CourseTable.column("contact",width=100 )
        self.CourseTable.column("gender",width=100 )
        self.CourseTable.column("admission",width=100 )
        self.CourseTable.column("course",width=100 )
        self.CourseTable.column("state",width=100 )
        self.CourseTable.column("city",width=100 )
        self.CourseTable.column("pin",width=100 )
        self.CourseTable.column("address",width=100 )



        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

#============ functions ========
    def add(self):
        # con = sqlite3.connect(database="rms.db")
        # cur = con.cursor()

        try:
            if self.var_rollno.get() == "":
                messagebox.showerror("Error", "Course Name should be required ", parent=self.root)
            else:
                mycursor.execute("select * from student where roll=%s", (self.var_rollno.get(),))
                row = mycursor.fetchone()
                if row == None:
                    val = (self.var_rollno.get(), self.var_name.get(), self.var_email.get(),
                           self.var_gender.get(),self.var_dob.get(),self.var_contact.get(),
                           self.var_a_date.get(),self.var_course.get(),self.var_state.get(),
                           self.var_city.get(),self.var_pin.get(),self.var_address.get(),)
                    sql = "insert into student(roll,name,email,gender,dob,contact,admission,course,state,city,pin,address) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    mycursor.execute(sql, val)
                    mydb.commit()
                    messagebox.showinfo("Success", "Student  Added Successfully ", parent=self.root)
                    self.show()
                else:
                    messagebox.showerror("Error", "The Student already exists", parent=self.root)

        except EXCEPTION as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")



    def clear(self):
        self.show()
        self.var_rollno.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_address.set("")
        self.var_contact.set("")
        self.var_a_date.set("")
        self.var_state.set("")
        self.var_city.set("")
        self.var_pin.set("")
        self.var_course.set("Select")
        self.var_search.set("")

    def show(self):
        try:
            mycursor.execute("select * from student")
            rows = mycursor.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('', END, values=row)
        except EXCEPTION as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
    def fetch_course(self):
        try:
            mycursor.execute("select name from course")
            rows = mycursor.fetchall()
            if len(rows) > 0 :
                for row in rows:
                    self.course_list.append(row[0])



        except EXCEPTION as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
    def get_data(self, ev):
        r = self.CourseTable.focus()
        content = self.CourseTable.item(r)
        row = content["values"]
        #self.txt_rollno.setstate(READABLE)
        self.var_rollno.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_dob.set(row[4])
        self.var_contact.set(row[5])
        self.var_a_date.set(row[6])
        self.var_course.set(row[7])
        self.var_state.set(row[8])
        self.var_city.set(row[9])
        self.var_pin.set(row[10])
        self.var_address.set(row[11])



    def update(self):
        # con = sqlite3.connect(database="rms.db")
        # cur = con.cursor()#

        try:
            if self.var_rollno.get() == "":
                messagebox.showerror("Error", "Roll Number is required ", parent=self.root)
            else:
                mycursor.execute("select * from student where roll=%s", (self.var_rollno.get(),))
                row = mycursor.fetchone()
                if row != None:
                    mycursor.execute("update student set name=%s,email=%s,gender=%s,dob=%s,contact=%s,admission=%s,course=%s,state=%s,city=%s,pin=%s,address=%s where roll=%s",(
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.var_address.get(),
                        self.var_rollno.get(),
                    ))
                    mydb.commit()
                    messagebox.showerror("Success", "Student details Updated successfully ", parent=self.root)
                    self.show()
                else:
                    messagebox.showerror("Error", "Select student from the list", parent=self.root)



        except EXCEPTION as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def search(self):
        try:
            if self.var_search.get() == "":
                messagebox.showerror("Error", "please enter the register number name", parent=self.root)
            else:

                mycursor.execute(("select * from student where roll=%s"), (self.var_search.get(),))
                rows = mycursor.fetchall()
                if rows != [] and rows != None:
                    self.CourseTable.delete(*self.CourseTable.get_children())
                    for row in rows:
                        self.CourseTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "please eneter the rollno that is present in the list",
                                         parent=self.root)
        except EXCEPTION as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def dele(self):
        try:
            if self.var_rollno.get() == "":
                messagebox.showerror("Error", "Roll Number is required ", parent=self.root)
            else:
                mycursor.execute("select * from student where roll=%s", (self.var_rollno.get(),))
                row = mycursor.fetchone()
                if row != None:
                    op = messagebox.askyesno("Confirm", "Do you reall want to delete?", parent=self.root)
                    if op == True:
                        sql = "delete from student where roll=%s"
                        mycursor.execute(sql, (self.var_rollno.get(),))
                        mydb.commit()
                        messagebox.showinfo("Success", "Student deleted Successfully ", parent=self.root)
                        self.show()
                        self.clear()
                else:
                    messagebox.showerror("Error", "please select from the list first", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to str{(ex)}")


if __name__=="__main__":
    root=Tk()
    obj=Studentclass(root)
    root.mainloop()
