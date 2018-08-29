my_list = ["one","two","three","four",5,6,7,8,9,10]
my_tup =("one","two","three","four",5,6,7,8,9,10)
my_set ={"one","two","three","four",5,6,7,8,9,10}
my_dict = {"one":"1","two":"2","three":"3","four":"4",
			"five":"5","six":"6","seven":"7","eight":"8","nine":"9","ten":"10"}
tup =set(my_tup)
print(len(tup))
for x in my_list:
	print (x)
	for y in my_tup:
		print(y)
num = int(input("please enter a number between 1-100"))
print("the entered number is :",num)
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
for i in numbers:
	print(i)
genre = ['pop','rock','jazz']
for j in range(len(genre)):
	print("i like",genre[j])
for k in my_set:
	print(k)
else: 
    print("all items are printed")
print(my_dict["three"])
print(my_list)
