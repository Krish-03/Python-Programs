import mysql.connector 
mydb=mysql.connector.connect(host="localhost",user="root", passwd="123",database= "SCHOOL")
mycursor=mydb.cursor() 
mycursor.execute("select * from student") 
myrecords=mycursor.fetchall() 
for i in myrecords:
	print(i)