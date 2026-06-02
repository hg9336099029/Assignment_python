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

