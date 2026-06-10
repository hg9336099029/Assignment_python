# ----------------------------------------------------------
# SEQUENCE GENERATOR
# ----------------------------------------------------------
# A sequence generator produces values in a sequence.
# Values are generated only when needed.
# This saves memory for large sequences.
# ----------------------------------------------------------

# def number_sequence(start, end):
#     current = start
#     while current <= end:
#         yield current
#         current += 1


# print("Number Sequence Generator")

# seq = number_sequence(1, 5)

# print(next(seq))
# print(next(seq))

# for num in seq:
#     print(num)


# # ----------------------------------------------------------
# # EVEN NUMBER SEQUENCE GENERATOR
# # ----------------------------------------------------------
# # Generates even numbers one by one.
# # ----------------------------------------------------------

def even_sequence(limit):

    for num in range(2, limit + 1, 2):
        yield num 
#---yield returns the current value and pauses execution until the next value is requested.

print("\nEven Number Sequence")

for num in even_sequence(10):
    print(num)


# # ----------------------------------------------------------
# # ODD NUMBER SEQUENCE GENERATOR
# # ----------------------------------------------------------
# # Generates odd numbers one by one.
# # ----------------------------------------------------------

# def odd_sequence(limit):

#     for num in range(1, limit + 1, 2):
#         yield num


# print("\nOdd Number Sequence")

# for num in odd_sequence(10):
#     print(num)


# # ----------------------------------------------------------
# # FIBONACCI SEQUENCE GENERATOR
# # ----------------------------------------------------------
# # Generates Fibonacci numbers on demand.
# # ----------------------------------------------------------

# def fibonacci_sequence(n):

#     a, b = 0, 1

#     for _ in range(n):

#         yield a

#         a, b = b, a + b


# print("\nFibonacci Sequence")

# for num in fibonacci_sequence(10):
#     print(num)


# # ----------------------------------------------------------
# # TICKET NUMBER SEQUENCE GENERATOR
# # ----------------------------------------------------------
# # Practical example:
# # Generating ticket IDs one by one.
# # ----------------------------------------------------------

# def ticket_sequence():

#     ticket = 1001

#     while ticket <= 1005:

#         yield ticket

#         ticket += 1


# print("\nTicket Number Sequence")

# for ticket in ticket_sequence():
#     print(ticket)


# # ----------------------------------------------------------
# # ALPHABET SEQUENCE GENERATOR
# # ----------------------------------------------------------
# # Generates characters from A to Z.
# # ----------------------------------------------------------

# def alphabet_sequence():

#     for code in range(ord('A'), ord('Z') + 1):
#         yield chr(code)


# print("\nAlphabet Sequence")

# for ch in alphabet_sequence():
#     print(ch, end=" ")


# # ----------------------------------------------------------
# # EXHAUSTED SEQUENCE GENERATOR
# # ----------------------------------------------------------
# # Once all values are consumed,
# # the sequence generator cannot be reused.
# # ----------------------------------------------------------

# print("\n\nExhausted Sequence Generator")

# seq = number_sequence(1, 3)

# print(next(seq))
# print(next(seq))
# print(next(seq))

# try:
#     print(next(seq))
# except StopIteration:
#     print("Sequence exhausted")


# # ----------------------------------------------------------
# # INFINITE SEQUENCE GENERATOR
# # ----------------------------------------------------------
# # Generates numbers forever.
# # Be careful when using infinite generators.
# # ----------------------------------------------------------

# def infinite_sequence():

#     num = 1

#     while True:

#         yield num

#         num += 1


# print("\nInfinite Sequence Generator")

# inf = infinite_sequence()

# for _ in range(5):
#     print(next(inf))