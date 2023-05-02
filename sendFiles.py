from create_db import mycursor;
from mail import mail;
import asyncio
async def sendfiles(selected,regno,var_semister,var_course):
    if(selected==True):
        mycursor.execute("select email from student where roll=%s", (regno.get(),))
        erows = mycursor.fetchall()
        for erow in erows:
            emailid = erow[0]
            mycursor.execute("select sem,result_file from result where regno=%s and sem=%s",
                                 (regno.get(),var_semister.get()))
            srows = mycursor.fetchall()
            for srow in srows:
                content = srow[1]
                name = str(srow[0]) + ".xlsx"
                mail(content, name, emailid)
    if(selected==False):
        mycursor.execute("select regno,result_file from result where sem=%s and course=%s",
                         (var_semister.get(), var_course.get()))
        rows = mycursor.fetchall()

        for row in rows:
            mycursor.execute("select email from student where roll=%s", (row[0],))
            erows = mycursor.fetchall()
            for erow in erows:
                emailid = erow[0]

            mycursor.execute("select sem,result_file from result where regno=%s and sem=%s",
                             (row[0],var_semister.get()))
            srows = mycursor.fetchall()
            for srow in srows:
                content = srow[1]

                name = str(srow[0]) + ".xlsx"
                mail(content, name, emailid)



