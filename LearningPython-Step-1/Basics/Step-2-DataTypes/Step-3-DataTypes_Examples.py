# Integer: whole numbers
age = 25
year = 2024
print("Integer examples:", age, year)
print("------------------------------------------------")

# Float: decimal numbers
height = 5.9
weight = 72.5
print("Float examples:", height, weight)
print("------------------------------------------------")

# String: text data, can use single or double quotes
name = "Alice"
greeting = 'Hello, world!'
print("String examples:", name, greeting)
print("------------------------------------------------")

# Boolean: represents True or False
is_student = True
has_passed = False
print("Boolean examples:", is_student, has_passed)
print("------------------------------------------------")

# List: ordered, mutable collection
colors = ["red", "green", "blue", "yellow"]
numbers = [1, 2, 3, 4, 5]
print("List examples:", colors, numbers)
print("------------------------------------------------")

# Tuple: ordered, immutable collection
coordinates = (10.0, 20.5)
dimensions = (1920, 1080)
print("Tuple examples:", coordinates, dimensions)
print("------------------------------------------------")

# Dictionary: key-value pairs
person = {"name": "Alice", "age": 25, "city": "New York"}
scores = {"math": 90, "science": 85, "english": 88}
print("Dictionary examples:", person, scores)
print("------------------------------------------------")

# Set: unordered collection of unique elements
unique_numbers = {1, 2, 3, 4, 4, 5}  # Duplicate '4' will be removed
fruits = {"apple", "banana", "cherry", "apple"}  # Duplicate 'apple' removed
print("Set examples:", unique_numbers, fruits)
print("------------------------------------------------")

# None: represents the absence of a value
unknown_value = None
no_data = None
print("None examples:", unknown_value, no_data)
print("------------------------------------------------")

# Multi-line comment
"""
This is a multi-line comment.
Use it to describe sections of code, functions, or anything that requires detailed explanation.
"""

# Single-line comment: explaining variables
# The following variable stores the country name.
country = "USA"
print("Single-line comment example:", country)
print("------------------------------------------------")

# Inline comment: explaining a line of code
x = 10 + 5  # Adding 10 and 5 to get 15
print("Inline comment example:", x)
print("------------------------------------------------")

#Functionalities in print statement
print('a')
print('b')
print('c')
print('a',"b",'c')
print("------------------------------------------------")

print('a', end=' ')
print('b', end=' ')
print('c')
print("------------------------------------------------")

print('a', end='*')
print('b', end='*')
print('c')#if we add end='*': here then next line will also be printed in same line
print("------------------------------------------------")

print('a','b','c', sep='-')
print("------------------------------------------------")

