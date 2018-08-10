for x in range(10,20):
	if(x%2!=0 and x%3!=0):
		print(x,"is a prime number")
	elif(x%2==0):
		print(x ,"equals 2 *", str(x//2) )
	elif(x%3==0):
		print(x ,"equals 3 *", str(x//3))
