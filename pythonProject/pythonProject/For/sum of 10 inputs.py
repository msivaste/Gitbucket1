# sum = 0
# for i in range(1,11):
#     i = int(input("Enter input for number: "))
#     sum = sum + i
# print("Average of all 10 input is ",sum/10)


# List
# a = [1,2,3,4,5]
# for i in a:
#     print(i)


a=[]
print("Enter 10 numbers 1 by 1: ")
for i in range(10):
    num = int(input("Enter num "+str(i+1)+":"))
    a.append(num)
print(a)
sum=0
for i in a:
    sum = sum+ i
print("Average of all 10 inputs: ", sum/10)



