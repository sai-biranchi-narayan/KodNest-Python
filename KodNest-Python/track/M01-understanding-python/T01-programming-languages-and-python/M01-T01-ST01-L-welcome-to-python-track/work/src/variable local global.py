c = 30
def add():
    global a
    a = 10
    b = 20
    print(a + b)
    print(c)
add()


x = 100
def display():
    x = 50
    print("Local", x)
display()
print("Global x:", x)

x = 10
def display():
    print(x)
    def add():
        print(c)
    add()


x = 100 
def display():
    x = 50
    print("Local x:", x)
display()
print("Global x:", x)


x = 10
def display():
    print(x)
    # x = 20 # local variable
    # print(x)
display()
print(x)


# Default Arguments
def add(a = 0 , b = 0 , c =0):
    return a + b + c
print(add(10))
print(add(10,20))
print(add(1 , 1 , 1))

# Variable number arguments
def add(*a):
    print(sum(a))

add(10 , 20)
add(10, 20 ,30)
add(10)
add()

# **kwargs (keyword arguments)
def stu_info(**kwargs):
    print(f"Name is {kwargs.get('name;')}" , end = " ")
    print(f"Age is {kwargs.get('age;')}" , end = " ")
    print(f"course is {kwargs.get('course;')}")

stu_info(name = "Sai" , age = 22 , course = "Python")

# count from 5 4 3 2 1
def count(n):
    if  n == 0:
        return
    print(n)
    count(n - 1)

count(5)


# Factorial of a number
def fact(n):
    if (n == 1):
        return 1
    return n * fact(n - 1)

print(fact(5))

# Fibonacci Series
def fib(n):
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    return fib(n - 1) + fib(n - 2)

print(fib(5))

    

    


    

  