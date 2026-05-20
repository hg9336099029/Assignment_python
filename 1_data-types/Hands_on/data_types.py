print("===== LIST =====")

lst = [10, 20, 30, 20, "Python", True]
print(lst)
print(lst[0])
print(lst[-1])

lst.append(100)
print(lst)

lst.insert(1, 99)
print(lst)

lst.remove(20)
print(lst)

lst.pop()
print(lst)

print(lst[1:4])

lst.reverse()
print(lst)


print("\n===== TUPLE =====")

t = (1, 2, 3, 2, "Hello")
print(t)
print(t[0])
print(t.count(2))
print(t.index("Hello"))


print("\n===== SET =====")

s = {10, 20, 30, 20, 40}
print(s)

s.add(50)
print(s)

s.remove(20)
print(s)

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
print(a & b)
print(a - b)
print(a ^ b)


print("\n===== FROZENSET =====")

fs = frozenset([1, 2, 3, 4])
print(fs)


print("\n===== DICTIONARY =====")

student = {
    "name": "Harsh",
    "age": 21,
    "city": "Lucknow"
}

print(student)
print(student["name"])

student["age"] = 22
print(student)

student["course"] = "BTech"
print(student)

print(student.keys())
print(student.values())
print(student.items())


print("\n===== RANGE =====")

r = range(1, 10, 2)

for i in r:
    print(i)


print("\n===== STRING =====")

s = "Python Programming"

print(s)
print(s[0])
print(s[0:6])
print(s.upper())
print(s.lower())
print(s.replace("Python", "Java"))


print("\n===== BYTES =====")

b = b"hello"
print(b)
print(b[0])


print("\n===== BYTEARRAY =====")

ba = bytearray([65, 66, 67])
print(ba)

ba[0] = 90
print(ba)


print("\n===== MEMORYVIEW =====")

data = bytes([10, 20, 30, 40])
mv = memoryview(data)

print(mv[0])


print("\n===== NESTED NON-PRIMITIVE =====")

nested = [
    [1, 2, 3],
    ("a", "b"),
    {"x": 100, "y": 200},
    {10, 20}
]

print(nested)
print(nested[0][1])
print(nested[2]["x"])