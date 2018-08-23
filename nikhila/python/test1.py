a=range(1,10)

def fun(p1,p2):
	if p1 in a:
		return False
	elif p2 in a:
		return False
	else:
		return True

for i in range(1, 4, 2):
	print("*", end="**")	
print("***")
print("**")



lst = [i // i for i in range(0,4)]
sum = 0
for n in lst:
 sum += n
print(sum)