a = int(input('Enter A: '))
b = int(input('Enter B: '))
# print('a + b:', (a+b))
c = int(input('Enter C: '))
if (a>b):
    if(a>c):
        print("A is big")
    else:
        print("C is big")
elif (b>c):
    print("B is big")
else:
    print("C is big")
