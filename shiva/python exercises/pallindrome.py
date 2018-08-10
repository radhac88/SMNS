print("*** pallindrome string ***")
my_str = input("enter a string")
rev_str = reversed(my_str)
if list(my_str) == list(rev_str):
	print("its pallindrome")
else:
	print("its not pallindrome")
