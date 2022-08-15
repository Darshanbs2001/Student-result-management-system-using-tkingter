from create_db import *
def refreshcourse():
    mycursor.execute("select * from course")
    rows = mycursor.fetchall()
    n = 0
    for row in rows:
        n = n + 1
    return(str(n))
def refreshstudent():
    mycursor.execute("select * from student")
    rows = mycursor.fetchall()
    n = 0
    for row in rows:
        n = n + 1
    return(str(n))
def refreshresult():
    mycursor.execute("select regno from result")
    rows = mycursor.fetchall()
    n = 0
    for row in rows:
        n = n + 1
    return(str(n))