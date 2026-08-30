def sum(a, b):
    print("Hey I am summing ")
    c = a + b
    global z #Please modify global variable called z    
    z = 0 #This will refer to global z and not create a local variable 
    return c

z = 3
print(sum(3,34))
print(z)