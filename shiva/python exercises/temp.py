import datetime as y
x = y.datetime.now()
print(x)
print(x.year)
print(x.day)
print(x.month)
print(x.strftime("%A"))
print(x.strftime("%B"))
print(x.strftime("%W"))
var = "hello python hello"
var1 = "python"
var2 = var.capitalize()
print(var2)
var3 = var2.casefold()
print(var3)
var4 = var1.center(20)
print(var4)
var5 = var.count("hello")
print(var5)
print(var1.isalpha())
var6 = "$".join(var)
print(var6)
z = var.replace("hello", "Hola")
print(z)
var7 = var + var2 + var3 + var4
print(var7)
for x in range(1,11):
	print ('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
my_str = input("enter a string:")
words = my_str.split()
words.sort()
print("the sorted words are :")
for word in words:
	print(word)
a = {0,2,5,8,9,10}
b = {1,3,6,9,15}
print("union", a|b)