# add 2 numbers
def add():
    a = 10
    b = 20
    c = a + b
    print(c)

    add()

# square of a number
def square():
    a = 10
    c = a * a
    print(c)

    square()
    
# Find the largest number in a list
def largest():
    a = 10
    b = 20
    c = 30
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    else:
        print(c)

    largest()

# Check if a number is even or odd
def even_or_odd():
    a = 10
    if a % 2 == 0:
       print("Even")
    else:
       print("Odd")

    even_or_odd()

# Greet with name
def greet ():
    name = "Sai"
    print("Hello", name)

greet()

# No arguments + No return value
def square():
    a = 5
    c = a * a
    print(c)

square()

# No arguments + Return value
def square():
    a = 5
    c = a * a
    print(c)
    return c


# Arguments + No return value
def square(a):
    c = a * a
    print(c)

square(5)

# Arguments + Return value
def square(a):
    return a * a

print(square(5))













    