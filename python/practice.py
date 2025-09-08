"""
print("Hello world")
print("It's really good")

# This is my first python program


# Basic variable  - Integer, float, string, boolean
 
full_name= "Sandeep"
age = 27
bankBalance = 34.57
mentally_stable = True

print(f"my name is {full_name}")
print(f"age is {age}")
print(f"my bank balance is {bankBalance}")
print(f"am i mentally stable? {mentally_stable}")

if mentally_stable:
    print("good for job")
else:
    print("not suitable for the job")



# Arithmatic operation: +, - , /{floor division}, *, //{integer division} % (no increment operator[++])

friends = 5.0
friends /= 2

print(friends)


# Type casting - str() , int(), float(), bool()

name = "Sandy"
age = 27
gpa = 5.6
is_student = True
class_roll = "6"

print(type(is_student))

gpa = int(gpa)
age = float(age)
age = str(age)
#name = int(name)
class_roll = int(class_roll)
print(type(age))

empty= ""
name = bool(name)
print(bool(empty))

gpa=-0.1
gpa=bool(gpa)
print(gpa)


# User Imput

name = input("enter the name: ")
age = int(input("Enter your age: "))
print(f"You're {age} old")
print(f"hello {name}")

print(type(age))


# if statements = execute only if its true, good for basic decision-making

age = int(input("Enter the age: "))
if age>=18: 
    print("You are an adult")
elif age<0:
    print("Unborn")
else:
    print("Childuuu")


# Logical operators - or and not 

# The not operator works with Python's truthy/falsy concept:

#    Falsy values: False, 0, "", [], {}, None

#    Truthy values: Everything else


temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("Cancel the outdoor event")
else:
    print("The outdoor event is still scheduled")

if not is_raining:
    print("its not raining")

if not None:
    print("its True value")


# While Loop = use to repeat code block until the condition is false

name = input("Enter the name: ")
password = input("enter your password: ")

while not name or not password:
    print("either name or password cant be empty")
    name = input("Pls enter your name: ")
    password = input("Pls enter your password: ")
    if name and password: 
        print(f"Hello {name} welcome to website")
        break 
else: 
    print(f"Hello {name} welcome to website")



# For loop = used to iterate over a sequence (string, list, tuple .. etc)

import time
name = "Sandeep Reddy"

for i in range(1, 10, 3):
    print(i, end=" ")

for letter in name:
    print(letter, end="-")

for i in range(10,0,-1):
    print(i)
    time.sleep(1)
print("Happy New Year!!!")


# List [] - mutable, most flexible
# Tuple () - immutable, faster
# Set {} - mutable (add/remove) , unordered(no index accessing), no duplicates, best for membership testing


fruits = ["apple", "orange", "banana"]
print(fruits[1])

fruits[2] = "mango"
fruits.append("coconut")
fruits.remove("apple")
fruits.pop(2)

for fruit in fruits:
    print(fruit, end = " ")

fruits.clear()
print(fruits)


veggies = ("carrot", "onion", "spinach")
print(veggies[0])
# veggies[0] = "potato" # not possible


brands = {"samsung", "lg", "hyndai"}
print(brands)
# print(brands[1]) # TypeError: 'set' object is not subscriptable

brands.add("nike")
brands.remove("lg")
print(brands)

# brands.pop(4) # TypeError: set.pop() takes no arguments (1 given)

brands.add("nike")
print(brands)


brand = input("enter a brand to search for: ")

if brand in brands:
    print(f"{brand} was found")
else:
    print(f"{brand} was not found")

"""
