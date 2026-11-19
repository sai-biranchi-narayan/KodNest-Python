# Shallow Copy
original = [[1,2], [3,4]]
import copy
s_copy = copy.copy(original)
original [1] [0] = 300
print(original)
print(s_copy)

# Deep copy 
import copy
original = [[1,2], [3,4]]
new_list = copy.deepcopy(original)
original [0][0] = 100
print(original)
print(new_list)
