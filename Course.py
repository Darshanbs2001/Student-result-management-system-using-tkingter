from tkinter import *
from create_db import *

from PIL import Image,ImageTk
from tkinter import ttk ,messagebox
class Courseclass:


    #=======================================main cours=============
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Mangament System")
        self.root.geometry("1200x480+70+170")
        self.root.config(bg="white")
        self.root.focus_force()
         #====title===
        title = Label(self.root, text="Manage Course Details",font=("goudy old style", 20, "bold"), bg="#033054",
                     fg="white").place(x=10, y=15, width=1180, height=35)
        #====variables====
        self.var_course=StringVar()
        self.var_duration=StringVar()
        self.var_charges=StringVar()
        self.var_subject1=StringVar()
        self.var_subject2=StringVar()
        self.var_subject3=StringVar()
        self.var_cid=IntVar()

        #=== widgets ====
        lbl_courseName=Label(self.root,text="Course Name",font=("goudy old style ",15,'bold'),bg="white").place(x=10,y=60)
        lbl_duration =Label(self.root,text="Duration",font=("goudy old style ",15,"bold"),bg="white").place(x=10,y=100)
        lbl_charges = Label(self.root, text="Charges", font=("goudy old style ", 15, "bold"), bg="white").place(x=10,y=140)
        lbl_subject1 = Label(self.root, text="Subject 1", font=("goudy old style ", 15, "bold"), bg="white").place(x=10,y=180)
        lbl_subject2 = Label(self.root, text="Subject 2", font=("goudy old style ", 15, "bold"), bg="white").place(x=10,y=220)
        lbl_subject3 = Label(self.root, text="Subejct 3", font=("goudy old style ", 15, "bold"), bg="white").place(x=10,y=260)

        #===entryfield===

        self.txt_courseName = Entry(self.root,textvariable=self.var_course, font=("goudy old style ", 15, 'bold'), bg="lightyellow")
        self.txt_courseName.place(x=150, y=60,width=200)
        self.txt_duration = Entry(self.root, textvariable=self.var_duration, font=("goudy old style ", 15,"bold"), bg="lightyellow")
        self.txt_duration.place(x=150,y=100,width=200)
        self.txt_charges =  Entry(self.root,textvariable=self.var_charges,  font=("goudy old style ", 15,"bold"), bg="lightyellow")
        self.txt_charges.place(x=150,y=140,width=200)
        self.txt_subject1=Entry(self.root,textvariable=self.var_subject1,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_subject1.place(x=150,y=180,width=200)
        self.txt_subject2 = Entry(self.root, textvariable=self.var_subject2, font=("goudy old style", 15,"bold"),
                                  bg="lightyellow")
        self.txt_subject2.place(x=150, y=220, width=200)
        self.txt_subject3 = Entry(self.root, textvariable=self.var_subject3, font=("goudy old style", 15,"bold"),
                                  bg="lightyellow")
        self.txt_subject3.place(x=150, y=260, width=200)
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
        lbl_search = Label(self.root, text="Course Name", font=("goudy old style ", 15, 'bold'), bg="white").place(
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
        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("cid","name","charges","s1","s2","s3","duration"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)
        self.CourseTable.heading("cid",text="Course ID")
        self.CourseTable.heading("name", text="Name")
        self.CourseTable.heading("charges", text="Charges")
        self.CourseTable.heading("s1", text="Subject 1")
        self.CourseTable.heading("s2", text="Subject 2")
        self.CourseTable.heading("s3", text="Subject 3")
        self.CourseTable.heading("duration", text="Durations")
        self.CourseTable["show"]="headings"
        self.CourseTable.column("cid",width=100 )
        self.CourseTable.column("name",width=100 )
        self.CourseTable.column("charges", width=100)
        self.CourseTable.column("s1",width=100 )
        self.CourseTable.column("s2",width=100 )
        self.CourseTable.column("s3",width=100 )
        self.CourseTable.column("duration",width=100 )



        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
#============ functions ========
    def add(self):
        # con = sqlite3.connect(database="rms.db")
        # cur = con.cursor()

        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error", "Course Name should be required ", parent=self.root)
            else:
                mycursor.execute("select * from course where name=%s", (self.var_course.get(),))
                row = mycursor.fetchone()
                if row == None:
                    val = (self.var_course.get(), self.var_duration.get(), self.var_charges.get(),
                           self.var_subject1.get(),self.var_subject2.get(),self.var_subject3.get())
                    sql = "insert into course(name,duration,charges,s1,s2,s3) values(%s,%s,%s,%s,%s,%s)"
                    mycursor.execute(sql, val)
                    mydb.commit()
                    messagebox.showerror("Success", "Course Added Successfully ", parent=self.root)
                    self.show()

                else:
                    messagebox.showerror("Error", "The course name already exists", parent=self.root)

        except EXCEPTION as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def clear(self):
        self.show()
        self.var_course.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        self.var_subject1.set("")
        self.var_subject2.set("")
        self.var_subject3.set("")

    def show(self):
        try:
            mycursor.execute("select * from course")
            rows = mycursor.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('', END, values=row)
        except EXCEPTION as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def get_data(self, ev):
        r = self.CourseTable.focus()
        content = self.CourseTable.item(r)
        row = content["values"]
        self.var_cid.set(row[0])
        self.var_course.set(row[1])
        self.var_charges.set(row[2])
        self.var_subject1.set(row[3])
        self.var_subject2.set(row[4])
        self.var_subject3.set(row[5])
        self.var_duration.set(row[5])


    def update(self):
        # con = sqlite3.connect(database="rms.db")
        # cur = con.cursor()#

        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error", "Course Name should be required ", parent=self.root)
            else:
                mycursor.execute("select * from course where cid=%s", (self.var_cid.get(),))
                row = mycursor.fetchone()
                if row != None:
                    mycursor.execute("update course set duration=%s,charges=%s,s1=%s,s2=%s,s3=%s,name=%s where cid=%s", (
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.var_subject1.get(),
                        self.var_subject2.get(),
                        self.var_subject3.get(),
                        self.var_course.get(),
                        self.var_cid.get()
                    ))
                    mydb.commit()
                    messagebox.showerror("Success", "Course Updated successfully ", parent=self.root)
                    self.show()
                else:
                    messagebox.showerror("Error", "Select course from the list", parent=self.root)



        except EXCEPTION as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def search(self):
        try:
            if self.var_search.get() == "":
                messagebox.showerror("Error", "please enter the course name", parent=self.root)
            else:

                mycursor.execute(("select * from course where name =%s"), (self.var_search.get(),))
                rows = mycursor.fetchall()
                if rows != [] and rows != None:
                    self.CourseTable.delete(*self.CourseTable.get_children())
                    for row in rows:
                        self.CourseTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "please eneter the course that is present in the list",
                                         parent=self.root)
        except EXCEPTION as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def dele(self):
        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error", "Course Name should be required ", parent=self.root)
            else:

                mycursor.execute("select * from course where name=%s", (self.var_course.get(),))
                row = mycursor.fetchone()
                if row != None:
                    op = messagebox.askyesno("Confirm", "Do you reall want to delete?", parent=self.root)
                    if op == True:
                        sql = "delete from course where name=%s"
                        mycursor.execute(sql, (self.var_course.get(),))
                        mydb.commit()
                        mycursor.execute("delete from result where course=%s", (self.var_course.get(),))
                        mydb.commit()
                        mycursor.execute("delete from student where course=%s",(self.var_course.get(),))
                        mydb.commit()

                        messagebox.showinfo("Success", "Course deleted Successfully ", parent=self.root)
                        self.show()
                        self.clear()


                else:
                    messagebox.showerror("Error", "please select from the list first", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to str{(ex)}")


if __name__=="__main__":
    root=Tk()
    obj=Courseclass(root)
    root.mainloop()
