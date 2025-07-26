''' 1st question '''
my_string = "  Welcome to Python Bootcamp! Let's learn Python.  "

# Q1  Remove leading and trailing spaces
stripped_string = my_string.strip()
print("Stripped String:", stripped_string)

#Q2. Convert to lowercase
lower_string = stripped_string.lower()
print("Lowercase:",lower_string)

#Q3 Convert to uppercase
upper_string = stripped_string.upper()
print("Uppercase:", upper_string)

#Q4 Replace "Python" with "JavaScript"
replaced_string = stripped_string.replace("Python", "JavaScript")
print("Replaced String:", replaced_string)


#5Q Count how many times "Python" appears
python_count = stripped_string.count("Python")
print("Count of 'Python':", python_count)

# 6. Check if the string ends with "."
ends_with_dot = stripped_string.endswith(".")
print("Ends with '.' :", ends_with_dot)

# 7. Split the string by "!"
split_string = stripped_string.split("!")
print("Split by '!':", split_string)

# 8. Print the length of the original string
original_length = len(my_string)
print("Length of original string:", original_length)

'''Second task'''

name = "John"
age = 25
country = "India"

'''Using f-string to format the sentence '''
sentence = f"My name is {name}, I am {age} years old and I live in {country}."
print(sentence)


#Task 3: Write a for loop to print each letter in the string "Artificial Intelligence" and also count length and also how many vowels are there in it? - 3 questions

text = "Artificial Intelligence"

#Initialize vowel count
vowel_count = 0
vowels = "aeiouAEIOU"


#1 Print each character
print("Characters in the string:")
for char in text:
    print(char)
    if char in vowels:
        vowel_count += 1


#2 Count length
length = len(text)
print("\nTotal length of the string:", length)


#3Count vowels
print("Number of vowels in the string:", vowel_count)



""" Task 4: If-Else Practice
Create a variable score = 85
🔹 Write a condition:
If score is 90 or above → print "Excellent"
If score is between 70 and 89 → print "Good"
If score is below 70 → print "Needs Improvement" """

score = 85

if score >= 90:
    print("Excellent")
elif 70 <= score <= 89:
    print("Good")
else:
    print("Needs Improvement")



''' Task 5: String Slicing Practice
Use this string: course_name = "Python Programming Language"

Print:
"Python" using slicing
"Programming" using slicing
"Language" using slicing
The reversed string of course_name '''

course_name = "Python Programming Language"
#Q1 Print "Python"
python_part = course_name[0:6]
print("Python:", python_part)

#Q2 Print "Programming"
programming_part = course_name[7:18]
print("Programming:", programming_part)

#3 Print "Language"
language_part = course_name[19:]
print("Language:", language_part)

#Q Print the reversed string
reversed_string = course_name[::-1]
print("Reversed String:", reversed_string)
