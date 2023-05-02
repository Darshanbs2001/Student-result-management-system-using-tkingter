import mysql.connector;
import smtplib;
from create_db import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import asyncio
def mail(content, filename, emailid):
    fromaddr = "Result Management System"
    toaddr = emailid
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "This is the result"
    body = "This is the result of the semsiter exam"
    msg.attach(MIMEText(body, 'plain'))
    file_name = filename
    p = MIMEBase('application', 'octet-stream')
    p.set_payload(content)
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment;filename=%s" % file_name)
    msg.attach(p)
    text = msg.as_string()
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("d9141525275@gmail.com", "nsfcubpixrlecuhs")
    s.sendmail(fromaddr, toaddr, text)
    s.quit()




        # n=n+1
        # with open("darshan_result.xlsx",'wb') as file:
        #   file.write(content)

