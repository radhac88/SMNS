def my_function():
    n = 1
    print("this is first statement")
    yield n
    n = n+1
    print("this is second statement")
    yield n
    n += 1
    print("this is third statement")
    yield n

for item in my_function():
    print(item)
a =  my_function()

x =next(a)
print(x)
y= next(a)
print(y)
z= next(a)
print(z)


def rev_string(my_str):
    my_strlen = len(my_str)
    for i in range(my_strlen-1, -1, -1):
        print(my_str[i])
        # yield my_str[i]

rev_string("hello")