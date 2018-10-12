st = input("enter string you want to print :")
n = int(input("enter how mant times it need to print:"))
global var ;
def string_times(str,n):
	var = " "
	while n > 0 :
		var = var + st;
		n = n-1; 
	print(" {0}".format(var)) 
string_times(str,n)

