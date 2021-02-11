import mysql.connector 
mydb=mysql.connector.connect(host="localhost",user="root", passwd="123",database= "SCHOOL")
mycursor=mydb.cursor() 
mycursor.execute("delete from student where admn_no= 12345") 
mydb.commit() 
print(mycursor.rowcount,"Record(s) Deleted")