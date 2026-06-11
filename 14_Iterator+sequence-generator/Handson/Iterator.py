#------------------------ ITERATOR IN PYTHON--------------------#
#
# An iterator is an object that allows us to access elements
# of a collection one at a time.
#
# iter()  -> Creates an iterator from an iterable.
# next()  -> Returns the next element from the iterator.
#
# The iterator remembers its current position.
#
# Examples of iterables:
#   List
#   Tuple
#   String
#   Set
#   Dictionary
#   Range
#   Generator
#
# When all elements are consumed, next() raises
# StopIteration.
#
# -----------------------------------------------------------------#

#------------------- LIST ITERATOR---------------------------------#

# List is an iterable.
# iter() converts it into a list_iterator object.
# next() fetches one value at a time.
#---------------------------------------------------------------#

lst = [10, 20, 30]

lst_it = iter(lst)

print(lst_it)  # <list_iterator object at 0x...>

while True:
    try:
        print(next(lst_it))
    except StopIteration:
        print("No more elements available")
        break


# ==========================================================
# TUPLE ITERATOR
# ==========================================================
# Tuple elements can also be accessed one by one.
# Python internally creates a tuple_iterator object.
# ==========================================================

# tup = (100, 200, 300)

# tup_it = iter(tup)

# print(next(tup_it))
# print(next(tup_it))
# print(next(tup_it))


# # ==========================================================
# # STRING ITERATOR
# # ==========================================================
# # String characters are returned one at a time.
# # ==========================================================

# name = "HARSH"

# str_it = iter(name)

# print(next(str_it))
# print(next(str_it))
# print(next(str_it))
# print(next(str_it))
# print(next(str_it))


# # ==========================================================
# # SET ITERATOR
# # ==========================================================
# # Set is unordered.
# # Elements may appear in any order.
# # ==========================================================

# st = {10, 20, 30}

# set_it = iter(st)

# for value in set_it:
#     print(value)


# # ==========================================================
# # DICTIONARY ITERATOR
# # ==========================================================
# # By default iter(dictionary) returns keys.
# # ==========================================================

# student = {
#     "name": "Harsh",
#     "age": 22,
#     "city": "Lucknow"
# }

# dict_it = iter(student)


# for key in dict_it:
#     print(key)


# # ==========================================================
# # DICTIONARY VALUE ITERATOR
# # ==========================================================
# # values() returns a view object.
# # iter() converts it into an iterator.
# # ==========================================================

# val_it = iter(student.values())

# for value in val_it:
#     print(value)


# # ==========================================================
# # DICTIONARY ITEM ITERATOR
# # ==========================================================
# # items() returns key-value pairs.
# # ==========================================================

# item_it = iter(student.items())


# for item in item_it:
#     print(item)


# # ==========================================================
# # RANGE ITERATOR
# # ==========================================================
# # range() does not create all numbers at once.
# # It generates them efficiently.
# # ==========================================================

# rng = range(1, 6)

# rng_it = iter(rng)

# for num in rng_it:
#     print(num)


# # ==========================================================
# # ZIP ITERATOR
# # ==========================================================
# # zip() combines multiple iterables.
# # It returns a zip object which is an iterator.
# # ==========================================================

# names = ["Harsh", "Amit", "Rohit"]
# marks = [90, 85, 95]

# zip_it = iter(zip(names, marks))

# for record in zip_it:
#     print(record)


# # ==========================================================
# # ENUMERATE ITERATOR
# # ==========================================================
# # enumerate() adds index values.
# # It returns an iterator.
# # ==========================================================

# enum_it = iter(enumerate(["Python", "SQL", "GenAI"], start=1))

# for item in enum_it:
#     print(item)


# # ==========================================================
# # GENERATOR ITERATOR
# # ==========================================================
# # Every generator is an iterator.
# # yield returns a value and pauses execution.
# # ==========================================================

# def numbers():

#     for i in range(1, 6):
#         yield i


# gen_it = iter(numbers())

# print("\nGENERATOR ITERATOR")

# for num in gen_it:
#     print(num)


# # ==========================================================
# # STOP ITERATION EXAMPLE
# # ==========================================================
# # When no elements remain, Python raises
# # StopIteration.
# # ==========================================================

# nums = [1, 2]

# it = iter(nums)


# print(next(it))
# print(next(it))

# try:
#     print(next(it))
# except StopIteration:
#     print("No more elements available")


# # ==========================================================
# # TYPES OF ITERATORS CREATED BY PYTHON
# # ==========================================================
# # Python creates specialized iterator objects
# # for different data types.
# # ==========================================================

# print(type(iter([1, 2, 3])))       # list_iterator
# print(type(iter((1, 2, 3))))       # tuple_iterator
# print(type(iter("abc")))           # str_iterator
# print(type(iter({1, 2, 3})))       # set_iterator
# print(type(iter({"a": 1})))        # dict_keyiterator
# print(type(iter(range(5))))        # range_iterator


# # ==========================================================
# # IMPORTANT POINTS
# # ==========================================================
# #
# # Iterable:
# #   An object that can be converted into an iterator.
# #
# # Iterator:
# #   An object that remembers its position and returns
# #   one element at a time using next().
# #
# # Every iterator is iterable.
# # Not every iterable is an iterator.
# #
# # Example:
# #
# # nums = [10,20,30]      -> Iterable
# # it = iter(nums)        -> Iterator
# #
# # ==========================================================