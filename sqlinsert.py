import mysql.connector 
mydb=mysql.connector.connect(host="localhost",user="root", passwd="123",database= "SCHOOL")
mycursor=mydb.cursor() 
mycursor.execute("insert into student values (%s,%s,%s,%s,%s,%s)",(12345,"ARUSH","M","2003-10- 04","Science",67.34))
mydb.commit()
print(mycursor.rowcount,"Record Inserted")