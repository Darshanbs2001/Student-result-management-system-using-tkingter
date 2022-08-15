import tkinter
from create_db import *
import os;
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #======variables=======
        self.var_question=StringVar()
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_password=StringVar()
        self.var_cpassword=StringVar()
        self.var_answer=StringVar()
        #=============bg image=============
        self.bg=ImageTk.PhotoImage(file="images/b2.jpg")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)
        self.left = ImageTk.PhotoImage(file="images/side.png")
        left = Label(self.root, image=self.left).place(x=80, y=100, width=400, height=500)
        btn_login=Button(self.root,text="Sign In",font=("times new roman",20),bd=0,cursor="hand2",command=self.add_signin).place(x=200,y=460,width=180)

        #===== register frame==========
        #==========left coulmn========
        frame1=Frame(self.root,bg="white").place(x=480,y=100,width=700,height=500)
        title=Label(frame1,text="REGISTER HERE ",font=("times new roman", 20,"bold"),bg="white",fg="green").place(x=530,y=130)
        f_name=Label(frame1,text="First Name",font=("times new roman ",15,"bold"),bg="white",fg="black").place(x=530,y=200)
        txt_fname=Entry(frame1,textvariable=self.var_fname,font=("times new roman",15),bg="lightgrey").place(x=530,y=230,width=250)
        contact = Label(frame1, text="Contact No", font=("times new roman ", 15, "bold"), bg="white", fg="black").place(x=530, y=270)
        txt_contact = Entry(frame1,textvariable=self.var_contact, font=("times new roman", 15), bg="lightgrey",fg="black").place(x=530, y=300, width=250)
        query= Label(frame1, text="Select Security Question", font=("times new roman ", 15, "bold"), bg="white", fg="black").place(
            x=530, y=340)
        txt_query = ttk.Combobox(frame1,textvariable=self.var_question,values=("Select","your First Pet Name","Your Birth Place","Your Best freind"),state="readonly", justify="center",font=("times new roman", 13)).place(x=530, y=370, width=250)
        password = Label(frame1, text="Password", font=("times new roman ", 15, "bold"), bg="white", fg="black").place(
            x=530, y=410)
        txt_password = Entry(frame1,textvariable=self.var_password, font=("times new roman", 15), bg="lightgrey").place(x=530, y=440, width=250)
        check=Checkbutton(frame1,text="I Agree The Terms & Conditions",font=("times new roman",12),bg="white",fg="black",onvalue=1,offvalue=0).place(x=530,y=470)
        self.btn_image=ImageTk.PhotoImage(file="images/register.png")
        btn_register=Button(frame1,image=self.btn_image,font=("times new roman",15,"bold"),bg="green",bd=0,cursor="hand2",command=self.register_data).place(x=530,y=520)
        #=============right coulmn============
        l_name = Label(frame1, text="Last Name", font=("times new roman ", 15, "bold"), bg="white", fg="black").place(x=850, y=200)
        txt_lname = Entry(frame1,text=self.var_lname,font=("times new roman", 15), bg="lightgrey").place(x=850, y=230, width=250)

        email = Label(frame1, text="Email", font=("times new roman ", 15, "bold"), bg="white", fg="black").place(x=850, y=270)
        txt_email = Entry(frame1,textvariable=self.var_email, font=("times new roman", 15), bg="lightgrey").place(x=850, y=300, width=250)
        answer = Label(frame1, text="Security answer", font=("times new roman ", 15, "bold"), bg="white", fg="black").place(x=850, y=340)
        txt_answer = Entry(frame1,text=self.var_answer, font=("times new roman", 15), bg="lightgrey").place(x=850, y=370, width=250)
        cpassword = Label(frame1, text="Confirm Password", font=("times new roman ", 15, "bold"), bg="white", fg="black").place(
            x=850, y=410)
        txt_cpassword = Entry(frame1,text=self.var_cpassword, font=("times new roman", 15), bg="lightgrey").place(x=850, y=440, width=250)
    def register_data(self):
        try:
            if self.var_question.get()=="" or self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_contact.get()=="" or self.var_email.get()=="" or self.var_password.get()=="" or self.var_cpassword.get()=="" or self.var_answer.get()=="":
                messagebox.showerror("Error","All fields are requried",parent=self.root)
            else:
                    mycursor.execute("select * from login where email=(%s)",(self.var_email.get(),))
                    rows=mycursor.fetchall()
                    if rows==[]:
                        if self.var_password.get()==self.var_cpassword.get():
                            contactno=int(self.var_contact.get())
                            mycursor.execute("insert into login values(%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_fname.get(),self.var_lname.get(),contactno,self.var_email.get(),self.var_password.get(),self.var_question.get(),self.var_answer.get(),"not logged in"))
                            mydb.commit()
                        else:
                            messagebox.showerror("Error","Password not matching",parent=self.root)
                    else:
                        messagebox.showerror("Error","Email alreay exists",parent=self.root)
        except EXCEPTION as ex:
            messagebox.showerror("Error",f"Error due to str{ex}")
    def add_signin(self):
        self.root.destroy()
        os.system("python login.py")



root=Tk()
obj=Register(root)
root.mainloop()