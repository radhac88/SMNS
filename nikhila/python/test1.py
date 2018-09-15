a=range(1,10)

def fun(p1,p2):
	if p1 in a:
		return False
	elif p2 in a:
		return False
	else:
		return True

for i in range(1, 4, 2):
	print("*", end="**")	
print("***")
print("**")

lst = [[c for c in range(r)] for r in range(3)]
print(lst)
for x in lst:
 for y in x:
 	if y < 2:
 		print('*',end='')

lst = [i // i for i in range(1,4)]
sum = 0
for n in lst:
 sum += n
print(sum)

lst1 = "12,34"
print(lst1)
print(len(lst1))
lst2 = lst1.split(',')
print(lst2)
print(len(lst2))
print(len(lst1) < len(lst2))

x = 10
f = lambda x: 1 + 2
print(f(x))


#from math import pi as xyz # line 01
#print(pi) 
import random
for i in range(10):
 print(random.randint(1, 5))

s = 'SPAM'
def f(x):
 return s + 'MAPS'
print(f(s))


try:
 print("Hello")
 raise Exception
 print(1/0)
except Exception as e:
 print(e)

print("*****")


print("1,2,3",end="|")
print("4,5,7")






import re
sum = 0

pattern = 'back'
if re.match(pattern, 'backup.txt'):
    sum += 1
    print(pattern)
if re.match(pattern, 'text.back'):
    sum += 2
    print(pattern)
if re.search(pattern, 'backup.txt'):
    sum += 4
    print(pattern)
if re.search(pattern, 'text.back'):
   sum += 8
   print(pattern)

print(sum)







country_counter = {}

def addone(country):
    if country in country_counter:
        country_counter[country] += 1
    else:
        country_counter[country] = 1

addone('China')
addone('Japan')
addone('china')

print(country_counter)



confusion = {}
confusion[1] = 1
confusion['1'] = 2
confusion[1] += 1

sum = 0
for k in confusion:
    sum += confusion[k]

print(sum)
print(confusion)


confusion = {}
confusion[1] = 1
confusion['1'] = 2
confusion[1.0] = 4

sum = 0
for k in confusion:
    sum += confusion[k]

print(sum)
print(confusion)


boxes = {}
jars = {}
crates = {}

boxes['cereal'] = 1
boxes['candy'] = 2
jars['honey'] = 4
crates['boxes'] = boxes
crates['jars'] = jars

print(boxes)
print(jars)

print(crates)
print(len(crates))



names1 = ['Amir', 'Barry', 'Chales', 'Dao']
names2 = names1	
names3 = names1[:]

names2[0] = 'Alice'
names3[1] = 'Bob'

sum = 0
x=0
for ls in (names1, names2, names3):
    if ls[0] == 'Alice':
        sum += 1
    if ls[1] == 'Bob':
        sum += 10
    if 1:
    	x+=1

print(sum)
print(names1)
print(names3)
print(names2)
print(x)



def addItem(listParam):
    listParam += [1]
    print(listParam)

mylist = [1, 2, 3, 4]
addItem(mylist)
print(len(mylist))
print(mylist)


class A:
    def __init__(self, a, b, c):
        self.x = a + b + c

a = A(1,2,3)
b = getattr(a, 'x')
print(b)
setattr(a, 'x', b+1)
print(a.x)


import copy

aList = [1,2]
bList = [3,4]

kvps = { '1' : aList, '2' : bList }
theCopy = copy.deepcopy(kvps)

kvps['1'][0] = 5

sum = kvps['1'][0] + theCopy['1'][0]
print(sum)
print(kvps)
print(theCopy)


aList = [1,2]
bList = [3,4]

kvps = { '1' : aList, '2' : bList }
theCopy = kvps.copy()

kvps['1'][0] = 5

sum = kvps['1'][0] + theCopy['1'][0]
print(sum)
print(kvps)
print(theCopy)


kvps = { '1' : 1, '2' : 2 }
theCopy = kvps.copy()

kvps['1'] = 5

sum = kvps['1'] + theCopy['1']
print(sum)
print(kvps)
print(theCopy)


mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))



def my_gen():
    print('This is printed first')
    print('hjdgujkejk')
    print('hehjqk')
    x=2;
    # Generator function contains yield statements
    yield 1

    n += 1
    print('This is printed second')
    yield 

    n += 1
    print('This is printed at last')
    yield n

  
a=my_gen();
x=next(a)
print(x)
#next(a)

"""

def print_msg(msg):
# This is the outer enclosing function

    def printer():
# This is the nested function
        print(msg)


    printer()

# We execute the function
# Output: Hello
print_msg("Hello")


def print_msg(msg):
# This is the outer enclosing function

    def printer():
# This is the nested function
        print(msg)

    return printer  # this got changed

# Now let's try calling this function.
# Output: Hello
another = print_msg("Hi")
print(another)
del print_msg
another();



def startAt(start):
    def incrementBy(inc):
        return start + inc
    return incrementBy

f = startAt(10)
g = startAt(100)

#print f(1), g(2)

mytuple = ["apple", "banana", "cherry"]
myit = iter(mytuple)

print(myit)"""


def rev_str(my_str):
    length = len(my_str)
    for i in range(4,-1,-1):
        yield my_str[i]

# For loop to reverse the string
# Output:
# o
# l
# l
# e
# h
for char in rev_str("hello"):
     print(char)






####
def rev():
    for i in range(101,1):
            yield i

for char in rev():
         print(char)
"""
def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

# Multiplier of 3
times3 = make_multiplier_of(3)
print(times3)
# Multiplier of 5
times5 = make_multiplier_of(5)

# Output: 27
print(times3(9))

# Output: 15
print(times5(3))

# Output: 30
print(times5(times3(2)))









print((1, 2) + (3, 4))


names = "{1}, {2} and {0}".format('John', 'Bill', 'Sean')
print(names)"""



my_list = [1, 3, 6, 10]

# square each term using list comprehension
# Output: [1, 9, 36, 100]
print([x**2 for x in my_list])

# same thing can be done using generator expression
# Output: <generator object <genexpr> at 0x0000000002EBDAF8>
a=(x**2 for x in my_list)
print(next(a))
print(next(a))
print(next(a))



def smart_divide(func):
    def inner(a,b):
        print("I am going to divide",a,"and",b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a,b)
    print(inner)  
    return inner

@smart_divide
def divide(a,b):
    return a/b

x=divide(2,5)
print(x)


def make_pretty(func):
    print("I got decorated")
    func()
    

def ordinary():
    print("I am ordinary")



x=int()
print(x)
inf = iter(int,1)
print(next(inf))
print(next(inf))

#
#

def is_called():
    def is_returned():
        print("Hello")
    return is_returned

new = is_called()
print(new)
#Outputs "Hello"
new()



###
def star(func):
    def inner(*args):
        print("*" * 30)
        func(*args)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args):
        print("%" * 30)
        func(*args)
        print("%" * 30)
    return inner

def printer(msg):
    print(msg)
printer = star(percent(printer))
printer('hello')



###
def make_pretty(func):
    print("I got decorated")
    func()

@make_pretty
def ordinary():
    print("I am ordinary")

thisdict =  {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#########

def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

@star
@percent
def printer(**kwargs):
    for key,value in kwargs.items():
        print(key)
        print(value)

printer(brand= "Ford",model="Mustang")



def hello(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print (key)
            print (value)

hello(name="nikhila")


###
def rev_str():
    for i in range(20,-1,-1):
        yield i

for char in rev_str():
     print(char)