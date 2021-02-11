import mysql.connector 
mydb=mysql.connector.connect(host="localhost",user="root", passwd="123",database= "SCHOOL")
mycursor=mydb.cursor() 
mycursor.execute("update student set marks=100 where admn_no= 1356") 
mydb.commit() 
print(mycursor.rowcount,"Record(s) Updated")