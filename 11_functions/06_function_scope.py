def sum(a, b):
    # a and b are local variables
    c = a + b
    z = 1 # It creates a local variable called z which is destroyed after his function returns
    print(z)
    return c 

def greet():
    z = 32 #Local variable 
    print("Hello")


z = 8 # z is a global variable
print(sum(4,7))
print(z)