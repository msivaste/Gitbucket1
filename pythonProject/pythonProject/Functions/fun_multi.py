# a = int(input("Enter A: "))
# b = int(input("Enter B: "))
# c = int(input("Enter C: "))
#
# def sum():
#     add = a+b
#     return add
#
# addition = sum()
# final_val = addition*c
# print(final_val)

def sum(n1, n2):
    add = n1 + n2
    return add

a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))

addition = sum(a,b)
final_val = addition*c
print(final_val)