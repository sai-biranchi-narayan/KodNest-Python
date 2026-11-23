# Square of numbers
nums = [1, 2, 3, 4]
sq_nums = []
for i in nums:
    sq_nums.append(i * i)

print(sq_nums)

# for even numbers
nums = [2, 4]
even = [i for i in nums if i % 2 == 0 ]
print(even)

# For odd Nums
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd = [i for i in range(1,10) if i % 2 != 0]
print(odd)

# uppercase
names = ["Ram", "Sita", "Lakshman", "Ravan"]
upper_list = [n.upper() for n in names]
print(upper_list)

# lengith of list
names = ["Ram", "Sita", "Lakshman", "Ravan"]
len_list = [len(n) for n in names]
print(len_list)

# if else even odd
numbers = [1, 2, 3, 4, 5, 6]
result = ["Even" if n % 2 ==0 else "odd" for n in numbers]
print(result)

# Greater nuif n > 5
num = [1, 7, 3, 8, 2]
gt_num = [n for n in num if n > 5]
print(gt_num)

# string into list
word = "Python"
lst = [i for i in word]
print(lst)

# matrix
matrix = [[1, 2], [3, 4], [5, 6]]
res = [n for row in matrix for n in row]
print(res)

# Multiplacitation pair
matrix = [(1,1), (1,2), (1,3), (2,1), (2,2),(2,3)]
res = [(i, j) for i in range (1,3) for j in range(1,4)]
print = (res)





