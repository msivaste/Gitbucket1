#List - supports duplicates, supports all data types inside list. List is also called a datatype

a=[1,2,3,4,5,6,True,"Siva"]
print(a[1])

#To append a value in list
a.append(7)
print(a)

#To replace a value
a[2]=8
print(a)

# remove a value from list
a.pop(5)
print(a)

# To remove last element
a.pop()
print(a)

# Extend - to merge 2 or more list
a = [1,2,3,4,5]
b = [6,7,8,9]
a.extend(b)
print(a)
