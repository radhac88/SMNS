num = int(input("enter a number to know its factorial :"))
fact = 1
if num < 0:
	print("please enter the number above zero ")
#elif num==0:
#	print("the factorail of zero is 1 ")
else:
	for i in range(1, num+1):
		fact = fact * i
print("The factorail of number is {0}".format(fact))
