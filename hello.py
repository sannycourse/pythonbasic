"""This is a beginning of a Python script."""

print("Hello, Raja")
print("Hello, World whow is this!")
print("Hello, Sanny!")

# Types of Comments =>
# 1. Single-line comment in Python starts with a hash (#).
# 2. Multi-line comments can be done using triple quotes (''' or """) or by using multiple single-line comments.


# Syntax
"""This is a multi-line comment in Python."""

if 5 > 2:
    print("Five is greater than two!")


# Variables
x = 5
y = "Hello, World!"
name = 'raushan'
lname = "Kumar"
CountryName = "India"

print(type(x))  # Output: <class 'int'>
print(x) # Output: 5
print(y)
print(name+" " + lname)  # Output: Sanny Kumar
print(CountryName)

# Variable - Type Casting/conversation - one data type to another data type conversion
a = str(4)
print(type(a))


# Case-Sensitive
Age = 20
age = 30
print(Age)
print(age)


# Data Types => Check w3school documntation for more details

# String
collegeName = "Dr. B. C. Roy Engineering College, Durgapur"
print(collegeName)
univerysityName = 'Maulana Abul Kalam Azad University of Technology, West Bengal'
print(univerysityName)

poem = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(poem)


# String are arrays => index start from 0,1,2,3,,,,,
print(univerysityName[2])  # Output: u
print(len(univerysityName))
print("Technology" in univerysityName)

# String method

#Slicing - cut a specific part of the string
animalName = "Elephant"
finalString = animalName[2:6] 
print(finalString)  # Output: Ele


startString = animalName[:2]  # From start to index 2
endString = animalName[4:]  # From index 6 to end
missingString = animalName[1:7:-1]

print(startString)  # Output: El
print(endString)  # Output: ant
print(missingString)  # Output: eph

#  String formatting
age = 21
formattedString = f"My name is {name} and I am {age} years old."
print(formattedString)  # Output: My name is Sanny and I am 20 years old.


# Task => practice more string methods


# boolean
age = 16
isAgeValid = False

if age >= 18:
    isAgeValid = True
elif age >= 60:
    isAgeValid = False
else:
    print("Age is not valid", isAgeValid)

print(isAgeValid)  # Output: False





print()
print()
print()
# For Loop
for x in univerysityName:
    print(x)



# if else
txt = "The best things in life are free!"

if "things" not in txt:
  print("1 No, 'expensive' is NOT present.")
elif "best12" not in txt:
  print("2 No, 'expensive' is NOT present.")
else:
  print("already available")









 

