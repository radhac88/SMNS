import mysql.connector
mydb = mysql.connector.connect(
  host="172.16.0.213",
  port="3306",
  user="root",
  passwd="welcome",
  database='nikhila'
)

mycursor = mydb.cursor()
