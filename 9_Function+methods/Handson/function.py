#------Functions----------------------------#
# In Python, a function is a reusable block of code 
# that performs a specific task. Instead of writing the 
# same code multiple times, you write it once inside a 
# function and call it whenever needed.

# FUNCTIONS


# Simple function
def greet(name):
    return "Hello " + name + "!"

print(greet("Harsh"))


# # Function with default argument
def power(num, p=2):
    return num ** p

print(power(5)) # if we not pass the power, it will default to 2 (square)
print(power(5, 3)) # we can also specify the power, in this case it will calculate 5^3


# Function returning multiple values
def calc(a, b):
    return a + b, a - b, a * b

s, d, m = calc(10, 5)
print("Sum:", s)
print("Difference:", d)
print("Multiplication:", m)


# Variable length arguments (*args)
# *args allows a function to accept any number of (positional arguments)
# * just says "pack" all extra positional arguments into a tuple called args
def total(*args):
    # print(type(args)) #------->args is a tuple
    return sum(args)
print(total(1, 2, 3, 4, 5)) #----->args is like tuple (1, 2, 3, 4, 5)


# Keyword arguments (**kwargs)
#---**kwargs allows a function to accept any number of keyword arguments.

# kwargs = {
#     "name": "Harsh",
#     "age": 21,
#     "city": "Lucknow"
# }

## ---So kwargs is a dictionary. The ** just says "pack" all extra 
#--------------> keyword arguments into a dictionary called kwargs.
## **kwargs is used to accept a variable number of keyword arguments in a function. Python collects all 
## keyword arguments into a dictionary, where the argument names become keys and their values become dictionary values.

def student(**kwargs):
    for k, v in kwargs.items():
        print(k, ":", v)

student(name="Harsh", age=21, city="Lucknow")


# # 2. METHODS

# # Methods belong to objects/classes

s = "hello world"

print(s.upper())       # HELLO WORLD
print(s.lower())       # hello world
print(s.title())       # Hello World
print(s.replace("world", "Python"))
print(s.split())

nums = [1, 2, 3]

nums.append(4)
print(nums)

nums.remove(2)
print(nums)

nums.reverse()
print(nums)

# # 3. ENUMERATE FUNCTION

#---->enumerate() is used when you need both the index 
# and the value while looping through an iterable (list, tuple, string, etc.).

fruits = ["apple", "banana", "mango"]

# Without enumerate
for i in range(len(fruits)):
    print(i, fruits[i])

print()

# With enumerate
for idx, value in enumerate(fruits):
    print(idx, value)

print()

# Start index from 1
for idx, value in enumerate(fruits, start=1):
    print(idx, value)

# # 4. REGULAR EXPRESSIONS (re)


# text = """
# My name is Harsh.
# Email: harsh@gmail.com
# Phone: 9876543210
# Roll Number: 2201234
# """

# # ------------------------------------------
# # re.search()
# # Finds first occurrence
# # ------------------------------------------

# result = re.search(r"Harsh", text)

# if result:
#     print("Found:", result.group())
#     print("Start:", result.start())
#     print("End:", result.end())


# # ------------------------------------------
# # re.findall()
# # Returns all matches
# # ------------------------------------------

# numbers = "10 20 30 40 50"

# print(re.findall(r"\d+", numbers))


# # ------------------------------------------
# # re.match()
# # Checks only beginning
# # ------------------------------------------

# print(re.match(r"My", text.strip()))


# # ------------------------------------------
# # re.split()
# # ------------------------------------------

# sentence = "Python,Java,C++,JavaScript"

# print(re.split(",", sentence))


# # ------------------------------------------
# # re.sub()
# # Replace pattern
# # ------------------------------------------

# print(re.sub(r"\d", "*", "Phone: 9876543210"))


# # ==========================================
# # 5. COMMON REGEX PATTERNS
# # ==========================================

# print("\n===== COMMON PATTERNS =====")

# sample = "abc123XYZ"

# print(re.findall(r"\d", sample))
# # digits

# print(re.findall(r"\D", sample))
# # non-digits

# print(re.findall(r"\w", sample))
# # letters + digits + underscore

# print(re.findall(r"\W", "@#$"))
# # special characters

# print(re.findall(r"[a-z]", sample))
# # lowercase

# print(re.findall(r"[A-Z]", sample))
# # uppercase


# # ==========================================
# # 6. EMAIL EXTRACTION
# # ==========================================

# print("\n===== EMAIL EXTRACTION =====")

# txt = """
# harsh@gmail.com
# test@yahoo.com
# abc123@outlook.com
# """

# emails = re.findall(
#     r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
#     txt
# )

# print(emails)


# # ==========================================
# # 7. PHONE NUMBER EXTRACTION
# # ==========================================

# print("\n===== PHONE EXTRACTION =====")

# text = """
# 9876543210
# 9123456789
# 8765432109
# """

# phones = re.findall(r"\b\d{10}\b", text)

# print(phones)


# # ==========================================
# # 8. VALIDATE EMAIL
# # ==========================================

# print("\n===== EMAIL VALIDATION =====")

# email = "harsh@gmail.com"

# pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

# if re.match(pattern, email):
#     print("Valid Email")
# else:
#     print("Invalid Email")


# # ==========================================
# # 9. ENUMERATE + REGEX TOGETHER
# # ==========================================

# print("\n===== ENUMERATE + REGEX =====")

# lines = [
#     "Name: Harsh",
#     "Phone: 9876543210",
#     "Email: harsh@gmail.com"
# ]

# for idx, line in enumerate(lines, start=1):

#     phone = re.findall(r"\d{10}", line)

#     if phone:
#         print(f"Line {idx}: Phone Found -> {phone[0]}")


# # ==========================================
# # 10. COMPILE REGEX
# # ==========================================

# print("\n===== COMPILED REGEX =====")

# pattern = re.compile(r"\d+")

# print(pattern.findall("100 200 300"))

# # Reuses compiled regex efficiently