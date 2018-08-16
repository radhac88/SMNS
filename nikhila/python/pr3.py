import mymodule
mymodule.mycursor.execute("select * from student")

myresult = mymodule.mycursor.fetchall()

for x in myresult:
  print(x)