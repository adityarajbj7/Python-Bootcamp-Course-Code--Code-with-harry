#Python suppuorts several built-in data types:
# Integers(Int): Whole numbers without a decimal point. Example: 5, -3, 0
# Floats(Float): Numbers with a decimal point. Example: 3.14, -0.5
# Strings(str): A sequence of characters enclosed in quotes. Example: "Hello, World!"
# Booleans(bool): A data type that can only have two values: True or False.
# Lists(list): An ordered collection of items, which can be of different data types. Example: [1, 2, 3], ["apple", "banana", "cherry"]
# Tuples(tuple): An ordered collection of items, similar to lists, but immutable (cannot be modified).
# Sets(set): An unordered collection of unique items. Example: {1, 2, 3}, {"apple", "banana", "cherry"}
# Dictionaries(dict): An unordered collection of key-value pairs. Example: {"name": "John", "age": 30, "city": "New York"}
age = 3
print(age) 
print(type(age)) # <class 'int'>

cgpa = 8.2
print(cgpa)
print(type(cgpa)) # <class 'float'>

name = "Aditya"
print(name)
print(type(name)) # <class 'str'>

is_completed = True # can also be False
print(is_completed)
print(type(is_completed)) # <class 'bool'>