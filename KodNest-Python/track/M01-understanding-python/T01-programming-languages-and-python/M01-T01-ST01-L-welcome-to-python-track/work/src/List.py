# List are mutable, ordered, and allow duplicate , index , []
# index 0  1  2  3  4  5
nums = [1, 2, 3, 4, 5]
print(nums)
print(nums[2])
print(type(nums)) # <class 'list'>

# List constructor list()
nums = list(1,2,3,4,5)
print(nums)
print(type(nums))
names = [ "Alice", "Bob", "Charlie"]
names[1] = "David"
names [3] = "Alice"
print(names)
print(type(names))

# List Methods
names = ["Alice", "Bob", "Charlie"]
names.append("Ram")
names.insert(2, "Sita")
names.pop()
names.remove()
names.clear()
del names
print(names)

names = ["Alice", "Bob", "Charlie"]
names1= ["David", "Eve", "Frank"]
list1 = names.extend(names1)
print(list1)
for i in names:
    print(i)

print(names.count("Alice"))
print(names.index("Bob"))
print(names.copy())
print(names.extend(names1))


n = [5, 7, 4, 1, 2]
narr = sorted(n)
print(narr)
print(n)
n.sort()
print(n)
n.reverse()
print(n)

arr = [1, 2, 3]
newarr = arr.copy()
print(newarr)
print(arr)

colors = ["red", "green", "blue", "yellow", "purple"]
colors[1:2] = ["black", "white"]
print(colors)


# practice questions

a = [10, 20, 30, 40, 50, 60, 70, 80]
print(a[-2:-7:-2])

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[-1:-9:-3])

a = [1, 2, 3, 4, 5, 6, 7]
print(a[-2:1:-2])

a = [10, 20, 30, 40, 50, 60,70]
print(a[-1:-8:-2])

a = [1, 2, 3, 4, 5, 6, 7, 8]
print(a[-5:-1:2])

a = [10, 20, 30, 40, 50, 60, 70]
print(a[-6:-1:3])

a= [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[-2:-8:-2])

a= [10, 20, 30, 40, 50]
print(a[-1:-6:-1])

a= [1, 2, 3, 4, 5, 6, 7]
print(a[-3:0:-1])

a= [10, 20, 30, 40, 50, 60, 70, 80]
print(a[5:-6:-2])

a= [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[-7:8:3])

a = [10, 20, 30, 40, 50, 60]
print(a[4:-5:-1])

a = [10, 20, 30, 40, 50, 60, 70]
print(a[2:-1:-1])

a = [1, 2, 3, 4, 5, 6, 7]
print(a[-5:1])

a = [10, 20, 30, 40, 50, 60]
print(a[5:-1:-1])

a = [1, 2, 3, 4, 5, 6, 7, 8]
print(a[-2:0:2])








