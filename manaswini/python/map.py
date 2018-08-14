def fun(a):
	return(len(a))
x=map(fun,('apple','grapes','orange'))
print(x)
print(list(x))
def fun(a,b):
	return a,-,+b
x=map(fun,('apple','grapes','banana'),('red','green','yellow'))
print(x)
print(list(x))
