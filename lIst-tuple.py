# -------------------- List-----------------------------#

a = [10, 20, 30]
b = []
c = list()
d = [1, "hello", 3.14, True]
nested = [[1, 2], [3, 4]]

print(a)
print(b)
print(c)
print(d)
print(nested)
print()

# 2. Indexing


nums = [10, 20, 30, 40, 50]
print(nums[0])
print(nums[2])
print(nums[-1])
print(nums[-2])
print()

# --------------------------------
# 3. Slicing


print(nums[1:4])
print(nums[:3])
print(nums[2:])
print(nums[::2])
print(nums[::-1])
print()

# --------------------------------
# 4. Modifying List

nums[1] = 999
print(nums)
print()

# --------------------------------
# 5. Adding Elements

lst = [1, 2, 3]

lst.append(4)
print("append:", lst)

lst.extend([5, 6, 7])
print("extend:", lst)

lst.insert(1, 100)
print("insert:", lst)
print()

# --------------------------------
# 6. Removing Elements


temp = [10, 20, 30, 20, 40]

temp.remove(20)
print("remove:", temp)

temp.pop()
print("pop last:", temp)

temp.pop(1)
print("pop index:", temp)

del temp[0]
print("del:", temp)

temp.clear()
print("clear:", temp)
print()

# --------------------------------
# 7. Searching Methods

arr = [1, 2, 3, 2, 2, 5]

print("index:", arr.index(3))
print("count:", arr.count(2))
print()

# --------------------------------
# 8. Sorting
# --------------------------------

data = [5, 2, 9, 1, 7]

data.sort()
print("ascending:", data)

data.sort(reverse=True)
print("descending:", data)

x = [4, 8, 1]
y = sorted(x)

print("original:", x)
print("sorted copy:", y)
print()

# --------------------------------
# 9. Reverse


rev = [1, 2, 3, 4]
rev.reverse()
print(rev)

print(rev[::-1])
print()

# --------------------------------
# 10. Copying Lists

a = [1, 2, 3]

b = a.copy()
c = a[:]
d = list(a)

print(b)
print(c)
print(d)
print()

# --------------------------------
# 11. Concatenation


a = [1, 2]
b = [3, 4]

c = a + b
print(c)
print()

# --------------------------------
# 12. Repetition
# --------------------------------
print("12. Repetition")

rep = [0] * 5
print(rep)
print()