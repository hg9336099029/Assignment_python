# CONDITIONAL STATEMENTS IN PYTHON

age = 20

if age >= 18:
    print("You can vote")

print("age >= 18 gives True")


num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


marks = 82
if marks >= 90:
    print("Grade A+")
elif marks >= 75:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Fail")


age = 22
has_id = True
if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Underage")


age = 25
salary = 50000
if age > 18 and salary > 30000:
    print("Eligible")


day = "Sunday"
if day == "Saturday" or day == "Sunday":
    print("Weekend")


logged_in = False
if not logged_in:
    print("Please login")



age = 19
status = "Adult" if age >= 18 else "Minor"
print(status)


name = ""
if name:
    print("Name exists")
else:
    print("Empty string")



day = 3
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid")


x = 10
y = 20
if x < y:
    print("x is smaller")


balance = 10000
amount = 3000
pin_correct = True

if pin_correct:
    if amount <= balance:
        print("Transaction successful")
    else:
        print("Insufficient balance")
else:
    print("Wrong PIN")
