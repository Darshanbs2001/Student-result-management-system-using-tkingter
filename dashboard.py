from tkinter import *
from tkinter import messagebox
from create_db import *
from PIL import Image,ImageTk
from Course import Courseclass
from Student import Studentclass
from result import Result
from view import View
import os;

class RMS:

    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Mangament System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #---- icons ----
        self.logo_dash=ImageTk.PhotoImage(file="images/logo_p.png")
        title = Label(self.root, text="Student Result Management System",compound=LEFT,padx=10,  image=self.logo_dash ,font=("goudy old style", 20, "bold"), bg="#033054",
                     fg="white").place(x=0, y=0, relwidth=1, height=50)
        self.window1=False
        self.window2=False
        self.window3=False
        self.window4=False
        #self.var_courseno=StringVar()
        #self.var_studentno=StringVar()
        #self.var_resultno=StringVar()
        #====menu ====
        M_Frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=70,width=1340,height=80)

        btn_course=Button(M_Frame,text="Course",font=("goudy old style ",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=180,height=40)
        btn_submit=Button(M_Frame,text="Student",font=("goudy old style ",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_Student).place(x=220,y=5,width=180,height=40)
        btn_result=Button(M_Frame,text="Result",font=("goudy old style ",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_Result).place(x=420,y=5,width=180,height=40)
        btn_view_student_result=Button(M_Frame,text="View Student Result",font=("goudy old style ",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_view).place(x=620,y=5,width=200,height=40)
        btn_logout=Button(M_Frame,text="Logout",command=self.logout,font=("goudy old style ",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=840,y=5,width=180,height=40)
        btn_exit=Button(M_Frame,text="Exit",font=("goudy old style ",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.exit).place(x=1040,y=5,width=180,height=40)
        #====content_window===
        self.bg_img=Image.open("images/bg.png")
        self.bg_img=self.bg_img.resize((920,350),Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=400,y=180,width=920,height=350)

        #===update_details===

        self.lbl_course=Label(self.root,text="Total Course\n [0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06")
        self.lbl_course.place( x = 400, y = 530, width = 270, height=80)

        self.lbl_student = Label(self.root, text="Total Students\n [0]", font=("goudy old style", 20), bd=10, relief=RIDGE,
                                bg="#0676ad")
        self.lbl_student.place(x=690, y=530, width=270, height=80)

        self.lbl_result = Label(self.root, text="Total Results\n [0]", font=("goudy old style", 20), bd=10, relief=RIDGE,
                                bg="#038074")
        self.lbl_result.place(x=980, y=530, width=270, height=80)
        #===footer====
        footer = Label(self.root, text="SRMS-Student Result Management System\nContact Us for any Technical Issue: 987xxx01",
                  font=("goudy old style", 15, "bold"), bg="#262626",
                  fg="white").pack(side=BOTTOM,fill=X)
        self.update_details()
    def add_course(self):
        if self.window1==True:
            self.new_win1.destroy()
            self.window1=False
        if self.window2==True:
            self.new_win2.destroy()
            self.window2=False
        if self.window3==True:
            self.new_win3.destroy()
            self.window3=False
        self.window1=True
        self.new_win1=Toplevel(self.root)
        self.new_obj1=Courseclass(self.new_win1)
    def update_details(self):
        mycursor.execute("select * from course")
        cr=mycursor.fetchall()
        self.lbl_course.config(text=f"Total Courses\n[{str(len(cr))}]")
        self.lbl_course.after(200,self.update_details)
        mycursor.execute("select * from student")
        sr=mycursor.fetchall()
        self.lbl_student.config(text=f"Total Students\n[{str(len(sr))}]")
        #self.lbl_student.after(200,self.update_details)
        mycursor.execute("select regno from result")
        rr=mycursor.fetchall()
        self.lbl_result.config(text=f"Total Results\n[{str(len(rr))}]")
        #self.lbl_result.after(200,self.update_details)

    def add_Student(self):
        if self.window1 == True:
            self.new_win1.destroy()
            self.window1 = False
        if self.window2==True:
            self.new_win2.destroy()
            self.window2=False
        if self.window3 == True:
            self.new_win3.destroy()
            self.window3=False
        if self.window3 == True:
            self.new_win3.destroy()
            self.window3 = False
        self.window2=True
        self.new_win2=Toplevel(self.root)
        self.new_obj2=Studentclass(self.new_win2)


    def add_view(self):
        if self.window1==True:
            self.new_win1.destroy()
            self.window1=False
        if self.window2 == True:
            self.new_win2.destroy()
            self.window2=False
        if self.window3 == True:
            self.new_win3.destroy()
            self.window3=False
        if self.window4 == True:
            self.new_win4.destroy()
            self.window4 = False
        self.window4=True
        self.new_win4 = Toplevel(self.root)
        self.new_obj4 = View(self.new_win4)
    def add_Result(self):
        if self.window1==True:
            self.new_win1.destroy()
            self.window1=False
        if self.window2 == True:
            self.new_win2.destroy()
            self.window2=False
        if self.window3 == True:
            self.new_win3.destroy()
            self.window3=False
        if self.window4 == True:
            self.new_win4.destroy()
            self.window4 = False
        self.window3=True
        self.new_win3 = Toplevel(self.root)
        self.new_obj3 = Result(self.new_win3)
    def logout(self):
        mycursor.execute("update login set status=%s",("not logged in",))
        mydb.commit()
        self.root.destroy()
        os.system("python login.py")

    def exit(self):
        mycursor.execute("update login set status=%s", ("not logged in",))
        mydb.commit()
        self.root.destroy()

if __name__ == "__main__":

    mycursor.execute("select email,status from login where status=%s",("logged in",))
    rows=mycursor.fetchall()
    if rows==[]:
        messagebox.showerror("Error","please login first to use the app")
    else:
       root = Tk()
       obj = RMS(root)
       root.mainloop()
