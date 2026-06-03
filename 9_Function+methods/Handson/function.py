#------Functions----------------------------#
# In Python, a function is a reusable block of code 
# that performs a specific task. Instead of writing the 
# same code multiple times, you write it once inside a 
# function and call it whenever needed.

# FUNCTIONS


# Simple function
# def greet(name):
#     return "Hello " + name + "!"

# print(greet("Harsh"))


# # Function with default argument
# def power(num, p=2):
#     return num ** p

# # print(power(5)) # if we not pass the power, it will default to 2 (square)
# print(power(5, 3)) # we can also specify the power, in this case it will calculate 5^3


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

#explore *args-----------
def total(args):
    print(type(args)) #------->args is a tuple
    return sum(args)

tp=(1,2,3)
print(total(tp)) #----->args is like tuple (1, 2, 3, 4, 5)


# Keyword arguments (**kwargs)
#---**kwargs allows a function to accept any number of keyword arguments.

# kwargs = {
#     "name": "Harsh",
#     "age": 21,
#     "city": "Lucknow"
# }

# ## ---So kwargs is a dictionary. The ** just says "pack" all extra 
# #--------------> keyword arguments into a dictionary called kwargs.
# ## **kwargs is used to accept a variable number of keyword arguments in a function. Python collects all 
# ## keyword arguments into a dictionary, where the argument names become keys and their values become dictionary values.

#--------explore **kwargs-----------
# def student(**kwargs):
#     for k, v in kwargs.items():
#         print(k, ":", v)

# student(name="Harsh", age=21, city="Lucknow")



##-->Mixing normal parameters and *args
#---------> name gets the first argument.
#---------> Remaining positional arguments go into marks as a tuple.
# def student(name, *marks):
#     print("Name:", name)
#     print("Marks:", marks)

# student("Harsh", 90, 85, 88)

# # 2. METHODS

# # Methods belong to objects/classes
##-->A method is a function that belongs to an object.

#-->object.method()

s = "hello world"

# s is a string object.
# nums is a list object.
# upper(), append() are methods.

# print(s.upper())       # HELLO WORLD
# print(s.lower())       # hello world
# print(s.title())       # Hello World
# print(s.replace("world", "Python"))
# print(s.split())

# nums = [1, 2, 3]
# #---->nums is a list object.
# # append() is a method of the list class.
# # Python calls the method on the object nums.
# nums.append(4)
# print(nums)

# nums.remove(2)
# print(nums)

# nums.reverse()
# print(nums)

# # # 3. ENUMERATE FUNCTION

# #---->enumerate() is used when you need both the index 
# # and the value while looping through an iterable (list, tuple, string, etc.).

fruits = ["apple", "banana", "mango"]

# # Without enumerate function is becoming the syntax heavy and less readable.
# for i in range(len(fruits)):
#     print(i, fruits[i])

# print()


# With enumerate function is more readable and cleaner.
for idx, value in enumerate(fruits):
    print(idx, value)
print()

# # We can also specify the starting index for enumerate using the start parameter.

# for idx, value in enumerate(fruits, start=1):
#     print(idx, value)

