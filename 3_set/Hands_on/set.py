a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# create
x = {1, 2, 2, 3, 4}
e = set()

# add
a.add(10)

# update
a.update([20, 30])

# remove
a.remove(10)

# discard
a.discard(100)

# pop
a.pop()

# copy
c = a.copy()

# clear
temp = {1, 2, 3}
temp.clear()

# union
u = a | b

# intersection
i = a & b

# difference
d = a - b

# symmetric difference
sd = a ^ b

# subset
x = {1, 2}
y = {1, 2, 3, 4}
sub = x.issubset(y)

# superset
sup = y.issuperset(x)

# disjoint
m = {10, 20}
n = {30, 40}
dis = m.isdisjoint(n)

# membership
check1 = 2 in y
check2 = 100 in y

# loop
for item in y:
    print(item)

# list to set
lst = [1, 2, 2, 3, 4, 4]
s = set(lst)

# frequency
data = [1, 2, 2, 3, 4, 4, 4, 5]

unique = set(data)

for i in unique:
    if data.count(i) > 1:
        print(i)

for i in unique:
    print(i, data.count(i))

# student example
python_students = {"Rahul","Amit","Sneha","John"}
sql_students = {"John","Sneha","David","Meena"}
aws_students = {"Rahul","David","Kiran"}

both = python_students & sql_students
all3 = python_students & sql_students & aws_students
only_python = python_students - sql_students - aws_students
total = python_students | sql_students | aws_students

for name in total:
    if name.startswith("Ra"):
        print(name)

for name in total:
    if name.endswith("na") or name.endswith("an"):
        print(name)