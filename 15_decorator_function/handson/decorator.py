# ==========================================================
# DECORATORS IN PYTHON - COMPLETE HANDS-ON PRACTICE FILE
# ==========================================================
# A decorator is a function that takes another function,
# adds extra functionality, and returns a modified function.
#
# Syntax:
#
# @decorator_name
# def my_function():
#     pass
#
# Internally Python does:
#
# my_function = decorator_name(my_function)
#
# ==========================================================


# ==========================================================
# 1. BASIC DECORATOR
# ==========================================================

def basic_decorator(func):

    def wrapper():

        print("\n[Basic Decorator] Before Function")

        func()

        print("[Basic Decorator] After Function")

    return wrapper


@basic_decorator
def greet():

    print("Hello Harsh!")


greet()


# # ==========================================================
# # 2. LOGGING DECORATOR
# # ==========================================================
# # Used to track when a function starts and ends.
# # ==========================================================

# def logger(func):

#     def wrapper():

#         print(f"\n[Logger] {func.__name__} started")

#         func()

#         print(f"[Logger] {func.__name__} completed")

#     return wrapper


# @logger
# def testing():

#     print("Running test cases...")


# testing()


# # ==========================================================
# # 3. DECORATOR WITH ARGUMENTS
# # ==========================================================
# # *args -> tuple of positional arguments
# # **kwargs -> dictionary of keyword arguments
# # ==========================================================

# def argument_logger(func):

#     def wrapper(*args, **kwargs):

#         print("\nArguments:", args)
#         print("Keyword Arguments:", kwargs)

#         return func(*args, **kwargs)

#     return wrapper


# @argument_logger
# def add(a, b):

#     print("Sum =", a + b)


# add(10, 20)


# # ==========================================================
# # 4. DECORATOR RETURNING VALUE
# # ==========================================================

# def value_logger(func):

#     def wrapper(*args, **kwargs):

#         print("\nFunction Started")

#         result = func(*args, **kwargs)

#         print("Function Ended")

#         return result

#     return wrapper


# @value_logger
# def multiply(a, b):

#     return a * b


# print("Result =", multiply(5, 6))


# # ==========================================================
# # 5. TIMER DECORATOR
# # ==========================================================
# # Used to measure execution time.
# # ==========================================================

# import time


# def timer(func):

#     def wrapper(*args, **kwargs):

#         start = time.time()

#         result = func(*args, **kwargs)

#         end = time.time()

#         print(f"Execution Time = {end-start:.2f} seconds")

#         return result

#     return wrapper


# @timer
# def task():

#     time.sleep(2)

#     print("\nTask Completed")


# task()


# # ==========================================================
# # 6. AUTHENTICATION DECORATOR
# # ==========================================================
# # Simulates login check.
# # ==========================================================

# logged_in = True


# def login_required(func):

#     def wrapper():

#         if logged_in:

#             return func()

#         print("Access Denied")

#     return wrapper


# @login_required
# def dashboard():

#     print("\nWelcome to Dashboard")


# dashboard()


# # ==========================================================
# # 7. EXCEPTION HANDLING DECORATOR
# # ==========================================================
# # Handles runtime errors.
# # ==========================================================

# def handle_error(func):

#     def wrapper(*args, **kwargs):

#         try:

#             return func(*args, **kwargs)

#         except Exception as e:

#             print("Error:", e)

#     return wrapper


# @handle_error
# def divide(a, b):

#     return a / b


# print("\nDivision Result =", divide(10, 2))

# divide(10, 0)


# # ==========================================================
# # 8. MULTIPLE DECORATORS
# # ==========================================================
# # Order:
# #
# # hello = decorator1(decorator2(hello))
# #
# # ==========================================================

# def decorator1(func):

#     def wrapper():

#         print("\nDecorator 1 Start")

#         func()

#         print("Decorator 1 End")

#     return wrapper


# def decorator2(func):

#     def wrapper():

#         print("Decorator 2 Start")

#         func()

#         print("Decorator 2 End")

#     return wrapper


# @decorator1
# @decorator2
# def hello():

#     print("Hello World")


# hello()


# # ==========================================================
# # 9. DECORATOR WITH PARAMETERS
# # ==========================================================
# # Example:
# #
# # @repeat(3)
# #
# # repeat(3) returns a decorator.
# # ==========================================================

# def repeat(n):

#     def decorator(func):

#         def wrapper():

#             for i in range(n):

#                 func()

#         return wrapper

#     return decorator


# @repeat(3)
# def say_hi():

#     print("Hi")


# print()
# say_hi()


# # ==========================================================
# # 10. CLASS BASED DECORATOR
# # ==========================================================
# # __call__ allows object to behave like a function.
# # ==========================================================

# class Logger:

#     def __init__(self, func):

#         self.func = func

#     def __call__(self):

#         print("\nBefore Function")

#         self.func()

#         print("After Function")


# @Logger
# def welcome():

#     print("Welcome User")


# welcome()


# # ==========================================================
# # 11. CACHE DECORATOR
# # ==========================================================
# # Stores previously computed results.
# # ==========================================================

# def cache(func):

#     memory = {}

#     def wrapper(n):

#         if n in memory:

#             print(f"\nCache Hit for {n}")

#             return memory[n]

#         print(f"Cache Miss for {n}")

#         result = func(n)

#         memory[n] = result

#         return result

#     return wrapper


# @cache
# def square(n):

#     return n * n


# print(square(5))
# print(square(5))
# print(square(10))


# # ==========================================================
# # 12. RETRY DECORATOR
# # ==========================================================
# # Retries function if exception occurs.
# # ==========================================================

# def retry(attempts):

#     def decorator(func):

#         def wrapper(*args, **kwargs):

#             for i in range(attempts):

#                 try:

#                     return func(*args, **kwargs)

#                 except Exception as e:

#                     print(f"Attempt {i+1} Failed")

#             print("All Attempts Failed")

#         return wrapper

#     return decorator


# counter = 0


# @retry(3)
# def unstable_function():

#     global counter

#     counter += 1

#     if counter < 3:

#         raise Exception("Temporary Error")

#     return "Success"


# print("\n", unstable_function())


# # ==========================================================
# # 13. INPUT VALIDATION DECORATOR
# # ==========================================================
# # Checks if age is positive.
# # ==========================================================

# def validate_age(func):

#     def wrapper(age):

#         if age < 0:

#             print("Invalid Age")

#             return

#         return func(age)

#     return wrapper


# @validate_age
# def register(age):

#     print(f"Age {age} Registered")


# register(25)
# register(-5)


# # ==========================================================
# # 14. PRESERVING FUNCTION METADATA
# # ==========================================================
# # Without wraps(), function name becomes wrapper.
# # ==========================================================

# from functools import wraps


# def preserve_metadata(func):

#     @wraps(func)
#     def wrapper():

#         print("\nExecuting Function")

#         return func()

#     return wrapper


# @preserve_metadata
# def sample():

#     """Sample Function"""

#     print("Inside Sample")


# sample()

# print("Function Name:", sample.__name__)
# print("Doc String:", sample.__doc__)

routes = {}

def route(path):

    def decorator(func):
        routes[path] = func
        return func

    return decorator


@route("/")
def home():
    return "Home Page"


@route("/login")
def login():
    return "Login Page"


@route("/profile")
def profile():
    return "Profile Page"


# Simulate browser requests
print(routes["/"]())
print(routes["/login"]())
print(routes["/profile"]())