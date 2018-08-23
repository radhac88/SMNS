def add(num1,num2):
	return num1+num2
def subtract(num1,num2):
	return num1-num2
def multiply(num1,num2):
	return num1*num2
def divide(num1,num2):
	return num1/num2
print("""select operation
	1.Add
	2.Subtract
	3.Multiply
	4.Divide""")
choice = input("choose 1/2/3/4 : ")

x = int(input("enter number one:"))
y = int(input("enter number two:"))

if choice == '1':
	print("The addition of {0} and {1} is {2} ".format(x,y,add(x,y)))
elif choice == '2':
	print("The addition of {0} and {1} is {2} ".format(x,y,subtract(x,y)))
elif choice == '3':
	print("The addition of {0} and {1} is {2} ".format(x,y,multiply(x,y)))
elif choice == '1':
	print("The addition of {0} and {1} is {2} ".format(x,y,divide(x,y)))
else:
	print("invalid input")
