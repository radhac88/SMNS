num = int(input("""enter a number to check 
	the number is prime or not: """))
if num>1:
	for i in range(2,num):
		if(num % i ) == 0:
			print("The number {0} is not a prime number ".format(num));
			break;
	else:
		print("The number {0} is  prime number".format(num));

else:
	print("The number {0} is   not prime number".format(num));