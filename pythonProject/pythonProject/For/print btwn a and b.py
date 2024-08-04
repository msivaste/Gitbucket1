# a = int(input("Enter A: "))
# b = int(input("Enter B: "))
# for i in range((a+1),b):
#     print(i)


# a = int(input("Enter A: "))
# b = int(input("Enter B: "))
# for i in range(a,b+1):
#     print(i)

from collections import namedtuple
a = namedtuple('Company', 'name , JD')
s = a('CGI', 'QA')
print(s)