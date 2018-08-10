st = input("enter string you want to print :")
n = int(input("enter how mant times it need to print:"))
global var ;
def string_times(st,n):
	var = ""
	while n > 0 :
		var = var + st;
		n = n-1; 
	print(var) 
string_times(st,n)

def stringBasic(n):
	print("Hi"*n);
stringBasic(2)
stringBasic(5)