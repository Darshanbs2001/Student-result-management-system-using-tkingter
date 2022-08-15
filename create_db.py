from tkinter import *
import mysql.connector
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Da@9141525275",
    database="another"

)
mycursor=mydb.cursor()