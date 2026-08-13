s = "hello world" # Strings are immutable

# s[0] = "R" # You cannot do this

a = len(s)
# print(a)
# print(s.upper(), s)
# print(s.lower())
# print(s.capitalize())
# print(s.title())

# text = " \nhello world "
# print(text.strip()) # Output: "hello world"
# print(text.lstrip()) # Output: "hello world "
# print(text.rstrip()) # Output: " hello world"

# text = "Python is fun and fun and fun"
# print(text.find("is")) # Output: 7 Index of first occurence
# print(text.replace("fun","awesome")) # This will replace all the occurence of fun with awesome

# text = "Apples,Bananas,Pineapples"
# print(text.split(","))
# print(",".join(['Apples', 'Bananas', 'Pineapples'])) #this will come in a part of this course named lists , don't worry about this syntax if you dosen't understand it , we will learn these in future.

text = "Python123"
print(text.isalpha()) #Output:False
print(text.isdigit()) #Output:False
print(text.isalnum()) #Output:True
print(text.isspace()) #Output:False