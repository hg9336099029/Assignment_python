import copy
#---------------1. Shallow Copy (copy.copy())------------------------
a=[1, 2, 10, 20]

b = copy.copy(a)   
 
b.append(30)
print(a)
print(b)
print(id(a[0]))
print(id(b[0]))
#------A shallow copy creates a new outer object, but the nested objects inside are still same shared memory address.--------------

a = [1, 2, [10, 20]]

b = copy.copy(a)


print(a)
print(b)

print(id(a[0]))
print(id(b[0]))

print(id(a[2]))
print(id(b[2]))

#---------------2. Deep Copy (copy.deepcopy())------------------------
#A deep copy creates a new outer object and also recursively copies all the nested objects, 
# resulting in completely independent objects with different memory addresses.
a = [1, 2, [10, 20]]
b= copy.deepcopy(a)
b[2].append(30)
print(a)
print(b)

print(id(a[0]))
print(id(b[0]))

print(id(a[2]))
print(id(b[2]))


