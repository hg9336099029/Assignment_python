# --------Exception Handling in Python --------------#
# Exception handling is a mechanism used to handle runtime errors so that the program does not crash unexpectedly.
# try:
#     a = 10
#     b = 0
#     print(a / b)
# except ZeroDivisionError:
#     print("Cannot divide by zero")


# # try-except-else example
# # else block executes only when no exception occurs

# try:
#     n = int(input("Enter a number: "))
#     result = 100 / n
# except ZeroDivisionError:
#     print("Division by zero is not allowed")
# else:
#     print("Result =", result)


# try-except-finally example
# finally block executes whether exception occurs or not
# try:
#     x = int(input("Enter a number: "))
#     print(50 / x)
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# finally:
#     print("Finally block executed")


# # Handling multiple exceptions separately
# try:
#     n = int(input("Enter a number: "))
#     print(100 / n)
# except ValueError:
#     print("Input must be an integer")
# except ZeroDivisionError:
#     print("Cannot divide by zero")


# # Generic exception handling
# # Exception as e stores the actual error object
# try:
#     lst = [10, 20, 30]
#     print(lst[5])
# except Exception as e:
#     print(e)


# # Raising an exception manually
# # raise keyword is used to generate exceptions
# try:
#     age = int(input("Enter age: "))
    
#     if age < 18:
#         raise ValueError("Age must be at least 18")
    
#     print("Eligible")
# except ValueError as e:
#     print(e)


# # Custom exception class
# # User-defined exceptions inherit from Exception
# class InvalidSalaryError(Exception):
#     pass

# try:
#     salary = int(input("Enter salary: "))
    
#     if salary < 0:
#         raise InvalidSalaryError("Salary cannot be negative")
    
#     print("Salary =", salary)
# except InvalidSalaryError as e:
#     print(e)


# # Assertion example
# # assert checks whether a condition is True
# try:
#     marks = int(input("Enter marks: "))
    
#     assert marks >= 0, "Marks cannot be negative"
    
#     print("Marks =", marks)
# except AssertionError as e:
#     print(e)


# # Nested try-except blocks
# # Inner exception is handled by inner except block
# try:
#     n = int(input("Enter a number: "))
    
#     try:
#         print(100 / n)
#     except ZeroDivisionError:
#         print("Inner Exception")
        
# except ValueError:
#     print("Outer Exception")


# # Exception handling inside functions
# def divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return "Cannot divide by zero"

# print(divide(10, 2))
# print(divide(10, 0))


# # finally executes even when return statement is present
# def test():
#     try:
#         return "Returned from try"
#     finally:
#         print("Finally executed")

# print(test())

# different type of exceptions
try:
    num = int(input("Enter a number: "))
    print(100 / num)
except ValueError:      
    print("Invalid input")  
except ZeroDivisionError:
    print("Cannot divide by zero")


#-------------#
try:
    num = int(input("Enter number: "))
    print(10 / num)

except ValueError:
    print("Invalid number")

except ZeroDivisionError:
    print("Cannot divide by zero")

except Exception as e:
    print("Some other error:", e)

finally:
    print("Always executes")