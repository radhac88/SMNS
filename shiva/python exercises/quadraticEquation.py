print("please enter a , b , c values for quadratic equation ")
a = float(input("enter a value :"))
b = float(input("enter b value :"))
c = float(input("enter c value :"))

d = ((b**2) - (4*a*c))**0.5
x = (-b + d)/ 2 *a
y = (-b - d)/2 * a
print("The roots of quadratic equation is {0} , {1}".format(x,y))