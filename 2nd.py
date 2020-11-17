import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Da@9141525275",
  database = "mydatabase"
)
mycursor=mydb.cursor()
#sql=("insert into customs (name,address) values(%s,%s)")
#val=("darshan","belur")
#mycursor.execute(sql,val)
#mydb.commit()
#print(mycursor.rowcount,"record inserted")
mycursor.execute("select * from customs")
myresult=mycursor.fetchall()


for x in myresult:
    print(x)
###

