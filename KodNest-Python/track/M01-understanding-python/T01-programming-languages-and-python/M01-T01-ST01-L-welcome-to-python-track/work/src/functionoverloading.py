# function overloading same name diffrent parameters
def add(a, b):
    print(a + b)

def add(a, b, c):
    print(a + b + c)

def add(a, b, c, d):
    print(a + b + c + d)

add(1,2)
add(1,2,3)
add(1,2,3,4)  
#python does not support function overloading
# the last function defination will 

# default arguments
def add(a, b=0, c=0, d=0):
    print(a + b + c + d)

# add() 
add(100)
add(1, 2)
add(1, 2, 3)
add(1, 2, 3, 4)

# *args = *(0.....infinity)
def add(*args):
    print(sum(args))

add(100)
add(1, 2)
add(1, 2, 3)
add(1, 2, 3, 4)
add()

# **kwargs = **{key:value, key:value}
def add(**kwargs):
    print(kwargs)

add(a=1,b=2) # {a:1,b:2}
