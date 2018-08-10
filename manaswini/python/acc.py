import moduleacc
print("welcome!!")
accn=str(input("enter bank acc num"))
if len(accn)==7:
	print("valid num")
	pin=str(input("enter pin"))
	if len(pin)==4:
		print("valid pin")
		choice = int(input("""choose :
		 1=deposit 
		 2=withdraw"""))
		if choice == 1 :
			dep = int(input("enter the amount need to deposit "))
			print("amount deposited",dep)
			total = dep + moduleacc.av
			print("total available balance is",total)
		elif choice == 2 :
			wit = int(input("enter the amount need to withdraw "))
			print("amount withdrwan",wit)
			total = moduleacc.av - wit
     		print("total available balance is",total)
     	else:
			print("invalid choice")
	else:
 		print("invalid")
else:
	print("invalid num")
