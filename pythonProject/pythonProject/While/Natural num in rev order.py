# i = 10
# while(i>=1):
#     print(i, end=",")
#     i=i-1
#

i = int(input("Enter N: "))
fact = 1
while(i>0):
    fact = fact * i
    i=i-1
print("Factorial value for given number is : ", fact)
