print(""" *** swap two numbers ***
			enter two values :	 """)
a = int(input("enter value a: "))
b = int(input("enter value b: "))
print("before swapping :" , a , b )
a = a + b
b = a - b
a = a - b
print("after swapping :" , a , b)