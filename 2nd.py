import mysql.connector

user_in=input("please enter the user id:")
pass_in=input("please enter the password:")
database=input("please enter the name of the database:")
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user=user_in,
  password=pass_in,
  database = database
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

