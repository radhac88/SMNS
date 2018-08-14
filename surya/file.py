i=1
j=1
while(i<3 or j<5):
    print(i)
    print(j)
    i+=1
    j+=1
fruits=["apple","banana","mango","orange"]
for x in fruits:
 print(x)
num=3
if num > 0:
    print(num, "this is always possitive number")
num=-1
if num > 3:
    print(num, "this is always negativr num")
    
 
num=4
if num > 1:
    print("one is  always lessthan four")
elif num < 3:
    print("four is greater than three")
num = 10
if num > 12:
    print("4,5,6,7,8,9")
elif num == 10:
    print("1,2,3,4,5,6,7,8,9")
else:
    print("condition is true")
num =int(input("Enter a number: "))
if num >=0:
    if num == 0:
        print("zero")
    elif num <0:
        print("positive number b/w 1 to 5")
    else:
        print("Positive number gt 5")
else:
    print("Negative number")
var1 = 100
if var1:
    print("1-got a true expression value")
    print ("var1")
var2=0
if var2:
    print("2-got a true expression value")
    print("var2")
    print("good bye")
    
def func_return():
    a = 10
    return a

def no_return():
    a = 10

print(func_return())
print(no_return())    
            

    
    


