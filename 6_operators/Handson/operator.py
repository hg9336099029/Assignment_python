
# 1. ARITHMETIC OPERATORS

a = 15
b = 4

# Addition
print(a + b)          # 19

# Subtraction
print(a - b)          # 11

# Multiplication
print(a * b)          # 60

# Division
print(a / b)          # 3.75

# Floor Division
print(a // b)         # 3

# Modulus
print(a % b)          # 3

# Power
print(a ** 2)         # 225


# 2. COMPARISON OPERATORS

age = 21

print(age > 18)       # True
print(age < 18)       # False
print(age == 21)      # True
print(age != 30)      # True
print(age >= 21)      # True
print(age <= 20)      # False

# 3. LOGICAL OPERATORS

has_ticket = True
has_id = False

print(has_ticket and has_id)     # False
print(has_ticket or has_id)      # True
print(not has_id)                # True


# 4. ASSIGNMENT OPERATORS

salary = 50000

salary += 5000
print(salary)

salary -= 2000
print(salary)

salary *= 2
print(salary)

salary //= 3
print(salary)

# 5. BITWISE OPERATORS

x = 6
y = 3

print(x & y)
print(x | y)
print(x ^ y)
print(~x)
print(x << 1)
print(x >> 1)

# 6. MEMBERSHIP OPERATORS
#-types------- 1. in 2.not in
fruits = ["apple", "banana", "mango"]

print("banana" in fruits)
print("grapes" not in fruits)


# 7. IDENTITY OPERATORS

a = [10, 20]
b = a
c = [10, 20]

print(a is b)
print(a is c)
print(a is not c)

# 8. CONDITIONAL OPERATOR

marks = 78

grade = "Pass" if marks >= 40 else "Fail"
print(grade)


# 9. STRING OPERATORS


first = "Hello"
second = "Python"

print(first + " " + second)
print(first * 3)

# 10. LIST OPERATORS

l1 = [1, 2]
l2 = [3, 4]

print(l1 + l2)
print(l1 * 2)


# 11. CHAIN COMPARISON

temp = 28

print(20 < temp < 35)
print(35 < temp < 50)


# 12. WALRUS OPERATOR


if (num := len("Python")) > 5:
    print(num)


# 13. OPERATOR PRECEDENCE

# Parentheses first
result = (10 + 5) * 2
print(result)

# Power before multiplication
result = 2 * 3 ** 2
print(result)

# Multiplication before addition
result = 10 + 5 * 2
print(result)

# Comparison after arithmetic
result = 10 + 5 > 12
print(result)

# Logical AND before OR
result = True or False and False
print(result)

# NOT before AND
result = not False and True
print(result)

# Complex example
result = 5 + 2 * 3 ** 2 > 20 and not False
print(result)


# OPERATOR PRECEDENCE ORDER

# 1. Parentheses ()
# 2. Power **
# 3. Unary + - ~
# 4. *, /, //, %
# 5. +, -
# 6. <<, >>
# 7. &
# 8. ^
# 9. |
# 10. Comparison (==, !=, >, <, >=, <=)
# 11. Identity (is, is not)
# 12. Membership (in, not in)
# 13. not
# 14. and
# 15. or
# 16. Conditional expression
# 17. Assignment