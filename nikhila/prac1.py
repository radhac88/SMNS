def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
    print(type(result))
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

import mysql.connector

