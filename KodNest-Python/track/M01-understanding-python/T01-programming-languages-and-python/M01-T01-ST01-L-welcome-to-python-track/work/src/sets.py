# set - {} , unordered, unindexed, mutable(items are unchangblale but add or remove), no duplicates
fruits = {"apple", "bannana", "kiwi", "apple"}
print(fruits, type(fruits))

# Set constructor
stu_info = set(("Ram", 23, 89.65, "a"))
print(stu_info, type(stu_info), len(stu_info))

fruits2 = set(("apple", "banana", "kiwi"))
print(fruits2, type(fruits2))

# Set methods
#add()
fruits = {"apple", "banana", "kiwi", "apple"}
fruits.add("orange")
nfruits = {"orange", "lemon", "grapes"}
fruits.update(nfruits)
print(fruits)

# Remove
fruits.remove("banana")

# discard
fruits.discard("apple")

# pop() last element removed
fruits.pop()
print(fruits)
#clear()
fruits.clear()
print(fruits)

#del
del fruits
print(fruits)

fruits = {"apple", "banana", "kiwi"}
for i in fruits:
    print(i)

# Immutable frozenset
fruits = frozenset({"apple", "banana", "kiwi"})
print(fruits, type(fruits))
for i in fruits:
    print(i)



# union() - | operator also can be used
fruits = {"apple", "banana", "kiwi"}
fruits2 = {"orange", "mango", "grapes"}

print(fruits.union(fruits2))

# intersection() - & operator can also be used
fruits = {"apple", "banana", "kiwi"}
fruits2 = {"orange", "mango", "grapes"}

print(fruits.intersection(fruits2))

# difference()
fruits = {"apple", "banana", "kiwi"}
fruits2 = {"orange", "mango", "grapes"}

print(fruits.difference(fruits2))

# symmetric_differen- ^ operator also can be usedce
fruits = {"apple", "banana", "kiwi"}
fruits2 = {"orange", "mango", "grapes"}

print(fruits.symmetric_difference(fruits2))

# update()
fruits = {"apple", "banana", "kiwi"}
fruits2 = {"orange", "mango", "grapes"}

fruits.update(fruits2)
print(fruits)

# discard()
fruits.discard("apple")
print(fruits)

# remove()
fruits.remove("banana")
print(fruits)

# difference_update()
fruits = {"apple", "banana", "kiwi"}
fruits2 = {"orange", "mango", "grapes"}

fruits.difference_update(fruits2)
print(fruits)


# intersection_update()
fruits = {"apple", "banana", "kiwi"}
fruits2 = {"orange", "mango", "grapes"}

fruits.intersection_update(fruits2)
print(fruits)

# symmetric_difference_update()
fruits = {"apple", "banana", "kiwi"}
fruits2 = {"orange", "mango", "grapes"}

fruits.symmetric_difference_update(fruits2)
print(fruits)

# isdisjoint()
fruits = {"apple", "banana", "kiwi"}
fruits2 = {"orange", "mango", "grapes"}

print(fruits.isdisjoint(fruits2))

# issubset()
fruits = {"apple", "banana", "kiwi"}
fruits2 = {"apple", "banana", "kiwi", "orange", "mango", "grapes"}

print(fruits.issubset(fruits2))

fruits = {"apple", "banana", "kiwi"}
fruits2 = {"apple", "banana", "kiwi", "orange", "mango", "grapes"}

print(fruits.issuperset(fruits2))

# issuperset()

fruits = frozenset({"apple", "banana", "kiwi"})
fruits2 = frozenset({"apple", "banana", "kiwi", "orange", "mango", "grapes"})

print(fruits.issuperset(fruits2))

# frozenset()

fruits = frozenset({"apple", "banana", "kiwi"})
print(fruits, type(fruits))

# frozen set methods
# union()

fruits = frozenset({"apple", "banana", "kiwi"})
fruits2 = frozenset({"orange", "mango", "grapes"})

print(fruits.union(fruits2))

# intersection()

fruits = frozenset({"apple", "banana", "kiwi"})
fruits2 = frozenset({"orange", "mango", "grapes"})

print(fruits.intersection(fruits2))


# isdisjoint()

fruits = frozenset({"apple", "banana", "kiwi"})
fruits2 = frozenset({"orange", "mango", "grapes"})

print(fruits.isdisjoint(fruits2))



