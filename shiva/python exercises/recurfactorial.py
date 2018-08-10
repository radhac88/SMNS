def recur_fact(n):
	if n==1:
		return n
	else:
		return n*recur_fact(n-1)

num = int(input("please enter a number"))
if num<0:
	print("there is no factorial for negative numbers")
elif  num==0:
	print("the factorial of 0 is 1")
else:
	print("the factorial of ", num ,"is",recur_fact(num))