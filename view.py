from tkinter import *
from create_db import mycursor
from mail import *
import threading
import asyncio
from asyncio import *;
from tkinter import ttk, messagebox
from sendFiles import sendfiles;
from async_tkinter_loop import async_mainloop,async_handler
class View:
     def __init__(self, root):
        self.root = root
        self.root.title("Student Result Mangament System")
        self.root.geometry("1200x480+70+170")
        self.root.config(bg="white")
        self.root.focus_force()
        # ====================variables===============
        self.var_course = StringVar()
        self.regno = StringVar()
        self.var_semister = StringVar()
        self.course_list = []
        self.selected = False
        self.fetch_course()
        self.var_subject1 = StringVar()
        self.var_subject2 = StringVar()
        self.var_subject3 = StringVar()
        self.deletevariable = StringVar()
        self.sendvariable = StringVar()


        # ====================title========================
        self.title = Label(self.root, text="View And Verify Students Result", font=("goudy old style", 20, "bold"),
                           bg="orange", fg="black", relief=RIDGE, bd=10)
        self.title.place(x=0, y=0, relwidth=1, height=50)
        # ==============================search panel======================
        self.lbl_coursename = Label(self.root, text="Course", font=("goudy old style", 15, "bold"), bg="white").place(
            x=130, y=70)
        self.lbl_Semistername = Label(self.root, text="Semister", font=("goudy old style", 15, "bold"),
                                      bg="white").place(x=440, y=70)
        self.lbl_course = ttk.Combobox(self.root, textvariable=self.var_course, values=self.course_list,
                                       font=("goudy old style", 15, "bold"), justify="center", state="readonly")
        self.lbl_course.place(x=200, y=70, width=200, height=35)
        self.lbl_semister = ttk.Combobox(self.root, textvariable=self.var_semister,
                                         values=["Select", "I-Semister", "II-Semister", "III-Semister", "IV-Semister",
                                                 "V-Semister", "VI-Semister"], font=("goudy old style", 15, "bold"),
                                         justify="center", state="readonly")
        self.lbl_semister.place(x=520, y=70, width=200, height=35)
        self.btn_sort = Button(self.root, text="Sort", font=("goudy old style", 15, "bold"), bg="red", fg="black", bd=5,
                               command=self.sort).place(x=760, y=70, width=150, height=35)

        # =============content tile====================
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=10, y=120, width=1180, height=300)

        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)
        self.CourseTable = ttk.Treeview(self.C_Frame,
                                        columns=("regno", "course", "sem", "tm1", "pm1", "tm2", "pm2", "m3", "pm3"),
                                        xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)
        self.CourseTable.heading("regno", text="Register NO")
        self.CourseTable.heading("course", text="Course")
        self.CourseTable.heading("sem", text="Semister")
        self.CourseTable.heading("tm1", text=self.var_subject1.get() + " Theory")
        self.CourseTable.heading("pm1", text=self.var_subject1.get() + " Practical")
        self.CourseTable.heading("tm2", text=self.var_subject2.get() + " Theory")
        self.CourseTable.heading("pm2", text=self.var_subject2.get() + " Practical")
        self.CourseTable.heading("m3", text=self.var_subject3.get() + " Theory")
        self.CourseTable.heading("pm3", text=self.var_subject3.get() + " Practical")
        self.CourseTable["show"] = "headings"
        self.CourseTable.column("regno", width=100)
        self.CourseTable.column("course", width=100)
        self.CourseTable.column("sem", width=100)
        self.CourseTable.column("tm1", width=100)
        self.CourseTable.column("pm1", width=100)
        self.CourseTable.column("tm2", width=100)
        self.CourseTable.column("pm2", width=100)
        self.CourseTable.column("m3", width=100)
        self.CourseTable.column("pm3", width=100)

        self.CourseTable.pack(fill=BOTH, expand=1)
        self.CourseTable.bind("<ButtonRelease-1>", self.get_data)

     def get_data(self, ev):
        r = self.CourseTable.focus()
        self.deletevariable.set("delete")
        self.sendvariable.set("send")
        content = self.CourseTable.item(r)
        row = content["values"]
        self.regno.set(row[0])
        self.selected = True

     def delete(self):
        if self.selected == True:
            mycursor.execute("delete from result where regno=%s and sem=%s and course=%s",
                             (self.regno.get(), self.var_semister.get(), self.var_course.get()))
            mydb.commit()
            messagebox.showinfo("Success", "the result has been deleted")
            self.sort()
        else:
            mycursor.execute("delete from result where sem=%s and course=%s",
                             (self.var_semister.get(), self.var_course.get()))
            mydb.commit()
            messagebox.showinfo("Success", "All the result is delected ")
            self.sort()

     def fetch_course(self):
        try:
            mycursor.execute("select name from course")
            rows = mycursor.fetchall()
            if len(rows) > 0:
                for row in rows:
                    self.course_list.append(row[0])
        except EXCEPTION as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

     def sort(self):
         try:
            self.sendvariable.set("send all")
            self.deletevariable.set("delete all")
            self.btn_sendmail = Button(self.root, textvariable=self.sendvariable, font=("goudy old style", 15, "bold"),
                                       bg="yellow", fg="black", bd=5, command=async_handler(self.send)).place(x=1020, y=433, width=150,
                                                                                               height=35)
            self.btn_delete = Button(self.root, textvariable=self.deletevariable, font=("goudy old style", 15, "bold"),
                                     bg="red", fg="black", bd=5, command=self.delete).place(x=850, y=433, width=150,height=35)
            mycursor.execute("select s1,s2,s3 from course where name=%s", (self.var_course.get(),))
            crows = mycursor.fetchall()
            for crow in crows:
                self.var_subject1.set(crow[0])
                self.var_subject2.set(crow[1])
                self.var_subject3.set(crow[2])

            mycursor.execute("select regno,course,sem,tm1,pm1,tm2,pm2,m3,pm3 from result where course=%s and sem=%s",
                             (self.var_course.get(), self.var_semister.get(),))
            rows = mycursor.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            if rows == []:
                messagebox.showerror("Error", "There are no results present")
            else:

                for row in rows:
                    self.CourseTable.insert('', END, values=row)




         except EXCEPTION as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


     async def send(self):
        # messagebox.showinfo("warning ","The emails are being sent",parent=self.root)
       await sendfiles(self.selected,self.regno,self.var_semister,self.var_course);
            # messagebox.showinfo("Success", "The emails have been sent", parent=self.root)
       messagebox.showinfo("Success", "The email has been sent", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = View(root)
    #root.mainloop()
    async_mainloop(root)

