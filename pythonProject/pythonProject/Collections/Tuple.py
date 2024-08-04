# Tuple means similar to list allows duplicate. Only difference is we cannot modify the items. We cannot add or remove or replace

a = (1,2,3,4,5)
b=list(a)
b.pop()
print(a)
print(b)

