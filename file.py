from create_db import *
mycursor.execute("create table if not exists image(id integer(45)not null AUTO_INCREMENT primary key,photo LONGBLOB not null)")
def insertblob(filepath):
    with open(filepath,'rb')as f:
        binary_data=f.read()
        mycursor.execute("insert into image (photo) values(%s)",(binary_data,))
        mydb.commit()
        print("the record has been created")

def retriveblob(choice):
    mycursor.execute("select * from image where id=1".format(str(choice)))
    myresult=mycursor.fecthone()[1]
    storepath="/images/result2.png"
    print(myresult)
    with open(storepath,'wb')as f:
        f.write(myresult[1])
        f.close()



print("1.insert image\n 2.Read images")
menuInput=input()
if int(menuInput)==1:
    userfilepath=input("Enter the file path:")
    insertblob(userfilepath)
elif int(menuInput)==2:
    useridchoice=input("Enter the id:")
    retriveblob(useridchoice)