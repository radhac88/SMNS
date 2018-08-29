import mysql.connector

mydb = mysql.connector.connect(
  host="172.16.0.213",
  user="root",
  passwd="welcome",
  database="manaswini"
)

mycursor = mydb.cursor()
#print all the data in customers table
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
#print id,lname in customers table
mycursor.execute("SELECT customersid,lname from customers")
myresult = mycursor.fetchone()
for x in myresult:
  print(x)

#??
import mysql.connector

mydb = mysql.connector.connect(
  host="172.16.0.213",
  user="root",
  passwd="welcome",
  database="manaswini"
)
mycursor = mydb.cursor()
#print details whose fname is manaswini note:fname is string
sql = "SELECT * FROM customers WHERE fname = %s"
adr = ("manaswini", )
mycursor.execute(sql, adr)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
#select all the details from customers and order by fname by default asc
sql = "SELECT * FROM customers ORDER BY fname"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
#order by desc 
sql = "SELECT * FROM customers ORDER BY fname DESC"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
#deletion of whole row consisting of fname
sql = "DELETE FROM customers WHERE fname = 'shiva'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")
#