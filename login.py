from tkinter import *
from PIL import Image,ImageTk,ImageDraw
from datetime import *
from math import *
from tkinter import messagebox
import time
import os;
from create_db import *
from dashboard import *
class Login:
    def __init__(self,root1):
        self.root=root1
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")
        self.lbl=Label(self.root,bg="white",bd=0)
        self.lbl.place(x=90,y=120,width=350,height=450)
        left_lbl=Label(self.root,bg="white",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=600)
        left_lbl = Label(self.root, bg="#08A302", bd=0)
        left_lbl.place(x=0, y=0, relheight=1, width=600)
        #==============variables===========
        self.emailid=StringVar()
        self.var_password=StringVar()
        right_lbl = Label(self.root, bg="#031F3C", bd=0)
        right_lbl.place(x=0, y=0, relheight=1, relwidth=1)
        #==================================login================
        self.loginframe=Frame(self.root,bg="white").place(x=250,y=100,width=800,height=500)
        self.heading=Label(self.loginframe,text="LOGIN HERE",font=("times new roman",30,"bold"),bg="white",fg="#08A3D2").place(x=500,y=150)
        self.email=Label(self.loginframe,text="EMAIL ADDRESS",font=("times new roman",18,"bold"),bg="white",fg="grey").place(x=500,y=250)
        self.email_txt=Entry(self.loginframe,textvariable=self.emailid,font=("times new roman",15),bd=0,bg="lightgrey",fg="black").place(x=500,y=300,width=350,height=35)

        self.password=Label(self.loginframe,text="PASSWORD",font=("times new roman",18,"bold"),bg="white",fg="grey").place(x=500,y=350)
        self.email_txt=Entry(self.loginframe,textvariable=self.var_password,font=("times new roman",15),bd=0,bg="lightgrey",fg="black").place(x=500,y=400,width=350,height=35)
        #======================buttons==============
        self.btn_reg=Button(self.loginframe,text="Register New Account",font=("times new roman",14),bg="white",bd=0,fg="#B00857",cursor="hand2",command=self.add_reg).place(x=500,y=440)
        self.btn_login=Button(self.loginframe,text="Login",font=("times new roman",20,"bold"),command=self.add_dashboard,fg="white",bg="#B00857",cursor="hand2").place(x=500,y=480,width=150,height=40)

    def add_reg(self):
        self.root.destroy()
        os.system("python register.py")

    def add_dashboard(self):
        if self.emailid.get()=="" or self.var_password.get()=="":
            messagebox.showerror("Error","Please fill all the field",parent=self.root)
        else:
             mycursor.execute("select email,password from login where email=%s",(self.emailid.get(),))
             rows=mycursor.fetchall()
             for row in rows:
                if self.emailid.get()==row[0] and self.var_password.get()==row[1]:
                    mycursor.execute("update login set status=%s",("logged in",))
                    mydb.commit()
                    self.root.destroy()
                    os.system("python dashboard.py")
                elif self.emailid.get()==row[0] and self.var_password.get()==row[1]:
                    messagebox.showerror("Error","Incorrect password",parent=self.root)
                else:
                    messagebox.showerror("Error","The User doesnot exist please register yourself",parent=self.root)



if __name__=="__main__":
    root1=Tk()
    obj=Login(root1)
    root1.mainloop()