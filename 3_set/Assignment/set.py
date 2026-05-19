python_students = {"Rahul","Amit","Sneha","John"}
sql_students = {"John","Sneha","David","Meena"}
aws_students = {"Rahul","David","Kiran"}

#  Students in both Python and SQL
both_python_sql = python_students & sql_students
print(both_python_sql)

#  Students in all 3 courses
all_three = python_students & sql_students & aws_students
print( all_three)

# Students only in Python
only_python = python_students - sql_students - aws_students
print( only_python)

# Total unique students
total_unique = python_students | sql_students | aws_students
print( total_unique)
print( len(total_unique))

# Students not enrolled in AWS
not_in_aws = (python_students | sql_students) - aws_students
print( not_in_aws)

#  Students in more than 2 courses
courses = [python_students, sql_students, aws_students]

students = set.union(*courses)

result = []

for s in students:
    count = 0
    for course in courses:
        if s in course:
            count += 1
    if count > 2:
        result.append(s)

print(result)

#------------------starts with ra-----------------
all_students = python_students | sql_students | aws_students

for i in all_students:
    if i.startswith("Ra"):
        print(i)

#------------------ends with na or an-----------------
for i in all_students:
    if i.endswith("na") or i.endswith("an"):
        print(i)


data = [1,2,2,3,4,4,4,5]

# unique values
print(set(data))

# duplicate values
for i in set(data):
    if(data.count(i)>1):
        print(i)
    
# count frequency of each element
for i in set(data):
    print(data.count(i))