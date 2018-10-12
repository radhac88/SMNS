# iterators
# implemented in for loop
# two methods __iter__() and __next__()
# inside for loop it will also use iter() and next() methods
# we can rasie errors in else statement and we have default error methods


class PowTwo:

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


a = PowTwo(4)
i = iter(a)
print(next(i))
print(next(i))
print(next(i))
print(next(i))

my_list = [4, 7, 0, 3]
my_iter = iter(my_list)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))


# generators
# in generators we have yeild statement
# yeild statement pauses the function saving all its states and later continues from there succeesive calls
# it can contain one more yeild functions
# value of n is stored for every call
# generator function creates anonymous generator function
# generator expression uses rounded parentheses
def my_function():
    n = 1
    print("this is first statement")
    yield n
    n = n + 1
    print("this is second statement")
    yield n
    n += 1
    print("this is third statement")
    yield n


for item in my_function():
    print(item)
a = my_function()

x = next(a)
print(x)
y = next(a)
print(y)
z = next(a)
print(z)


def rev_string(my_str):
    my_strlen = len(my_str)
    for i in range(my_strlen - 1, -1, -1):
        yield my_str[i]


for char in rev_string("hello"):
    print(char)

my_gen_list = [1, 2, 3, 4, 5]

b = (x ** 2 for x in my_gen_list)
for char in b:
    print(char)

add = sum(x ** 2 for x in my_gen_list)
print(add)
max_num = max(x ** 2 for x in my_list)
print(max_num)


def PowTwoGen(n):
    max = 0
    while n > max :
        yield 2 ** n
        n += 1

a =PowTwoGen(1)

print(next(a))
print(next(a))

#closure

def printMyName(name):
    def myName():
        print(name)
    return myName

myname = printMyName("shiva")
myname()
#another example

def make_mulilier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = make_mulilier_of(3)
times5 = make_mulilier_of(5)

print(times3(9))

#decorators are used to add functionality to an existing code
# is also called as metaprogramming
#it try to change the value at compile time
#we can chain decorators ny using @ symbol

def first(mesg):
    print(mesg)


first("shiva")
second = first
third = second
second("harish")
first("hey")
second("hi")
third("hello")

def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

@star
@percent
def printer(msg):
    print(msg)

printer("hey ...")