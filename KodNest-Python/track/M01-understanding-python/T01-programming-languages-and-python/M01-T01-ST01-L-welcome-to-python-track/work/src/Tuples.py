# Tuples -> () ordered
nums = (1, 2, 3, 4)
# nums[0] = 100 # immutable
print(nums, type(nums))

stu_info = ("Mohammad", True, 7.93, 22)
print(stu_info)
print(stu_info[3]) # indexing
print(stu_info[0:3]) # slicing
print(stu_info[-2]) # negative indexing

name = ("Sai",) * 3
print(name)
print(type(name)) # check type of the veriable

# Tuple Constructor
lst = [1, 2, 3]
print(lst, type(lst))
rgb = tuple(lst)
print(rgb)
print(type(rgb)) # check type of the veriable

rgb = tuple(["r", "e", "d"])
print(rgb)
print(type(rgb))

# Adding and removing element
x = (1, 2, 3)
z = (10, 11, 12)
#z.pop()
del z
print(z)
x += z # x = x + z
print(x)
y = list(x)
y.append(4)
print(4)
print(y)

# loop
z = (10, 11, 12, 10)
for i in range(len(z)):
    print(z[i])

# methods in tuple
print(z.count(10)) # 2
print(z.index(10)) # 0
print(z.index(10, 2)) # 3


# Unpacking of tuples
emp = ("Mohammad", 22, "Developer")
print(emp, type(emp))
(name, age, role) = emp # unpack
print(name)
print(age)
print(role)

# tuple b*
s = (2, 4, 6, 8, 10)
(a, *b, c) = s
print(a)
print(b)
print(c)

# Other methods
t = (10, 20, 30, 40, 50)
print(len(t)) # 5
print(max(t)) # 50
print(min(t)) # 10
print(sum(t)) # 150
print(sorted(t)) # [10, 20, 30, 40, 50]
print(any(t)) # True
print(all(t)) # True
print(10 in t) # True

t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)
print(t1 * 2)

del t


