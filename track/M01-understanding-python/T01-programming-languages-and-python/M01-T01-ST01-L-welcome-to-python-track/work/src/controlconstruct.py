# Part 1 - IF, IF-ELSE, If-Elif-Else

# # Program 1 :  check if a number is positive. Num = 5
# number = int(input("enter the num: "))
# if number > 0:
#     print("Number is positive")

# # Program 2 : Check if a person is eligible to donate blood (age >= 18)
# age = int(input("enter your age : "))
# if age >= 18:
#     print("Eligible for blood donation")
# else:
#     print("Not eligible for blood donation")    

#  # Program 3 : Check if the temperature is abobe 30 degree cels and print "Hot Day"
# temp = int(input("enter the temp: "))
# if temp > 30:
#     print("Hot Day")

# # Program 4 : Check wheather a studednt attened atleast 75% of the classes
# classes = int(input("enter the number of classes attended: "))
# total_classes = int(input("enter the total number of classes: "))
# if (classes / total_classes) * 100 >= 75:
#     print("Eligible for exams")
# else:
#     print("Not eligible for exams")

# # program 5 : Check wheather a number is even or odd
# number = int(input("enter the number: "))
# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# # program 6 : Check wheather a given year is leap year

# year = int(input("Enter a year: "))

# if year % 400 == 0:
#     print("Leap year")
# elif year % 100 == 0:
#     print("Not a leap year")
# elif year % 4 == 0:
#     print("Leap year")
# else:
#     print("Not a leap year")

# # Progtram 8 : Compare two numbers and print greater number
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))
# if num1 > num2:
#     print("num1 is greater")
# else:
#     print("num2 is greater")

# program 9 : Assin grades based on marks 
# 90 - 100 : A
# 80 - 89 : B
# 70 - 79 : C
# 60 - 69 : D
# 0 - 59 : Fail

marks = int(input("Enter the marks: "))
if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
elif marks >= 60:
    print("D")
else:
    print("F")

# program 10 : Categorize electricty usages
# Above 500 : High
# 301 - 500 : Medium
# 101 - 300 : Low
# 0 - 100 : Very Low

units = int(input("Enter the units: "))
if units > 500:
    print("High")
elif units > 300:
    print("Medium")
elif units > 100:
    print("Low")
else:
    print("Very Low")

# Program 11: Scholarship Eligibility
# Marks >= 85
# Family Income < 300000
scholarship = False
marks = int(input("Enter the marks: "))
family_income = int(input("Enter the family income: "))

if marks >= 85 and family_income < 300000:
    scholarship = True
    print("Eligible for scholarship")
else:
    print("Not eligible for scholarship")

# Program 12:  User login 
# User is Correct
# Password is correct
username = input("Enter the username: ")
password = input("Enter the password: ")
if username == "Admin" and password == "12345":
    print("Login successful")
else:
    print("Login failed")

# Pogtram 13 : Display weekday using number(1 -7)

num = int(input("Enter the number: "))
if num == 1:
    print("Monday")
elif num == 2:
    print("Tuesday")
elif num == 3:
    print("Wednesday")
elif num == 4:
    print("Thursday")
elif num == 5:
    print("Friday")
elif num == 6:
    print("Saturday")
elif num == 7:
    print("Sunday")
else:
    print("Invalid number")

# program 14: Display seasons based on month number 
# Dec - Feb : Winter
# Mar - May : Summer
# Jun - Sep : Monsoon
# Oct - Nov : Autumn

month = int(input("Enter the month number: "))
if month == 12 or month == 1 or month == 2:
    print("Winter")
elif month == 3 or month == 4 or month == 5:
    print("Summer")
elif month == 6 or month == 7 or month == 8:
    print("Monsoon")
elif month == 9 or month == 10 or month == 11:
    print("Autumn")
else:
    print("Invalid month")





    




   




    









