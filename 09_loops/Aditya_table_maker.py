#This a my own idea from 01_for_loops.py file , when you will run this file in terminal it will need a number convert into table .

a = int(input("Enter a number to convert into table: "))

for i in range(1, 11):
    print(a,"X", i, "=", a*i)
