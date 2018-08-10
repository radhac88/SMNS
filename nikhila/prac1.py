def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)



def myfunc(n):
  return lambda i: i*n

doubler = myfunc(1)
tripler = myfunc(3)
val = 11
print("Doubled: " + str(doubler(val)) + ". Tripled: " + str(tripler(val)))


thislist=["apple","banana","cherry"]
thistuple=("red","green","white")
thisset={"nikhila","manaswini","surya","srinija","shiva"}
thisdict={"a":"python","b":"javascript","c":"jquery"}
thislist.append(thisset)
print(thistuple)

with open('output.txt', 'a') as f:
	f.write("hello python")
	print(f.readable())	

with open('output.txt', 'r') as f:
	print(f.readline(5))

count = 0
while count < 3:
   print (count, " is  less than 5")
   count = count + 1
else:
   print (count, " is not less than 5")

 
