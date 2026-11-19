# practice Questions
# Q1- Negative Indexing
t = (10, 20, 30, 40, 50, 60, 70, 80)
print(t[-6:-1])
print(t[-1:-6:-2])

# Q2. Negative Step

t = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(t[7:2:-1])
print(t[8:1:-2])

# Q3. Multiple Negative Slicing

t = (10, 20, 30, 40, 50, 60, 70, 80, 90)
print(t[-2:-8:-2])
print(t[-8:-2:2])

# Q4. Reverse Slicing

t = (5, 10, 15, 20, 25, 30, 35, 40, 45, 50)
print(t[::-2])
print(t[8::-3])
print(t[-2::-3])

# Q5. Empty Tuple Slicing

t = (10, 20, 30, 40, 50)
print(t[2:2])
print(t[4:1])
print(t[-1:2])
print(t[1:4:-1])

# Q6. Multiple Slicing Operations

t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
a = t[::-1]
b = a[2:8:2]
print(a)
print(b)
print(b[::-1])

# Q7. Out-of-Range Indexes

t = (10, 20, 30, 40, 50)
print(t[2:100])
print(t[-100:3])
print(t[100:0:-1])
print(t[-100:100:2])

# Q8. Nested Tuple Slicing

t = ((10, 20, 30), (40, 50, 60),
     (70, 80, 90), (100, 110, 120))
print(t[::-1])
print(t[1:4:2])
print(t[0][::-1])
print(t[::-1][1][1:])

# Q9. Tuple Concatenation and Slicing

t1 = (1, 2, 3, 4, 5)
t2 = (6, 7, 8, 9, 10)
t = t1[::-1] + t2[1::2]
print(t)
print(t[2:8:2])
print(t[-2::-3])

# Q10. Advanced Slicing Challenge

t = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120)
a = t[::-1]
b = a[1:-1:2]
c = b[::-1]
print(a)
print(b)
print(c)
print(c[1::2])
print(c[-2::-2])