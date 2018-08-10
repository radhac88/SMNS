print("""area of traingle :
	1:base and height
	2:sides of traingle
	3:points of traingle""")

choice = input("enter the choice1/2/3:")

if choice=='1':
	num1 = int(input("enter number one:"))
	num2 = int(input("enter number two:"))
	print(0.5*num1*num2)
elif choice=='2':
	num1 = float(input("enter number one : "))
	num2 = float(input("enter number two :"))
	num3 = float(input("enter number three :"))
	s = float((num1 + num2 + num3) / 2)
	area = (s*(s-num1)*(s-num2)*(s-num3)) ** 0.5
	print("""area of traingle 
		when sides are given
		 {0}" "{1}" "{2} is  %0.3f """.format(num1,num2,num3) %area) 
elif choice=='3' :
	x1 = float(input("enter x1 cordinate"))
	y1 = float(input("enter y1 cordinate"))
	x2 = float(input("enter x2 cordinate"))
	y2 = float(input("enter y2 cordinate"))
	x3 = float(input("enter x3 cordinate"))
	y3 = float(input("enter y3 cordinate"))
	temp = float(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))
	area =	abs(temp/2)
	print("""The area of traingle 
			when points are given 
			({0},{1}) ({2},{3}) ({4},{5}) is %0.5f  """.format(x1,y1,x2,y2,x3,y3) %area)
else: 
	print("please choose correct choice ")
