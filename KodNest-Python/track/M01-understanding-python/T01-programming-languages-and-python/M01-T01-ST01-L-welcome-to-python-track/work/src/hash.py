from Input import name
print(hash(2))
print(hash("hello"))
print(hash(1.0))

x = "Python"
print(hash(x))

# hashing in sets
#s = {1, "Python"}
# print(hash(s))

# hash collision
a = 1
b = 1.0
print(hash(a))
print(hash(b))
print(a == b)
print(a is b)

# custom hashing in sets
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age  
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
   

    

p1 = person("John", 30)
p2 = person("John", 30)
print(p1 == p2)



