# input name
name = input("Enter full name (in incorrect casing): ")

# put name in proper title casing
name = name.title()

# remove spaces
name = name.replace(" ", "")

# print name in pascal case
print(name)