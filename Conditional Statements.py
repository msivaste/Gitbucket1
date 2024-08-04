# age = int(input("Enter Age: "))
# if age>=18:
#     print("Eligible for Vote")
# else:
#     print("Sorry, not eligible for Vote")

#Specifying Boolean directly
#
# if False:
#     print("Condition is True")
# else:
#     print("Condition is False")

#Specifying direct numbers
#
# if 0:
#     print('One')
# else:
#     print('Not one')
#

#Finding a number is even or odd

# a = int(input("Enter number: "))
# if a % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")

#---Combining whole into one single statement (Ternary operator)
# a = int(input("Enter number: "))
# print("Even number") if a%2==0 else print("Odd number")

#---Multiple statements in single line
# a = 10
# {print("Hello"),print("Python")} if a==10 else {print("Hi"),print("Java")}

# #---Multiple Condition---
# Weekno = 7
# if Weekno == 1:
#     print("Sunday")
# elif Weekno == 2:
#     print("Monday")
# elif Weekno == 3:
#     print ("Tuesday")
# elif Weekno == 4:
#     print("Wednesday")
# elif Weekno == 5:
#     print("Thursday")
# elif Weekno == 6:
#     print("Friday")
# elif Weekno == 7:
#     print("Saturday")
# else:
#     print("Invalid input")


#Assignment 1: Check the given number is positive or negative
# a = 1;
# if a<0:
#     print("Negative")
# else:
#     print("Positive")

#Assignment 2: Check the largest of 2 numbers
# a = 10
# b = 9
# print("a is bigger") if a>b else print("b is bigger")

# # Assignment 3: Check the largest of 2 numbers
# a = 10
# b = 1000
# c = 100
# if a>b:
#     if a>c:
#         print("a is big")
#     else:
#         print("c is big")
# elif b>c:
#     print("b is big")
# else:
#     print("c is big")

# Assignment 4 - Print weeknumber if we input weekname

Weekname = "Tuesday"
if Weekname == "Sunday":
    print("1")
elif Weekname == 'Monday':
    print("2")
elif Weekname == "Tuesday":
    print (3)
elif Weekname == "Wednesday":
    print("4")
elif Weekname == "Thursday":
    print("5")
elif Weekname == "Friday":
    print("6")
elif Weekname == "Saturday":
    print("7")
else:
    print("Invalid input")