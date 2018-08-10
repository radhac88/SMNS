print("conditional statements")
#if else
n=int(input("Number?"));
if n<0:
    print("the absolute value of ",n,"is",-n)
else:
    print("the absolute value of ",n,"is",n)

#elif
import datetime
x = datetime.datetime.now()

hours=int(x.strftime("%H"))
if(hours<12):
    print("Good morning")
elif(hours>=12 and hours<17):
    print("Good afternoon")
else:
    print("Good evening")

#nested if
p=int(input("Number?"))
if p>=0:
    if p==0:
        print("Zero")
    else:
        print("Positive integer")
else:
    print("Negative integer")


#for loop
b=[3,4,5,6,9,12]
for num in b:
    print(num)

#while loop
a=1
s=0
print("enter num to add to sum")
print("enter 0 to quit")
while a!=0:
    print('current sum:',s)
    a=float(input('Number?'))
    a=float(a)
    s+=a
print('Total sum',s)




#excercise1
import math
for i in range(1,10):
    x= math.factorial(i)
    if(x>=100 and x<1000):
        print("factorial of",i,"is in between 100 and 1000 ")
    elif(x>=1000 and x<2000):
        print("factorial of",i,"is in between 1000 and 2000 ")
    

#excercise2
a=int(input("enter first number?"))
b=int(input("enter second number?"))
def sumofnos(a,b):
    if(a==b):
        print(2*a+2*b)
    else:
        print(a+b)
        
sumofnos(a,b);


#excercise3
for x in range(10,20):
    if(x%2!=0) and (x%3!=0):
        print(x,"is a prime no")
    elif x%2==0:
        print(x,"equals 2 * ",(x//2))
    elif x%3==0:
        print(x,"equals 3 * ",(x//3))
            
        
#excercise4
var1="This is a C Class"
print(var1.replace("C","Python",1))
      
#excercise5
st=input("enter a string")
nt=int(input("enter a number"))

def string_times(st,nt):
    str1=""
    while nt>0:
        str1=str1+st
        nt=nt-1
    return str1
        
res=string_times(st,nt)
print(res)


#excercise6
vrb=input("enter a verb")
def make_3sg_form(vrb):
    if(vrb.endswith('y')):
        print(vrb.replace("y","ies"))
    elif(vrb.endswith('o')):
        print(vrb+"es")
    elif(vrb.endswith('ch')):
        print(vrb+"es")
    elif(vrb.endswith('s')):
        print(vrb+"es")
    elif(vrb.endswith('sh')):
        print(vrb+"es")
    elif(vrb.endswith('x')):
        print(vrb+"es")
    elif(vrb.endswith('z')):
        print(vrb+"es")
    else:
        print(vrb+"s")
make_3sg_form(vrb);

#ex
import sys
print(sys.version)

#
class MyClass:
  x = 5
  print(x)

#excercise
from datetime import date
d1=date(2018,6,11)
d2=date(2018,7,31)
#d1=date(input("enter first date"))
#d2=date(input("enter second date"))
x=abs(d1-d2)
print(x.days)


#ex
def new_string(str):
  if len(str) >= 2 and str[:2] == "Is":
    return str
  return "Is" + str

print(new_string("Array"))
print(new_string("IsEmpty"))

#ex
def fahrenheit(T):
    return ((float(9)/5)*T + 32)
def celsius(T):
    return (float(5)/9)*(T-32)
temp = (36.5, 37, 37.5,39)

F = list(map(fahrenheit, temp))
print(F)
C = list(map(celsius, F))
print(C)
