sentence = "My name is Aditya Raj"
sum = 0
vowels = ['a','e','i','o','u']

for char in sentence:
    if (char in vowels):
        sum+= 1
    

print(f"There are {sum} vowels in this sentence.")