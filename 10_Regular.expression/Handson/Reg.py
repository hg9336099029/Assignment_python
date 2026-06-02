#  REGULAR EXPRESSIONS (re)
#----A Regular Expression (Regex) is a pattern used to search, match, extract, replace, or validate text.--#
import re #--importing the regex module

#-Without regex:

email = "abc@gmail.com"

if "@" in email and ".com" in email:
    print("Valid")


#-With regex:
pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
if re.match(pattern, email):
    print("Valid")
else:
    print("Invalid")

#-----Regex can validate:-----#

# Email
# Phone numbers
# Passwords
# URLs
# Dates
# Log files
# Data extraction

#------Basic Regex Functions--------#
#--1. re.search()---->Searches entire string and returns first match.

txt = "My age is 21"

result = re.search(r"\d+", txt) # \d+ matches one or more digits in the string.

print(result.group())


#-----2. re.match()------>Searches only from the beginning of the string and returns a match if found.
print(re.match(r"Hello", "Hello World"))

print(re.match(r"World", "Hello World")) #--No match because "World" is not at the beginning of the string.


#--3. re.findall()---->Returns a list of all matches in the string.

txt = "1 apple 2 mango 3 banana"
print(re.findall(r"\d+", txt))

#--4. re.sub()---->Replaces all occurrences of a pattern with a specified replacement string.

txt = "The price is $100"
new_txt = re.sub(r"\$\d+", "$50", txt)
print(new_txt)

#--5. re.finditer()---->Returns an iterator yielding match objects for all matches in the string.

txt = "1 apple 2 mango 3 banana"
matches = re.finditer(r"\d+", txt)
for match in matches:
    print(match.group())


#--6. re.split()---->Splits the string by the occurrences of the pattern and returns a list of substrings.

txt = "apple,banana,mango"
print(re.split(r",", txt))

#--7. re.compile()---->Compiles a regex pattern into a regex object for faster execution.

pattern = re.compile(r"\d+")
txt = "My age is 21"
result = pattern.search(txt)
print(result.group())


# \d -> matches any digit (0-9)

print(re.findall(r"\d", "a1b2c3"))

# Output: ['1', '2', '3']


# \D -> matches any non-digit character

print(re.findall(r"\D", "a1b2"))

# Output: ['a','b']



# \w -> matches letters, digits and underscore

print(re.findall(r"\w", "ab_12"))

# Output: ['a', 'b', '_', '1', '2']



# \W -> matches characters that are not letters, digits or underscore

print(re.findall(r"\W", "ab@12"))

# Output: ['@']

# \s -> matches whitespace characters (space, tab, newline)

print(re.findall(r"\s", "a b c"))

# Output: [' ', ' ']

# \S -> matches non-whitespace characters

print(re.findall(r"\S", "a b"))

# Output: ['a', 'b']



# * -> previous character appears 0 or more times

print(re.findall(r"ab*", "a ab abb abbb"))

# Output: ['a', 'ab', 'abb', 'abbb']



# + -> previous character appears 1 or more times

print(re.findall(r"ab+", "a ab abb"))

# Output: ['ab', 'abb']



# ? -> previous character appears 0 or 1 time

print(re.findall(r"ab?", "a ab abb"))

# Output: ['a', 'ab', 'ab']



# {3} -> exactly 3 digits

print(re.findall(r"\d{3}", "123 45 678"))

# Output: ['123', '678']



# {2,4} -> between 2 and 4 digits

print(re.findall(r"\d{2,4}", "1 12 123 1234 12345"))

# Output: ['12', '123', '1234', '1234']



# [abc] -> match either a, b or c

print(re.findall(r"[abc]", "apple"))

# Output: ['a']



# [0-9] -> any digit

print(re.findall(r"[0-9]", "a1b2"))

# Output: ['1', '2']



# [a-z] -> lowercase letters

print(re.findall(r"[a-z]", "AbC123"))

# Output: ['b']

# [A-Z] -> uppercase letters

print(re.findall(r"[A-Z]", "AbC"))

# Output: ['A', 'C']



# [^0-9] -> anything except digits

print(re.findall(r"[^0-9]", "a1b2"))

# Output: ['a', 'b']



# ^ -> match at start of string

print(re.search(r"^Hello", "Hello World"))



# $ -> match at end of string

print(re.search(r"World$", "Hello World"))



# . -> match any single character except newline

print(re.findall(r"a.c", "abc axc a7c"))

# Output: ['abc', 'axc', 'a7c']



# | -> OR operator

print(re.findall(r"cat|dog", "cat dog tiger"))

# Output: ['cat', 'dog']

# () -> capture groups

txt = "John 25"

m = re.search(r"(\w+)\s(\d+)", txt)


# First group = name

print(m.group(1))  # John



# Second group = age

print(m.group(2))  # 25



# Extract all numbers from text

txt = "Order 123 Amount 500"

print(re.findall(r"\d+", txt))

# Output: ['123', '500']



# Extract email addresses

txt = """

abc@gmail.com

test@yahoo.com

"""



print(re.findall(r"\w+@\w+\.\w+", txt))

# Output: ['abc@gmail.com', 'test@yahoo.com']



# Validate 10-digit mobile number

num = "9876543210"

if re.fullmatch(r"\d{10}", num):
    print("Valid")
else:
    print("Invalid")



# Validate 6-digit PIN code

pin = "226001"

print(bool(re.fullmatch(r"\d{6}", pin)))

# Output: True

# Extract hashtags from text

txt = "Learning #Python and #AI"
print(re.findall(r"#\w+", txt))

# Output: ['#Python', '#AI']

