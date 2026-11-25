# 1. Searching a List (Time Complexity: O(n))

products_list = [
    ["P101", "Keyboard", 1200],
    ["P102", "Mouse", 600],
    ["P103", "Monitor", 8500]
]

required_code = "P103"

# Linear search across the list
found_product = None
for product in products_list:
    if product[0] == required_code:
        found_product = product
        break

print("List Search Result:", found_product)


# 2. Direct Dictionary Lookup (Time Complexity: O(1))

products_dict = {
    "P101": ["Keyboard", 1200],
    "P102": ["Mouse", 600],
    "P103": ["Monitor", 8500]
}

# Safe lookup using the 'in' operator
if required_code in products_dict:
    print("Dictionary Lookup Result:", products_dict[required_code])
else:
    print("Product not found")

# Alternative: Safe lookup using .get() with a default fallback
product_info = products_dict.get(required_code, "Product not found")
print("Using .get():", product_info)


# 3. Direct Update Through Key
# Update price of P102 directly without searching
products_dict["P102"][1] = 650
print("Updated P102 Details:", products_dict["P102"])

# List of records
employees = [
    {"employee_id": "E101", "name": "Asha", "department": "Development"},
    {"employee_id": "E102", "name": "Ravi", "department": "Testing"},
    {"employee_id": "E103", "name": "Meera", "department": "Support"},
]

# 2. Build the indexed dictionary
employee_by_id = {}

for employee in employees:
    employee_id = employee["employee_id"]
    employee_by_id[employee_id] = employee

# 3. Quick O(1) lookup
required_id = "E102"

if required_id in employee_by_id:
    employee = employee_by_id[required_id]
    print("Name:", employee["name"])
    print("Department:", employee["department"])
else:
    print("Employee not found")




students = [
    {"name": "Asha", "course": "Python"},
    {"name": "Ravi", "course": "Java"},
    {"name": "Meera", "course": "Python"},
    {"name": "Kiran", "course": "SQL"},
]

students_by_course = {}
for student in students:
    course = student["course"]
    name = student["name"]

    if course not in students_by_course:
            students_by_course[course] = []

    students_by_course[course].append(name)

    print(students_by_course)

     
