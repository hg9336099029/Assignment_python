import re

# 1. EXTRACT EMAIL ADDRESSES

# text = "Contact us at support@test.com or admin123@gmail.com"
# pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# emails = re.findall(pattern, text) # re.findall() return a list of all matches in the string.
# print(emails)


# 2. VALIDATE PASSWORD

#pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

# password1 = "Password@123"
# result1 = bool(re.match(pattern, password1))
# print(result1)

# password2 = "password123"
# result2 = bool(re.match(pattern, password2))
# print(result2)

# password3 = "SecurePass@1"
# result3 = bool(re.match(pattern, password3))
# print(result3)

# # 3.------------------ EXTRACT DATES---------------------#

# text = "Meeting on 12-05-2026 and another on 2026-06-01. Event: 15/06/2026"
# pattern = r'(\d{2}[-/]\d{2}[-/]\d{4}|\d{4}[-/]\d{2}[-/]\d{2})'
# dates = re.findall(pattern, text)
# print(dates)

# #----------------- 4. FIND DUPLICATE WORDS-------------------#

# text = "This is is a sample sample text."
# pattern = r'\b(\w+)\s+\1\b'
# duplicates = re.findall(pattern, text, re.IGNORECASE)

# print(duplicates)




# #------ 5. CONVERT MULTIPLE SPACES TO ONE--------------#

# text = "Hello     World\t\tPython"
# result = re.sub(r'[ \t]+', ' ', text).strip() 
# # re.sub() replaces all occurrences of the pattern 
# # with a single space. .strip() removes leading and trailing spaces.

# print(result)


# #------------------- 6. LOG FILE PARSER -------------------#

# log_text = """2026-06-01 10:23:45 ERROR Database connection failed
# 2026-06-01 10:24:12 INFO User login successful
# 2026-06-01 10:25:30 WARNING High memory usage detected"""

# pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+(\w+)\s+(.+)'
# matches = re.findall(pattern, log_text)


# for match in matches:
#     log_dict = {
#         'timestamp': match[0],
#         'level': match[1],
#         'message': match[2]
#     }
#     print(log_dict)


# # 7.----------- EXTRACT HTML TAGS-------------------#


# html_text = "Hello<div>World</div><p>Text</p><a href='#'>Link</a></div>"
# pattern = r'</?([a-zA-Z][a-zA-Z0-9]*)'
# tags = re.findall(pattern, html_text)
# tags = list(dict.fromkeys(tags))  # Remove duplicates, preserve order
# print(f"HTML: {html_text}")
# print(f"Result: {tags}")
# print(f"Expected: ['div', 'p', 'a']")



# # 8. EXTRACT CURRENCY VALUES


text = "Revenue was $1,200.50, profit ₹50,000 and loss €300, also £150.99"
pattern = r'[$₹€£¥]\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
currencies = re.findall(pattern, text)
print(f"Text: {text}")
print(f"Result: {currencies}")

