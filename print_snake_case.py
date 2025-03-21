# input name
name = input("Enter full name (in incorrect casing): ")

# put name in lower case
name = name.lower()

# replace spaces with underscore
name = name.replace(" ", "_")

# print name
print(name)