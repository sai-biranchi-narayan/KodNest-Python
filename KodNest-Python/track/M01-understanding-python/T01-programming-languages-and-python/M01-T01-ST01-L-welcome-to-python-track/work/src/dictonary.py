# Dictonary - {key:value} - curly braces with key:value pairs (key cannot be duplicate value can be duplicate)


dict1 = {"name": "John", "age": 30, "city": "New York"}
print(dict1 , type(dict1))


dict1 = {"name": "John", "age": 30, 
"city": ["New York", "USA", "Germany"]}

dict1["name"] = "Doe"
print(dict1, dict.keys(), dict1.values(), dict1.items())
print(type(dict1), dict1["names"], dict1["city"][1])

# constructor
stu_info = dict(name = "Ram", age = 30, city = "USA")
stu_info["salary"] = 50000
stu_info["salary"] = 30000
stu_info.update({"salary": 20000})
stu_info.pop("age")
stu_info.popitem() #last
del stu_info["city"]
stu_info.clear()
del stu_info
print(stu_info)

# loop dicts
dict1 = {"name": "John", "age": 30, 
"city": ["New York", "USA", "Germany"]}
for i in dict1.values():
        print(i)

# Dict Methods
print(dict1.get("name"))
print(dict1.get("salary", 0))
# formkeys
print(dict1.form(["name", "age", "city"]))
#setdefault
print(dict1.setdefault("name", "John"))
#copy
dict2 = dict1.copy()
print(dict2)







