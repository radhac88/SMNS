a=1
s=0
print("enter num to add to the sum")
print("enter 0 to quit")
while a!=0:
	print('current Sum:',s)
	a=float(input('Number?'))
	a=float(a)
	s+=a
print("total sum=",s)


#program to sum all the ticket prices

sum= 0
print("Total customers 10 ")
for i in range(0, 10):
    # cost = [60, 90, 120]
    tickets=int(input("enter ticket cost - 60 / 90 /120 "))
    if tickets == 60 and tickets == 90 and tickets == 120:
        print("customer {0} price : {1} ".format(i, tickets))
        sum += tickets
        print(sum)
print(sum)

