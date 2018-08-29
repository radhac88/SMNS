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


