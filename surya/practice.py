array=["surya","python"]
print(array)
a="hello. world"
print(a.split(","))
thislist = ["banana", "apple", "cat"]
thislist.append("surya")
print(thislist)
thislist=list(("banana", "apple", "cat"))
print(thislist)
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()
fruits = ["apple", "banana", "cherry","banana"]
x=fruits.count("banana")
print(x)

fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1,"orange")
print(fruits)

fruits = ['apple', 'banana', 'cherry']
fruits.pop(2)
print(fruits)
cars = ['Ford', 'BMW', 'Volvo']

cars.sort()

print(cars)
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(reverse=True, key=myFunc)

print(cars)
thistuple = ["apple", "banana", "cherry"]
print(thistuple)
thisset =("apple", "banana", "cherry")
print(thisset)
thisset = {"apple", "banana", "cherry"}
thisset.add("surya")
print(thisset)
thisdict =	dict(apple="green", banana="yellow", cherry="red")
thisdict["damson"] = "purple"
print(thisdict)
def my_function(country):
  print("I am from " + country)
my_function("bjtuy6")
def my_function(x):[
    { "keys": ["ctrl+alt+b"], "command": "run_existing_window_command", "args":
    {
        "id": "repl_python_run",
        "file": "config/Python/Main.sublime-menu"
    }}
]
y = 5*x
print(y)

   

my_function(3)
my_function(5)
my_function(9)
myfunc = lambda x,y: x*y
print(myfunc(3,6))

def myfunc(n):
	return lambda i: i*n
doubler = myfunc(2)
tripler = myfunc(3)
val = 11
print("Doubled:" + str(doubler(val))+ "Tripled:" + str(tripler(val)))	
class Person:
	"""docstring for person"""
	def __init__(self, name, age):
		
		self.name = name
		self.age = age
p1 = Person("surya", 21)	
print(p1.name)
print(p1.age)

class surya(object):
	"""docstring for"""
	def __init__(self, name,age):
		
		self.name = name
		self.age = age
	def myfunc(self):
	  	print("hello my name is" + self.name)
	  	print("hello my age is" + str(self.age))

p1=surya("venu", 24)
p1.myfunc()
count = 0
while (count <8 ):
	print("count is:", count)
	count+=1
else:	
	print("gud bye")
marks = int(input("enter your marks"))
if (marks > 50):
	print("pass")
elif(marks < 50):
	print("fail")
for letter in 'Python':
	print("current letter:",letter)
fruits = ["apple", "banana","orangr"]
for index in range(len(fruits)):
	print(fruits[index])

for x in range(10, 20):

	if (x%2!=0 and x%3!=0):
		print(x,"is a prime number ")
	elif(x%2==0):
		print(x,"equals to 2*",x//2)
	elif(x%3==0):
		print(x,"equals to 3*",x//3)
for letter in "Python":
	if (letter=="h"):
		
		print("this is pass block")
	print(letter)
	
var1 = "this is c class"

print(var1.replace("c","Python",1))

print("surya"*3)
st=str(input("enter your "))

def string_times(t):
	str1=""
	nt=4
	while (nt>0):
		str1=str1+t
		nt=nt-1
	print(str1)
string_times(st)
print("my name is%s"%('surya'))	
print("{0} daughter of {1}".format('surya','sudharshan'))
my_str = "abcdDCBA"
my_str = my_str.casefold()
rev_str = reversed(my_str)	
if list(my_str)==list(rev_str):
	print("string is polydome")
else:
	print("string is not polyndrome")	
my_str ="suryakala daughter of sudharshan"
words = my_str.split()
words.sort()
for word in words:
	print(word)	
vowels="aeiou"
my_str ="independence day celebrated on august"	
my_str=my_str.casefold()
count={}.fromkeys(vowels,0)
for char in my_str:
	if char in count:
		count[char]+=1

print(count)
x=[[1,2,3],
  [3,4,5],
  [5,6,7]]
y=[[3,2,5],
	[4,5,6],
	[6,7,8]]
result = [[0,0,0],
         [0,0,0],
         [0,0,0]]	
	
for i in range (len(x)):	
	for j in range (len(x[0])):
		result [i][j]=x[i][j]+y[i][j]
for r in result:
	print(r)	
x= [12, 65, 54, 39, 102, 339, 221]
print("Numbers divisible by 13 are :")
for x1 in x:	
	if (x1%13==0):
		print(x1)
def surya_kala(num):
	if num>=0:
		return num
	else:
		return -num
print(surya_kala(5))
def sum_num():
	x=2
	y=3
	sum=x+y
	return sum


import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
  
print("suryakala")
f=open("surya1.txt","r")
print(f.read())
f=open("surya1.txt","a")
f.write("python is simple and easy to learn")
f=open("surya1.txt","w")
f.write("python is simple and easy to learn")


import os
if os.path.exists("surya2.txt"):
  os.remove("surya4.txt")
else:
  print("The file does not exist")
fruits = ['app', 'ban', 'che']
thisset = tuple(("appl", "bana", "cher"))
fruits.extend(thisset)
print(fruits)
def my_function1(x):
	return x+5
print(my_function1(4))
surya=lambda a:a+5
print(surya(3))	
class myclass:
	"""docstring for ClassName"""
	def __init__(self,name,age):
		self.name="surya"
		self.age =21

		
	
p1=myclass("name","age")
print(p1.age)
print(p1.name)	
class suryakala:
	"""docstring for suryakala"""
	def __init__(self, name,age):
		super(suryakala, self).__init__()
		self.name = "venu"
		self.age  = 23
	def my_function2(abc):
		print("hello my name is",abc.name)
	
p1=suryakala("name","age")
p1.my_function2()
print(p1.age)
import mymodule 
a=mymodule.person["age"]
print(a)
import datetime
x=datetime.datetime.now()
print(x)
y=datetime.datetime.now()
print(y.strftime("%w"))
cars = ["Ford", "Volvo", "BMW"]
for x in cars:
	print(len(x))
x=input("enter a string")
if(x.endswith("y")):
	print(x.replace("y","ies"))
elif(x.endswith("o") or x.endswith("ch") or x.endswith("z")):
	print(x+"es")
else:
	print(x+"s")
print(3.5e2)
tup1=(50)
print(tup1)		
for x in (1,2,3):
	print(x,'')
dict={}
print(dict)	
h_letters=list(map(lambda a:a,"python"))
print(h_letters)
surya=[x for x in range(100) if x%2==0 if x%5==0]
print(surya)
obj=["even" if i%2==0 else "odd" for i in range(10)]
print(obj)
matrix=[[1, 2],
[3, 4],
[4, 5],
[6, 7],
[8, 9]]
transposed=[]
for i in range(2):
 		transposed_row=[]
 		for row in matrix:
 			transposed_row.append(row[i])
 		transposed.append(transposed_row)	
print(transposed)
matrix=[[1,2],
	[3,4],
	[5,6],
	[7,8]]
matrix1=[[1,2],
	[3,4],
	[5,6],
	[7,8]]
print(matrix+matrix1)
def fahrenheit(T):
	return((float(9)/(5))*T+32)
def celsius(T):
	return((float(5)/(9))*(T-32))
temparetures=(36.5, 37, 37.5, 38, 39)
F=list(map(fahrenheit,temparetures))
c=list(map(celsius,F))
print(F)
print(c)
a=[1,2,3,4]
b=[2,3,4]
c=[1,2,3,4,5]
sum=list(map(lambda x,y:x+y, b,c))
print(sum)
from math import sin, cos,tan,pi
def map_functions(x,functions):
    return [func(x) for func in functions ]
family=[sin,cos,tan]
print(map_functions(pi,family))
num_list=[1,2,3,4,5,6,7,8,9]
oddnum=list(filter(lambda x:x%2, num_list))
print(oddnum)
evennum=list(filter(lambda x:x%2==0, num_list))
print(evennum)
a=[['Roy',80,75,85,90,95],
    ['John',75,80,75,85,100],
    ['Dave',80,80,80,90,95]]

a= a+ [['Sam',82,79,88,97,99]]

print(a)
from fractions import Fraction as F

# Output: 2/3
print(F(1,3) + F(1,3))

# Output: 6/5
print(1 / F(5,6))

# Output: False
print(F(-3,10) > 0)

# Output: True
print(F(-3,10) < 0)
odd = [1, 9]
odd.insert(1,3)
pow2 = []
for x in range(10):
   pow2.append(2 ** x)
print("4y3434r34vbsr" "")
 
def reverse_a_string():
    # Reading input from console
    a_string = input("Enter a string")
    new_strings = []
 
    # Storing length of input string
    index = len(a_string)
 
    # Reversing the string using while loop
    while index:
        index -= 1
        new_strings.append(a_string[index])
 
    #Printing the reversed string
    print(''.join(new_strings))
 
reverse_a_string()
travelling = input("Are you travelling? Yes or No:")
while travelling == 'yes':
   num = int(input("Enter the number of people travelling:"))
   for num in range(1,num+1):
      name = input("Enter Details \n Name:")
      age = input("Age:")
      sex = input("Male or Female:")
      print("Details Stored \n",name)
      print(age)
      print(sex)
   print("Thank you!")
   travelling = input("Are you travelling? Yes or No:")
print("Please come back again.")
def function():
	list=["jan"]
	for m in list:
		print(m)
function()
def surya1():
	print("suryakala")
surya1()	
			

	




			
		

		

	













        




	
