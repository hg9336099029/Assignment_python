#---------------create dictionary----------------
students = {
    "Rahul": 85,
    "Sneha": 67,
    "Amit": 67,
    "John": 45
}

#----------highesrt marks----------------

for  name , marks in students.items():
    if marks == max(students.values()):
        print(name, marks)

#---------find failed students less than 50 marks----------------

for name , marks in students.items():
    if marks < 50:
        print(name, marks)

#--------find students with same  marks----------------

marks_dict = {}

for name, marks in students.items():
    if marks not in marks_dict:
        marks_dict[marks] = [name]
    else:
        marks_dict[marks].append(name)

for marks, names in marks_dict.items():
    if len(names) > 1:
        print(marks, names)


#------------print grades----------------

for marks in students.values():
    print(marks)

     
#-----Merge Dictionaries---------------------
#--------------Merge and sort dictionary both by key and value-------------
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
d1.update(d2)
print(d1)



#---------Shopping Cart System------------
#------------------Create cart dictionary example :-----------
cart = {
    "Laptop": {
        "price": 50000,
        "qty": 1
        },
    "Mouse": {
        "price": 500,
        "qty": 2
        }
}

# Add product
cart["Keyboard"] = {"price": 1500, "qty": 1}
cart["Smartphone"] = {"price": 1000, "qty": 3}
print(cart)

# Update quantity
cart["Laptop"]["qty"] = 2
print(cart)
# Remove product

del  cart["Mouse"]
print(cart)
# Calculate total bill
total_bill = 0
for product in cart:
    total_bill += cart[product]["price"] * cart[product]["qty"]

print("Total Bill:", total_bill)
# Find most expensive product
expensive_product = None
max_price = 0   
for product in cart:
    if cart[product]["price"] > max_price:
        max_price = cart[product]["price"]
        expensive_product = product

print(expensive_product, max_price)

# Apply 10% discount if total > 50000

if total_bill > 50000:
    total_bill *= 0.9   

print("Total Bill after discount:", total_bill)