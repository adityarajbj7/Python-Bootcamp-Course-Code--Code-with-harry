# String formatting

template = "Dear {}, your are awesome. Take this ${} bag."
a = "John"
a1 = 10000
b = "Jack"
b1 = 1000
c = "Marie"
c1 = 300

s1 = template.format(a,a1)
print(s1)

print(f"{a} your are awesome, Take this ${a1} bag.")