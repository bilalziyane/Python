#tuples=like lists but are unchangeable

student =("bilal",21,"male")
print(student.count("bilal"))
print(student.index("male"))
for x in student:
    print(x)

if "bilal" in student :
    print("the element you seek exists")