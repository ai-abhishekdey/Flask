
import mysql.connector

# Establishing mysql connection

connection=mysql.connector.connect(
    host='localhost',
    user='abhishek',
    password='*Pass1234#',
    database='calculator_database')

# Creating a cursor object using the cursor() method

cursor=connection.cursor()



operation='addition'
num1=10
num2=20
result=30


#mysql_query = "insert into calculator_table(operation,num1,num2,result) values(?,?,?,?)"
#val=(operation,num1,num2,result)

cursor.execute("insert into calculator_table (operation,num1,num2,result) values(%s,%s,%s,%s)", (operation,num1,num2,result))
connection.commit()
        
connection.close()
