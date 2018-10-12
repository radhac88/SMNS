print("enter two numbers ")
a = int(input("enter value of a:"))
b = int(input("enter value of b:"))
print("if both values are equal it will returns sum else it will return's double their sum ")

def sum_double(a,b):
	if(a==b):
		print(2*a + 2*b);
	elif(a!=b):
		print(a+b);
sum_double(a,b)
