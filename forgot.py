from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk,ImageDraw
from datetime import *
from math import *
from tkinter import messagebox
import time
import os;
from create_db import *
from dashboard import *
class Forgot:
    var_emailid = ""
    def __init__(self,root):
                self.root=root



                self.root.config(bg="white")
                self.root.title("Forgot Password")
                self.root.geometry("400x400+450+150")
                self.root.focus_force()
                self.root.grab_set()
                self.var_question = StringVar()
                self.var_answer = StringVar()
                self.var_newpassword=StringVar()
                t = Label(self.root, text="Forgot Password", font=("times new roman", 20, "bold"), bg="white",
                          fg="red").place(x=0, y=10, relwidth=1)
                query = Label(self.root, text="Select Security Question", font=("times new roman ", 15, "bold"),
                              bg="white",
                              fg="black").place(
                    x=50, y=100)
                txt_query = ttk.Combobox(self.root, textvariable=self.var_question, values=(
                "Select", "your First Pet Name", "Your Birth Place", "Your Best freind"), state="readonly",
                                         justify="center", font=("times new roman", 13)).place(x=50, y=130, width=250)
                answer = Label(self.root, text="Security answer", font=("times new roman ", 15, "bold"), bg="white",
                               fg="black").place(x=50, y=180)
                txt_answer = Entry(self.root, text=self.var_answer, font=("times new roman", 15), bg="lightgrey").place(
                    x=50,
                    y=210,
                    width=250)
                password = Label(self.root, text="New Password", font=("times new roman ", 15, "bold"), bg="white",
                                 fg="black").place(x=50, y=260)
                txt_newpassword = Entry(self.root, text=self.var_newpassword, font=("times new roman", 15),
                                        bg="lightgrey").place(x=50,
                                                              y=290,
                                                              width=250)
                btn_change = Button(self.root, text="Reset Password", font=("times new roman", 15, "bold"), fg="white",
                                    bg="green", cursor="hand2", command=self.change).place(x=50, y=340, width=150,
                                                                                        height=30)


    def change(self):
        if self.var_newpassword.get()=="":
            messagebox.showerror("Error","Please enter the new password to reset")
            #print(self.var_emailid)
        else:
             mycursor.execute("select question,answer from login where email=%s",(self.var_emailid,))
             rows=mycursor.fetchall()
             for row in rows:
                 if self.var_question.get()==row[0] and self.var_answer.get()==row[1]:
                     mycursor.execute("update login set password=%s where email=%s",(self.var_newpassword.get(),self.var_emailid))
                     mydb.commit()
                     messagebox.showinfo("Success","Your password has been changed ")
                     self.root.destroy()
                 elif self.var_question.get()!=row[0] or self.var_answer.get()!=row[1]:
                     messagebox.showerror("Error","Wrong question or answer ")



if __name__=="__main__":
    root=Tk()
    obj=Forgot(root)
    root.mainloop()