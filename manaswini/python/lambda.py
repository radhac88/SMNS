x=lambda a:a+10
print(x(5))
x=lambda a,b:a*b
print(x(2,3))
def fun(n):
 return  lambda a:a*n
doub = fun(2)
print(doub(3))
def fun2(n):
 return lambda a,b:a+b+n
d = fun2(3)
print(d(2,2))
print(d(3,3))