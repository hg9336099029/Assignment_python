#----------In-built Functions in Python----------

# # int() -> convert value to integer
# print(int("10"))

# # float() -> convert value to float
# print(float("10"))

# # str() -> convert value to string
# print(str(100))

# # bool() -> convert value to boolean
# print(bool(1))
# print(bool(0))

# # list() -> convert iterable to list
# print(list("abc"))

# # tuple() -> convert iterable to tuple
# print(tuple([1, 2, 3]))

# # set() -> remove duplicate values
# print(set([1, 2, 2, 3]))

# # len() -> returns number of elements
# print(len([1, 2, 3, 4]))

# # max() -> returns largest element
# print(max([5, 2, 8, 1]))

# # min() -> returns smallest element
# print(min([5, 2, 8, 1]))

# # sum() -> returns sum of all elements
# print(sum([1, 2, 3, 4]))

# # abs() -> returns absolute value
# print(abs(-10))

# # round() -> rounds to nearest integer
# print(round(3.76))

# # pow() -> returns base raised to power
# print(pow(2, 3))

# # type() -> returns datatype
# print(type(100))

# # isinstance() -> checks datatype
# print(isinstance(100, int))

# # range() -> generates numbers from 0 to 4
# for i in range(5):
#     print(i)

# # enumerate() -> gives index and value
# fruits = ["apple", "banana", "mango"]
# for idx, fruit in enumerate(fruits):
#     print(idx, fruit)

# # zip() -> combines multiple iterables
# names = ["Harsh", "Aman"]
# ages = [21, 22]
# for name, age in zip(names, ages):
#     print(name, age)

# # sorted() -> returns new sorted list
# nums = [5, 3, 1, 4]
# print(sorted(nums))

# # reversed() -> returns reverse iterator
# print(list(reversed(nums)))

# # all() -> True if all values are True
# print(all([True, True, True]))
# print(all([True, False, True]))

# # any() -> True if at least one value is True
# print(any([False, False, True]))
# print(any([False, False, False]))

# # ord() -> character to Unicode value
# print(ord('A'))

# # chr() -> Unicode value to character
# print(chr(65))

# # iter() -> creates iterator from iterable
# nums = [10, 20, 30]
# it = iter(nums)

# # next() -> gets next value from iterator
# print(next(it))
# print(next(it))
# print(next(it))

# # map() -> applies function to every element
# nums = [1, 2, 3, 4]
# result = list(map(lambda x: x * 2, nums))
# print(result)

# # filter() -> keeps elements matching condition
# result = list(filter(lambda x: x % 2 == 0, nums))
# print(result)

# # bin() -> decimal to binary
# print(bin(10))

# # oct() -> decimal to octal
# print(oct(10))

# # hex() -> decimal to hexadecimal
# print(hex(10))

# # id() -> returns unique object identifier
# a = [1, 2, 3]
# print(id(a))

# # dir() -> shows available methods and attributes
# print(dir("hello"))

# # input() -> takes user input
# # name = input("Enter your name: ")
# # print("Hello", name)

# # help() -> shows documentation
# # help(str)

# # String input
# name = input("Enter your name: ")
# print(name)

# # Integer input
# age = int(input("Enter your age: "))
# print(age)

# # Float input
# salary = float(input("Enter your salary: "))
# print(salary)

# # Two integers in one line
# a, b = map(int, input("Enter two numbers: ").split())
# print(a, b)

# # Three integers in one line
# x, y, z = map(int, input("Enter three numbers: ").split())
# print(x, y, z)

# # List of integers
# nums = list(map(int, input("Enter numbers: ").split()))
# print(nums)

# # List of strings
# words = input("Enter words: ").split()
# print(words)

# # Character input
# ch = input("Enter a character: ")
# print(ch[0])

# # Taking n numbers using a loop
# n = int(input("How many numbers? "))

# arr = []

# for i in range(n):
#     num = int(input())
#     arr.append(num)

# print(arr)

# # Matrix input
# rows = int(input("Enter number of rows: "))

# matrix = []

# for i in range(rows):
#     row = list(map(int, input().split()))
#     matrix.append(row)

# print(matrix)

# # Input always returns string
# value = input("Enter anything: ")
# print(type(value))

# # Convert string input to integer
# num = int(input("Enter an integer: "))
# print(type(num))

# # Convert string input to float
# price = float(input("Enter a float value: "))
# print(type(price))


# # Single integer
# n = int(input())

# # String
# s = input()

# # Two integers
# a, b = map(int, input().split())

# # List of integers
# arr = list(map(int, input().split()))

# # Matrix
# matrix = [list(map(int, input().split())) for _ in range(n)]

#ceil and floor
import math

print(math.ceil(3.2))
print(math.floor(3.8))
