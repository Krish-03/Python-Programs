import mysql.connector 
mydb=mysql.connector.connect(host="localhost",user="root", passwd="123",database= "SCHOOL")
mycursor=mydb.cursor() 
mycursor.execute("CREATE TABLE STUDENT (admn_no int primary key, sname varchar(30), gender char(1), DOB date, stream varchar(15), marks float(4,2))") 