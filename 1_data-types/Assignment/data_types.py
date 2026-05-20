

print("Q1. STRING STORAGE IN PYTHON")
print()

s1 = "hello"
s2 = "hello"

print("String value:", s1)
print("Type:", type(s1))
print("Same object check:", s1 is s2)

print("""
Explanation:
- Strings are immutable in Python.
- Immutable means once created, they cannot be changed.
- Python stores strings as objects.
- Small/repeated strings may be interned (memory optimization).
- Because of interning, identical strings can point to same memory object.
""")

print("=" * 60)
print("Q2. NONE IN PYTHON")

a = None
b = None

print("a == b:", a == b)
print("a is b:", a is b)

print("""
Explanation:
- None represents absence of value.
- Python has only one None object (singleton).
- == checks value equality.
- is checks memory identity.
- Since None is singleton, both return True.
""")

print("=" * 60)

print("Q3. DOCSTRINGS")
print()

def add(x, y):
    """
    Adds two numbers and returns result.
    """
    return x + y

print("Function Output:", add(10, 20))
print("DocString:")
print(add.__doc__)

class Student:
    """
    Represents a student object.
    """
    def __init__(self, name):
        self.name = name

print("""
Explanation:
- DocStrings are documentation strings.
- Written inside triple quotes.
- Used to describe modules, functions, classes, methods.
- Access using __doc__.
""")

print("=" * 60)

print("Q4. FLOAT VS DECIMAL")
print()

from decimal import Decimal

x = 0.1 + 0.2
y = Decimal("0.1") + Decimal("0.2")

print("Float Result:", x)
print("Decimal Result:", y)

print("""
Explanation:
FLOAT:
- Faster
- Uses binary floating-point
- May cause precision errors
- Example: 0.1 + 0.2 = 0.30000000000000004

DECIMAL:
- Higher precision
- Exact decimal arithmetic
- Used in banking, finance
- Slower than float
""")

print("=" * 60)

print("Q5. LIST, TUPLE, DICTIONARY")
print()

numbers = [10, 20, 30]
print("LIST")
print(numbers)
numbers.append(40)
print("After append:", numbers)
numbers[0] = 99
print("After modification:", numbers)

print("""
List:
- Ordered
- Mutable
- Allows duplicates
- Indexing supported
""")

print("-" * 40)

data = (1, 2, 3, 4)
print("TUPLE")
print(data)

print("""
Tuple:
- Ordered
- Immutable
- Allows duplicates
- Faster than list
- Indexing supported
""")

print("-" * 40)

student = {
    "name": "Harsh",
    "age": 21,
    "city": "Lucknow"
}

print("DICTIONARY")
print(student)
print("Name:", student["name"])

student["age"] = 22
student["course"] = "BTech"

print("Updated Dictionary:", student)

print("""
Dictionary:
- Key-value pairs
- Mutable
- Keys must be unique
- Fast lookup
- Ordered (Python 3.7+)
""")

print("=" * 60)

print("COMPARISON TABLE")
print()

print("""
Feature         List        Tuple       Dictionary
--------------------------------------------------
Ordered         Yes         Yes         Yes
Mutable         Yes         No          Yes
Duplicates      Yes         Yes         Values yes
Indexing        Yes         Yes         No
Key-Value       No          No          Yes
Syntax          []          ()          {}
""")